"""Generator für die 14 fehlenden Wissen-Artikel auf REHAB FIVE NUTRITION.

Pattern entspricht den 7 bereits gebauten Artikeln, aber kompakter:
- HEAD mit SEO + JSON-LD (MedicalCondition + MedicalWebPage + FAQPage + Breadcrumb)
- Header / Hero mit Breadcrumb
- Quick-Answer-Box
- 4 Content-Sektionen
- CTA-Block
- FAQ (5 Fragen)
- Quellen (6-8)
- Verwandte Indikationen
- Footer
"""

import os
import html

OUT_DIR = "/Users/aricbramswig/Downloads/rehab-five-nutrition/wissen"
BASE_URL = "https://rehab-five-nutrition-ernaehrungsberatung.com"

# ============================================================
# DATEN PRO INDIKATION
# ============================================================

INDIKATIONEN = [
    {
        "slug": "untergewicht-mangelernaehrung",
        "title_short": "Untergewicht & Mangelernährung",
        "title_full": "Untergewicht & Mangelernährung: Strukturierter Aufbau statt Crash",
        "icd": "E43–E46 / R63.6",
        "icd_schema": "E43-E46",
        "name_schema": "Mangelernährung",
        "alt_names": ["Untergewicht", "Malnutrition"],
        "h1_top": "Untergewicht:",
        "h1_bottom": "Strukturierter Aufbau.",
        "meta_desc": "Untergewicht & Mangelernährung (ICD E43–46): Eiweiß, Kalorien, Mikronährstoffe — wie Aufbau wirklich gelingt. Kassen-Zuschuss in Münster.",
        "keywords": "Untergewicht Ernährung, Mangelernährung, Aufbau Ernährung, BMI unter 18,5, Eiweißbedarf, REHAB FIVE Nutrition",
        "symptoms": ["BMI < 18,5 kg/m²", "ungewollter Gewichtsverlust", "Erschöpfung", "Mikronährstoff-Mangel"],
        "treatments": ["Energiereiche, eiweißreiche Mischkost", "Anreicherung mit gesunden Fetten", "Mikronährstoff-Substitution"],
        "quick": "Bei <strong>Untergewicht (BMI < 18,5)</strong> oder <strong>Mangelernährung</strong> ist eine strukturierte Erhöhung der <strong>Energie- und Eiweißzufuhr</strong> entscheidend — mit hochwertigen Fetten und Mikronährstoff-Sicherung. Crash-Aufbau mit Fast Food schadet langfristig. Realistisch sind <strong>0,5–1 kg Aufbau pro Monat</strong>. Kasse erstattet die Beratung typisch zu 80%.",
        "sections": [
            ("Was ist Mangelernährung?", "Mangelernährung umfasst Untergewicht (BMI < 18,5) sowie qualitative Defizite (Mikronährstoffe, Eiweiß). Ursachen: Erkrankungen, Appetitlosigkeit, Resorptionsstörungen, Essstörungen, hohes Alter. Ohne strukturierte Behandlung folgen Muskelabbau, Infektanfälligkeit und Osteoporose-Risiko.[1]"),
            ("Strukturierter Aufbau — wie es funktioniert", "Die DGEM empfiehlt eine schrittweise Erhöhung um <strong>500–700 kcal/Tag</strong> über das Erhaltungs-Niveau hinaus. Wichtige Säulen:<ul><li><strong>Eiweiß:</strong> 1,2–1,5 g/kg KG (z. B. Quark, Eier, Hülsenfrüchte, Fleisch)</li><li><strong>Gesunde Fette:</strong> Olivenöl, Nüsse, Avocado — energiedicht und entzündungsarm</li><li><strong>Häufige kleine Mahlzeiten</strong> (5–6 pro Tag) statt 3 große</li><li><strong>Trinknahrung</strong> als Ergänzung bei starker Appetitlosigkeit</li></ul>"),
            ("Mikronährstoffe — was zu prüfen ist", "Eisen, Ferritin, Vitamin B12, Folsäure, Vitamin D, Zink, Magnesium, Kalzium. Bei chronischen Erkrankungen (z. B. Zöliakie, M. Crohn) ist die Resorption gestört — gezielte Substitution nötig.[2]"),
            ("Wann professionelle Begleitung?", "Bei BMI < 17, schnellem Gewichtsverlust (> 5% in 6 Monaten), nach Erkrankung oder bei Verdacht auf Essstörung. Bei Mangelernährung (ICD E43–46) ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — Erstattung typisch 80%."),
        ],
        "faqs": [
            ("Wie schnell darf ich zunehmen?", "Gesund sind 0,5–1 kg pro Monat. Schneller Aufbau führt zu vermehrtem Fett statt Muskelmasse und belastet den Stoffwechsel."),
            ("Welche Lebensmittel helfen beim Aufbau?", "Energiedichte, nährstoffreiche Lebensmittel: Nüsse, Olivenöl, Avocado, fetter Fisch, Vollkornprodukte, Hülsenfrüchte, Quark, Eier. Trinknahrung als Ergänzung bei Bedarf."),
            ("Reicht mehr essen aus?", "Nicht immer. Resorptionsstörungen, Schilddrüsenfunktion und psychische Faktoren sollten geprüft werden. Strukturierte Begleitung hilft, Plateaus zu durchbrechen."),
            ("Übernimmt die Krankenkasse?", "Ja. Mangelernährung (ICD E43–46) ist erstattungsfähig nach §43 SGB V. Mit ärztlicher Notwendigkeitsbescheinigung übernehmen Kassen typischerweise 80%."),
            ("Was, wenn der Appetit fehlt?", "Häufige kleine Mahlzeiten, energiereiche Snacks, Trinknahrung. Bei anhaltender Appetitlosigkeit ärztliche Abklärung (Schilddrüse, Magen, psychische Faktoren)."),
        ],
        "quellen": [
            ("DGEM", "(2022): „S3-Leitlinie der Deutschen Gesellschaft für Ernährungsmedizin.\" AWMF-Register 073/004.", "https://www.awmf.org/leitlinien/detail/ll/073-004.html"),
            ("Cederholm T et al.", "(2017): „ESPEN guidelines on definitions and terminology of clinical nutrition.\" Clin Nutr, 36(1):49–64.", "https://www.clinicalnutritionjournal.com/article/S0261-5614(16)31144-2/fulltext"),
            ("BMEL", "(2023): „Ernährungsbericht Deutschland.\"", "https://www.bmel.de"),
            ("DGE", "(2024): „Referenzwerte für die Nährstoffzufuhr.\"", "https://www.dge.de/wissenschaft/referenzwerte/"),
            ("Volkert D et al.", "(2019): „ESPEN guideline on clinical nutrition and hydration in geriatrics.\" Clin Nutr, 38(1):10–47.", "https://www.clinicalnutritionjournal.com/article/S0261-5614(18)32511-7/fulltext"),
            ("DGEM-Pocket", "(2023): „Praktische Anwendung der Trinknahrung.\"", "https://www.dgem.de"),
        ],
        "related": ["adipositas-ernaehrungstherapie", "osteoporose-ernaehrung", "zoeliakie-ernaehrung"],
    },
    {
        "slug": "dyslipoproteinaemien-ernaehrung",
        "title_short": "Dyslipoproteinämien",
        "title_full": "Erhöhte Blutfette & Ernährung: LDL senken, Herz schützen",
        "icd": "E78",
        "icd_schema": "E78",
        "name_schema": "Dyslipoproteinämie",
        "alt_names": ["Hyperlipidämie", "Fettstoffwechselstörung"],
        "h1_top": "Erhöhte Blutfette:",
        "h1_bottom": "LDL senken, Herz schützen.",
        "meta_desc": "Dyslipoproteinämien (ICD E78): Wie Ernährung LDL, Triglyceride und Lp(a) beeinflusst. Mediterrane Kost, gesättigte Fette, Cholesterin. Kassen-Zuschuss.",
        "keywords": "Dyslipoproteinämie, Cholesterin senken, LDL Ernährung, Triglyceride, Hyperlipidämie, Statine, REHAB FIVE Nutrition",
        "symptoms": ["LDL-Cholesterin erhöht", "Triglyceride > 150 mg/dl", "HDL erniedrigt", "Lp(a) erhöht"],
        "treatments": ["Mediterrane Ernährung", "Reduktion gesättigter Fette", "Erhöhung Ballaststoffe", "Pflanzliche Eiweißquellen"],
        "quick": "Bei <strong>Dyslipoproteinämien (ICD E78)</strong> sind <strong>Ernährungsumstellung und Bewegung</strong> die Basis jeder Therapie. Mediterrane Kost senkt LDL um <strong>5–15 %</strong>. Reduktion gesättigter Fette (rotes Fleisch, Butter, Käse), mehr Ballaststoffe (Hafer, Hülsenfrüchte) und pflanzliche Eiweißquellen wirken am besten. Kasse erstattet die Beratung typisch zu 80%.",
        "sections": [
            ("Was sind Dyslipoproteinämien?", "Dyslipoproteinämien (auch Hyperlipidämien) sind Fettstoffwechselstörungen mit erhöhten LDL- oder Triglycerid-Werten und/oder erniedrigtem HDL. Sie sind zentrale Risikofaktoren für Atherosklerose und Herzinfarkt. Diagnose über Nüchtern-Lipidprofil.[1]"),
            ("Was die ESC-Leitlinie 2019/2024 empfiehlt", "Bei hohem kardiovaskulärem Risiko gilt LDL-Ziel < 70 mg/dl (sehr hoch < 55 mg/dl). Lifestyle-Empfehlungen:<ul><li><strong>Gesättigte Fette < 10 % der Energie</strong> (rotes Fleisch, Butter, Käse, Wurst reduzieren)</li><li><strong>Trans-Fette streichen</strong> (Frittiertes, Industriebackwaren)</li><li><strong>Lösliche Ballaststoffe</strong> (Hafer, Hülsenfrüchte, Äpfel) — senken LDL um 5–10 %</li><li><strong>Phytosterole</strong> 2 g/Tag (angereicherte Margarine)</li><li><strong>Omega-3-Fettsäuren</strong> aus fettem Fisch oder pflanzlich (Lein, Walnuss)</li><li><strong>Mediterrane Ernährung</strong> als Gesamtmuster</li></ul>"),
            ("Ernährung vs. Medikamente", "Lifestyle-Maßnahmen senken LDL um 10–20 %, Statine um 30–50 %. Sie ersetzen sich nicht — sie ergänzen sich. Auch unter Statin-Therapie verbessert Ernährung die Prognose zusätzlich.[2]"),
            ("Wann professionelle Begleitung?", "Bei familiärer Hypercholesterinämie, kombinierten Fettstoffwechselstörungen, Statin-Unverträglichkeit oder unzureichendem Therapieerfolg. Bei Dyslipoproteinämie (ICD E78) ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Wie schnell senkt Ernährung das LDL?", "Erste Effekte nach 4–6 Wochen. Volle Wirkung der mediterranen Ernährung nach 3 Monaten — typisch LDL-Senkung um 10–20 %."),
            ("Muss ich Eier streichen?", "Nein. Studien zeigen, dass moderater Eierkonsum (bis 6 pro Woche) bei den meisten Menschen das LDL kaum beeinflusst. Wichtiger sind gesättigte und trans-Fette."),
            ("Was bringen Omega-3-Kapseln?", "Bei sehr hohen Triglyceriden (> 500 mg/dl) helfen hochdosierte Omega-3-Fettsäuren. Für LDL-Senkung dagegen kaum wirksam — bevorzugt fettreichen Fisch 2× pro Woche."),
            ("Übernimmt die Krankenkasse?", "Ja. Dyslipoproteinämie (ICD E78) ist erstattungsfähig nach §43 SGB V. Mit ärztlicher Bescheinigung typisch 80%."),
            ("Sind Phytosterole sinnvoll?", "Bei moderat erhöhtem LDL ja — 2 g/Tag senken LDL zusätzlich um 7–10 %. Wirken auch in Kombination mit Statinen."),
        ],
        "quellen": [
            ("ESC/EAS", "(2019/2024): „Guidelines for the management of dyslipidaemias.\" Eur Heart J, 41:111–188.", "https://academic.oup.com/eurheartj/article/41/1/111/5556353"),
            ("Mach F et al.", "(2020): „ESC/EAS Guidelines for the management of dyslipidaemias.\"", "https://www.escardio.org/Guidelines"),
            ("Sacks FM et al.", "(2017): „Dietary Fats and Cardiovascular Disease: A Presidential Advisory From the American Heart Association.\" Circulation, 136:e1–e23.", "https://www.ahajournals.org/doi/10.1161/CIR.0000000000000510"),
            ("Estruch R et al.", "(2018): „PREDIMED — Mediterranean Diet for Cardiovascular Prevention.\" N Engl J Med, 378:e34.", "https://www.nejm.org/doi/full/10.1056/NEJMoa1800389"),
            ("DEGAM", "(2023): „NVL Chronische KHK.\" AWMF-Register nvl-007.", "https://www.leitlinien.de/nvl/khk"),
            ("DGE", "(2024): „Empfehlungen für Erwachsene mit Hyperlipidämie.\"", "https://www.dge.de"),
        ],
        "related": ["hypertonie-ernaehrung", "diabetes-typ-2-ernaehrung", "fettleber-ernaehrung"],
    },
    {
        "slug": "gicht-hyperurikaemie-ernaehrung",
        "title_short": "Gicht / Hyperurikämie",
        "title_full": "Gicht & Ernährung: Harnsäure senken durch den Teller",
        "icd": "E79.0 / M10",
        "icd_schema": "E79.0",
        "name_schema": "Hyperurikämie",
        "alt_names": ["Gicht", "Arthritis urica"],
        "h1_top": "Gicht:",
        "h1_bottom": "Harnsäure senken durch den Teller.",
        "meta_desc": "Hyperurikämie & Gicht (ICD E79.0 / M10): Wie Ernährung Harnsäure senkt — purinarme Kost, Fructose, Alkohol. Kassen-Zuschuss in Münster.",
        "keywords": "Gicht Ernährung, Harnsäure senken, purinarme Kost, Hyperurikämie, Fructose Gicht, REHAB FIVE Nutrition",
        "symptoms": ["Harnsäure > 6,8 mg/dl", "Gichtanfall (Großzehe)", "Gichtknoten / Tophi", "Nierensteine"],
        "treatments": ["Purinarme Ernährung", "Alkohol-Reduktion (Bier!)", "Fructose-Reduktion", "Gewichtsreduktion"],
        "quick": "Bei <strong>Hyperurikämie und Gicht (ICD E79.0 / M10)</strong> wirken <strong>purinarme Ernährung</strong>, <strong>Alkohol-Reduktion (besonders Bier)</strong>, <strong>Fructose-Verzicht</strong> und Gewichtsreduktion zusammen. Vegetarisch-betonte Kost senkt Harnsäure um <strong>1–2 mg/dl</strong>. Wichtig: viel trinken (2–3 l/Tag). Kasse erstattet die Beratung typisch zu 80%.",
        "sections": [
            ("Was ist Gicht?", "Gicht ist eine Stoffwechselerkrankung mit erhöhter Harnsäure im Blut (> 6,8 mg/dl). Beim akuten Gichtanfall lagern sich Harnsäure-Kristalle in Gelenken ab — meist in der Großzehe (Podagra). Chronisch drohen Tophi, Nierensteine und Gelenkschäden.[1]"),
            ("Purine — die wichtigsten Quellen", "Purine werden im Körper zu Harnsäure abgebaut. Stark purinhaltig sind:<ul><li><strong>Innereien</strong> (Leber, Niere, Bries) — meiden</li><li><strong>Rotes Fleisch, Wurst</strong> — stark reduzieren</li><li><strong>Sardinen, Sardellen, Hering, Forelle</strong> — moderat</li><li><strong>Bier (auch alkoholfrei!)</strong> — komplett meiden</li><li><strong>Hochfructose-Sirup, Softdrinks</strong> — komplett meiden</li></ul>Pflanzliche Purine (Hülsenfrüchte, Pilze) erhöhen das Gicht-Risiko nicht.[2]"),
            ("Was wirklich hilft", "<ul><li><strong>Vegetarisch-betonte mediterrane Kost</strong> — senkt Harnsäure deutlich</li><li><strong>Magermilchprodukte:</strong> 200–400 g/Tag senken Harnsäure und Gichtanfall-Risiko</li><li><strong>Kirschen / Sauerkirschen</strong> — RCT-Evidenz für Reduktion akuter Anfälle</li><li><strong>Kaffee</strong> (3–4 Tassen) — protektiv</li><li><strong>Vitamin C</strong> (500 mg/Tag) — leicht harnsäuresenkend</li><li><strong>2–3 l Wasser/Tag</strong> — Verdünnung & Ausscheidung</li></ul>"),
            ("Wann professionelle Begleitung?", "Bei wiederkehrenden Gichtanfällen, Tophi, Nierensteinen oder Hyperurikämie mit Begleiterkrankungen. Beratung ist mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Darf ich bei Gicht Hülsenfrüchte essen?", "Ja. Pflanzliche Purine (Bohnen, Linsen, Erbsen) erhöhen das Gicht-Risiko in großen Studien nicht. Tierische Purine sind das Problem."),
            ("Ist Bier wirklich so schlimm?", "Ja. Bier enthält besonders viele Purine (auch alkoholfreies!). Schon 1 Bier/Tag erhöht das Gicht-Risiko deutlich. Wein in moderaten Mengen ist neutraler."),
            ("Helfen Kirschen wirklich?", "Studien zeigen: 10–12 Kirschen täglich oder 1 Tasse Tart-Cherry-Juice senkt das Risiko akuter Anfälle. Effekt ähnlich wie bei manchen Medikamenten."),
            ("Übernimmt die Krankenkasse?", "Ja. Hyperurikämie / Gicht (ICD E79.0 / M10) ist erstattungsfähig nach §43 SGB V — typisch 80%."),
            ("Wie schnell wirkt Ernährung?", "Erste Senkung der Harnsäure innerhalb von 2–4 Wochen. Volle Wirkung nach 2–3 Monaten."),
        ],
        "quellen": [
            ("Richette P et al.", "(2017): „2016 updated EULAR evidence-based recommendations for the management of gout.\" Ann Rheum Dis, 76:29–42.", "https://ard.bmj.com/content/76/1/29"),
            ("Choi HK et al.", "(2004): „Purine-rich foods, dairy and protein intake, and the risk of gout in men.\" N Engl J Med, 350:1093–1103.", "https://www.nejm.org/doi/full/10.1056/NEJMoa035700"),
            ("Zhang Y et al.", "(2012): „Cherry consumption and decreased risk of recurrent gout attacks.\" Arthritis Rheum, 64(12):4004–4011.", "https://onlinelibrary.wiley.com/doi/10.1002/art.34677"),
            ("FitzGerald JD et al.", "(2020): „2020 American College of Rheumatology Guideline for the Management of Gout.\" Arthritis Care Res, 72:744–760.", "https://onlinelibrary.wiley.com/doi/10.1002/acr.24180"),
            ("DGRh", "(2023): „S2e-Leitlinie Gichtarthritis.\" AWMF-Register 060/005.", "https://www.awmf.org"),
            ("DGE", "(2024): „Vollwertige Ernährung bei Hyperurikämie.\"", "https://www.dge.de"),
        ],
        "related": ["adipositas-ernaehrungstherapie", "fettleber-ernaehrung", "hypertonie-ernaehrung"],
    },
    {
        "slug": "osteoporose-ernaehrung",
        "title_short": "Osteoporose",
        "title_full": "Osteoporose & Ernährung: Kalzium, Vitamin D, Eiweiß",
        "icd": "M80–M82",
        "icd_schema": "M80-M82",
        "name_schema": "Osteoporose",
        "alt_names": ["Knochenschwund"],
        "h1_top": "Osteoporose:",
        "h1_bottom": "Knochen-Aufbau durch Ernährung.",
        "meta_desc": "Osteoporose (ICD M80–M82): Kalzium, Vitamin D, Eiweiß — was Knochen wirklich stärkt. DVO-Leitlinie, evidenzbasiert. Münster, Kassen-Zuschuss.",
        "keywords": "Osteoporose Ernährung, Kalzium, Vitamin D, Knochengesundheit, DVO-Leitlinie, REHAB FIVE Nutrition",
        "symptoms": ["Verminderte Knochendichte (T-Score < -2,5)", "Erhöhte Frakturneigung", "Größenverlust", "Wirbelkörperfrakturen"],
        "treatments": ["Kalzium 1000–1200 mg/Tag", "Vitamin D 800–1000 IE/Tag", "Eiweiß 1,0–1,2 g/kg KG", "Krafttraining"],
        "quick": "Bei <strong>Osteoporose (ICD M80–M82)</strong> sind <strong>Kalzium (1000–1200 mg/Tag)</strong>, <strong>Vitamin D (800–1000 IE/Tag)</strong> und ausreichend <strong>Eiweiß (1,0–1,2 g/kg KG)</strong> entscheidend. Krafttraining und Bewegung sind unverzichtbar — Ernährung allein reicht nicht. Kasse erstattet die Beratung typisch zu 80%.",
        "sections": [
            ("Was ist Osteoporose?", "Osteoporose ist eine systemische Skeletterkrankung mit verminderter Knochendichte und erhöhtem Frakturrisiko. Diagnose über Knochendichtemessung (DXA) — T-Score < -2,5. In Deutschland sind über 6 Millionen Menschen betroffen, vor allem Frauen nach der Menopause.[1]"),
            ("DVO-Leitlinie 2023 — Ernährungs-Eckpfeiler", "<ul><li><strong>Kalzium:</strong> 1000–1200 mg/Tag, bevorzugt aus Milchprodukten (Quark, Käse, Joghurt). Pflanzliche Quellen: Brokkoli, Grünkohl, Mandeln, kalziumreiches Mineralwasser (> 400 mg/l)</li><li><strong>Vitamin D:</strong> 800–1000 IE/Tag, im Winter Supplementierung empfohlen — die Eigensynthese durch Sonnenlicht reicht in Mitteleuropa nicht aus</li><li><strong>Eiweiß:</strong> 1,0–1,2 g/kg KG, ältere Menschen sogar 1,2–1,5 g — Eiweißmangel beschleunigt Knochenabbau</li><li><strong>Magnesium, Vitamin K:</strong> aus Vollkorn, Nüssen, grünem Gemüse</li><li><strong>Reduzieren:</strong> Salz (> 6 g/Tag fördert Kalziumverlust), Cola (Phosphorsäure), Alkohol, Rauchen</li></ul>"),
            ("Mythos „Milch macht Knochen brüchig\"", "Studien zeigen das Gegenteil: Moderate Milchprodukte (200–400 g/Tag) reduzieren das Frakturrisiko signifikant. Wer keine Milch verträgt: Hartkäse (laktosearm), Joghurt oder pflanzliche Drinks mit Kalzium-Anreicherung.[2]"),
            ("Wann professionelle Begleitung?", "Bei Osteoporose-Diagnose, nach Fraktur ohne adäquates Trauma, bei Risikofaktoren (Glukokortikoide, frühe Menopause, Untergewicht). Bei Osteoporose (ICD M80–M82) ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Wie viel Kalzium brauche ich täglich?", "Bei Osteoporose 1000–1200 mg/Tag. Beispiel: 200 g Joghurt + 50 g Käse + 200 ml Mineralwasser (kalziumreich) decken etwa 1000 mg."),
            ("Reicht Sonnenlicht für Vitamin D?", "In Mitteleuropa von Oktober bis April nicht — Supplementierung empfohlen (800–1000 IE/Tag). Im Sommer 15–20 Min Sonne (Gesicht/Arme) reichen oft."),
            ("Schadet zu viel Eiweiß den Knochen?", "Nein — moderne Studien zeigen sogar, dass Eiweißmangel das größere Problem ist. 1,0–1,2 g/kg KG ist sicher und förderlich."),
            ("Übernimmt die Krankenkasse?", "Ja. Osteoporose (ICD M80–M82) ist erstattungsfähig nach §43 SGB V — typisch 80%."),
            ("Welche Rolle spielt Bewegung?", "Sehr wichtig. Krafttraining (2× pro Woche) und Stoßbelastungen aktivieren den Knochenaufbau direkt — Ernährung allein reicht nicht."),
        ],
        "quellen": [
            ("DVO", "(2023): „S3-Leitlinie Osteoporose.\" AWMF-Register 183/001.", "https://www.awmf.org/leitlinien/detail/ll/183-001.html"),
            ("Bischoff-Ferrari HA et al.", "(2017): „Calcium intake and hip fracture risk in men and women: a meta-analysis.\" Am J Clin Nutr, 86(6):1780–1790.", "https://academic.oup.com/ajcn/article/86/6/1780/4757381"),
            ("Rizzoli R et al.", "(2018): „Benefits and safety of dietary protein for bone health.\" Osteoporos Int, 29:1933–1948.", "https://link.springer.com/article/10.1007/s00198-018-4534-5"),
            ("DGE", "(2024): „Referenzwerte für Kalzium und Vitamin D.\"", "https://www.dge.de"),
            ("IOF (International Osteoporosis Foundation)", "(2024): „Nutrition for bone health.\"", "https://www.osteoporosis.foundation/"),
            ("EFSA", "(2022): „Scientific opinion on dietary reference values for vitamin D.\"", "https://www.efsa.europa.eu"),
        ],
        "related": ["zoeliakie-ernaehrung", "wechseljahre-ernaehrung", "untergewicht-mangelernaehrung"],
    },
    {
        "slug": "reflux-gerd-ernaehrung",
        "title_short": "Reflux / GERD",
        "title_full": "Reflux & GERD: Was Ernährung wirklich verändert",
        "icd": "K21",
        "icd_schema": "K21",
        "name_schema": "Refluxkrankheit",
        "alt_names": ["GERD", "Sodbrennen", "Refluxösophagitis"],
        "h1_top": "Reflux:",
        "h1_bottom": "Sodbrennen am Teller stoppen.",
        "meta_desc": "Reflux / GERD (ICD K21): Welche Ernährung Sodbrennen reduziert — Triggerfaktoren, mediterrane Kost, Lebensstil. Kassen-Zuschuss in Münster.",
        "keywords": "Reflux Ernährung, Sodbrennen, GERD Diät, Refluxösophagitis, Ernährung bei Reflux, REHAB FIVE Nutrition",
        "symptoms": ["Sodbrennen", "Saures Aufstoßen", "Druck hinter dem Brustbein", "Globusgefühl", "Heiserkeit morgens"],
        "treatments": ["Mediterrane Ernährung", "Trigger-Vermeidung", "Spätes Essen vermeiden", "Gewichtsreduktion"],
        "quick": "Bei <strong>Reflux / GERD (ICD K21)</strong> hilft Ernährung deutlich: <strong>Mediterrane Kost</strong> reduziert in Studien die Refluxsymptome bei vielen Patient:innen vergleichbar mit PPI-Medikamenten. Trigger meiden (Schokolade, Pfefferminze, Alkohol, fetthaltiges Essen, scharfes Essen, Kaffee). <strong>Letzte Mahlzeit 3 Stunden vor dem Schlafen.</strong> Kasse erstattet die Beratung typisch zu 80%.",
        "sections": [
            ("Was ist GERD?", "Die Gastroösophageale Refluxkrankheit (GERD, ICD K21) entsteht durch Rückfluss von Magensäure in die Speiseröhre — meist wegen unzureichender Funktion des unteren Speiseröhrenschließmuskels. Symptome: Sodbrennen, Aufstoßen, Druck retrosternal. Langfristig: Refluxösophagitis, Barrett-Ösophagus.[1]"),
            ("Was Ernährung wirklich bewirken kann", "Die <strong>Mediterrane Ernährung</strong> hat in einer wegweisenden Studie (Zalvan et al. 2017) Reflux-Symptome stärker reduziert als hochdosierte PPI-Medikamente.[2] Praktische Empfehlungen:<ul><li><strong>Reduzieren:</strong> Schokolade, Pfefferminze, Kaffee, Alkohol (besonders Wein), Cola, fettreiche Speisen, scharfe Gewürze, Tomaten, Zitrusfrüchte (individuell)</li><li><strong>Bevorzugen:</strong> Gemüse, Vollkorn, magere Eiweißquellen, Olivenöl, ungesüßte Getränke</li><li><strong>Mahlzeitenstruktur:</strong> kleinere Portionen, 4–5× pro Tag, letzte Mahlzeit 3 Stunden vor dem Schlafen</li><li><strong>Gewichtsreduktion:</strong> 5–10% Reduktion kann bei Übergewicht die Symptome deutlich lindern</li><li><strong>Schlafposition:</strong> Oberkörper hochlagern, linke Seite</li></ul>"),
            ("Ernährungs-Tagebuch — der schnellste Weg zu deinen Triggern", "Trigger sind individuell. Ein 14-Tage-Symptom-Tagebuch hilft, persönliche Auslöser zu identifizieren — wirkungsvoller als pauschale Verbotslisten."),
            ("Wann professionelle Begleitung?", "Bei chronischen Beschwerden (> 4 Wochen), PPI-Abhängigkeit, Barrett-Ösophagus oder unklaren Schluckbeschwerden. Bei Reflux (ICD K21) ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Kann Ernährung PPI-Medikamente ersetzen?", "Bei milder bis mittelschwerer GERD ja — Studien zeigen vergleichbare Effekte. Bei schwerer Refluxösophagitis oder Barrett-Ösophagus sollte die medikamentöse Therapie in Abstimmung mit der Ärztin / dem Arzt bestehen bleiben."),
            ("Welche Lebensmittel sind die häufigsten Trigger?", "Schokolade, Pfefferminze, Alkohol, fetthaltige und frittierte Speisen, Kaffee, scharfe Gewürze. Individuell oft auch Tomaten und Zitrusfrüchte."),
            ("Wie lange dauert es, bis Ernährung wirkt?", "Erste Verbesserungen oft schon in 1–2 Wochen. Volle Wirkung nach 6–8 Wochen konsequenter Umstellung."),
            ("Übernimmt die Krankenkasse?", "Ja. Reflux (ICD K21) ist erstattungsfähig nach §43 SGB V — typisch 80%."),
            ("Hilft Schlafposition?", "Ja. Linke Seitenlage und leicht erhöhter Oberkörper reduzieren nächtliche Refluxepisoden signifikant."),
        ],
        "quellen": [
            ("Zalvan CH et al.", "(2017): „A Comparison of Alkaline Water and Mediterranean Diet vs PPI in Laryngopharyngeal Reflux.\" JAMA Otolaryngol Head Neck Surg, 143(10):1023–1029.", "https://jamanetwork.com/journals/jamaotolaryngology/fullarticle/2649381"),
            ("Katz PO et al.", "(2022): „ACG Clinical Guideline for the Diagnosis and Management of Gastroesophageal Reflux Disease.\" Am J Gastroenterol, 117(1):27–56.", "https://journals.lww.com/ajg/Fulltext/2022/01000/ACG_Clinical_Guideline_for_the_Diagnosis_and.14.aspx"),
            ("Ness-Jensen E et al.", "(2016): „Lifestyle intervention in gastroesophageal reflux disease.\" Clin Gastroenterol Hepatol, 14(2):175–182.", "https://www.cghjournal.org/article/S1542-3565(15)01088-0/fulltext"),
            ("DGVS", "(2023): „S2k-Leitlinie Gastroösophageale Refluxkrankheit.\" AWMF-Register 021/013.", "https://www.awmf.org/leitlinien/detail/ll/021-013.html"),
            ("Singh M et al.", "(2013): „Weight loss can lead to resolution of gastroesophageal reflux disease symptoms.\" Obesity, 21:284–290.", "https://onlinelibrary.wiley.com/doi/10.1002/oby.20279"),
            ("DGE", "(2024): „Vollwertige Ernährung bei Refluxbeschwerden.\"", "https://www.dge.de"),
        ],
        "related": ["adipositas-ernaehrungstherapie", "reizdarm-syndrom-ernaehrung", "fettleber-ernaehrung"],
    },
    {
        "slug": "rheumatoide-arthritis-ernaehrung",
        "title_short": "Rheumatoide Arthritis",
        "title_full": "Rheumatoide Arthritis & Ernährung: Anti-entzündlich essen",
        "icd": "M05–M06",
        "icd_schema": "M05-M06",
        "name_schema": "Rheumatoide Arthritis",
        "alt_names": ["Rheuma", "RA"],
        "h1_top": "Rheuma:",
        "h1_bottom": "Entzündung durch den Teller bremsen.",
        "meta_desc": "Rheumatoide Arthritis (ICD M05–M06): Anti-entzündliche Ernährung, Omega-3, Mediterrane Kost — Beschwerden lindern. Kassen-Zuschuss in Münster.",
        "keywords": "Rheumatoide Arthritis Ernährung, Rheuma essen, anti-entzündlich, Omega-3 Rheuma, mediterrane Ernährung, REHAB FIVE Nutrition",
        "symptoms": ["Symmetrische Gelenkentzündung", "Morgensteifigkeit > 1h", "Schmerzen Hand-, Fußgelenke", "Erhöhte Entzündungsmarker (CRP)"],
        "treatments": ["Mediterrane / anti-entzündliche Ernährung", "Omega-3-Fettsäuren", "Pflanzenbetonte Mischkost", "Optional Fasten unter Begleitung"],
        "quick": "Bei <strong>rheumatoider Arthritis (ICD M05–M06)</strong> wirkt eine <strong>anti-entzündliche, mediterrane Ernährung</strong> nachweislich — Studien zeigen Reduktion von Schmerz und Morgensteifigkeit um <strong>20–30 %</strong>. <strong>Omega-3-Fettsäuren</strong> (fettiger Fisch, Leinöl) sind besonders wichtig. Pflanzenbetonte Kost, wenig rotes Fleisch, kein Zucker. Kasse erstattet die Beratung typisch zu 80%.",
        "sections": [
            ("Was ist rheumatoide Arthritis?", "Die rheumatoide Arthritis (RA) ist eine chronisch-entzündliche Autoimmunerkrankung der Gelenke. Charakteristisch: symmetrische Entzündung kleiner Gelenke, Morgensteifigkeit > 1 Stunde, erhöhte Entzündungsmarker (CRP, BSG). In Deutschland sind etwa 500.000 Menschen betroffen.[1]"),
            ("Anti-entzündliche Ernährung — was die Evidenz zeigt", "Eine <strong>mediterrane Ernährung</strong> reduziert in mehreren Studien Schmerz, Morgensteifigkeit und Krankheitsaktivität bei RA-Patient:innen.[2] Wichtige Bausteine:<ul><li><strong>Omega-3-Fettsäuren:</strong> 2–3 g EPA+DHA pro Tag (Fisch oder Algenöl). Studien zeigen klare entzündungshemmende Effekte</li><li><strong>Olivenöl extra vergine</strong> (3 EL/Tag) — Oleocanthal wirkt ähnlich wie Ibuprofen</li><li><strong>Reichlich Gemüse, Beeren, Vollkorn</strong> — Polyphenole, Antioxidantien</li><li><strong>Hülsenfrüchte und Nüsse</strong></li><li><strong>Wenig rotes Fleisch und Wurst</strong> — fördern Entzündung</li><li><strong>Zucker und hochverarbeitete Produkte deutlich reduzieren</strong></li></ul>"),
            ("Heilfasten / intermittierendes Fasten", "Studien zeigen, dass mehrtägiges Fasten unter ärztlicher Begleitung bei RA-Patient:innen kurzfristig Symptome reduzieren kann. Anschließende vegetarisch-mediterrane Kost erhält die Effekte oft 6–12 Monate.[3] Wichtig: Fasten nur unter Begleitung — Methotrexat und Biologica beachten!"),
            ("Wann professionelle Begleitung?", "Bei RA-Diagnose, schlechtem Ansprechen auf Medikamente, Gewichtsproblemen, Begleiterkrankungen (Osteoporose, Kardiovaskulär). Bei RA (ICD M05–M06) ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Hilft Ernährung wirklich bei Rheuma?", "Ja, ergänzend. Sie ersetzt keine Basistherapie (Methotrexat, Biologica), kann aber Schmerz, Morgensteifigkeit und Krankheitsaktivität signifikant reduzieren."),
            ("Welche Lebensmittel sollte ich meiden?", "Rotes und verarbeitetes Fleisch, Zucker, Transfette (Frittiertes), hochverarbeitete Produkte. Bei einigen Patient:innen auch Milchprodukte und Nachtschattengewächse — individuell prüfen."),
            ("Wie viel Omega-3 ist sinnvoll?", "2–3 g EPA+DHA pro Tag aus fettem Fisch (2× pro Woche) oder hochwertigen Kapseln. Pflanzlich (Lein, Walnuss) ist eine Ergänzung, ersetzt aber EPA/DHA nicht vollständig."),
            ("Übernimmt die Krankenkasse?", "Ja. Rheumatoide Arthritis (ICD M05–M06) ist erstattungsfähig nach §43 SGB V — typisch 80%."),
            ("Ist Heilfasten sinnvoll?", "Unter ärztlicher Begleitung kann es Beschwerden kurzfristig lindern. Wichtig: Methotrexat-Dosis und Hydrierung beachten. Eigentherapie nicht empfohlen."),
        ],
        "quellen": [
            ("Smolen JS et al.", "(2023): „EULAR recommendations for the management of rheumatoid arthritis with synthetic and biological disease-modifying antirheumatic drugs.\" Ann Rheum Dis, 82:3–18.", "https://ard.bmj.com/content/82/1/3"),
            ("Forsyth C et al.", "(2018): „The effects of the Mediterranean diet on rheumatoid arthritis prevention and treatment: a systematic review.\" Rheumatol Int, 38:737–747.", "https://link.springer.com/article/10.1007/s00296-017-3912-1"),
            ("Müller H et al.", "(2001): „Fasting followed by vegetarian diet in patients with rheumatoid arthritis: a systematic review.\" Scand J Rheumatol, 30:1–10.", "https://www.tandfonline.com/doi/abs/10.1080/030097401750065256"),
            ("DGRh", "(2023): „S3-Leitlinie Management der frühen rheumatoiden Arthritis.\" AWMF-Register 060/002.", "https://www.awmf.org/leitlinien/detail/ll/060-002.html"),
            ("Sköldstam L et al.", "(2003): „An experimental study of a Mediterranean diet intervention for patients with rheumatoid arthritis.\" Ann Rheum Dis, 62:208–214.", "https://ard.bmj.com/content/62/3/208"),
            ("Deutsche Rheuma-Liga", "(2024): „Ernährung bei Rheuma.\"", "https://www.rheuma-liga.de"),
        ],
        "related": ["osteoporose-ernaehrung", "fettleber-ernaehrung", "diabetes-typ-2-ernaehrung"],
    },
    {
        "slug": "laktose-intoleranz-ernaehrung",
        "title_short": "Laktose-Intoleranz",
        "title_full": "Laktose-Intoleranz: Diagnostik, Karenz, Reintroduktion",
        "icd": "E73",
        "icd_schema": "E73",
        "name_schema": "Laktose-Intoleranz",
        "alt_names": ["Milchzucker-Unverträglichkeit", "Hypolaktasie"],
        "h1_top": "Laktose-Intoleranz:",
        "h1_bottom": "Diagnostik & strukturierte Karenz.",
        "meta_desc": "Laktose-Intoleranz (ICD E73): Diagnose per H2-Atemtest, individuelle Toleranz, Mikronährstoff-Sicherung. Kassen-Zuschuss in Münster.",
        "keywords": "Laktose-Intoleranz, Milchzucker-Unverträglichkeit, H2-Atemtest, laktosefrei, Hypolaktasie, REHAB FIVE Nutrition",
        "symptoms": ["Blähungen nach Milchprodukten", "Bauchschmerzen", "Durchfall", "Übelkeit"],
        "treatments": ["Strukturierte Karenz", "Reintroduktion zur Toleranz-Ermittlung", "Laktase-Präparate bei Bedarf", "Kalzium-Sicherung"],
        "quick": "<strong>Laktose-Intoleranz (ICD E73)</strong> ist keine Krankheit, sondern ein Enzymdefizit (Laktase). 15–25 % der Erwachsenen in Deutschland betroffen. Wichtig: <strong>nicht pauschal verzichten</strong> — die meisten vertragen 5–12 g Laktose/Tag. Strukturierte Toleranz-Ermittlung statt Verbote. Kalzium-Versorgung sichern. Kasse erstattet die Beratung typisch zu 80%.",
        "sections": [
            ("Was ist Laktose-Intoleranz?", "Laktose-Intoleranz ist ein Mangel des Enzyms Laktase, das den Milchzucker (Laktose) in Glukose und Galaktose spaltet. Folge: unverdaute Laktose gelangt in den Dickdarm, wird fermentiert — Blähungen, Bauchschmerzen, Durchfall. Genetisch bedingt oder sekundär nach Darminfekt / bei Zöliakie.[1]"),
            ("Diagnose: H2-Atemtest", "Der <strong>H2-Atemtest</strong> ist der Goldstandard: nach Trinken einer Laktose-Lösung wird Wasserstoff in der Atemluft gemessen — erhöhte Werte beweisen die Unverdaulichkeit. Alternativ: Laktose-Toleranz-Test (Blutzucker). Gentest auf LCT-Polymorphismus möglich, aber selten nötig.[2]"),
            ("Individuelle Toleranz — die meisten verzehren mehr als gedacht", "Studien zeigen: 80 % der Laktose-Intoleranten vertragen <strong>5–12 g Laktose pro Mahlzeit</strong> ohne Symptome — das entspricht 100–250 ml Milch. Was hilft:<ul><li><strong>Reifer Käse:</strong> Hartkäse (Parmesan, Bergkäse) enthält < 0,1 g Laktose pro Portion — meist unproblematisch</li><li><strong>Joghurt:</strong> die enthaltenen Milchsäurebakterien spalten Laktose teilweise vor</strong></li><li><strong>Kleine Mengen über den Tag verteilt</strong> statt Milch-Bombe</li><li><strong>Laktose mit anderen Lebensmitteln kombinieren</strong> (Frühstück, nicht solo)</li><li><strong>Laktase-Präparate</strong> bei ausnahmsweisem Konsum</li></ul>"),
            ("Wann professionelle Begleitung?", "Wenn deine Toleranz unklar ist, du unnötig stark restriktiv lebst oder ein begleitendes Reizdarmsyndrom besteht. Bei Laktose-Intoleranz (ICD E73) ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Muss ich auf alle Milchprodukte verzichten?", "Nein. Die meisten Betroffenen vertragen 5–12 g Laktose pro Mahlzeit. Hartkäse und Joghurt sind oft unproblematisch."),
            ("Wie sichere ich meine Kalzium-Versorgung?", "Hartkäse, kalziumreiches Mineralwasser (> 400 mg/l), Brokkoli, Grünkohl, Mandeln, kalziumangereicherte Pflanzendrinks. Wir berechnen das in der Beratung individuell."),
            ("Was unterscheidet Laktose-Intoleranz von Milchallergie?", "Allergie ist eine Immunreaktion gegen Milchproteine (selten, oft im Kindesalter). Laktose-Intoleranz ist ein Enzymmangel — kein Immungeschehen, keine schwere Reaktion."),
            ("Übernimmt die Krankenkasse?", "Ja. Laktose-Intoleranz (ICD E73) ist erstattungsfähig nach §43 SGB V — typisch 80%."),
            ("Sind Laktase-Tabletten sinnvoll?", "Ja, für Ausnahme-Situationen (Restaurant, Urlaub). Für den Alltag ist die strukturierte Anpassung der Ernährung effektiver."),
        ],
        "quellen": [
            ("Misselwitz B et al.", "(2019): „Update on lactose malabsorption and intolerance.\" Gut, 68:2080–2091.", "https://gut.bmj.com/content/68/11/2080"),
            ("Suchy FJ et al.", "(2010): „NIH Consensus Development Conference Statement: Lactose Intolerance and Health.\" Ann Intern Med, 152:792–796.", "https://www.acpjournals.org/doi/10.7326/0003-4819-152-12-201006150-00248"),
            ("Hammer HF et al.", "(2022): „European H2-CH4-breath test group consensus.\" United European Gastroenterol J, 10:15–40.", "https://onlinelibrary.wiley.com/doi/10.1002/ueg2.12133"),
            ("Lomer MC", "(2015): „Review article: the aetiology, diagnosis, mechanisms and clinical evidence for food intolerance.\" Aliment Pharmacol Ther, 41:262–275.", "https://onlinelibrary.wiley.com/doi/10.1111/apt.13041"),
            ("DGE", "(2024): „Vollwertige Ernährung bei Laktose-Intoleranz.\"", "https://www.dge.de"),
            ("EFSA", "(2010): „Scientific Opinion on lactose thresholds in lactose intolerance and galactosaemia.\" EFSA Journal, 8(9):1777.", "https://www.efsa.europa.eu/en/efsajournal/pub/1777"),
        ],
        "related": ["zoeliakie-ernaehrung", "reizdarm-syndrom-ernaehrung", "fructose-malabsorption-ernaehrung"],
    },
    {
        "slug": "fructose-malabsorption-ernaehrung",
        "title_short": "Fructose-Malabsorption",
        "title_full": "Fructose-Malabsorption: H2-Atemtest & 3-Stufen-Protokoll",
        "icd": "E74.1",
        "icd_schema": "E74.1",
        "name_schema": "Fructose-Malabsorption",
        "alt_names": ["Fructose-Intoleranz (intestinal)"],
        "h1_top": "Fructose-Malabsorption:",
        "h1_bottom": "Strukturierte Karenz & Toleranz.",
        "meta_desc": "Fructose-Malabsorption (ICD E74.1): Diagnostik per H2-Atemtest, 3-Stufen-Protokoll, individuelle Toleranz finden. Kassen-Zuschuss in Münster.",
        "keywords": "Fructose-Malabsorption, Fruchtzucker-Unverträglichkeit, H2-Atemtest, fructosearm, Sorbit, REHAB FIVE Nutrition",
        "symptoms": ["Blähungen nach Obst / Süßem", "Bauchschmerzen", "Durchfall", "Übelkeit"],
        "treatments": ["3-Stufen-Karenz-Reintroduktion", "Glukose-Kombination zur Toleranz", "Sorbit-Reduktion", "FODMAP-Konzept ergänzend"],
        "quick": "Bei <strong>Fructose-Malabsorption (ICD E74.1)</strong> wird Fruchtzucker im Dünndarm unzureichend resorbiert — Symptome wie Blähungen, Bauchschmerzen, Durchfall. Wichtig: <strong>Abgrenzung von der seltenen, schweren hereditären Fructose-Intoleranz (HFI)</strong>. Die intestinale Form lässt sich mit einem 3-Stufen-Protokoll (Karenz, Test, Toleranz) gut managen. Kasse erstattet die Beratung typisch zu 80%.",
        "sections": [
            ("Was ist Fructose-Malabsorption?", "Bei intestinaler Fructose-Malabsorption wird Fructose unzureichend über den GLUT5-Transporter im Dünndarm aufgenommen. Sie gelangt in den Dickdarm, wird fermentiert — Symptome. Wichtig: Das ist <strong>nicht</strong> die seltene, lebensbedrohliche hereditäre Fructose-Intoleranz (HFI), die einen kompletten lebenslangen Verzicht erfordert.[1]"),
            ("Diagnose & Abgrenzung", "<strong>H2-Atemtest mit 25 g Fructose</strong> ist Standard. Vorher ärztliche Anamnese zur Abgrenzung der HFI (Aldolase-B-Defekt). Häufige Kombination: <strong>Sorbit-Intoleranz</strong> — Sorbit blockiert den GLUT5-Transporter zusätzlich.[2]"),
            ("Das 3-Stufen-Protokoll", "<ol><li><strong>Karenzphase (2–4 Wochen):</strong> strikt fructosearm — Symptomfreiheit als Ziel</li><li><strong>Testphase (4–6 Wochen):</strong> schrittweise Wiedereinführung in kleinen Mengen, gemeinsam mit <strong>Glukose</strong> (Glukose erleichtert die Fructose-Resorption)</li><li><strong>Dauerernährung:</strong> individuell tolerierte Menge — meist 8–15 g Fructose pro Mahlzeit möglich</li></ol>Vermieden werden in Phase 1: Apfel, Birne, Mango, Süßstoffe (Sorbit, Xylit), Honig, Agavendicksaft, Fruchtsaft.<br>Bevorzugt: Banane, Beeren, Zitrusfrüchte (Fructose:Glukose-Verhältnis ≤ 1)."),
            ("Wann professionelle Begleitung?", "Bei unklarer Diagnose, ausbleibender Besserung nach Karenz oder gleichzeitigem Reizdarm. Bei Fructose-Malabsorption (ICD E74.1) ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Muss ich alle Obstsorten meiden?", "Nein. Beeren, Zitrusfrüchte und Bananen werden meist gut vertragen (Glukose:Fructose-Verhältnis günstig). Apfel, Birne, Mango sind kritischer."),
            ("Was ist der Unterschied zur hereditären Fructose-Intoleranz (HFI)?", "HFI ist eine seltene, lebensbedrohliche Enzymdefekt-Erkrankung — strikter, lebenslanger Verzicht nötig. Intestinale Malabsorption ist häufig und meist gut managebar."),
            ("Hilft Glukose dabei, Fructose besser zu verdauen?", "Ja. Glukose unterstützt die Fructose-Resorption über den GLUT2-Transporter. Praktisch bedeutet das: Obst lieber zu Mahlzeiten mit Stärke essen, nicht solo."),
            ("Übernimmt die Krankenkasse?", "Ja. Fructose-Malabsorption (ICD E74.1) ist erstattungsfähig nach §43 SGB V — typisch 80%."),
            ("Hat das was mit Reizdarm zu tun?", "Ja. Bei vielen Reizdarm-Patient:innen findet sich begleitend eine Fructose-Malabsorption. Das Low-FODMAP-Konzept adressiert beide gleichzeitig."),
        ],
        "quellen": [
            ("Fedewa A, Rao SS", "(2014): „Dietary fructose intolerance, fructan intolerance and FODMAPs.\" Curr Gastroenterol Rep, 16:370.", "https://link.springer.com/article/10.1007/s11894-013-0370-0"),
            ("Hammer HF et al.", "(2022): „European H2-CH4-breath test group consensus.\" United European Gastroenterol J, 10:15–40.", "https://onlinelibrary.wiley.com/doi/10.1002/ueg2.12133"),
            ("Born P", "(2007): „Carbohydrate malabsorption in patients with non-specific abdominal complaints.\" World J Gastroenterol, 13:5687–5691.", "https://www.wjgnet.com/1007-9327/full/v13/i43/5687.htm"),
            ("DGVS", "(2023): „S3-Leitlinie Reizdarmsyndrom (FODMAP-Konzept).\" AWMF-Register 021/016.", "https://www.awmf.org/leitlinien/detail/ll/021-016.html"),
            ("Wilder-Smith CH et al.", "(2013): „Fructose and lactose intolerance and malabsorption testing.\" Aliment Pharmacol Ther, 37:1074–1083.", "https://onlinelibrary.wiley.com/doi/10.1111/apt.12306"),
            ("Monash University", "(2024): „FODMAP-Datenbank.\"", "https://www.monashfodmap.com/"),
        ],
        "related": ["reizdarm-syndrom-ernaehrung", "laktose-intoleranz-ernaehrung", "sorbit-intoleranz-ernaehrung"],
    },
    {
        "slug": "sorbit-intoleranz-ernaehrung",
        "title_short": "Sorbit-Intoleranz",
        "title_full": "Sorbit-Intoleranz: Karenz, versteckte Quellen, Toleranz",
        "icd": "E74.3",
        "icd_schema": "E74.3",
        "name_schema": "Sorbit-Intoleranz",
        "alt_names": ["Sorbitol-Intoleranz"],
        "h1_top": "Sorbit-Intoleranz:",
        "h1_bottom": "Versteckte Quellen erkennen.",
        "meta_desc": "Sorbit-Intoleranz (ICD E74.3): Diagnostik, versteckte Quellen in Kaugummi, zuckerfreien Produkten und Steinobst. Kassen-Zuschuss in Münster.",
        "keywords": "Sorbit-Intoleranz, Sorbitol, zuckerfrei, E420, Kaugummi Sorbit, REHAB FIVE Nutrition",
        "symptoms": ["Blähungen", "Bauchschmerzen", "Durchfall nach Sorbit-haltigen Produkten"],
        "treatments": ["Karenz mit Reintroduktion", "Lesen von Zutatenlisten (E420)", "Vermeidung versteckter Quellen"],
        "quick": "<strong>Sorbit-Intoleranz (ICD E74.3)</strong> entsteht durch unzureichende Resorption des Zuckeralkohols Sorbit. Hauptquellen: <strong>zuckerfreie Produkte, Kaugummi, Bonbons, Steinobst</strong> (Pflaume, Pfirsich, Aprikose). Häufig kombiniert mit Fructose-Malabsorption. Strukturierte Karenz und Toleranz-Findung sind der Weg. Kasse erstattet die Beratung typisch zu 80%.",
        "sections": [
            ("Was ist Sorbit-Intoleranz?", "Sorbit (E420) ist ein Zuckeralkohol, der industriell als Süßungsmittel in zuckerfreien Produkten eingesetzt wird — natürlich vorkommend in Steinobst und Trockenfrüchten. Bei unzureichender Resorption gelangt Sorbit in den Dickdarm und verursacht osmotische Diarrhö und Blähungen. Sorbit hemmt zudem den GLUT5-Transporter und verstärkt Fructose-Malabsorption.[1]"),
            ("Versteckte Quellen erkennen", "<ul><li><strong>Süßstoff-Etikett:</strong> E420, Sorbit, Sorbitol, Sorbitolsirup</li><li><strong>Zuckerfreie Produkte:</strong> Kaugummi, Bonbons, Schokolade, Gummibärchen</li><li><strong>Medikamente / Hustensaft:</strong> oft Sorbit als Trägerstoff</li><li><strong>Steinobst:</strong> Pflaumen, Aprikosen, Pfirsiche, Kirschen</li><li><strong>Trockenfrüchte:</strong> besonders konzentriert</li><li><strong>Light-Joghurts und Diätprodukte</strong></li></ul>"),
            ("3-Stufen-Protokoll wie bei Fructose", "<ol><li><strong>Karenzphase (2–4 Wochen):</strong> strikt sorbitarm</li><li><strong>Testphase:</strong> schrittweise Wiedereinführung in definierten Mengen</li><li><strong>Dauerernährung:</strong> individuelle Toleranzgrenze ermitteln — meist 5–10 g/Tag möglich</li></ol>Bei kombinierter Fructose-Sorbit-Problematik: gemeinsames Vorgehen, das die Wechselwirkung berücksichtigt."),
            ("Wann professionelle Begleitung?", "Bei chronischen Beschwerden, unklaren Ergebnissen, kombinierten Intoleranzen oder Verdacht auf Reizdarm. Bei Sorbit-Intoleranz (ICD E74.3) ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Wie wird Sorbit-Intoleranz diagnostiziert?", "H2-Atemtest mit Sorbit-Lösung. Ärztliche Anamnese und Symptom-Tagebuch sind ergänzend wichtig."),
            ("Welche Lebensmittel sind besonders sorbit-reich?", "Trockenfrüchte (besonders Pflaumen), zuckerfreie Bonbons und Kaugummi, Light-Produkte, Steinobst."),
            ("Hängt Sorbit mit Fructose zusammen?", "Ja. Sorbit hemmt den GLUT5-Transporter, der Fructose resorbiert. Wer beides hat, sollte gemeinsam beraten werden."),
            ("Übernimmt die Krankenkasse?", "Ja. Sorbit-Intoleranz (ICD E74.3) ist erstattungsfähig nach §43 SGB V — typisch 80%."),
            ("Sind alle zuckerfreien Produkte tabu?", "Nein — wenn der Süßstoff Stevia, Erythrit oder Sucralose ist, oft unproblematisch. Achte auf die Zutatenliste."),
        ],
        "quellen": [
            ("Hammer HF et al.", "(2022): „European H2-CH4-breath test group consensus.\" United European Gastroenterol J, 10:15–40.", "https://onlinelibrary.wiley.com/doi/10.1002/ueg2.12133"),
            ("Fedewa A, Rao SS", "(2014): „Dietary fructose intolerance, fructan intolerance and FODMAPs.\" Curr Gastroenterol Rep, 16:370.", "https://link.springer.com/article/10.1007/s11894-013-0370-0"),
            ("Wilder-Smith CH et al.", "(2013): „Fructose and lactose intolerance and malabsorption testing.\" Aliment Pharmacol Ther, 37:1074–1083.", "https://onlinelibrary.wiley.com/doi/10.1111/apt.12306"),
            ("DGVS", "(2023): „S3-Leitlinie Reizdarmsyndrom.\" AWMF-Register 021/016.", "https://www.awmf.org/leitlinien/detail/ll/021-016.html"),
            ("Monash University", "(2024): „FODMAP-Datenbank.\"", "https://www.monashfodmap.com/"),
            ("EFSA", "(2011): „Scientific Opinion on the substantiation of health claims related to sugar replacers.\" EFSA Journal, 9:2076.", "https://www.efsa.europa.eu"),
        ],
        "related": ["fructose-malabsorption-ernaehrung", "laktose-intoleranz-ernaehrung", "reizdarm-syndrom-ernaehrung"],
    },
    {
        "slug": "pcos-endometriose-ernaehrung",
        "title_short": "PCOS / Endometriose",
        "title_full": "PCOS & Endometriose: Anti-entzündlich, Insulin-bewusst essen",
        "icd": "E28.2 / N80",
        "icd_schema": "E28.2",
        "name_schema": "PCOS / Endometriose",
        "alt_names": ["Polyzystisches Ovarial-Syndrom", "Endometriose"],
        "h1_top": "PCOS & Endometriose:",
        "h1_bottom": "Insulin-bewusst & anti-entzündlich.",
        "meta_desc": "PCOS (ICD E28.2) und Endometriose (ICD N80): Mediterrane, anti-entzündliche, Insulin-bewusste Ernährung. Evidenzbasiert in Münster.",
        "keywords": "PCOS Ernährung, Endometriose, Insulinresistenz Ernährung, Inositol, mediterrane Ernährung Frauen, REHAB FIVE Nutrition",
        "symptoms": ["Zyklusstörungen", "Hirsutismus", "Akne", "Insulinresistenz", "Schmerzhafte Menstruation (Endometriose)"],
        "treatments": ["Mediterrane, anti-entzündliche Kost", "Niedriger glykämischer Index", "Omega-3-Fettsäuren", "Optional Inositol-Supplementierung"],
        "quick": "Bei <strong>PCOS (ICD E28.2)</strong> stehen <strong>Insulinresistenz</strong> und Entzündung im Zentrum — eine <strong>mediterrane, kohlenhydrat-bewusste</strong> Ernährung verbessert Zyklus, Akne und Fruchtbarkeit. Bei <strong>Endometriose (ICD N80)</strong> hilft anti-entzündliche Kost (Omega-3, Polyphenole) zur Schmerzreduktion. Gewicht-Stabilisierung wichtig. Kasse erstattet die Beratung typisch zu 80%.",
        "sections": [
            ("PCOS & Endometriose im Überblick", "PCOS (Polyzystisches Ovarial-Syndrom) ist die häufigste hormonelle Störung bei Frauen im gebärfähigen Alter — geprägt von Hyperandrogenämie, Zyklusstörungen, oft Insulinresistenz. Endometriose ist eine chronisch-entzündliche Erkrankung mit Endometrium-Gewebe außerhalb der Gebärmutter — starke Menstruations- und Beckenschmerzen.[1][2]"),
            ("PCOS — Ernährung als Schlüssel", "Die internationale PCOS-Leitlinie (Teede et al. 2023) empfiehlt:<ul><li><strong>Mediterrane oder DASH-Ernährung</strong> als Basis</li><li><strong>Niedriger glykämischer Index</strong> — Vollkorn, Hülsenfrüchte, Beeren</li><li><strong>Eiweißreiche Mahlzeiten</strong> (1,2 g/kg KG)</li><li><strong>Wenig Zucker und Fertigprodukte</strong> — Insulin-Spitzen vermeiden</li><li><strong>Bei Übergewicht:</strong> 5–10 % Gewichtsreduktion verbessert Zyklus und Fruchtbarkeit deutlich</li><li><strong>Inositol-Supplementierung (Myo + D-Chiro 40:1):</strong> in Studien bei PCOS hilfreich</li></ul>"),
            ("Endometriose — anti-entzündlich essen", "Mediterrane Kost mit hohem Omega-3-Anteil reduziert in Beobachtungsstudien Schmerzen und Krankheitsaktivität. Reduktion: rotes Fleisch (RR ↑), trans-Fette. Erhöhung: Gemüse, Fisch, Olivenöl, Beeren. Bei manchen Patientinnen lindert Low-FODMAP zusätzlich Reizdarm-Symptome, die mit Endometriose koexistieren.[3]"),
            ("Wann professionelle Begleitung?", "Bei Diagnose, Kinderwunsch, Insulinresistenz, deutlicher Gewichtsproblematik oder ausgeprägten Endometriose-Schmerzen. Bei PCOS / Endometriose ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Hilft Ernährung wirklich bei PCOS?", "Ja. Mediterrane, kohlenhydrat-bewusste Ernährung verbessert Zyklus, Insulinwerte, Hautbild und Fruchtbarkeit. In Kombination mit Bewegung sind die Effekte mit Metformin vergleichbar."),
            ("Brauche ich Inositol?", "Bei PCOS mit Insulinresistenz haben Studien moderate Effekte gezeigt (Myo-Inositol + D-Chiro im Verhältnis 40:1, 4 g/Tag). Vor Einnahme ärztlich abklären."),
            ("Welche Ernährung hilft bei Endometriose-Schmerzen?", "Anti-entzündlich, Omega-3-reich, mediterran. Reduktion von rotem Fleisch und trans-Fetten. Beobachtungsstudien zeigen Schmerz-Reduktion."),
            ("Übernimmt die Krankenkasse?", "Ja. PCOS (ICD E28.2) und Endometriose (ICD N80) sind erstattungsfähig nach §43 SGB V — typisch 80%."),
            ("Was, wenn ich abnehmen will?", "Bei PCOS reichen schon 5–10 % Gewichtsverlust für deutliche Verbesserung. Langsam und nachhaltig — keine Crash-Diäten."),
        ],
        "quellen": [
            ("Teede HJ et al.", "(2023): „Recommendations from the 2023 International Evidence-based Guideline for the Assessment and Management of PCOS.\" Hum Reprod, 38(9):1655–1679.", "https://academic.oup.com/humrep/article/38/9/1655/7234490"),
            ("Saguyod SJU et al.", "(2018): „Diet, polycystic ovary syndrome, and obesity.\" Endocrinol Metab Clin North Am, 47:801–812.", "https://www.endo.theclinics.com/article/S0889-8529(18)30077-1/abstract"),
            ("Parazzini F et al.", "(2013): „Diet and endometriosis risk: a literature review.\" Reprod Biomed Online, 26:323–336.", "https://www.rbmojournal.com/article/S1472-6483(13)00010-5/fulltext"),
            ("Unfer V et al.", "(2017): „Myo-inositol effects in women with PCOS: a meta-analysis.\" Endocr Connect, 6:647–658.", "https://ec.bioscientifica.com/view/journals/ec/6/8/EC-17-0243.xml"),
            ("Endometriose-Vereinigung Deutschland", "(2024): „Ernährung bei Endometriose.\"", "https://www.endometriose-vereinigung.de"),
            ("Becker CM et al.", "(2022): „ESHRE Guideline on Endometriosis.\" Hum Reprod Open, 2:hoac009.", "https://academic.oup.com/hropen/article/2022/2/hoac009/6537540"),
        ],
        "related": ["lipoedem-ernaehrung", "wechseljahre-ernaehrung", "schwangerschaft-stillzeit-ernaehrung"],
    },
    {
        "slug": "schwangerschaft-stillzeit-ernaehrung",
        "title_short": "Schwangerschaft & Stillzeit",
        "title_full": "Schwangerschaft & Stillzeit: Mikronährstoffe & Energie",
        "icd": "Z32–Z39",
        "icd_schema": "Z32-Z39",
        "name_schema": "Schwangerschaft und Stillzeit",
        "alt_names": ["Gravidität", "Laktation"],
        "h1_top": "Schwangerschaft & Stillzeit:",
        "h1_bottom": "Für zwei essen — bewusst.",
        "meta_desc": "Ernährung in Schwangerschaft & Stillzeit: Folsäure, Jod, Eisen, Omega-3, Energie. Was wirklich wichtig ist — evidenzbasiert in Münster.",
        "keywords": "Schwangerschaft Ernährung, Stillzeit, Folsäure, Jod, Eisen, Gestationsdiabetes, REHAB FIVE Nutrition",
        "symptoms": ["Erhöhter Energiebedarf", "Mikronährstoff-Bedarf", "Risiko Gestationsdiabetes", "Erhöhter Eisenbedarf"],
        "treatments": ["Vollwertige Mischkost", "Folsäure 400 µg/Tag (vor & in der Frühschwangerschaft)", "Jod 100–150 µg/Tag", "Vitamin D, B12 bei Risiko"],
        "quick": "In <strong>Schwangerschaft und Stillzeit</strong> liegt der Energiebedarf nur moderat höher (+250 kcal in der zweiten Schwangerschaftshälfte, +500 kcal in der Stillzeit). Wichtig: <strong>Folsäure</strong>, <strong>Jod</strong>, <strong>Eisen</strong>, <strong>Omega-3</strong>, <strong>Vitamin D</strong>. Bestimmte Lebensmittel meiden (Rohmilch, Rohfleisch, hohe Quecksilber-Fische). Kasse erstattet die Beratung typisch zu 80%.",
        "sections": [
            ("Energiebedarf — kein „Essen für zwei\"", "Der Energiebedarf steigt nur moderat: <strong>+250 kcal/Tag</strong> ab dem 2. Trimester, <strong>+500 kcal/Tag</strong> in der Stillzeit. Eine vollwertige Mischkost reicht in der Regel — keine Spezial-Diäten nötig. Wichtiger als Mehr ist Besser: höhere Nährstoffdichte.[1]"),
            ("Die wichtigsten Mikronährstoffe", "<ul><li><strong>Folsäure:</strong> 400 µg/Tag vor und während der Frühschwangerschaft (Neuralrohrdefekte verhindern) — Supplementierung empfohlen</li><li><strong>Jod:</strong> 230 µg/Tag — Jodsalz und Seefisch</li><li><strong>Eisen:</strong> 30 mg/Tag — Hülsenfrüchte, Fleisch, Eisen-angereichertes Vollkornbrot</li><li><strong>Omega-3 (DHA):</strong> 200 mg/Tag — fetter Fisch 2× pro Woche oder Algenöl</li><li><strong>Vitamin D:</strong> 800 IE/Tag, vor allem im Winter</li><li><strong>Vitamin B12:</strong> bei veganer Ernährung Supplementierung obligat</li></ul>"),
            ("Was zu meiden ist", "<ul><li><strong>Rohmilch & Rohmilchkäse:</strong> Listerien-Risiko</li><li><strong>Rohes Fleisch, Salami:</strong> Toxoplasmose</li><li><strong>Roher Fisch, Sushi:</strong> Parasiten</li><li><strong>Quecksilber-reiche Fische:</strong> Thunfisch, Schwertfisch (max. 1× pro Woche)</li><li><strong>Alkohol:</strong> komplett</li><li><strong>Koffein:</strong> max. 200 mg/Tag (2 kleine Tassen Kaffee)</li><li><strong>Leber:</strong> hoher Vitamin-A-Gehalt — selten und sparsam</li></ul>"),
            ("Wann professionelle Begleitung?", "Bei Gestationsdiabetes, übermäßigem Gewichtszuwachs / -verlust, veganer Ernährung, Mehrlingsschwangerschaft, Vorerkrankungen (PCOS, Schilddrüse). Die Beratung in Schwangerschaft / Stillzeit ist bei medizinischer Notwendigkeit über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Wie viel mehr muss ich essen?", "Im 2. Trimester +250 kcal/Tag, in der Stillzeit +500 kcal/Tag. Das entspricht ca. einer zusätzlichen Hauptmahlzeit oder mehreren Snacks."),
            ("Brauche ich Nahrungsergänzungsmittel?", "Folsäure ist klar empfohlen (400 µg/Tag), Jod wird oft kombiniert. Vitamin D ganzjährig sinnvoll. Bei veganer Ernährung B12 obligat. Eisen nach Laborwerten."),
            ("Welche Lebensmittel sollte ich meiden?", "Rohmilchprodukte, rohes Fleisch, roher Fisch, quecksilberreicher Fisch, Alkohol, übermäßig Koffein. Leber nur sparsam."),
            ("Übernimmt die Krankenkasse?", "Bei medizinischer Notwendigkeit (Gestationsdiabetes, Untergewicht, etc.) ja — typisch 80%. Bei rein vorsorglicher Beratung Einzelfallprüfung."),
            ("Was, wenn ich vegetarisch oder vegan lebe?", "Vegetarisch ist mit guter Planung gut machbar. Vegan erfordert konsequente Supplementierung (B12, Eisen, Omega-3, Jod, Zink, Vitamin D) — eine Beratung ist hier dringend empfohlen."),
        ],
        "quellen": [
            ("DGE", "(2024): „Ernährung in Schwangerschaft und Stillzeit — Handlungsempfehlungen.\"", "https://www.gesund-ins-leben.de"),
            ("WHO", "(2023): „WHO recommendations on antenatal care for a positive pregnancy experience.\"", "https://www.who.int/publications/i/item/9789241549912"),
            ("Koletzko B et al.", "(2018): „Nutrition during pregnancy and lactation.\" Ann Nutr Metab, 73:35–48.", "https://www.karger.com/Article/FullText/494269"),
            ("BfR", "(2024): „Sichere Ernährung in der Schwangerschaft.\"", "https://www.bfr.bund.de"),
            ("NetzWerk Gesund ins Leben", "(2024): „Vegetarische und vegane Ernährung in der Schwangerschaft.\"", "https://www.gesund-ins-leben.de/"),
            ("IOM", "(2009): „Weight Gain During Pregnancy: Reexamining the Guidelines.\"", "https://www.ncbi.nlm.nih.gov/books/NBK32813/"),
        ],
        "related": ["pcos-endometriose-ernaehrung", "diabetes-typ-2-ernaehrung", "vegan-vegetarisch-ernaehrung"],
    },
    {
        "slug": "sport-performance-ernaehrung",
        "title_short": "Sport & Performance",
        "title_full": "Sport-Ernährung: Energie, Timing & Recovery",
        "icd": "Sport",
        "icd_schema": "Z71.3",
        "name_schema": "Sport-Ernährung",
        "alt_names": ["Sporternährung", "Performance-Ernährung"],
        "h1_top": "Sport & Performance:",
        "h1_bottom": "Energie. Timing. Recovery.",
        "meta_desc": "Sport- und Performance-Ernährung: Makronährstoffe, Timing, Recovery, Wettkampf-Vorbereitung. Wissenschaftlich, ohne Mythen. Münster.",
        "keywords": "Sport-Ernährung, Performance, Recovery, Eiweißbedarf Sportler, Wettkampf-Ernährung, REHAB FIVE Nutrition",
        "symptoms": ["Erhöhter Energiebedarf", "Erhöhter Eiweißbedarf", "Glykogenmanagement", "Mikronährstoff-Bedarf"],
        "treatments": ["Periodisierte Kohlenhydratzufuhr", "1,4–2,0 g Eiweiß/kg KG", "Hydration & Elektrolyte", "Recovery-Mahlzeiten"],
        "quick": "<strong>Sport- und Performance-Ernährung</strong> ist mehr als nur Eiweißshakes. Entscheidend sind <strong>periodisierte Kohlenhydrate</strong> (mehr an Trainingstagen), <strong>1,4–2,0 g Eiweiß/kg KG</strong>, <strong>Recovery-Mahlzeit innerhalb von 60 Min nach dem Training</strong> und Mikronährstoff-Sicherung. Bei Wettkampf-Athleten zusätzlich gezielte Carb-Strategie.",
        "sections": [
            ("Makros — der Rahmen", "<ul><li><strong>Kohlenhydrate:</strong> 3–5 g/kg KG bei moderatem Training, 5–7 g bei hartem Training, 8–10 g bei Ausdauer-Wettkampftagen</li><li><strong>Eiweiß:</strong> Ausdauer 1,4 g/kg, Kraft 1,6–2,0 g/kg, in Diätphasen bis 2,2 g/kg — verteilt auf 4 Mahlzeiten mit je 0,3–0,4 g/kg</li><li><strong>Fett:</strong> 0,8–1,5 g/kg KG — bevorzugt einfach ungesättigt und Omega-3</li></ul>"),
            ("Timing — wann was?", "<ul><li><strong>Vor dem Training (1–3 h):</strong> Kohlenhydrate (1–3 g/kg KG), moderates Eiweiß, wenig Fett & Ballaststoffe</li><li><strong>Während des Trainings:</strong> bei Einheiten > 90 Min: 30–60 g KH/h</li><li><strong>Nach dem Training (Recovery-Fenster 0–60 Min):</strong> 0,3 g Eiweiß/kg + 1 g Kohlenhydrate/kg</li><li><strong>Schlaf:</strong> 30–40 g langsam verdauliches Eiweiß (z. B. Quark) zur Nacht — fördert Regeneration</li></ul>"),
            ("Hydration & Mikronährstoffe", "<strong>Flüssigkeitsbedarf:</strong> Bedarf + 500–1000 ml pro Trainingsstunde. Bei längeren Einheiten Elektrolyte (Natrium 0,3–0,7 g/l). <strong>Eisen</strong> regelmäßig kontrollieren (vor allem Frauen, Vegetarier:innen). <strong>Vitamin D, B12, Omega-3:</strong> oft kritisch in Diätphasen.[1]"),
            ("Wann professionelle Begleitung?", "Vor Wettkampf-Vorbereitungen, in Diätphasen, bei Energie-Mangel-Syndromen (RED-S), Performance-Plateaus oder Übertraining-Symptomen. Bei Sportverletzungen kann die Beratung als ergänzende Maßnahme über §43 SGB V erstattungsfähig sein — typisch 80 %. Reine Performance-Beratung meist privat."),
        ],
        "faqs": [
            ("Wie viel Eiweiß brauche ich wirklich?", "Kraft: 1,6–2,0 g/kg KG. Ausdauer: 1,4 g/kg. Mehr als 2,2 g/kg bringt keinen Mehrwert. Verteilt auf 4 Mahlzeiten."),
            ("Brauche ich Eiweißshakes?", "Nicht zwingend. Sie sind praktisch nach dem Training. Naturbelassene Quellen (Quark, Eier, Fisch, Hülsenfrüchte) sind gleichwertig."),
            ("Was ist die beste Recovery-Mahlzeit?", "Innerhalb von 60 Min nach dem Training: 20–30 g Eiweiß + 60–100 g Kohlenhydrate. Beispiele: Quark mit Banane und Haferflocken; Sandwich mit Putenbrust."),
            ("Brauche ich Supplements?", "Wenige sind evidenzbasiert: Kreatin, Koffein, Beta-Alanin (für bestimmte Sportarten), Vitamin D, Eisen bei Mangel."),
            ("Übernimmt die Krankenkasse die Beratung?", "Bei medizinischer Indikation (Verletzung, RED-S, etc.) ja. Reine Performance-Beratung ohne Diagnose meist privat."),
        ],
        "quellen": [
            ("Thomas DT et al.", "(2016): „Position of the Academy of Nutrition and Dietetics, Dietitians of Canada, and the American College of Sports Medicine: Nutrition and Athletic Performance.\" J Acad Nutr Diet, 116:501–528.", "https://www.jandonline.org/article/S2212-2672(15)01802-X/fulltext"),
            ("Jäger R et al.", "(2017): „International Society of Sports Nutrition position stand: protein and exercise.\" J Int Soc Sports Nutr, 14:20.", "https://jissn.biomedcentral.com/articles/10.1186/s12970-017-0177-8"),
            ("Burke LM et al.", "(2018): „Carbohydrates for training and competition.\" J Sports Sci, 29:S17–S27.", "https://www.tandfonline.com/doi/full/10.1080/02640414.2011.585473"),
            ("Mountjoy M et al.", "(2018): „IOC consensus statement on relative energy deficiency in sport (RED-S).\" Br J Sports Med, 52:687–697.", "https://bjsm.bmj.com/content/52/11/687"),
            ("Maughan RJ et al.", "(2018): „IOC consensus statement: dietary supplements and the high-performance athlete.\" Br J Sports Med, 52:439–455.", "https://bjsm.bmj.com/content/52/7/439"),
            ("DOSB / DGE", "(2024): „Ernährung im Leistungssport.\"", "https://www.dge.de"),
        ],
        "related": ["adipositas-ernaehrungstherapie", "diabetes-typ-2-ernaehrung", "untergewicht-mangelernaehrung"],
    },
    {
        "slug": "wechseljahre-ernaehrung",
        "title_short": "Wechseljahre",
        "title_full": "Wechseljahre & Ernährung: Hormone, Knochen, Gewicht",
        "icd": "N95",
        "icd_schema": "N95",
        "name_schema": "Klimakterische Beschwerden",
        "alt_names": ["Menopause", "Klimakterium"],
        "h1_top": "Wechseljahre:",
        "h1_bottom": "Hormone, Knochen, Gewicht.",
        "meta_desc": "Wechseljahre (ICD N95): Wie Ernährung Hitzewallungen, Knochengesundheit und Gewicht beeinflusst. Phytoöstrogene, Mediterrane Kost. Münster.",
        "keywords": "Wechseljahre Ernährung, Menopause, Hitzewallungen, Phytoöstrogene, Knochengesundheit Frauen, REHAB FIVE Nutrition",
        "symptoms": ["Hitzewallungen", "Schlafstörungen", "Stimmungsschwankungen", "Gewichtszunahme", "Knochen-Risiko"],
        "treatments": ["Mediterrane Ernährung", "Eiweiß 1,2 g/kg KG", "Kalzium & Vitamin D", "Phytoöstrogene (individuell)"],
        "quick": "In den <strong>Wechseljahren (ICD N95)</strong> verändert sich der Stoffwechsel: weniger Östrogen → erhöhtes Risiko für Bauchfett, Insulinresistenz, Osteoporose, Herz-Kreislauf-Erkrankungen. <strong>Mediterrane Ernährung</strong> mit ausreichend <strong>Eiweiß (1,2 g/kg KG)</strong>, <strong>Kalzium</strong> und <strong>Vitamin D</strong> wirkt protektiv. <strong>Phytoöstrogene</strong> können Hitzewallungen lindern. Kasse erstattet die Beratung typisch zu 80%.",
        "sections": [
            ("Was passiert in den Wechseljahren?", "Die Wechseljahre umfassen Prä-, Peri- und Postmenopause. Östrogen sinkt — mit Folgen für Körperzusammensetzung (mehr viszerales Fett), Knochendichte, Lipidprofil, Insulinwirkung und Stimmung. Hauptsymptome: Hitzewallungen, Schlafstörungen, Gewichtszunahme.[1]"),
            ("Ernährung als Schutz", "<ul><li><strong>Mediterrane Ernährung:</strong> reduziert kardiovaskuläres Risiko und unterstützt Gewichts-Stabilisierung</li><li><strong>Eiweiß 1,2 g/kg KG:</strong> erhält Muskelmasse (entscheidend für Stoffwechsel und Sturzprävention)</li><li><strong>Kalzium 1000 mg + Vitamin D 800–1000 IE:</strong> Osteoporose-Prävention</li><li><strong>Phytoöstrogene</strong> (Soja, Leinsamen): Studien zeigen moderate Reduktion von Hitzewallungen</li><li><strong>Reduktion: Zucker, Alkohol, Koffein</strong> — verstärken Hitzewallungen und Schlafprobleme</li><li><strong>Omega-3:</strong> 2× fetter Fisch/Woche für Herz und Stimmung</li></ul>"),
            ("Gewichtsmanagement — anders als vor 40", "Der Grundumsatz sinkt um 1–2 % pro Jahrzehnt. Kombination aus geringerem Energiebedarf, hormonellen Veränderungen und veränderter Fettverteilung. Lösung: <strong>weniger Kohlenhydrate, mehr Eiweiß, regelmäßiges Krafttraining</strong> — die Kombination ist entscheidend.[2]"),
            ("Wann professionelle Begleitung?", "Bei deutlicher Gewichtszunahme, Osteoporose-Risiko, Hitzewallungen, in Vorbereitung auf eine Hormonersatztherapie. Wechseljahre-Beratung ist mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Helfen Soja und Phytoöstrogene wirklich bei Hitzewallungen?", "In Meta-Analysen zeigt Soja moderate Effekte (Reduktion um etwa 20 %). Konsequente tägliche Zufuhr nötig. Bei Brustkrebs-Vorgeschichte vorher ärztlich abklären."),
            ("Wie viel Eiweiß brauche ich in der Menopause?", "1,2 g/kg KG — also etwa 70–80 g pro Tag bei einer 60-kg-Frau. Verteilt auf 3–4 Mahlzeiten."),
            ("Warum nehme ich plötzlich zu?", "Östrogenmangel verändert Fettverteilung (mehr Bauchfett), Grundumsatz sinkt, oft auch Muskelabbau. Lösung: weniger einfache Kohlenhydrate, mehr Eiweiß, Krafttraining."),
            ("Übernimmt die Krankenkasse?", "Ja. Wechseljahre-Beschwerden (ICD N95) sind erstattungsfähig nach §43 SGB V — typisch 80%."),
            ("Was schützt vor Osteoporose?", "Kalzium 1000 mg + Vitamin D 800 IE + Eiweiß 1,2 g/kg + Krafttraining 2× pro Woche. In Kombination am wirksamsten."),
        ],
        "quellen": [
            ("North American Menopause Society", "(2022): „The 2022 Hormone Therapy Position Statement.\" Menopause, 29:767–794.", "https://journals.lww.com/menopausejournal/Fulltext/2022/07000/The_2022_hormone_therapy_position_statement_of_The.4.aspx"),
            ("Chen MN et al.", "(2015): „Efficacy of phytoestrogens for menopausal symptoms: a meta-analysis and systematic review.\" Climacteric, 18:260–269.", "https://www.tandfonline.com/doi/full/10.3109/13697137.2014.966241"),
            ("Stuenkel CA et al.", "(2015): „Treatment of Symptoms of the Menopause: An Endocrine Society Clinical Practice Guideline.\" J Clin Endocrinol Metab, 100:3975–4011.", "https://academic.oup.com/jcem/article/100/11/3975/2836091"),
            ("DGGG", "(2020): „S3-Leitlinie Peri- und Postmenopause — Diagnostik und Interventionen.\" AWMF-Register 015/062.", "https://www.awmf.org/leitlinien/detail/ll/015-062.html"),
            ("Sayón-Orea C et al.", "(2015): „Mediterranean diet and lifestyle in women in menopausal transition.\" Maturitas, 81:283–289.", "https://www.maturitas.org/article/S0378-5122(15)00601-2/fulltext"),
            ("DGE", "(2024): „Empfehlungen für Frauen in den Wechseljahren.\"", "https://www.dge.de"),
        ],
        "related": ["osteoporose-ernaehrung", "adipositas-ernaehrungstherapie", "pcos-endometriose-ernaehrung"],
    },
    {
        "slug": "vegan-vegetarisch-ernaehrung",
        "title_short": "Vegan / vegetarisch",
        "title_full": "Vegan & vegetarisch: B12, Eisen, Eiweiß, Omega-3",
        "icd": "Vegan",
        "icd_schema": "Z72.4",
        "name_schema": "Vegane / vegetarische Ernährung",
        "alt_names": ["Plant-based", "Pflanzenbasierte Ernährung"],
        "h1_top": "Vegan & vegetarisch:",
        "h1_bottom": "Pflanzlich essen, vollwertig leben.",
        "meta_desc": "Vegane & vegetarische Ernährung: Vitamin B12, Eisen, Eiweiß, Omega-3, Jod sicherstellen. DGE-Empfehlungen, evidenzbasiert. Münster.",
        "keywords": "Vegane Ernährung, vegetarisch, B12, Eisen pflanzlich, Eiweißbedarf vegan, Omega-3 vegan, REHAB FIVE Nutrition",
        "symptoms": ["Mögliche Mangelzustände bei schlechter Planung: B12, Eisen, Zink, Omega-3, Vitamin D, Jod"],
        "treatments": ["Strukturierte Planung", "B12-Supplementierung (vegan obligat)", "Eisen-Quellen kombiniert mit Vitamin C", "Omega-3 aus Lein/Walnuss/Algen"],
        "quick": "<strong>Vegane und vegetarische Ernährung</strong> ist mit guter Planung gesund und kann vor zahlreichen Erkrankungen schützen. Kritisch: <strong>Vitamin B12</strong> (vegan: obligate Supplementierung), <strong>Eisen</strong>, <strong>Zink</strong>, <strong>Omega-3 (DHA/EPA)</strong>, <strong>Jod</strong>, <strong>Vitamin D</strong>. <strong>Eiweißbedarf</strong> mit Hülsenfrüchten, Soja und Vollkorn gut abgedeckt. Beratung sinnvoll vor Umstellung — bei Schwangerschaft, Kindern und Senioren besonders.",
        "sections": [
            ("Pflanzlich essen — die Studienlage", "Vegetarische und vegane Ernährung ist in der Mehrzahl der Studien mit niedrigerem Risiko für Typ-2-Diabetes, Herzinfarkt, Bluthochdruck und einigen Krebsarten verbunden. Vegane Ernährung führt zu niedrigerem LDL und systolischem Blutdruck. Voraussetzung: gute Planung.[1]"),
            ("Die kritischen Nährstoffe", "<ul><li><strong>Vitamin B12:</strong> bei veganer Ernährung <em>obligat supplementieren</em> (z. B. 25 µg/Tag oder 2000 µg/Woche). Bei lakto-ovo-vegetarisch kontrollieren</li><li><strong>Eisen:</strong> pflanzliche Quellen (Hülsenfrüchte, Vollkorn, Tofu) — Aufnahme verbessern durch Vitamin C zur Mahlzeit, Kaffee/Tee versetzt</li><li><strong>Zink:</strong> Hülsenfrüchte, Nüsse, Vollkorn — Phytat reduzieren durch Einweichen und Keimen</li><li><strong>Omega-3 (DHA/EPA):</strong> aus Algenöl-Kapseln; Lein- und Walnussöl liefern nur Vorstufe (ALA)</li><li><strong>Jod:</strong> Jodsalz oder Seealgen (nur Nori in kleinen Mengen — andere Algen oft überjodiert)</li><li><strong>Vitamin D:</strong> Eigensynthese + Supplementierung im Winter</li><li><strong>Kalzium:</strong> Mineralwasser (> 400 mg/l), Brokkoli, Grünkohl, Mandeln, angereicherte Pflanzendrinks</li></ul>"),
            ("Eiweißbedarf einfach decken", "Empfehlung: 0,8–1,0 g/kg KG (mehr bei Sportler:innen, Schwangerschaft, Alter). Pflanzliche Eiweißquellen:<ul><li>Hülsenfrüchte (Linsen, Kichererbsen, Bohnen, Lupine)</li><li>Soja & Soja-Produkte (Tofu, Tempeh, Edamame)</li><li>Vollkorn-Getreide (Hafer, Quinoa, Dinkel)</li><li>Nüsse und Samen</li><li>Optional Eiweißpulver auf Erbsen-/Reisbasis</li></ul>Wichtig: <strong>Variation</strong> — verschiedene Quellen kombinieren ergänzt die Aminosäure-Profile."),
            ("Wann professionelle Begleitung?", "Vor der Umstellung, in Schwangerschaft/Stillzeit, bei Kindern, Senioren, Leistungssportler:innen, bei chronischen Erkrankungen oder Mangelzuständen. Bei nachgewiesenem Mangel ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Muss ich als Veganer B12 supplementieren?", "Ja, immer. Es gibt keine zuverlässig veganen B12-Quellen. Supplementierung ist nicht optional, sondern obligat."),
            ("Bekomme ich genug Eiweiß ohne Fleisch?", "Ja. Hülsenfrüchte, Soja, Vollkorn, Nüsse decken den Bedarf gut. Wichtig: Vielfalt und ausreichende Menge."),
            ("Welches Omega-3 ist am besten?", "Für DHA/EPA: Algenöl-Kapseln. Lein- und Walnussöl liefern nur die Vorstufe ALA, die nur zu 5–15 % umgewandelt wird."),
            ("Übernimmt die Krankenkasse?", "Bei nachgewiesenem Mangel oder Begleiterkrankungen ja, typisch 80%. Bei vorsorglicher Beratung Einzelfallprüfung."),
            ("Ist vegan für Kinder sicher?", "Mit strukturierter Begleitung ja. Wichtig: regelmäßige Kontrollen (B12, Eisen, Vitamin D), Supplementierung, ausreichend Energie und Eiweiß."),
        ],
        "quellen": [
            ("DGE", "(2024): „Position der Deutschen Gesellschaft für Ernährung zur veganen Ernährung.\" Ernährungs Umschau, 71:60–84.", "https://www.dge.de/wissenschaft/positionen/"),
            ("Melina V et al.", "(2016): „Position of the Academy of Nutrition and Dietetics: Vegetarian Diets.\" J Acad Nutr Diet, 116:1970–1980.", "https://www.jandonline.org/article/S2212-2672(16)31192-3/fulltext"),
            ("Dinu M et al.", "(2017): „Vegetarian, vegan diets and multiple health outcomes: A systematic review.\" Crit Rev Food Sci Nutr, 57:3640–3649.", "https://www.tandfonline.com/doi/abs/10.1080/10408398.2016.1138447"),
            ("Pawlak R et al.", "(2014): „How prevalent is vitamin B12 deficiency among vegetarians?\" Nutr Rev, 71:110–117.", "https://academic.oup.com/nutritionreviews/article/71/2/110/1940320"),
            ("EFSA", "(2017): „Dietary Reference Values for nutrients.\"", "https://www.efsa.europa.eu"),
            ("ProVeg", "(2024): „Veganer Ernährungsleitfaden für Eltern und Kinder.\"", "https://proveg.com/de/"),
        ],
        "related": ["schwangerschaft-stillzeit-ernaehrung", "sport-performance-ernaehrung", "diabetes-typ-2-ernaehrung"],
    },
]


