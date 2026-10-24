import json, pathlib
g = pathlib.Path(r"C:\Users\mirco\Desktop\repository\gamingcorp")
cats = [("Handheld","handheld","Console portatili e basi TV."),
        ("Controller","controller","Pad, stick arcade e controller pro."),
        ("Accessori","accessori","Audio, custodie, memoria e supporti.")]
P = [
 ("vortex-pro","Vortex Pro – Console portatile OLED 7\"","handheld",54900,"🎮","Schermo OLED 7\" 120 Hz, 16 GB RAM, 512 GB SSD, 3 ore di gioco reali.","Console portatile con schermo OLED 7\" a 120 Hz, 16 GB di RAM e SSD da 512 GB. Stick a effetto Hall senza drift, grilletti regolabili, ventola silenziosa. Compatibile con i principali store PC."),
 ("vortex-lite","Vortex Lite – Console portatile 6\"","handheld",32900,"🕹️","La portatile leggera: schermo 6\" LCD, 8 GB RAM, 256 GB, sotto i 550 g.","Console portatile da 550 g con schermo LCD 6\" a 90 Hz, 8 GB di RAM e 256 GB di memoria espandibile. Pensata per i giochi indie, il retrogaming e il cloud gaming."),
 ("dock-vortex","Dock Vortex – Base TV 4K","accessori",7900,"📺","Dock con HDMI 2.1 4K 60, USB-C pass-through e 2 porte USB-A.","Base di ricarica e uscita TV per le console Vortex: HDMI 2.1 fino a 4K 60 Hz, ricarica pass-through da 65 W, 2 USB-A per controller e tastiera."),
 ("nova","Nova – Controller wireless a effetto Hall","controller",5900,"🎮","Stick e grilletti a effetto Hall: zero drift, 30 ore di batteria.","Controller wireless a effetto Hall, stick senza drift, grilletti con corsa regolabile, vibrazione fine, 30 ore di batteria. Bluetooth e dongle 2.4 GHz, compatibile PC, Android e portatili."),
 ("nova-elite","Nova Elite – Controller con palette posteriori","controller",12900,"🏆","Palette posteriori, profili salvabili e custodia rigida inclusa.","Versione pro del Nova: 4 palette posteriori rimappabili, 3 profili salvabili, stick intercambiabili, base di ricarica magnetica e custodia rigida."),
 ("dojo","Dojo – Arcade stick a leve ottiche","controller",19900,"🥋","Leva e 8 pulsanti ottici, scocca in alluminio, cavo USB-C removibile.","Arcade stick con leva e pulsanti ottici da 0,1 ms, scocca in alluminio spazzolato, cavo USB-C removibile e vano porta-attrezzi. Per picchiaduro e retrogaming."),
 ("echo","Echo – Cuffie gaming 7.1","accessori",8900,"🎧","Audio surround 7.1, microfono staccabile con cancellazione del rumore.","Cuffie chiuse con driver da 50 mm, audio surround 7.1 virtuale, microfono staccabile con cancellazione del rumore, archetto in memory foam. Jack 3,5 mm e USB-C."),
 ("grip-pro","Grip Pro – Custodia rigida per portatile","accessori",3900,"🧳","Custodia rigida con scomparti per caricatore, microSD e cuffie.","Custodia rigida antiurto con interno in microfibra e scomparti per console, caricatore, schede e cuffie. Cerniera robusta e maniglia."),
 ("pixel-512","Pixel – Scheda microSD 512 GB","accessori",4900,"💾","microSD A2 512 GB, letture fino a 190 MB/s, ideale per le portatili.","Scheda microSD A2 da 512 GB, letture fino a 190 MB/s, scritture fino a 130 MB/s. Per espandere lo spazio delle console portatili."),
 ("titan","Titan – Supporto da scrivania per controller","accessori",2900,"🪝","Supporto in metallo per due controller e un paio di cuffie.","Supporto da scrivania in metallo nero opaco per due controller e un paio di cuffie, base antiscivolo, montaggio senza viti."),
]
d = {"_nota":"Catalogo GamingCorp (DEMO SHOP, pre-ordine, nessun pagamento). Prezzi in centesimi. Fonte UNICA di /negozio/ e delle pagine prodotto. L'id categoria e' riservato.",
     "categorie":[{"nome":n,"id":i,"icona":""} for n,i,_ in cats],
     "prodotti":[{"tipo":"fisico","id":i,"nome":n,"categoria":c,"prezzo_centesimi":p,"descrizione":s,"descrizione_completa":l,"immagine":"","icona":ic,"visibile":True} for i,n,c,p,ic,s,l in P]}
(g/"_data"/"catalogo.json").write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding="utf-8")
(g/"_negozio").mkdir(exist_ok=True)
for i,n,c,p,ic,s,l in P:
    (g/"_negozio"/f"{i}.md").write_text(f'---\nlayout: negozio-prodotto\ntitle: "{n.replace(chr(34),chr(39))}"\npid: {i}\npermalink: /negozio/{i}/\ndescription: "{s.replace(chr(34),chr(39))}"\n---\n',encoding="utf-8")
for n,i,desc in cats:
    (g/"_negozio"/f"categoria-{i}.md").write_text(f'---\nlayout: negozio-categoria\ntitle: "{n}"\ncid: {i}\npermalink: /negozio/categoria/{i}/\ndescription: "{desc}"\n---\n',encoding="utf-8")
# config
cfg = g/"_config.yml"; t = cfg.read_text(encoding="utf-8")
if "\necommerce:" not in t:
    t += "\n\necommerce: true\n# Ordini (SMOKE TEST, nessun pagamento): URL dell'Apps Script. Vuoto = il pulsante 'Invia richiesta d'ordine' resta spento.\nordini:\n  tracker: \"\"\n"
    cfg.write_text(t,encoding="utf-8")
# nav
nav = g/"_data"/"navigation.yml"; t = nav.read_text(encoding="utf-8")
if "/negozio/" not in t:
    t = t.replace('  - title: "Tour"', '  - title: "Negozio"\n    url: /negozio/\n  - title: "Tour"',1)
    nav.write_text(t,encoding="utf-8")
print("ok", len(P))
