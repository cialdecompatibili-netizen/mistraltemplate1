---
layout: single
classes: wide
author_profile: false
title: "Giochi"
permalink: /giochi/
description: "I giochi di GamingCorp: sviluppati da noi per browser, Android e PC."
ref: giochi
---
{%- comment -%} Elenco da _data/giochi.json (fonte unica). Stile in assets/css/gaming.css. {%- endcomment -%}
<div class="gc"><div class="gc-wrap gc-sec" style="padding-top:0">
<p class="gc-lead">Tutti i giochi qui sotto li sviluppiamo noi. Nessun gioco &egrave; ancora uscito: ogni scheda dice a che punto siamo.</p>
<div class="gc-grid">
{%- for g in site.data.giochi.giochi -%}
<a class="gc-card" href="{{ '/giochi/' | append: g.id | append: '/' | relative_url }}">
<div class="gc-art" style="--c1:{{ g.colori[0] }};--c2:{{ g.colori[1] }}" aria-hidden="true">{{ g.simbolo }}</div>
<div class="gc-card-b"><div class="gc-badges">{% for x in g.piattaforme %}<span class="gc-badge">{{ x }}</span>{% endfor %}<span class="gc-badge gc-badge-n">{{ g.stato }}</span></div>
<span class="gc-card-t">{{ g.nome }}</span><span class="gc-card-d">{{ g.breve }}</span><span class="gc-card-m">{{ g.genere }} &middot; {{ g.prezzo }}</span></div></a>
{%- endfor -%}
</div></div></div>