# ============================================================
# HTML-TEMPLATE
# ============================================================

def render_article(ind):
    """Render kompletten HTML-Artikel für eine Indikation."""
    sections_html = "\n".join(
        f'        <h2 id="section-{i+1}">{html.escape(title)}</h2>\n        <p>{body}</p>'
        for i, (title, body) in enumerate(ind["sections"])
    )
    faqs_html_details = "\n".join(
        f'''          <details class="group rounded-xl bg-white ring-1 ring-ink-100 p-5 shadow-card"><summary class="flex justify-between items-center cursor-pointer font-semibold text-lg list-none text-ink-900">{html.escape(q)}<span class="chev text-brand-600">▾</span></summary><p class="mt-3 text-ink-700">{a}</p></details>'''
        for q, a in ind["faqs"]
    )
    faqs_schema = ",\n        ".join(
        f'''{{"@type":"Question","name":{repr(q)},"acceptedAnswer":{{"@type":"Answer","text":{repr(a)}}}}}'''
        for q, a in ind["faqs"]
    )
    quellen_html = "\n".join(
        f'          <li id="q{i+1}"><strong>{html.escape(author)}</strong> {body} <a href="{url}" target="_blank" rel="noopener">Link</a></li>'
        for i, (author, body, url) in enumerate(ind["quellen"])
    )
    symptoms_schema = ",\n          ".join(
        f'{{"@type":"MedicalSignOrSymptom","name":{repr(s)}}}'
        for s in ind["symptoms"]
    )
    treatments_schema = ",\n          ".join(
        f'{{"@type":"MedicalTherapy","name":{repr(t)}}}'
        for t in ind["treatments"]
    )
    alt_names_schema = ", ".join(repr(n) for n in ind["alt_names"])
    related_html = ""
    for r_slug in ind["related"]:
        # Suche den Titel
        title_short = r_slug.replace("-ernaehrung", "").replace("-ernaehrungstherapie", "").replace("-", " ").title()
        for other in INDIKATIONEN:
            if other["slug"] == r_slug:
                title_short = other["title_short"]
                break
        # Auch in den 7 bereits gebauten Artikeln suchen
        known_titles = {
            "reizdarm-syndrom-ernaehrung": "Reizdarm-Syndrom",
            "adipositas-ernaehrungstherapie": "Adipositas",
            "diabetes-typ-2-ernaehrung": "Diabetes Typ 2",
            "lipoedem-ernaehrung": "Lipödem",
            "zoeliakie-ernaehrung": "Zöliakie",
            "hypertonie-ernaehrung": "Hypertonie",
            "fettleber-ernaehrung": "Fettleber",
        }
        if r_slug in known_titles:
            title_short = known_titles[r_slug]
        related_html += f'''          <a href="{r_slug}.html" class="group rounded-2xl bg-white ring-1 ring-ink-100 p-5 hover:ring-brand-500/40 hover:shadow-lg transition flex flex-col"><p class="text-xs font-semibold uppercase tracking-wider text-brand-700 bg-brand-500/10 rounded-full px-2.5 py-1 w-max">→</p><h3 class="mt-3 font-bold text-base group-hover:text-brand-700" style="color:#1F342D">{html.escape(title_short)}</h3><p class="mt-2 text-sm text-ink-700 flex-1">Mehr erfahren →</p></a>\n'''

    return f'''<!DOCTYPE html>
<html lang="de">
<head>
<script src="https://consent.cookiefirst.com/sites/ads.rehab-five.com-c57f4a38-bb6e-4ba0-8ad3-2bd4c7fcbab2/consent.js"></script>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(ind["title_full"])} | REHAB FIVE NUTRITION</title>
  <meta name="description" content="{html.escape(ind["meta_desc"])}" />
  <meta name="keywords" content="{html.escape(ind["keywords"])}" />
  <meta name="author" content="REHAB FIVE NUTRITION" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <meta name="theme-color" content="#1F342D" />
  <link rel="canonical" href="{BASE_URL}/wissen/{ind["slug"]}.html" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{html.escape(ind["title_full"])}" />
  <meta property="og:description" content="{html.escape(ind["meta_desc"])}" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700;800&display=swap" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>tailwind.config = {{ theme: {{ extend: {{ colors: {{ ink:{{50:'#FAFAFA',100:'#F5F5F5',200:'#C9C9C9',700:'#4A4A4A',900:'#1A1A1A'}}, forest:{{700:'#1F342D',800:'#172620'}}, brand:{{100:'#FBF1E0',500:'#D99129',600:'#C57F1F',700:'#A66819'}}, accent:{{500:'#D99129'}} }}, fontFamily:{{sans:['Barlow','system-ui','sans-serif']}}, boxShadow:{{card:'0 4px 24px -8px rgba(26,26,26,0.10)'}} }} }} }}</script>
  <style>
    html {{ scroll-behavior: smooth; }}
    body {{ font-family: 'Barlow', system-ui, sans-serif; color:#1A1A1A; }}
    .display {{ font-weight: 800; letter-spacing: -0.01em; text-transform: uppercase; }}
    .eyebrow {{ font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; }}
    .gradient-hero {{ background: radial-gradient(60% 50% at 80% 15%, rgba(217,145,41,0.22), transparent 60%), linear-gradient(180deg, #1F342D 0%, #172620 100%); }}
    .prose-r5 {{ font-size: 1.05rem; line-height: 1.7; }}
    .prose-r5 h2 {{ font-size: 1.6rem; font-weight: 700; color:#1F342D; margin: 2.2rem 0 0.8rem; }}
    .prose-r5 h3 {{ font-size: 1.2rem; font-weight: 700; color:#1F342D; margin: 1.6rem 0 0.6rem; }}
    .prose-r5 p {{ margin: 0 0 1.1rem; }}
    .prose-r5 ul, .prose-r5 ol {{ margin: 0 0 1.1rem 1.2rem; }}
    .prose-r5 ul li {{ list-style: disc; margin-bottom: 0.35rem; }}
    .prose-r5 ol li {{ list-style: decimal; margin-bottom: 0.35rem; }}
    .prose-r5 a {{ color:#A66819; text-decoration: underline; }}
    .prose-r5 strong {{ color:#1F342D; }}
    details[open] > summary .chev {{ transform: rotate(180deg); }}
    .chev {{ transition: transform .2s ease; }}
  </style>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{ "@type": "Organization", "@id": "https://rehab-five.com/#organization", "name": "REHAB FIVE", "url": "https://rehab-five.com" }},
      {{
        "@type": "MedicalCondition",
        "@id": "{BASE_URL}/wissen/{ind["slug"]}.html#condition",
        "name": {repr(ind["name_schema"])},
        "alternateName": [{alt_names_schema}],
        "code": {{ "@type": "MedicalCode", "code": "{ind["icd_schema"]}", "codingSystem": "ICD-10-GM" }},
        "signOrSymptom": [
          {symptoms_schema}
        ],
        "possibleTreatment": [
          {treatments_schema}
        ]
      }},
      {{
        "@type": "MedicalWebPage",
        "@id": "{BASE_URL}/wissen/{ind["slug"]}.html#webpage",
        "url": "{BASE_URL}/wissen/{ind["slug"]}.html",
        "name": {repr(ind["title_full"])},
        "about": {{ "@id": "{BASE_URL}/wissen/{ind["slug"]}.html#condition" }},
        "audience": [{{ "@type": "PatientsAudience" }}],
        "lastReviewed": "2026-05-15",
        "publisher": {{ "@id": "https://rehab-five.com/#organization" }}
      }},
      {{
        "@type": "Article",
        "headline": {repr(ind["title_full"])},
        "datePublished": "2026-05-15",
        "dateModified": "2026-05-15",
        "author": {{ "@id": "https://rehab-five.com/#organization" }},
        "publisher": {{ "@id": "https://rehab-five.com/#organization" }},
        "mainEntityOfPage": {{ "@id": "{BASE_URL}/wissen/{ind["slug"]}.html#webpage" }}
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
        {faqs_schema}
        ]
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{ "@type": "ListItem", "position": 1, "name": "Startseite", "item": "{BASE_URL}/" }},
          {{ "@type": "ListItem", "position": 2, "name": "Wissen", "item": "{BASE_URL}/wissen/" }},
          {{ "@type": "ListItem", "position": 3, "name": {repr(ind["title_short"])}, "item": "{BASE_URL}/wissen/{ind["slug"]}.html" }}
        ]
      }}
    ]
  }}
  </script>
  <script async src="https://cdn.docmedico-rezeption.de/j9u4c9m7a/reception_embed.js"></script>
</head>
<body class="bg-white text-ink-900 antialiased">
  <a href="#main" class="sr-only focus:not-sr-only focus:fixed focus:top-3 focus:left-3 focus:z-50 focus:bg-ink-900 focus:text-white focus:px-4 focus:py-2 focus:rounded">Zum Inhalt springen</a>

  <header class="sticky top-0 z-40 bg-forest-700 text-white border-b border-forest-800 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-3">
      <a href="../" class="flex items-center gap-3 shrink-0" aria-label="REHAB FIVE NUTRITION Startseite"><img src="../R5-Logo-B-white_RZ.png" alt="REHAB FIVE Logo" class="h-7 w-auto" /><span class="hidden sm:inline-block text-[11px] font-semibold tracking-[0.22em] uppercase text-white/70 border-l border-white/20 pl-3">Nutrition · Wissen</span></a>
      <nav class="hidden lg:flex items-center gap-6 text-sm font-medium text-white/80" aria-label="Hauptnavigation"><a href="../#programme" class="hover:text-white">Programme</a><a href="../#ablauf" class="hover:text-white">Ablauf</a><a href="../#preise" class="hover:text-white">Preise</a><a href="./" class="hover:text-white text-white font-semibold">Wissen</a><a href="../#standort" class="hover:text-white">Standort</a></nav>
      <div class="flex items-center gap-2">
        <a href="../#anmelden" class="hidden sm:inline-flex items-center justify-center rounded-lg bg-brand-500 hover:bg-brand-600 text-ink-900 font-semibold text-sm px-4 py-2 transition shadow-lg shadow-brand-500/20">Erstgespräch</a>
        <button class="lg:hidden inline-flex items-center justify-center w-10 h-10 rounded-lg text-white hover:bg-white/10 transition" aria-label="Menü öffnen" aria-expanded="false" data-mobile-toggle>
          <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" data-icon-menu><path d="M4 6h16M4 12h16M4 18h16"/></svg>
          <svg class="w-6 h-6 hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" data-icon-close><path d="M6 6l12 12M18 6L6 18"/></svg>
        </button>
      </div>
    </div>
    <div class="hidden lg:hidden bg-forest-800 border-t border-forest-900" data-mobile-menu>
      <nav class="max-w-7xl mx-auto px-4 sm:px-6 py-4 grid grid-cols-2 gap-x-4 gap-y-1 text-sm font-medium text-white/85">
        <a href="../#programme" class="block py-2 hover:text-brand-500" data-mobile-link>Programme</a>
        <a href="../#konzept" class="block py-2 hover:text-brand-500" data-mobile-link>Konzept</a>
        <a href="../#ablauf" class="block py-2 hover:text-brand-500" data-mobile-link>Ablauf</a>
        <a href="../#indikationen" class="block py-2 hover:text-brand-500" data-mobile-link>Indikationen</a>
        <a href="../#preise" class="block py-2 hover:text-brand-500" data-mobile-link>Preise</a>
        <a href="./" class="block py-2 hover:text-brand-500 text-brand-500" data-mobile-link>Wissen</a>
        <a href="../#standort" class="block py-2 hover:text-brand-500" data-mobile-link>Standort</a>
        <a href="../#faq" class="block py-2 hover:text-brand-500" data-mobile-link>FAQ</a>
        <a href="tel:+4925174788200" class="block py-2 col-span-2 mt-2 border-t border-white/10 pt-3 text-white font-semibold hover:text-brand-500">📞 0251 74788 200 anrufen</a>
        <a href="../#anmelden" class="block sm:hidden py-3 col-span-2 mt-2 rounded-lg bg-brand-500 hover:bg-brand-600 text-ink-900 font-semibold text-center" data-mobile-link>Erstgespräch sichern</a>
      </nav>
    </div>
  </header>
  <script>(function(){{var b=document.querySelector('[data-mobile-toggle]');var m=document.querySelector('[data-mobile-menu]');if(!b||!m)return;var im=b.querySelector('[data-icon-menu]');var ic=b.querySelector('[data-icon-close]');function s(o){{m.classList.toggle('hidden',!o);im.classList.toggle('hidden',o);ic.classList.toggle('hidden',!o);b.setAttribute('aria-expanded',o?'true':'false');b.setAttribute('aria-label',o?'Menü schließen':'Menü öffnen');}}b.addEventListener('click',function(){{s(m.classList.contains('hidden'));}});m.querySelectorAll('[data-mobile-link]').forEach(function(a){{a.addEventListener('click',function(){{s(false);}});}});}})();</script>

  <main id="main">
    <section class="gradient-hero text-white">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-14 md:py-20">
        <nav class="text-xs text-white/60"><a href="../" class="hover:text-brand-500">Startseite</a> › <a href="./" class="hover:text-brand-500">Wissen</a> › <span class="text-white/85">{html.escape(ind["title_short"])}</span></nav>
        <p class="mt-6 inline-flex items-center gap-2 text-xs font-semibold uppercase tracking-[0.18em] text-brand-500 bg-brand-500/10 ring-1 ring-brand-500/30 rounded-full px-3 py-1"><span class="w-1.5 h-1.5 rounded-full bg-brand-500"></span>Indikation · ICD-10 {ind["icd"]}</p>
        <h1 class="display mt-5 text-3xl md:text-5xl leading-[1.05]">{html.escape(ind["h1_top"])}<br><span class="text-brand-500">{html.escape(ind["h1_bottom"])}</span></h1>
        <p class="mt-5 text-lg text-white/85 max-w-2xl">{html.escape(ind["meta_desc"])}</p>
        <div class="mt-6 flex flex-wrap gap-x-6 gap-y-2 text-xs text-white/60"><span>📅 Stand: 15. Mai 2026</span><span>⏱ 6 Min Lesezeit</span><span>🔬 {len(ind["quellen"])} wissenschaftliche Quellen</span></div>
      </div>
    </section>

    <section class="bg-ink-50 border-b border-ink-100">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10 md:py-12">
        <div class="rounded-2xl bg-white ring-1 ring-ink-100 shadow-card p-6 md:p-8 border-l-4 border-brand-500">
          <p class="eyebrow text-xs text-brand-600">Kurz & Knapp</p>
          <p class="mt-3 text-lg md:text-xl text-ink-900 leading-relaxed">{ind["quick"]}</p>
        </div>
      </div>
    </section>

    <article class="prose-r5">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-16">
{sections_html}
      </div>
    </article>

    <section class="bg-forest-700 text-white">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-16">
        <div class="rounded-2xl bg-white/5 ring-1 ring-white/10 p-6 md:p-8 grid md:grid-cols-[1.2fr_1fr] gap-8 items-center">
          <div>
            <p class="eyebrow text-xs text-brand-500">Ernährungstherapie</p>
            <h2 class="display mt-3 text-2xl md:text-3xl">Brauchst du individuelle Begleitung?</h2>
            <p class="mt-3 text-white/85">Buche dir ein unverbindliches 15-Min-Kennenlern-Gespräch — wir prüfen gemeinsam, ob eine begleitete Ernährungstherapie für dich passt. Bei vielen Diagnosen mit Kassen-Zuschuss.</p>
          </div>
          <div class="flex flex-col gap-3">
            <a href="../#anmelden" class="inline-flex items-center justify-center rounded-xl bg-brand-500 hover:bg-brand-600 text-ink-900 font-semibold px-6 py-3.5 text-base transition shadow-lg shadow-brand-500/20">Gratis Kennenlern-Call</a>
            <a href="../kassen-check-rehab-five.pdf" target="_blank" rel="noopener" class="inline-flex items-center justify-center rounded-xl bg-white/10 hover:bg-white/15 text-white font-semibold px-6 py-3.5 text-base ring-1 ring-white/20 transition">Kassen-Check PDF</a>
          </div>
        </div>
      </div>
    </section>

    <section id="faq" class="bg-forest-700 text-white">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16 md:py-20">
        <p class="eyebrow text-sm text-brand-500">Häufige Fragen</p>
        <h2 class="display mt-3 text-3xl md:text-4xl">{html.escape(ind["title_short"])} — kurz erklärt.</h2>
        <div class="mt-10 space-y-3">
{faqs_html_details}
        </div>
      </div>
    </section>

    <section class="bg-white border-t border-ink-100">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-16">
        <p class="eyebrow text-xs text-brand-600">Wissenschaftliche Quellen</p>
        <h2 class="display mt-3 text-2xl md:text-3xl" style="color:#1F342D">Quellen & weiterführende Literatur</h2>
        <ol class="mt-8 space-y-4 text-sm text-ink-900 list-decimal list-inside">
{quellen_html}
        </ol>
        <div class="mt-10 rounded-xl bg-ink-50 ring-1 ring-ink-100 p-5 text-xs text-ink-700"><p><strong>Medizinischer Disclaimer:</strong> Diese Seite ersetzt keine ärztliche Diagnose oder Therapie. Bei medizinischen Beschwerden bitte zunächst die behandelnde Ärztin / den behandelnden Arzt konsultieren. Stand: Mai 2026.</p></div>
      </div>
    </section>

    <section class="bg-ink-50 border-t border-ink-100">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-16">
        <p class="eyebrow text-xs text-brand-600">Verwandte Indikationen</p>
        <h2 class="display mt-3 text-2xl md:text-3xl" style="color:#1F342D">Auch interessant für dich</h2>
        <div class="mt-8 grid md:grid-cols-3 gap-4">
{related_html}
        </div>
      </div>
    </section>
  </main>

  <footer class="bg-forest-700 text-white/85 text-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 grid md:grid-cols-4 gap-10">
      <div class="md:col-span-2"><img src="../R5-Logo-B-white_RZ.png" alt="REHAB FIVE Logo" class="h-8 w-auto" /><p class="mt-3 max-w-md text-white/75">REHAB FIVE NUTRITION — Ernährung neu gedacht.</p></div>
      <div><h3 class="text-white font-semibold">Standort</h3><address class="not-italic mt-3 space-y-3 text-white/80"><div>Weseler Straße 71<br>48151 Münster</div><a href="tel:+4925174788200" class="block text-white hover:text-brand-500">0251 74788 200</a><a href="mailto:info@rehab-five.com" class="block text-white hover:text-brand-500">info@rehab-five.com</a></address></div>
      <div><h3 class="text-white font-semibold">Rechtliches</h3><ul class="mt-3 space-y-2 text-white/80"><li><a href="../impressum.html" class="hover:text-brand-500">Impressum</a></li><li><a href="../datenschutz.html" class="hover:text-brand-500">Datenschutz</a></li></ul></div>
    </div>
    <div class="border-t border-white/10"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5 text-xs flex flex-wrap items-center justify-between gap-3 text-white/60"><p>© <span id="y"></span> REHAB FIVE.</p><p>Made in Münster</p></div></div>
  </footer>
  <div class="md:hidden fixed bottom-3 inset-x-3 z-30 flex gap-2"><a href="tel:+4925174788200" class="flex-1 inline-flex items-center justify-center rounded-xl bg-white ring-1 ring-ink-200 text-ink-900 font-semibold px-4 py-3 shadow-card">Anrufen</a><a href="../#anmelden" class="flex-[1.4] inline-flex items-center justify-center rounded-xl bg-brand-600 hover:bg-brand-700 text-white font-semibold px-4 py-3 shadow-card">Erstgespräch</a></div>
  <script>document.getElementById('y').textContent = new Date().getFullYear();</script>
</body>
</html>
'''


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    for ind in INDIKATIONEN:
        path = os.path.join(OUT_DIR, f"{ind['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(render_article(ind))
        size = os.path.getsize(path)
        print(f"✓ {ind['slug']:50s} {size:>6,} bytes")
    print(f"\n{len(INDIKATIONEN)} Artikel erfolgreich generiert in {OUT_DIR}")
