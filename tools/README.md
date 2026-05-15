# REHAB FIVE NUTRITION — Wissen-Artikel-Generator

Ein Python-Skript, das alle 14 kompakten Indikations-Artikel im `wissen/`-Verzeichnis aus einer zentralen Datenstruktur erzeugt. Pattern-identisch zu den 7 ausführlichen Artikeln (Quick-Answer · Sektionen · FAQ · JSON-LD · Quellen).

## Wann nutzen?

- **Leitlinien-Update:** Wenn z. B. die S3-Leitlinie zu Adipositas neu erscheint, passe die Quellen / Quick-Answer im Skript an und regeneriere.
- **Neue Indikation hinzufügen:** Füge einen weiteren `INDIKATIONEN`-Eintrag in der Liste hinzu, regeneriere.
- **Inhalt erweitern:** Sektionen, FAQs oder Quellen pro Indikation ergänzen → regeneriere.
- **Brand-Update:** Wenn sich Farben / Schriften ändern, einmal im Template anpassen → wirkt auf alle 14 Artikel.

## Voraussetzungen

```bash
python3 --version   # Python 3.9+ vorhanden auf macOS
```

Keine externen Dependencies nötig — pure Standard-Library.

## Ausführen

```bash
cd /Users/aricbramswig/Downloads/rehab-five-nutrition/tools
python3 build_wissen_articles.py
```

Erwartete Ausgabe:

```
✓ untergewicht-mangelernaehrung              22,860 bytes
✓ dyslipoproteinaemien-ernaehrung            22,788 bytes
...
14 Artikel erfolgreich generiert in /Users/aricbramswig/Downloads/rehab-five-nutrition/wissen
```

Die HTML-Dateien werden in `../wissen/<slug>.html` überschrieben.

## Datenstruktur pro Indikation

Jeder Eintrag in der `INDIKATIONEN`-Liste folgt diesem Schema:

```python
{
    "slug": "diabetes-typ-2-ernaehrung",     # URL-Slug
    "title_short": "Diabetes Typ 2",         # Card-Titel, Breadcrumb
    "title_full": "Diabetes Typ 2 & ...",    # SEO-Title, H1-Subtitle
    "icd": "E11",                            # Anzeige im Hero-Badge
    "icd_schema": "E11",                     # JSON-LD MedicalCondition.code
    "name_schema": "Diabetes mellitus Typ 2",# JSON-LD MedicalCondition.name
    "alt_names": ["Altersdiabetes"],         # JSON-LD alternateName
    "h1_top": "Diabetes Typ 2:",             # Hero H1 obere Zeile
    "h1_bottom": "HbA1c senken …",           # Hero H1 untere Zeile (orange)
    "meta_desc": "...",                      # SEO-Description + Hero-Lead
    "keywords": "...",                       # SEO-Keywords
    "symptoms": ["..."],                     # JSON-LD signOrSymptom
    "treatments": ["..."],                   # JSON-LD possibleTreatment
    "quick": "Bei <strong>Diabetes …</strong>...",  # Quick-Answer-Box (HTML)
    "sections": [                            # Content-Sektionen (Title, HTML-Body)
        ("Was ist Diabetes?", "Diabetes ist ..."),
        ("Mediterrane Ernährung", "<ul><li>...</li></ul>"),
        ...
    ],
    "faqs": [                                # FAQ-Block + FAQPage-Schema
        ("Frage?", "Antwort."),
        ...
    ],
    "quellen": [                             # Quellen-Liste mit Links
        ("Autor", "(Jahr): ‚Titel.' Journal.", "https://..."),
        ...
    ],
    "related": [                             # Verwandte Artikel (slugs)
        "adipositas-ernaehrungstherapie",
        ...
    ],
}
```

## Wichtig: deutsche Anführungszeichen

Innerhalb der Quellen-/Sektions-Strings verwende **„..."** (typografische Anführungszeichen) statt **"..."** (ASCII). ASCII-Doublequotes innerhalb von Strings schließen den Outer-String und führen zu `SyntaxError`. Falls trotzdem nötig: mit `\"` escapen.

## Pattern: was wird generiert?

Pro Artikel entsteht eine vollständige HTML-Seite mit:

- **SEO-Head:** Title (~60 Zeichen), Description, Keywords, OG-Tags, Canonical
- **JSON-LD:** Organization · MedicalCondition (mit ICD + Symptomen + Therapien) · MedicalWebPage · Article · FAQPage · BreadcrumbList
- **Header** mit Logo + Navigation
- **Hero** mit Breadcrumb, ICD-Badge, Headline, Subtitle, Meta-Info
- **Quick-Answer-Box** (für AEO / ChatGPT-Citations)
- **Content-Sektionen** im Prose-Style
- **CTA-Block** zum Erstgespräch + Kassen-Check-PDF
- **FAQ-Block** mit Accordion (alle Fragen aus Daten)
- **Quellen-Block** mit nummerierter Liste + Links
- **Verwandte Indikationen** (3 Cards)
- **Footer** mit Standort, Rechtliches, Cookie-Hinweis
- **Mobile-Sticky-CTA**

## Brand-Konventionen

Die Tailwind-Konfiguration im Template entspricht dem REHAB FIVE CD-Manual (29.11.2023):

- **Forest:** `#1F342D` (Hintergrund Hero & Forest-Sektionen)
- **Brand-Orange:** `#D99129` (Akzent, Highlights, Badges)
- **Brand-Hover:** `#C57F1F`
- **Ink-900:** `#1A1A1A` (Body-Text)
- **Schrift:** Barlow (Weights 400–800)

## Tipps zur Pflege

1. **Vor dem Anpassen:** Ein Backup der `wissen/`-HTML-Dateien anlegen (`cp -r wissen wissen.bak`).
2. **Nach jeder Änderung:** Test im lokalen Server (`python3 -m http.server 8088` im Projekt-Root) → Browser öffnen.
3. **JSON-LD validieren:** Mit dem Google Rich Results Test (https://search.google.com/test/rich-results) prüfen, ob `MedicalCondition` und `FAQPage` korrekt erkannt werden.
4. **Inkonsistenzen vermeiden:** Wenn du eine Indikation umbenennst, auch die Cross-Referenzen in `related` aller anderen Einträge prüfen.

## Wo werden die Artikel angezeigt?

1. **Hauptseite Indikationen-Grid:** `../index.html` — Sektion „Indikationen" (alle 21 verlinkt mit ICD-Codes)
2. **Wissen-Übersicht:** `../wissen/index.html` — Top-7 mit Card-Grid, restliche 14 als Kompakt-Liste
3. **Direkt-URL:** `../wissen/<slug>.html`

## Backlog (Ideen für später)

- [ ] Symbol-Icon pro Indikation (statt nur ICD-Badge)
- [ ] Lesezeit dynamisch aus Wortzahl berechnen statt hardcoded
- [ ] Sitemap.xml-Generator für die 21 Artikel
- [ ] Auto-Verlinkung gleichbedeutender Begriffe (z. B. „Adipositas" im Fettleber-Artikel → auto-link)
- [ ] llms.txt-File erzeugen (für AI-Crawler-Indexierung)

---

**Wartung:** Aric Brämswig · REHAB FIVE GmbH · Stand 2026-05-15
