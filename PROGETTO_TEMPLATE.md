# mistraltemplate1 - progetto template stabile e adattivo

Creata il 24/10/2026. Base: clone di `gamingcorp` (che a sua volta deriva da edilextreme4/renzoferrucci con motore multilingua). Account GitHub `cialdecompatibili-netizen`, cartella `C:\Users\mirco\Desktop\repository\mistraltemplate1`.

## Obiettivo (da Mirco)
Un template STABILE e ADATTIVO che qualsiasi nuova repo possa prendere, con tutto automatico: si clona, si cambia (quasi) solo la configurazione e il sito si adatta da solo (lingua, URL, brand, menu, shop, date, eta').

## Principi
- Zero valori fissi nei file: brand, descrizione, lingue, remoto/baseurl, WhatsApp, contatti stanno solo in `_config.yml` (e `_data/`).
- Software con remoto/baseurl automatici (come italfuni/edilextreme2): nessun URL scritto a mano nei layout.
- Multilingua automatico: IT alla radice, altre lingue in `/xx/` create dall'admin (voce Lingue), lette dal sito senza codice. Per un clone si cambia solo `languages` e `default_lang`.
- Nessun plugin fuori da GitHub Pages; build nativa (un push = un deploy).
- Contenuti a blocchi (`_data/blocks_home.json`), menu da `_data/navigation.yml` + `sottomenu.yml`, tutto gestibile dall'admin.
- Eta' e anni automatici (`data-eta`, `data-anni-da`), mai scritti a mano.
- Regole di design: niente bordi laterali colorati su box/citazioni/CTA.

## Cosa c'e' gia' (ereditato da gamingcorp)
- Motore multilingua FASE 1-3 (config, defaults, i18n, hreflang, selettore con bandiera, admin Lingue, sync `tr: da_aggiornare` via `automation/traduzioni_sync.py` + workflow).
- Admin in `admin/`, collezioni `_negozio`, `_tour`, `_pages`, `_posts`; ecommerce con ordini smoke test.
- `template-map.json`, `version.json`.

## Da fare (ordine proposto)
1. Pulire i contenuti specifici di gaming (brand GamingCorp, `_tour`, `_negozio`, post demo) lasciando struttura e un esempio minimo per tipo.
2. Rendere `_config.yml` l'unico punto da cambiare: brand, description, languages, default_lang, whatsapp, contact_endpoint, ecommerce on/off.
3. `url` e `baseurl` automatici (nessun valore fisso in layout, include, JS, admin).
4. Script `nuovo_sito.ps1`: copia il template in una nuova cartella, git init, imposta brand/lingue, `gh repo create`, push, attiva Pages.
5. Admin: interruttore Shop/Tour/Blog per attivare o spegnere sezioni senza toccare file.
6. Aggiornare `CLAUDE.md` (oggi dice ancora edilextreme4) con regole generiche del template.
7. Provare il template clonandolo su una repo di prova e verificare che si adatti da solo.

## Note
- Pubblicare con `..\pubblica.ps1` (vedi `..\claude.md`), sempre con `-Files` espliciti.
- Non aspettare la build dopo il push: Mirco verifica da solo.
- Prima di modificare JSON: backup, poi rileggere e verificare.

- WORKFLOW DA AGGIUNGERE: .github/workflows/traduzioni.yml e' presente in locale ma NON ancora su GitHub (il token gh non ha lo scope workflow). Fare: gh auth refresh -s workflow, poi git add -f .github/workflows; commit; push.

## STATO (24/10/2026)
- FATTO: contenuti gaming rimossi (giochi, _negozio, post, .bak, crea_shop_gaming.py), sostituiti da esempi minimi (post, prodotto e categoria shop); _config.yml unico punto di configurazione con commenti guida; shop spento di default.
- FATTO: admin senza repo fisso (detectRepo, su dominio personalizzato chiede il repo una volta); publish.py senza percorsi/URL fissi (repo = cartella del file, URL dal remote git); CLAUDE.md riscritto come guida ai cloni.
- RESTA: punto 4 (script 
uovo_sito.ps1), punto 5 (interruttori Shop/Tour/Blog nell'admin), punto 7 (prova di clone), commenti guida nei layout/include/JS/CSS ancora da completare, workflow traduzioni su GitHub.
