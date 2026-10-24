# GUIDA-SVILUPPO: PERSONALIZZA UN CLONE IN UN COLPO SOLO (colori, logo, sfondo home). Lo chiama nuovo_sito.ps1; si puo' lanciare anche a mano.
# Uso, dalla radice del clone:
#   python automation/personalizza_clone.py --accent "#8a6a3a" --dark "#503629" --iniziale P --stile pelle [--bg "#fbf8f3"] [--text "#2b2622"]
# Cosa fa (idempotente, si puo' rilanciare):
#   1) scrive _data/tema.json (accent, accent_dark, nav_hover, link, + bg/text se passati)
#   2) sostituisce nei css/html/layout i colori di default del template (azzurro/teal/ghiaccio) con la palette nuova
#   3) rinomina lo sfondo home artico-hero.jpg -> hero.jpg (css aggiornati) e lo rigenera con genera_texture.py
#   4) rigenera logo e favicon con genera_logo.py
# Non committa: committa UNA volta sola chi lo chiama (nuovo_sito.ps1 lo fa prima del primo commit).
import argparse, json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap = argparse.ArgumentParser()
ap.add_argument('--accent', required=True); ap.add_argument('--dark', default='')
ap.add_argument('--iniziale', default=''); ap.add_argument('--stile', default='pelle', choices=['pelle', 'liscio'])
ap.add_argument('--bg', default=''); ap.add_argument('--text', default='')
a = ap.parse_args()
def hx(s): s = s.lstrip('#'); return tuple(int(s[i:i+2], 16) for i in (0, 2, 4))
def mix(c, t, k): return tuple(round(c[i] + (t[i] - c[i]) * k) for i in range(3))
def h(c): return '#%02x%02x%02x' % c
def rgb(c): return '%d,%d,%d' % c
ACC, W = hx(a.accent), (255, 255, 255)
if not a.dark: a.dark = '#%02x%02x%02x' % tuple(round(v * .45) for v in ACC)  # scuro automatico = accento al 45%
DARK = hx(a.dark)
# 1) tema.json
tf = os.path.join(ROOT, '_data', 'tema.json'); tema = json.load(open(tf, encoding='utf-8'))
tema.update({'accent': a.accent.lower(), 'accent_dark': a.dark.lower(), 'nav_hover': a.accent.lower(), 'link': a.accent.lower()})
if a.bg: tema.update({'nav_bg': a.bg, 'body_bg': a.bg})
if a.text: tema.update({'text': a.text})
json.dump(tema, open(tf, 'w', encoding='utf-8', newline='\n'), indent=2, ensure_ascii=False); open(tf, 'a').write('\n')
# 2) colori di default del template -> palette nuova (derivati dall'accento)
MAP = {'#0e7490': h(ACC), '#0891b2': h(ACC), '#155e75': h(DARK), '#164e63': h(DARK), '14,116,144': rgb(ACC),
       '#7fd8e6': h(mix(ACC, W, .55)), '#67e8f9': h(mix(ACC, W, .55)), '#22d3ee': h(mix(ACC, W, .35)), '#06b6d4': h(mix(ACC, DARK, .15)),
       '#a5f3fc': h(mix(ACC, W, .7)), '#cffafe': h(mix(ACC, W, .88)), '#ecfeff': h(mix(ACC, W, .95)), '#eef8fa': h(mix(ACC, W, .92)),
       '#e8f4f8': h(mix(ACC, W, .92)), '#e6f6f9': h(mix(ACC, W, .92)), '#eaf3fb': h(mix(ACC, W, .9)),
       '236,245,255': rgb(mix(ACC, W, .93)), '30,70,110': rgb(DARK), 'artico-hero.jpg': 'hero.jpg',
       'azzurro ghiaccio': 'tinta chiara', 'palette acqua: teal + tinta chiara': 'palette del tema'}
SKIP = re.compile(r'[\\/](\.git|_site|node_modules|__pycache__|docs|automation)[\\/]|tema\.json$')
n = 0
for dp, dn, fn in os.walk(ROOT):
    for f in fn:
        p = os.path.join(dp, f)
        if not f.lower().endswith(('.css', '.html', '.yml', '.js', '.scss')) or SKIP.search(p): continue
        t = open(p, encoding='utf-8').read(); o = t
        for k, v in MAP.items(): t = re.sub(re.escape(k), v, t, flags=re.I)
        if t != o: open(p, 'w', encoding='utf-8', newline='').write(t); n += 1
print('colori: %d file aggiornati' % n)
# 3) sfondo home + 4) logo
old = os.path.join(ROOT, 'assets', 'images', 'artico-hero.jpg')
if os.path.exists(old): os.remove(old)
py = sys.executable; auto = os.path.join(ROOT, 'automation')
subprocess.run([py, os.path.join(auto, 'genera_texture.py'), '--stile', a.stile, '--out', 'hero.jpg'], cwd=ROOT, check=True)
subprocess.run([py, os.path.join(auto, 'genera_logo.py'), a.accent, a.dark] + ([a.iniziale] if a.iniziale else []), cwd=ROOT, check=True)
print('FATTO: tema + colori + sfondo home + logo. Ora un solo commit.')
