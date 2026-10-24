# mistraltemplate1 - guida per Claude (template Jekyll adattivo)

Template Jekyll per GitHub Pages: si clona, si cambia quasi solo `_config.yml` e il sito si adatta (lingua, URL, brand, menu, shop). Obiettivo e stato del lavoro: `PROGETTO_TEMPLATE.md`.

## Prima di toccare un clone (checklist)
1. `_config.yml`: `brand`, `description`, `default_lang`, `languages`, `whatsapp`, `contact_endpoint`, `ecommerce`. NON scrivere `url:`/`baseurl:` (li imposta GitHub Pages).
2. Menu: `_data/navigation.yml` (voci) + `_data/sottomenu.yml` (tendine, chiave = title identico). Url interni SENZA nome repo.
3. Home a blocchi: `_data/blocks_home.json` (campi id, nome, enabled, html). Modificare solo `html`, mai la struttura. Backup prima, rileggere il JSON dopo.
4. Colori/tema: `_data/tema.json`; kit blocchi in `assets/css/gaming.css` (nome storico, non rinominare; accento = `--gc-acc`).
5. Shop: `ecommerce: true` accende tutto. Dati in `_data/catalogo.json` (prezzi in centesimi) + una pagina per prodotto/categoria in `_negozio/` (esempi inclusi: `prodotto-esempio.md`, `categoria-esempio.md`).
6. Contenuti: `_pages/`, `_posts/`. Ogni pagina/articolo ha `ref:` (chiave di collegamento tra lingue).

## Regole d'oro
- ZERO valori fissi: niente nome repo, utente, dominio, telefono scritti nei layout/include/JS. Si usa `relative_url`, `site.*`, `_includes/site-name.html`.
- Admin (`admin/index.html`): `detectRepo()` ricava utente/repo dall'URL. Su dominio personalizzato chiede il repo una volta (localStorage `cms_repo`). Non hardcodarlo.
- `automation/publish.py`: percorso e URL ricavati da soli (cartella del file + remote git).
- Valore vuoto in config = funzione spenta, mai errore: i layout controllano che il campo sia pieno.
- Nessun plugin fuori da GitHub Pages. Build locale non disponibile su questo PC: si controlla online dopo il deploy.
- COMMENTARE i punti critici (layout, include, JS, CSS, config): dire cosa fa, cosa legge, cosa NON toccare.

## Multilingua (dettagli in `docs/MULTILINGUA.md`)
IT alla radice, altre lingue in `/xx/` create da admin > Lingue. Cambiare solo `default_lang` e `languages`. Traduzioni: `tr: copia|tradotto|da_aggiornare`, `tr_hash`; `automation/traduzioni_sync.py` + workflow marcano `da_aggiornare`. In Liquid niente `a contains b == false`: usare `{% if a contains b %}{% continue %}{% endif %}`.

## Eta' e date
MAI a mano: `<span data-eta="AAAA-MM-GG">N</span> anni`, `<span data-anni-da="AAAA">N</span> anni` (script in `_includes/footer/custom.html`).

## Design
MAI bordi laterali colorati su box, citazioni, avvisi, CTA. Box puliti con sfondo leggero o bordo uniforme.

## Pubblicare e lavorare
- Pubblicare con `..\pubblica.ps1` con `-Files` espliciti. Dopo il push NON aspettare la build: Mirco verifica da solo.
- Sessione interrotta: prima `read_file` e `git status --short`; spesso manca solo commit e push.
- PowerShell lungo: salvare in .ps1 e lanciare con `-NoProfile -ExecutionPolicy Bypass -File`. Mai chiamare funzioni RD/WR/CD/LS (alias: RD cancella!).
- Il workflow `.github/workflows/traduzioni.yml` va su GitHub solo dopo `gh auth refresh -s workflow`, poi `git add -f .github/workflows`.
- Risposte brevissime, modifiche in una sola chiamata.
