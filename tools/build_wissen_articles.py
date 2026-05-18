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
            ("Was ist Mangelernährung?", "Mangelernährung umfasst Untergewicht (BMI < 18,5) sowie qualitative Defizite (Mikronährstoffe, Eiweiß). Ursachen: Erkrankungen, Appetitlosigkeit, Resorptionsstörungen, Essstörungen, hohes Alter. Ohne strukturierte Behandlung folgen Muskelabbau, Infektanfälligkeit und Osteoporose-Risiko. In Deutschland sind 1,5 Millionen Senior:innen betroffen — ein massiv unterschätztes Problem.[1][7]"),
            ("Strukturierter Aufbau — wie es funktioniert", "Die DGEM empfiehlt eine schrittweise Erhöhung um <strong>500–700 kcal/Tag</strong> über das Erhaltungs-Niveau hinaus. Wichtige Säulen:<ul><li><strong>Eiweiß:</strong> 1,2–1,5 g/kg KG (z. B. Quark, Eier, Hülsenfrüchte, Fleisch)</li><li><strong>Gesunde Fette:</strong> Olivenöl, Nüsse, Avocado — energiedicht und entzündungsarm</li><li><strong>Häufige kleine Mahlzeiten</strong> (5–6 pro Tag) statt 3 große</li><li><strong>Trinknahrung</strong> als Ergänzung bei starker Appetitlosigkeit</li><li><strong>Krafttraining 2–3× pro Woche</strong> stimuliert Muskelaufbau parallel zur Ernährung</li></ul>"),
            ("Mikronährstoffe — was zu prüfen ist", "Eisen, Ferritin, Vitamin B12, Folsäure, Vitamin D, Zink, Magnesium, Kalzium. Bei chronischen Erkrankungen (z. B. Zöliakie, M. Crohn) ist die Resorption gestört — gezielte Substitution nötig.[2] Bei Senior:innen sind B12 und Vitamin D besonders kritisch — die Eigensynthese sinkt mit dem Alter, Aufnahme über den Darm wird schlechter.[5]"),
            ("Praktische Umsetzung im Alltag", "Konkrete Maßnahmen, die sofort wirken:<ul><li><strong>Frühstück ‚verdichten':</strong> Müsli mit Nüssen, Quark, Banane, Honig + Olivenöl-Spritzer</li><li><strong>Snacks immer dabei:</strong> Studentenfutter, Käsewürfel, Vollkornbrot mit Avocado</li><li><strong>Getränke verkalorisieren:</strong> Vollmilch statt Wasser, Smoothies mit Banane + Erdnussmus</li><li><strong>Energiedichte vor Volumen:</strong> kleine, nährstoffreiche Portionen statt riesiger Salate</li><li><strong>Esstagebuch</strong> für 7 Tage führen — zeigt Lücken auf</li><li><strong>Soziale Mahlzeiten:</strong> alleine essen reduziert oft den Appetit</li></ul>"),
            ("Häufige Fehler beim Aufbau", "<ol><li><strong>Crash-Aufbau mit Fast Food:</strong> erhöht Fettmasse statt Muskelmasse, fördert Insulinresistenz</li><li><strong>Zu wenig Eiweiß:</strong> ohne 1,2 g/kg KG bleibt der Muskelaufbau aus</li><li><strong>Mahlzeiten überspringen:</strong> wer 2× am Tag isst, schafft den kcal-Bedarf selten</li><li><strong>Ohne Bewegung:</strong> ohne Krafttraining geht Aufbau in Fett, nicht in Muskel</li><li><strong>Eigentherapie ohne ärztliche Abklärung:</strong> hinter Untergewicht steckt oft eine behandelbare Erkrankung</li></ol>"),
            ("Spezielle Lebenssituationen", "<strong>Senior:innen (> 65):</strong> Sarkopenie-Risiko hoch — Eiweißbedarf steigt auf 1,2–1,5 g/kg, oft Trinknahrung sinnvoll.[5]<br><strong>Nach Erkrankung / OP:</strong> Wundheilung braucht 1,5–2 g Eiweiß/kg KG, Mikronährstoff-Substitution gezielt.<br><strong>Sport mit Untergewicht:</strong> RED-S-Risiko prüfen (Energie-Mangel-Syndrom), Hormonstatus testen.<br><strong>Verdacht auf Essstörung:</strong> Vor Aufbau psychotherapeutische Diagnostik — Ernährungsberatung allein reicht nicht."),
            ("Wann professionelle Begleitung?", "Bei BMI < 17, schnellem Gewichtsverlust (> 5% in 6 Monaten), nach Erkrankung oder bei Verdacht auf Essstörung. Bei Mangelernährung (ICD E43–46) ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — Erstattung typisch 80%."),
        ],
        "faqs": [
            ("Wie schnell darf ich zunehmen?", "Gesund sind 0,5–1 kg pro Monat. Schneller Aufbau führt zu vermehrtem Fett statt Muskelmasse und belastet den Stoffwechsel."),
            ("Welche Lebensmittel helfen beim Aufbau?", "Energiedichte, nährstoffreiche Lebensmittel: Nüsse, Olivenöl, Avocado, fetter Fisch, Vollkornprodukte, Hülsenfrüchte, Quark, Eier. Trinknahrung als Ergänzung bei Bedarf."),
            ("Reicht mehr essen aus?", "Nicht immer. Resorptionsstörungen, Schilddrüsenfunktion und psychische Faktoren sollten geprüft werden. Strukturierte Begleitung hilft, Plateaus zu durchbrechen."),
            ("Sind Eiweiß-Shakes sinnvoll?", "Als Ergänzung ja — vor allem nach dem Training oder bei Appetitlosigkeit. Naturbelassene Quellen (Quark, Eier, Hülsenfrüchte) bleiben aber wichtiger. Bei Senior:innen sind klinisch geprüfte Trinknahrungen (Fresubin, Fortimel) oft praktikabler."),
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
            ("Norman K et al.", "(2021): „Malnutrition in Older Adults — Recent Advances and Remaining Challenges.\" Nutrients, 13(8):2764.", "https://www.mdpi.com/2072-6643/13/8/2764"),
            ("Deutz NEP et al.", "(2014): „Protein intake and exercise for optimal muscle function with aging.\" Clin Nutr, 33(6):929–936.", "https://www.clinicalnutritionjournal.com/article/S0261-5614(14)00111-3/fulltext"),
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
            ("Was sind Dyslipoproteinämien?", "Dyslipoproteinämien (auch Hyperlipidämien) sind Fettstoffwechselstörungen mit erhöhten LDL- oder Triglycerid-Werten und/oder erniedrigtem HDL. Sie sind zentrale Risikofaktoren für Atherosklerose und Herzinfarkt. Diagnose über Nüchtern-Lipidprofil.[1] Genetische Formen (familiäre Hypercholesterinämie) müssen früh erkannt werden — bereits Kinder können betroffen sein.[7]"),
            ("Was die ESC-Leitlinie 2019/2024 empfiehlt", "Bei hohem kardiovaskulärem Risiko gilt LDL-Ziel < 70 mg/dl (sehr hoch < 55 mg/dl). Lifestyle-Empfehlungen:<ul><li><strong>Gesättigte Fette < 10 % der Energie</strong> (rotes Fleisch, Butter, Käse, Wurst reduzieren)</li><li><strong>Trans-Fette streichen</strong> (Frittiertes, Industriebackwaren)</li><li><strong>Lösliche Ballaststoffe</strong> (Hafer, Hülsenfrüchte, Äpfel) — senken LDL um 5–10 %</li><li><strong>Phytosterole</strong> 2 g/Tag (angereicherte Margarine)</li><li><strong>Omega-3-Fettsäuren</strong> aus fettem Fisch oder pflanzlich (Lein, Walnuss)</li><li><strong>Mediterrane Ernährung</strong> als Gesamtmuster</li></ul>"),
            ("Ernährung vs. Medikamente", "Lifestyle-Maßnahmen senken LDL um 10–20 %, Statine um 30–50 %. Sie ersetzen sich nicht — sie ergänzen sich. Auch unter Statin-Therapie verbessert Ernährung die Prognose zusätzlich.[2]"),
            ("Was einzelne Lebensmittel bewirken (Zahlen aus Studien)", "<ul><li><strong>Hafer (3 g Beta-Glucan/Tag):</strong> LDL ↓ 5–7 % (Cochrane Review)[8]</li><li><strong>Phytosterole (2 g/Tag):</strong> LDL ↓ 8–10 % (EFSA-Health-Claim genehmigt)</li><li><strong>Mandeln (40 g/Tag):</strong> LDL ↓ 3–5 % (Meta-Analyse 2018)</li><li><strong>Avocado (1 pro Tag):</strong> LDL ↓ 13 mg/dl bei moderat Hyperlipidämischen</li><li><strong>Olivenöl extra vergine (50 ml/Tag):</strong> HDL ↑, LDL-Oxidation ↓ (PREDIMED)</li><li><strong>Fisch 2×/Woche:</strong> Triglyceride ↓ 15–25 %</li><li><strong>Walnüsse (30 g/Tag):</strong> Triglyceride ↓ 10 %, LDL ↓ 4 %</li></ul>Kumuliert: ‚Portfolio-Diet' (Hafer + Phytosterole + Sojaeiweiß + Nüsse) erreicht LDL-Senkung von ca. 30 % — fast Statin-Niveau.[9]"),
            ("Praktische Umsetzung — Mein Teller", "Drei Mahlzeiten konkret:<ul><li><strong>Frühstück:</strong> Haferflocken mit Walnüssen, Beeren, Soja-Drink (statt Vollmilch)</li><li><strong>Mittag:</strong> Linsen-Eintopf mit Karotten, Olivenöl + Vollkornbrot</li><li><strong>Abend:</strong> gebackener Lachs, Brokkoli, Süßkartoffeln, kleiner Salat mit Avocado-Olivenöl-Dressing</li></ul><strong>Snacks:</strong> 1 Apfel, eine Handvoll Mandeln, 1 Stück 70 % Zartbitterschokolade.<br>Diese Konfiguration entspricht der Portfolio-Diet und senkt nach 4 Wochen nachweislich LDL und CRP."),
            ("Häufige Fehler", "<ol><li><strong>Eier pauschal meiden:</strong> moderater Konsum (bis 6/Woche) beeinflusst LDL kaum.[3]</li><li><strong>Kokosöl als ‚gesundes Fett':</strong> trotz Hype erhöht es nachweislich das LDL — gesättigte Fettsäuren bleiben gesättigt.</li><li><strong>Margarine ohne Phytosterole kaufen:</strong> verschwendete Chance — nur die ‚becel pro-activ' / ‚Benecol' Varianten enthalten 2 g</li><li><strong>‚Light'-Produkte:</strong> oft Zucker statt Fett — Triglyceride steigen</li><li><strong>Ernährung allein bei Familiärer Hypercholesterinämie:</strong> hier sind Medikamente obligat</li></ol>"),
            ("Wann professionelle Begleitung?", "Bei familiärer Hypercholesterinämie, kombinierten Fettstoffwechselstörungen, Statin-Unverträglichkeit oder unzureichendem Therapieerfolg. Bei Dyslipoproteinämie (ICD E78) ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Wie schnell senkt Ernährung das LDL?", "Erste Effekte nach 4–6 Wochen. Volle Wirkung der mediterranen Ernährung nach 3 Monaten — typisch LDL-Senkung um 10–20 %."),
            ("Muss ich Eier streichen?", "Nein. Studien zeigen, dass moderater Eierkonsum (bis 6 pro Woche) bei den meisten Menschen das LDL kaum beeinflusst. Wichtiger sind gesättigte und trans-Fette."),
            ("Was bringen Omega-3-Kapseln?", "Bei sehr hohen Triglyceriden (> 500 mg/dl) helfen hochdosierte Omega-3-Fettsäuren. Für LDL-Senkung dagegen kaum wirksam — bevorzugt fettreichen Fisch 2× pro Woche."),
            ("Hilft die Portfolio-Diet wirklich Statine zu vermeiden?", "Bei moderater Hyperlipidämie ja — kombiniert mit Bewegung wurde in der Jenkins-Studie LDL um 30 % gesenkt. Bei sehr hohen Werten oder familiärer Form bleiben Statine unverzichtbar."),
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
            ("Nordestgaard BG et al.", "(2013): „Familial hypercholesterolaemia is underdiagnosed and undertreated.\" Eur Heart J, 34:3478–3490.", "https://academic.oup.com/eurheartj/article/34/45/3478/582685"),
            ("Hollænder PLB et al.", "(2015): „Whole-grain and blood lipid changes — meta-analysis.\" Am J Clin Nutr, 102:556–572.", "https://academic.oup.com/ajcn/article/102/3/556/4564513"),
            ("Jenkins DJA et al.", "(2011): „Effect of a dietary portfolio of cholesterol-lowering foods.\" JAMA, 306:831–839.", "https://jamanetwork.com/journals/jama/fullarticle/1104223"),
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
            ("Was ist Gicht?", "Gicht ist eine Stoffwechselerkrankung mit erhöhter Harnsäure im Blut (> 6,8 mg/dl). Beim akuten Gichtanfall lagern sich Harnsäure-Kristalle in Gelenken ab — meist in der Großzehe (Podagra). Chronisch drohen Tophi, Nierensteine und Gelenkschäden.[1] In Deutschland leiden etwa 1,4 Millionen Menschen an Gicht — Männer 4–9× häufiger als Frauen (vor der Menopause).[7]"),
            ("Purine — die wichtigsten Quellen", "Purine werden im Körper zu Harnsäure abgebaut. Stark purinhaltig sind:<ul><li><strong>Innereien</strong> (Leber, Niere, Bries) — meiden</li><li><strong>Rotes Fleisch, Wurst</strong> — stark reduzieren</li><li><strong>Sardinen, Sardellen, Hering, Forelle</strong> — moderat</li><li><strong>Bier (auch alkoholfrei!)</strong> — komplett meiden</li><li><strong>Hochfructose-Sirup, Softdrinks</strong> — komplett meiden</li></ul>Pflanzliche Purine (Hülsenfrüchte, Pilze) erhöhen das Gicht-Risiko nicht.[2]"),
            ("Was wirklich hilft", "<ul><li><strong>Vegetarisch-betonte mediterrane Kost</strong> — senkt Harnsäure deutlich</li><li><strong>Magermilchprodukte:</strong> 200–400 g/Tag senken Harnsäure und Gichtanfall-Risiko</li><li><strong>Kirschen / Sauerkirschen</strong> — RCT-Evidenz für Reduktion akuter Anfälle</li><li><strong>Kaffee</strong> (3–4 Tassen) — protektiv</li><li><strong>Vitamin C</strong> (500 mg/Tag) — leicht harnsäuresenkend</li><li><strong>2–3 l Wasser/Tag</strong> — Verdünnung & Ausscheidung</li></ul>"),
            ("Studien zu Kirschen, Vitamin C & Milchprodukten", "<strong>Kirschen:</strong> Choi & Curhan (2012) zeigte bei 633 Gicht-Patient:innen: 10–12 Kirschen/Tag oder 1 EL Tart-Cherry-Konzentrat halbieren das Anfall-Risiko in 48 h.[3][8]<br><strong>Vitamin C:</strong> Choi (2009, Arch Intern Med) — 500 mg/Tag senken Harnsäure um 0,5 mg/dl im Schnitt. Bei 1500 mg sogar 0,7 mg/dl. Allerdings: bei manifester Gicht keine ausreichende Wirkung allein.[9]<br><strong>Magermilchprodukte:</strong> Dalbeth (2010) — 250 ml fettarme Milch/Tag senkt Harnsäure um 10 % innerhalb 4 Wochen (Casein und Whey hemmen die Harnsäureausscheidung in der Niere).<br><strong>Kaffee:</strong> Choi (2007) — > 4 Tassen/Tag = 40 % weniger Gicht-Risiko bei Männern. Mechanismus: Xanthin-Oxidase-Hemmung."),
            ("Akuter Gichtanfall — was tun", "Bei akutem Anfall ist Ernährung sekundär — die Schmerztherapie steht im Vordergrund (NSAR, Colchicin oder Glukokortikoide nach ärztlicher Anweisung). Was Ernährung dann beitragen kann:<ul><li><strong>Sehr viel trinken</strong> — 3 l Wasser/Tag, hilft bei Ausscheidung</li><li><strong>Sauerkirsch-Saft</strong> — 30 ml Konzentrat 2× täglich für 2 Wochen reduziert Wiederholungsrisiko</li><li><strong>Strikt purinarm</strong> für 2 Wochen — Innereien, Bier, rotes Fleisch komplett weglassen</li><li><strong>Kein Fasten</strong> — Fasten erhöht Harnsäure (Ketonkörper konkurrieren um Ausscheidung)</li><li><strong>Gelenk kühlen, ruhigstellen, hochlagern</strong></li></ul>Nach Abklingen (5–10 Tage) langsam zur Dauer-Ernährung übergehen."),
            ("Häufige Fehler", "<ol><li><strong>Bier weiterhin trinken:</strong> die Nr. 1 Ursache für wiederkehrende Anfälle — auch alkoholfrei nicht erlaubt</li><li><strong>Fasten / Crash-Diät:</strong> Ketonkörper blockieren Harnsäure-Ausscheidung — Anfall droht</li><li><strong>Hülsenfrüchte meiden:</strong> Mythos — sie sind sicher</li><li><strong>Süße Getränke unterschätzen:</strong> 1 Liter Softdrink/Woche = 50 % höheres Risiko</li><li><strong>Ohne Medikamente bei chronischer Gicht:</strong> Ernährung reicht nicht — Allopurinol oder Febuxostat sind oft nötig</li></ol>"),
            ("Wann professionelle Begleitung?", "Bei wiederkehrenden Gichtanfällen, Tophi, Nierensteinen oder Hyperurikämie mit Begleiterkrankungen. Beratung ist mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Darf ich bei Gicht Hülsenfrüchte essen?", "Ja. Pflanzliche Purine (Bohnen, Linsen, Erbsen) erhöhen das Gicht-Risiko in großen Studien nicht. Tierische Purine sind das Problem."),
            ("Ist Bier wirklich so schlimm?", "Ja. Bier enthält besonders viele Purine (auch alkoholfreies!). Schon 1 Bier/Tag erhöht das Gicht-Risiko deutlich. Wein in moderaten Mengen ist neutraler."),
            ("Helfen Kirschen wirklich?", "Studien zeigen: 10–12 Kirschen täglich oder 1 Tasse Tart-Cherry-Juice senkt das Risiko akuter Anfälle. Effekt ähnlich wie bei manchen Medikamenten."),
            ("Wie viel Wasser pro Tag?", "Bei Gicht 2,5–3 Liter Wasser oder ungesüßter Tee. Verdünnt Harnsäure und unterstützt die renale Ausscheidung. Vorsicht bei eingeschränkter Herz- oder Nierenfunktion — vorher ärztlich abklären."),
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
            ("Kuo CF et al.", "(2015): „Global epidemiology of gout: prevalence, incidence and risk factors.\" Nat Rev Rheumatol, 11:649–662.", "https://www.nature.com/articles/nrrheum.2015.91"),
            ("Choi HK, Curhan G", "(2012): „Coffee, tea, and caffeine consumption and serum uric acid level.\" Arthritis Rheum, 67:816–821.", "https://onlinelibrary.wiley.com/doi/10.1002/acr.21610"),
            ("Choi HK et al.", "(2009): „Vitamin C intake and the risk of gout in men.\" Arch Intern Med, 169:502–507.", "https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/414655"),
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
            ("Was ist Osteoporose?", "Osteoporose ist eine systemische Skeletterkrankung mit verminderter Knochendichte und erhöhtem Frakturrisiko. Diagnose über Knochendichtemessung (DXA) — T-Score < -2,5. In Deutschland sind über 6 Millionen Menschen betroffen, vor allem Frauen nach der Menopause.[1] Pro Jahr ereignen sich allein in Deutschland ~750.000 osteoporotische Frakturen — Hüftfraktur ist eine der häufigsten Todesursachen bei Senior:innen.[7]"),
            ("DVO-Leitlinie 2023 — Ernährungs-Eckpfeiler", "<ul><li><strong>Kalzium:</strong> 1000–1200 mg/Tag, bevorzugt aus Milchprodukten (Quark, Käse, Joghurt). Pflanzliche Quellen: Brokkoli, Grünkohl, Mandeln, kalziumreiches Mineralwasser (> 400 mg/l)</li><li><strong>Vitamin D:</strong> 800–1000 IE/Tag, im Winter Supplementierung empfohlen — die Eigensynthese durch Sonnenlicht reicht in Mitteleuropa nicht aus</li><li><strong>Eiweiß:</strong> 1,0–1,2 g/kg KG, ältere Menschen sogar 1,2–1,5 g — Eiweißmangel beschleunigt Knochenabbau</li><li><strong>Magnesium, Vitamin K:</strong> aus Vollkorn, Nüssen, grünem Gemüse</li><li><strong>Reduzieren:</strong> Salz (> 6 g/Tag fördert Kalziumverlust), Cola (Phosphorsäure), Alkohol, Rauchen</li></ul>"),
            ("Mythos „Milch macht Knochen brüchig\"", "Studien zeigen das Gegenteil: Moderate Milchprodukte (200–400 g/Tag) reduzieren das Frakturrisiko signifikant. Wer keine Milch verträgt: Hartkäse (laktosearm), Joghurt oder pflanzliche Drinks mit Kalzium-Anreicherung.[2]"),
            ("Bewegung als Schlüssel — was wirkt", "Ernährung allein reicht nicht. Knochenaufbau braucht <strong>mechanische Stimulation</strong>:<ul><li><strong>Krafttraining 2× pro Woche</strong> — verbessert Knochendichte an Wirbelsäule und Hüfte signifikant (Howe-Meta-Analyse[8])</li><li><strong>Stoßbelastungen / Sprünge</strong> — selbst 10 Sprünge/Tag wirken</li><li><strong>Walking 30 Min/Tag</strong> — Mindestmaß bei Senior:innen</li><li><strong>Gleichgewichtstraining</strong> — verhindert Stürze (Sturzprophylaxe)</li><li><strong>Schwimmen NICHT ausreichend</strong> — fehlende Schwerkraft-Belastung</li></ul>Bei Beginn: physiotherapeutisch begleitet, danach Health-Club oder Gym."),
            ("Vitamin K2 & D3 — die unterschätzten Helfer", "<strong>Vitamin K2 (Menachinon):</strong> aktiviert Osteocalcin, das Kalzium in die Knochen einbaut. Studien (Cockayne 2006, Knapen 2013) zeigen frakturreduzierende Effekte bei 180 µg MK-7/Tag.[9] Quellen: Natto (japanisches Soja-Produkt), fermentierter Käse, Eigelb. Supplementierung sinnvoll bei niedrigem Konsum.<br><strong>Vitamin D3:</strong> ohne ausreichend D3 wird Kalzium nicht resorbiert. Zielwert 25-OH-D > 30 ng/ml. Im Winter Supplementierung praktisch immer nötig — 1000–2000 IE/Tag.<br><strong>Magnesium 300–400 mg/Tag:</strong> Co-Faktor für D-Aktivierung und Kalzium-Einbau.<br><strong>Bor:</strong> 3 mg/Tag (Nüsse, Obst) reduziert Kalziumausscheidung."),
            ("Praktische Umsetzung — Mein Knochen-Tag", "Beispieltag mit 1100 mg Kalzium + 800 IE D3 + 1,2 g Eiweiß/kg:<ul><li><strong>Frühstück:</strong> 200 g Skyr-Joghurt mit 30 g Mandeln und Beeren (≈ 380 mg Ca)</li><li><strong>Snack:</strong> 30 g Emmentaler + 1 Apfel (≈ 320 mg Ca)</li><li><strong>Mittag:</strong> Brokkoli mit Lachs + Quinoa (≈ 200 mg Ca + Vit D)</li><li><strong>Snack:</strong> 1 Becher Buttermilch (≈ 180 mg Ca)</li><li><strong>Abend:</strong> Salat mit Sardinen, Olivenöl, Vollkornbrot mit Käse (≈ 200 mg Ca + Vit D)</li><li><strong>Tagsüber:</strong> 1 l kalziumreiches Mineralwasser (≈ 400 mg Ca)</li><li><strong>Supplement:</strong> 800 IE D3 (Oktober–April)</li></ul>"),
            ("Häufige Fehler", "<ol><li><strong>Kalzium-Supplemente ohne Bedarf:</strong> erhöhen das kardiovaskuläre Risiko leicht (Bolland 2010). Besser: Nahrung optimieren.</li><li><strong>Vitamin D mit Kalzium kombinieren ohne Test:</strong> Hyperkalzämie-Risiko</li><li><strong>Cola und Phosphor unterschätzen:</strong> > 1 l Cola/Tag erhöht Frakturrisiko</li><li><strong>Schwimmen statt Krafttraining:</strong> wirkt nicht knochenaufbauend</li><li><strong>Untergewicht akzeptieren:</strong> BMI < 19 ist Risikofaktor — Aufbau-Ernährung parallel</li></ol>"),
            ("Wann professionelle Begleitung?", "Bei Osteoporose-Diagnose, nach Fraktur ohne adäquates Trauma, bei Risikofaktoren (Glukokortikoide, frühe Menopause, Untergewicht). Bei Osteoporose (ICD M80–M82) ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Wie viel Kalzium brauche ich täglich?", "Bei Osteoporose 1000–1200 mg/Tag. Beispiel: 200 g Joghurt + 50 g Käse + 200 ml Mineralwasser (kalziumreich) decken etwa 1000 mg."),
            ("Reicht Sonnenlicht für Vitamin D?", "In Mitteleuropa von Oktober bis April nicht — Supplementierung empfohlen (800–1000 IE/Tag). Im Sommer 15–20 Min Sonne (Gesicht/Arme) reichen oft."),
            ("Schadet zu viel Eiweiß den Knochen?", "Nein — moderne Studien zeigen sogar, dass Eiweißmangel das größere Problem ist. 1,0–1,2 g/kg KG ist sicher und förderlich."),
            ("Vitamin K2 — was sagt die Studie?", "Cockayne (2006) und Knapen (2013) zeigen: 180 µg MK-7/Tag verbessern Knochenmineraldichte und reduzieren Frakturrisiko. Wirkung bei kombinierter Gabe mit D3 verstärkt. Supplementierung sinnvoll bei niedrigem Natto- und Käse-Konsum."),
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
            ("RKI", "(2023): „Osteoporose in Deutschland — GEDA-Studie.\"", "https://www.rki.de"),
            ("Howe TE et al.", "(2011): „Exercise for preventing and treating osteoporosis in postmenopausal women.\" Cochrane Database Syst Rev, CD000333.", "https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD000333.pub2/full"),
            ("Knapen MHJ et al.", "(2013): „Three-year low-dose menaquinone-7 supplementation helps decrease bone loss.\" Osteoporos Int, 24:2499–2507.", "https://link.springer.com/article/10.1007/s00198-013-2325-6"),
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
            ("Was ist GERD?", "Die Gastroösophageale Refluxkrankheit (GERD, ICD K21) entsteht durch Rückfluss von Magensäure in die Speiseröhre — meist wegen unzureichender Funktion des unteren Speiseröhrenschließmuskels. Symptome: Sodbrennen, Aufstoßen, Druck retrosternal. Langfristig: Refluxösophagitis, Barrett-Ösophagus.[1] In Deutschland leiden ca. 20 % der Bevölkerung mindestens 1× pro Woche unter Symptomen — Tendenz steigend (Adipositas, Stress, Ernährungsmuster).[7]"),
            ("Was Ernährung wirklich bewirken kann", "Die <strong>Mediterrane Ernährung</strong> hat in einer wegweisenden Studie (Zalvan et al. 2017) Reflux-Symptome stärker reduziert als hochdosierte PPI-Medikamente.[2] Praktische Empfehlungen:<ul><li><strong>Reduzieren:</strong> Schokolade, Pfefferminze, Kaffee, Alkohol (besonders Wein), Cola, fettreiche Speisen, scharfe Gewürze, Tomaten, Zitrusfrüchte (individuell)</li><li><strong>Bevorzugen:</strong> Gemüse, Vollkorn, magere Eiweißquellen, Olivenöl, ungesüßte Getränke</li><li><strong>Mahlzeitenstruktur:</strong> kleinere Portionen, 4–5× pro Tag, letzte Mahlzeit 3 Stunden vor dem Schlafen</li><li><strong>Gewichtsreduktion:</strong> 5–10% Reduktion kann bei Übergewicht die Symptome deutlich lindern</li><li><strong>Schlafposition:</strong> Oberkörper hochlagern, linke Seite</li></ul>"),
            ("Ernährungs-Tagebuch — der schnellste Weg zu deinen Triggern", "Trigger sind individuell. Ein 14-Tage-Symptom-Tagebuch hilft, persönliche Auslöser zu identifizieren — wirkungsvoller als pauschale Verbotslisten."),
            ("So führst du ein effektives Trigger-Tagebuch", "Über 14 Tage protokollieren:<ul><li><strong>Was gegessen / getrunken?</strong> Mengen abschätzen</li><li><strong>Wann?</strong> Uhrzeit (besonders abends entscheidend)</li><li><strong>Symptom-Intensität</strong> auf Skala 0–10 (0 = kein Sodbrennen, 10 = stark)</li><li><strong>Zeitpunkt der Symptomatik</strong> — sofort nach Essen? Nachts? Aufstehen?</li><li><strong>Begleitfaktoren:</strong> Stress, Schlaf, körperliche Aktivität</li></ul>Nach 14 Tagen Muster erkennen — typischerweise findet sich 1–3 individuelle Trigger, die der Großteil der Beschwerden verursacht. Eliminieren statt pauschal verbieten."),
            ("Schlafposition & Gewicht — die strukturellen Hebel", "<strong>Schlafposition:</strong> Linke Seitenlage reduziert Reflux-Episoden um bis zu 40 % gegenüber Rückenlage. Rechte Seite oder Bauch sind ungünstig.[8] Oberkörper-Hochlagerung (Keil-Kissen, Bett 15–20 cm hochstellen) zusätzlich wirksam.<br><strong>Gewichtsreduktion:</strong> Bei BMI > 25 reduziert jeder 5 kg Verlust die Symptome signifikant. Bei BMI > 30: 5–10 % Gewichtsverlust = oft komplette Symptomfreiheit.[5][9] Mechanismus: weniger intraabdominaler Druck → weniger Reflux.<br><strong>Enge Kleidung:</strong> Korsetts, Gürtel, enge Hosen erhöhen den Bauchdruck und fördern Reflux.<br><strong>Stress / Schlafmangel:</strong> verstärken Symptome — Stressmanagement (Yoga, Atemübungen) hilft mehr als gedacht."),
            ("Häufige Fehler", "<ol><li><strong>Pauschale Trigger-Listen:</strong> nicht jeder reagiert auf Tomaten oder Zitrone — Tagebuch nutzen</li><li><strong>PPI dauerhaft ohne Ernährungsumstellung:</strong> langfristige Risiken (B12-Mangel, Knochen-Risiko)</li><li><strong>Zu spät essen:</strong> letzte Mahlzeit < 3 h vor Schlafen — 1 Std Pufferzeit reicht nicht</li><li><strong>Apfelessig oder Backpulver:</strong> populäre ‚Hausmittel' — keine wissenschaftliche Grundlage, oft kontraproduktiv</li><li><strong>Stress unterschätzen:</strong> stressreduktion ist oft genauso wichtig wie der Teller</li></ol>"),
            ("Wann professionelle Begleitung?", "Bei chronischen Beschwerden (> 4 Wochen), PPI-Abhängigkeit, Barrett-Ösophagus oder unklaren Schluckbeschwerden. Bei Reflux (ICD K21) ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Kann Ernährung PPI-Medikamente ersetzen?", "Bei milder bis mittelschwerer GERD ja — Studien zeigen vergleichbare Effekte. Bei schwerer Refluxösophagitis oder Barrett-Ösophagus sollte die medikamentöse Therapie in Abstimmung mit der Ärztin / dem Arzt bestehen bleiben."),
            ("Welche Lebensmittel sind die häufigsten Trigger?", "Schokolade, Pfefferminze, Alkohol, fetthaltige und frittierte Speisen, Kaffee, scharfe Gewürze. Individuell oft auch Tomaten und Zitrusfrüchte."),
            ("Wie lange dauert es, bis Ernährung wirkt?", "Erste Verbesserungen oft schon in 1–2 Wochen. Volle Wirkung nach 6–8 Wochen konsequenter Umstellung."),
            ("Hilft Apfelessig wirklich?", "Studienlage dünn bis ablehnend. Wissenschaftlich plausibel ist nur sehr verdünnter Essig vor fetthaltigen Mahlzeiten — bei akutem Sodbrennen aber meist kontraproduktiv. Mediterrane Kost zeigt deutlich bessere und belegte Wirkung."),
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
            ("El-Serag HB et al.", "(2014): „Update on the epidemiology of gastro-oesophageal reflux disease.\" Gut, 63:871–880.", "https://gut.bmj.com/content/63/6/871"),
            ("Khan BA et al.", "(2012): „Effect of bed head elevation during sleep in symptomatic patients of nocturnal GERD.\" J Gastroenterol Hepatol, 27:1078–1082.", "https://onlinelibrary.wiley.com/doi/10.1111/j.1440-1746.2011.06968.x"),
            ("Park SK et al.", "(2017): „Weight loss and waist reduction is associated with improvement in gastroesophageal disease reflux symptoms.\" PLoS One, 12:e0177241.", "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0177241"),
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
            ("Was ist rheumatoide Arthritis?", "Die rheumatoide Arthritis (RA) ist eine chronisch-entzündliche Autoimmunerkrankung der Gelenke. Charakteristisch: symmetrische Entzündung kleiner Gelenke, Morgensteifigkeit > 1 Stunde, erhöhte Entzündungsmarker (CRP, BSG). In Deutschland sind etwa 500.000 Menschen betroffen.[1] Frauen 3× häufiger als Männer, Erstmanifestation meist 40–60 Jahre. Frühe Diagnose und Therapie (innerhalb 12 Wochen) verhindert Gelenkschäden."),
            ("Anti-entzündliche Ernährung — was die Evidenz zeigt", "Eine <strong>mediterrane Ernährung</strong> reduziert in mehreren Studien Schmerz, Morgensteifigkeit und Krankheitsaktivität bei RA-Patient:innen.[2] Wichtige Bausteine:<ul><li><strong>Omega-3-Fettsäuren:</strong> 2–3 g EPA+DHA pro Tag (Fisch oder Algenöl). Studien zeigen klare entzündungshemmende Effekte</li><li><strong>Olivenöl extra vergine</strong> (3 EL/Tag) — Oleocanthal wirkt ähnlich wie Ibuprofen</li><li><strong>Reichlich Gemüse, Beeren, Vollkorn</strong> — Polyphenole, Antioxidantien</li><li><strong>Hülsenfrüchte und Nüsse</strong></li><li><strong>Wenig rotes Fleisch und Wurst</strong> — fördern Entzündung</li><li><strong>Zucker und hochverarbeitete Produkte deutlich reduzieren</strong></li></ul>"),
            ("Heilfasten / intermittierendes Fasten", "Studien zeigen, dass mehrtägiges Fasten unter ärztlicher Begleitung bei RA-Patient:innen kurzfristig Symptome reduzieren kann. Anschließende vegetarisch-mediterrane Kost erhält die Effekte oft 6–12 Monate.[3] Wichtig: Fasten nur unter Begleitung — Methotrexat und Biologica beachten!"),
            ("Omega-3 in Studien — die Zahlen", "Goldberg & Katz (2007) Meta-Analyse[7]: 3–6 g EPA+DHA/Tag reduziert Morgensteifigkeit um 30 Min und Anzahl schmerzhafter Gelenke um 30 %. Daily fish oil bei 60 Patient:innen über 24 Wochen (Galarraga 2008): Reduktion des NSAR-Bedarfs um 39 %.[8] Kremer (2000): kombiniert mit niedriger gesättigter Fettzufuhr klarer Schmerz-Score-Effekt. Praktisch: 2× wöchentlich fetter Fisch + 1 g hochkonzentrierte Omega-3-Kapsel/Tag erreicht den therapeutisch wirksamen Dosis-Bereich. Bei Veganismus: Algenöl 2 g DHA+EPA/Tag."),
            ("Praktische Umsetzung im Alltag", "Anti-entzündlich essen ist mehr als ‚Fisch + Gemüse'. Konkrete Strategien:<ul><li><strong>Curcumin:</strong> 1 TL Kurkuma + schwarzer Pfeffer in warmer Milch täglich (Khanna 2017 zeigt anti-entzündliche Wirkung)[9]</li><li><strong>Olivenöl extra vergine:</strong> 30–50 ml/Tag, kalt verwenden oder leicht erwärmen</li><li><strong>Beeren (Heidelbeeren, Erdbeeren):</strong> 1 Handvoll täglich — Anthocyane senken CRP</li><li><strong>Grüner Tee:</strong> 2–3 Tassen/Tag (EGCG)</li><li><strong>Ingwer:</strong> 1–2 g frisch oder als Tee</li><li><strong>Vermeiden:</strong> Wurst, Fertigprodukte, Süßgetränke, Transfette</li></ul>Effekt bei konsequenter Umsetzung: 4–8 Wochen bis spürbare Symptomverbesserung."),
            ("Häufige Fehler", "<ol><li><strong>Ernährung als Ersatz für Methotrexat / Biologica sehen:</strong> Ernährung wirkt ergänzend, nicht ersetzend</li><li><strong>Eigenständig Heilfasten:</strong> ohne ärztliche Begleitung gefährlich bei Methotrexat-Therapie</li><li><strong>Nachtschattengewächse pauschal meiden:</strong> nur bei nachgewiesener individueller Unverträglichkeit sinnvoll — sonst Verlust an Vitaminen</li><li><strong>Omega-3 zu niedrig dosiert:</strong> < 1 g/Tag wirkt kaum — hochkonzentrierte Präparate wählen</li><li><strong>Curcumin-Kapseln ohne Piperin / Lecithin:</strong> 95 % nicht resorbiert</li></ol>"),
            ("Wann professionelle Begleitung?", "Bei RA-Diagnose, schlechtem Ansprechen auf Medikamente, Gewichtsproblemen, Begleiterkrankungen (Osteoporose, Kardiovaskulär). Bei RA (ICD M05–M06) ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Hilft Ernährung wirklich bei Rheuma?", "Ja, ergänzend. Sie ersetzt keine Basistherapie (Methotrexat, Biologica), kann aber Schmerz, Morgensteifigkeit und Krankheitsaktivität signifikant reduzieren."),
            ("Welche Lebensmittel sollte ich meiden?", "Rotes und verarbeitetes Fleisch, Zucker, Transfette (Frittiertes), hochverarbeitete Produkte. Bei einigen Patient:innen auch Milchprodukte und Nachtschattengewächse — individuell prüfen."),
            ("Wie viel Omega-3 ist sinnvoll?", "2–3 g EPA+DHA pro Tag aus fettem Fisch (2× pro Woche) oder hochwertigen Kapseln. Pflanzlich (Lein, Walnuss) ist eine Ergänzung, ersetzt aber EPA/DHA nicht vollständig."),
            ("Sollte ich Nachtschattengewächse meiden?", "Pauschal nein. Tomaten, Paprika, Auberginen, Kartoffeln enthalten Solanin, das bei wenigen Menschen Beschwerden auslösen kann. Wer Verdacht hat: 4-Wochen-Eliminations-Test unter Begleitung, dann strukturiert wieder einführen."),
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
            ("Goldberg RJ, Katz J", "(2007): „A meta-analysis of the analgesic effects of omega-3 polyunsaturated fatty acid supplementation for inflammatory joint pain.\" Pain, 129:210–223.", "https://journals.lww.com/pain/Abstract/2007/05000/A_meta_analysis_of_the_analgesic_effects_of_omega.7.aspx"),
            ("Galarraga B et al.", "(2008): „Cod liver oil reduces NSAID requirement in patients with rheumatoid arthritis.\" Rheumatology, 47:665–669.", "https://academic.oup.com/rheumatology/article/47/5/665/2916571"),
            ("Khanna D et al.", "(2017): „Natural products as a gold mine for arthritis treatment.\" Curr Opin Pharmacol, 7:344–351.", "https://www.sciencedirect.com/science/article/pii/S1471489207000598"),
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
            ("Was ist Laktose-Intoleranz?", "Laktose-Intoleranz ist ein Mangel des Enzyms Laktase, das den Milchzucker (Laktose) in Glukose und Galaktose spaltet. Folge: unverdaute Laktose gelangt in den Dickdarm, wird fermentiert — Blähungen, Bauchschmerzen, Durchfall. Genetisch bedingt oder sekundär nach Darminfekt / bei Zöliakie.[1] In Deutschland sind 15–25 % der Erwachsenen betroffen, weltweit sogar 65 % (in manchen asiatischen Ländern > 90 %). Die ‚normale' Erwachsenen-Variante ist eigentlich die genetische Ausnahme."),
            ("Diagnose: H2-Atemtest", "Der <strong>H2-Atemtest</strong> ist der Goldstandard: nach Trinken einer Laktose-Lösung wird Wasserstoff in der Atemluft gemessen — erhöhte Werte beweisen die Unverdaulichkeit. Alternativ: Laktose-Toleranz-Test (Blutzucker). Gentest auf LCT-Polymorphismus möglich, aber selten nötig.[2]"),
            ("Individuelle Toleranz — die meisten verzehren mehr als gedacht", "Studien zeigen: 80 % der Laktose-Intoleranten vertragen <strong>5–12 g Laktose pro Mahlzeit</strong> ohne Symptome — das entspricht 100–250 ml Milch. Was hilft:<ul><li><strong>Reifer Käse:</strong> Hartkäse (Parmesan, Bergkäse) enthält < 0,1 g Laktose pro Portion — meist unproblematisch</li><li><strong>Joghurt:</strong> die enthaltenen Milchsäurebakterien spalten Laktose teilweise vor</strong></li><li><strong>Kleine Mengen über den Tag verteilt</strong> statt Milch-Bombe</li><li><strong>Laktose mit anderen Lebensmitteln kombinieren</strong> (Frühstück, nicht solo)</li><li><strong>Laktase-Präparate</strong> bei ausnahmsweisem Konsum</li></ul>"),
            ("Toleranz-Ladder — deine Schwelle finden", "Statt pauschal zu verzichten, finde deine individuelle Schwelle in 6 Stufen:<ol><li><strong>Hartkäse</strong> (Parmesan, Bergkäse, alter Gouda) — fast laktosefrei, meist immer verträglich</li><li><strong>Naturjoghurt</strong> 150 g — Bakterien spalten Laktose vor</li><li><strong>Halbreifer Käse</strong> (Edamer, Gouda jung) — 30 g</li><li><strong>Quark</strong> 100 g — bei zur Mahlzeit verträglich</li><li><strong>Frischkäse, Sahne</strong> in kleinen Mengen</li><li><strong>Milch / Buttermilch</strong> — meist nur in Mengen < 100 ml verträglich</li></ol>Jede Stufe 3 Tage testen, Symptome notieren. Bei Verträglichkeit: nächste Stufe.[7]"),
            ("Kalzium ohne Milch sichern", "Kalziumbedarf 1000 mg/Tag — auch ohne Milchprodukte machbar:<ul><li><strong>Kalziumreiches Mineralwasser</strong> (> 400 mg/l): 1 l = 400 mg</li><li><strong>Brokkoli</strong> 200 g = 105 mg</li><li><strong>Grünkohl</strong> 100 g = 200 mg</li><li><strong>Mandeln</strong> 50 g = 130 mg</li><li><strong>Sesam (Tahini)</strong> 30 g = 230 mg</li><li><strong>Kalzium-angereicherter Soja-/Hafer-Drink</strong> 250 ml = 300 mg</li><li><strong>Sardinen mit Gräten</strong> 100 g = 380 mg</li><li><strong>Tofu (mit Kalziumsulfat)</strong> 150 g = 260 mg</li></ul>Bei Frauen > 50 und Männern > 65 zusätzlich Vitamin D 800 IE/Tag — sonst nützt das Kalzium nichts."),
            ("Häufige Fehler", "<ol><li><strong>Komplette Karenz ohne Test:</strong> die meisten vertragen mehr als sie denken</li><li><strong>‚Laktosefrei'-Produkte ohne Notwendigkeit:</strong> oft Marketing-Hype, teurer und manchmal süßer</li><li><strong>Pflanzendrinks ohne Kalzium-Anreicherung:</strong> liefern kein Kalzium — Etikett lesen</li><li><strong>Vitamin D vergessen:</strong> ohne D-Spiegel > 30 ng/ml wird Kalzium nicht resorbiert</li><li><strong>Versteckte Laktose nicht erkennen:</strong> in Brot, Wurst, Süßigkeiten, Medikamenten — Zutatenliste prüfen</li></ol>"),
            ("Wann professionelle Begleitung?", "Wenn deine Toleranz unklar ist, du unnötig stark restriktiv lebst oder ein begleitendes Reizdarmsyndrom besteht. Bei Laktose-Intoleranz (ICD E73) ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Muss ich auf alle Milchprodukte verzichten?", "Nein. Die meisten Betroffenen vertragen 5–12 g Laktose pro Mahlzeit. Hartkäse und Joghurt sind oft unproblematisch."),
            ("Wie sichere ich meine Kalzium-Versorgung?", "Hartkäse, kalziumreiches Mineralwasser (> 400 mg/l), Brokkoli, Grünkohl, Mandeln, kalziumangereicherte Pflanzendrinks. Wir berechnen das in der Beratung individuell."),
            ("Was unterscheidet Laktose-Intoleranz von Milchallergie?", "Allergie ist eine Immunreaktion gegen Milchproteine (selten, oft im Kindesalter). Laktose-Intoleranz ist ein Enzymmangel — kein Immungeschehen, keine schwere Reaktion."),
            ("Sind A2-Milchprodukte besser verträglich?", "A2-Milch (nur A2-β-Casein) ist ein anderer Aspekt — sie hilft Menschen mit Casein-Empfindlichkeit, nicht der klassischen Laktose-Intoleranz. Bei Laktose-Intoleranz enthält A2-Milch genauso viel Laktose wie normale Milch — kein Vorteil."),
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
            ("Savaiano DA", "(2014): „Lactose digestion from yogurt: mechanism and relevance.\" Am J Clin Nutr, 99(5 Suppl):1251S–1255S.", "https://academic.oup.com/ajcn/article/99/5/1251S/4577405"),
            ("Szilagyi A", "(2015): „Adaptation to lactose in lactase non persistent people.\" Nutrients, 7:6751–6779.", "https://www.mdpi.com/2072-6643/7/8/5333"),
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
            ("Was ist Fructose-Malabsorption?", "Bei intestinaler Fructose-Malabsorption wird Fructose unzureichend über den GLUT5-Transporter im Dünndarm aufgenommen. Sie gelangt in den Dickdarm, wird fermentiert — Symptome. Wichtig: Das ist <strong>nicht</strong> die seltene, lebensbedrohliche hereditäre Fructose-Intoleranz (HFI), die einen kompletten lebenslangen Verzicht erfordert.[1] Etwa 30 % der mitteleuropäischen Bevölkerung haben eine reduzierte Fructose-Resorption — nicht alle entwickeln Symptome."),
            ("Diagnose & Abgrenzung", "<strong>H2-Atemtest mit 25 g Fructose</strong> ist Standard. Vorher ärztliche Anamnese zur Abgrenzung der HFI (Aldolase-B-Defekt). Häufige Kombination: <strong>Sorbit-Intoleranz</strong> — Sorbit blockiert den GLUT5-Transporter zusätzlich.[2]"),
            ("Das 3-Stufen-Protokoll", "<ol><li><strong>Karenzphase (2–4 Wochen):</strong> strikt fructosearm — Symptomfreiheit als Ziel</li><li><strong>Testphase (4–6 Wochen):</strong> schrittweise Wiedereinführung in kleinen Mengen, gemeinsam mit <strong>Glukose</strong> (Glukose erleichtert die Fructose-Resorption)</li><li><strong>Dauerernährung:</strong> individuell tolerierte Menge — meist 8–15 g Fructose pro Mahlzeit möglich</li></ol>Vermieden werden in Phase 1: Apfel, Birne, Mango, Süßstoffe (Sorbit, Xylit), Honig, Agavendicksaft, Fruchtsaft.<br>Bevorzugt: Banane, Beeren, Zitrusfrüchte (Fructose:Glukose-Verhältnis ≤ 1)."),
            ("Der Glukose-Trick — wie Glukose Fructose ausgleicht", "Der Trick mit Glukose ist wissenschaftlich gut belegt[7]: Sobald Glukose im Darm vorhanden ist, aktiviert sich GLUT2, der auch Fructose mit-transportiert. Praktisch bedeutet das:<ul><li><strong>Obst zu einer Mahlzeit</strong> mit Stärke (Brot, Müsli, Kartoffel) → bessere Toleranz</li><li><strong>Banane statt Apfel</strong> — Glukose:Fructose 1:1 (Apfel 1:2)</li><li><strong>Beeren bevorzugen</strong> — günstiges Verhältnis</li><li><strong>Traubenzucker (Dextrose) im Notfall:</strong> 1 TL zur Fructose-Mahlzeit kann Symptome reduzieren</li><li><strong>Vorsicht bei Säften:</strong> hohe Konzentration ohne Ballaststoffe → Symptome wahrscheinlicher</li></ul>"),
            ("Lebensmittel-Kombinationen, die helfen", "<strong>Gut verträglich:</strong><ul><li>Banane mit Haferflocken & Milch</li><li>Beeren auf Vollkornbrot mit Quark</li><li>Mandarine zur Reis-Mahlzeit</li><li>Kartoffeln mit Gemüse (Glukose-haltig)</li></ul><strong>Schlecht verträglich:</strong><ul><li>Apfelsaft solo (hohe Fructose, kein Glukose-Puffer)</li><li>Trockenfrüchte als Snack</li><li>Honig pur</li><li>Light-Joghurt (oft mit Fructose-Sirup)</li></ul><strong>Versteckte Quellen:</strong> Wurst (Geschmacksverstärker), Cola, Süßigkeiten, ‚gesunde' Bio-Riegel mit Agavendicksaft."),
            ("Häufige Fehler", "<ol><li><strong>Komplette Obst-Karenz langfristig:</strong> Ballaststoff- und Mikronährstoff-Mangel droht</li><li><strong>Fructose-freie Spezial-Produkte ohne Test:</strong> oft unnötig teuer</li><li><strong>Sorbit-haltige ‚zuckerfreie' Süßigkeiten:</strong> doppelt schlecht (verschärft GLUT5-Blockade)</li><li><strong>Solo-Obst-Snacks zwischen Mahlzeiten:</strong> hohe Fructose-Last ohne Glukose-Puffer</li><li><strong>Eigentherapie ohne H2-Test:</strong> bei Verdacht erst Diagnose sichern</li></ol>"),
            ("Wann professionelle Begleitung?", "Bei unklarer Diagnose, ausbleibender Besserung nach Karenz oder gleichzeitigem Reizdarm. Bei Fructose-Malabsorption (ICD E74.1) ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Muss ich alle Obstsorten meiden?", "Nein. Beeren, Zitrusfrüchte und Bananen werden meist gut vertragen (Glukose:Fructose-Verhältnis günstig). Apfel, Birne, Mango sind kritischer."),
            ("Was ist der Unterschied zur hereditären Fructose-Intoleranz (HFI)?", "HFI ist eine seltene, lebensbedrohliche Enzymdefekt-Erkrankung — strikter, lebenslanger Verzicht nötig. Intestinale Malabsorption ist häufig und meist gut managebar."),
            ("Hilft Glukose dabei, Fructose besser zu verdauen?", "Ja. Glukose unterstützt die Fructose-Resorption über den GLUT2-Transporter. Praktisch bedeutet das: Obst lieber zu Mahlzeiten mit Stärke essen, nicht solo."),
            ("Ist Honig erlaubt?", "Honig hat ein ungünstiges Fructose:Glukose-Verhältnis (~1,2:1) und ist in der Karenzphase tabu. In der Toleranzphase einzeln testen — kleinere Mengen (≤ 1 TL) in Kombination mit Brot oft verträglich."),
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
            ("Truswell AS et al.", "(1988): „Incomplete absorption of pure fructose in healthy subjects and the facilitating effect of glucose.\" Am J Clin Nutr, 48:1424–1430.", "https://academic.oup.com/ajcn/article-abstract/48/6/1424/4716234"),
            ("Skoog SM, Bharucha AE", "(2004): „Dietary fructose and gastrointestinal symptoms: a review.\" Am J Gastroenterol, 99:2046–2050.", "https://journals.lww.com/ajg/Abstract/2004/10000/Dietary_Fructose_and_Gastrointestinal_Symptoms__A.36.aspx"),
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
            ("Was ist Sorbit-Intoleranz?", "Sorbit (E420) ist ein Zuckeralkohol, der industriell als Süßungsmittel in zuckerfreien Produkten eingesetzt wird — natürlich vorkommend in Steinobst und Trockenfrüchten. Bei unzureichender Resorption gelangt Sorbit in den Dickdarm und verursacht osmotische Diarrhö und Blähungen. Sorbit hemmt zudem den GLUT5-Transporter und verstärkt Fructose-Malabsorption.[1] Etwa 30–35 % der Erwachsenen können nur kleine Mengen Sorbit ohne Symptome verarbeiten."),
            ("Versteckte Quellen erkennen", "<ul><li><strong>Süßstoff-Etikett:</strong> E420, Sorbit, Sorbitol, Sorbitolsirup</li><li><strong>Zuckerfreie Produkte:</strong> Kaugummi, Bonbons, Schokolade, Gummibärchen</li><li><strong>Medikamente / Hustensaft:</strong> oft Sorbit als Trägerstoff</li><li><strong>Steinobst:</strong> Pflaumen, Aprikosen, Pfirsiche, Kirschen</li><li><strong>Trockenfrüchte:</strong> besonders konzentriert</li><li><strong>Light-Joghurts und Diätprodukte</strong></li></ul>"),
            ("3-Stufen-Protokoll wie bei Fructose", "<ol><li><strong>Karenzphase (2–4 Wochen):</strong> strikt sorbitarm</li><li><strong>Testphase:</strong> schrittweise Wiedereinführung in definierten Mengen</li><li><strong>Dauerernährung:</strong> individuelle Toleranzgrenze ermitteln — meist 5–10 g/Tag möglich</li></ol>Bei kombinierter Fructose-Sorbit-Problematik: gemeinsames Vorgehen, das die Wechselwirkung berücksichtigt."),
            ("Medikamenten-Check — die übersehene Quelle", "Viele Patient:innen unterschätzen, dass Medikamente Sorbit als Hilfsstoff enthalten:<ul><li><strong>Hustensäfte und Säfte für Kinder</strong> — fast immer mit Sorbit</li><li><strong>Vitamin-Sirupe</strong> für Senioren</li><li><strong>Abführmittel</strong> (Macrogol-Pulver oft sorbitfrei, aber Sirupe gerne mit)</li><li><strong>Magensäure-Tabletten (Antazida)</strong> wie Maaloxan</li><li><strong>Lösungen für Diabetiker</strong> als ‚Zucker-Alternative'</li></ul>Wenn Symptome trotz konsequenter Ernährung bleiben: Beipackzettel checken oder Apotheker:in fragen. Alternativen lassen sich fast immer finden."),
            ("Praktische Umsetzung — Restaurant & Reise", "<strong>Restaurant-Strategie:</strong> nach hausgemachten Saucen fragen (industrielle enthalten oft Sorbit), Desserts meiden oder nach Mengen fragen.<br><strong>Im Hotel:</strong> Frühstücks-Buffets vorsichtig — Trockenfrüchte und ‚Diät'-Joghurts vermeiden.<br><strong>Reise-Snack:</strong> normale Schokolade besser als ‚zuckerfreie' Riegel (oft mit Sorbit/Xylit).<br><strong>Apotheke / Notfall:</strong> auf Reise immer Pankreasenzym-Präparat sorbitfrei mitnehmen.<br><strong>Etiketten-Schnellcheck:</strong> E420 = Sorbit, E421 = Mannit (ähnlich problematisch), E965 = Maltit, E966 = Lactit, E967 = Xylit (oft besser verträglich)."),
            ("Häufige Fehler", "<ol><li><strong>Kaugummi nach dem Essen ‚für die Zähne':</strong> kann sorbithaltig sein und stundenlang Beschwerden verursachen</li><li><strong>Trockenpflaumen als ‚Verdauungshelfer':</strong> 5 Pflaumen = 8–12 g Sorbit → Übermäßige Wirkung gerade bei Intoleranz</li><li><strong>Light-Eis oder zuckerfreies Eis:</strong> fast immer Sorbit-haltig</li><li><strong>Kombination mit Fructose ignorieren:</strong> Verstärkt sich gegenseitig dramatisch</li><li><strong>Eigentherapie ohne H2-Test:</strong> Symptome können auch andere Ursachen haben (SIBO, Reizdarm)</li></ol>"),
            ("Wann professionelle Begleitung?", "Bei chronischen Beschwerden, unklaren Ergebnissen, kombinierten Intoleranzen oder Verdacht auf Reizdarm. Bei Sorbit-Intoleranz (ICD E74.3) ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Wie wird Sorbit-Intoleranz diagnostiziert?", "H2-Atemtest mit Sorbit-Lösung. Ärztliche Anamnese und Symptom-Tagebuch sind ergänzend wichtig."),
            ("Welche Lebensmittel sind besonders sorbit-reich?", "Trockenfrüchte (besonders Pflaumen), zuckerfreie Bonbons und Kaugummi, Light-Produkte, Steinobst."),
            ("Hängt Sorbit mit Fructose zusammen?", "Ja. Sorbit hemmt den GLUT5-Transporter, der Fructose resorbiert. Wer beides hat, sollte gemeinsam beraten werden."),
            ("Sorbit in Trockenfrüchten — welche Mengen?", "Pflaumen 6–10 g/100 g, Aprikosen 5 g/100 g, Pfirsiche 1–2 g/100 g, Kirschen 1–2 g/100 g. Toleranz bei Intoleranten meist < 5 g/Tag — also schon 50 g Trockenpflaumen können Beschwerden auslösen."),
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
            ("Beaugerie L et al.", "(1996): „Digestion and absorption of polyols and sugar substitutes.\" Eur J Clin Nutr, 50(Suppl 1):S77–S81.", "https://pubmed.ncbi.nlm.nih.gov/8735755/"),
            ("Born P et al.", "(2007): „Carbohydrate malabsorption — sorbitol and intestinal symptoms.\" Z Gastroenterol, 45:1019–1024.", "https://www.thieme-connect.com/products/ejournals/abstract/10.1055/s-2007-963495"),
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
            ("PCOS & Endometriose im Überblick", "PCOS (Polyzystisches Ovarial-Syndrom) ist die häufigste hormonelle Störung bei Frauen im gebärfähigen Alter — geprägt von Hyperandrogenämie, Zyklusstörungen, oft Insulinresistenz. Endometriose ist eine chronisch-entzündliche Erkrankung mit Endometrium-Gewebe außerhalb der Gebärmutter — starke Menstruations- und Beckenschmerzen.[1][2] In Deutschland sind ca. 1,4 Millionen Frauen von PCOS und 2 Millionen von Endometriose betroffen — beide häufig viel zu spät diagnostiziert."),
            ("PCOS — Ernährung als Schlüssel", "Die internationale PCOS-Leitlinie (Teede et al. 2023) empfiehlt:<ul><li><strong>Mediterrane oder DASH-Ernährung</strong> als Basis</li><li><strong>Niedriger glykämischer Index</strong> — Vollkorn, Hülsenfrüchte, Beeren</li><li><strong>Eiweißreiche Mahlzeiten</strong> (1,2 g/kg KG)</li><li><strong>Wenig Zucker und Fertigprodukte</strong> — Insulin-Spitzen vermeiden</li><li><strong>Bei Übergewicht:</strong> 5–10 % Gewichtsreduktion verbessert Zyklus und Fruchtbarkeit deutlich</li><li><strong>Inositol-Supplementierung (Myo + D-Chiro 40:1):</strong> in Studien bei PCOS hilfreich</li></ul>"),
            ("Endometriose — anti-entzündlich essen", "Mediterrane Kost mit hohem Omega-3-Anteil reduziert in Beobachtungsstudien Schmerzen und Krankheitsaktivität. Reduktion: rotes Fleisch (RR ↑), trans-Fette. Erhöhung: Gemüse, Fisch, Olivenöl, Beeren. Bei manchen Patientinnen lindert Low-FODMAP zusätzlich Reizdarm-Symptome, die mit Endometriose koexistieren.[3]"),
            ("Insulinresistenz verstehen — warum sie zentral ist", "Bei PCOS ist Insulinresistenz das zentrale Problem: Die Zellen reagieren schlechter auf Insulin, der Körper produziert mehr → die Eierstöcke werden zu erhöhter Testosteron-Produktion stimuliert → Zyklusstörungen, Akne, Haarausfall, Gewichtszunahme.[7] Was Ernährung tut: Niedrig-glykämische Mahlzeiten reduzieren die Insulin-Spitzen, brechen den Teufelskreis. <strong>Praktische Marker:</strong> Nüchterninsulin sollte < 10 µU/ml, HOMA-IR < 2,5 sein. <strong>Effekte einer kohlenhydrat-bewussten Ernährung:</strong> Nüchterninsulin sinkt um 20–40 % innerhalb 12 Wochen (Moran 2013), Zyklen normalisieren sich bei 50 % der PCOS-Patient:innen.[7]"),
            ("Fruchtbarkeit & Ernährung", "Wenn Kinderwunsch besteht, ist Ernährung ein unterschätzter Hebel:<ul><li><strong>5–10 % Gewichtsverlust</strong> bei Adipositas → Spontane Ovulation in 30–60 % der Fälle</li><li><strong>Mediterrane Ernährung</strong> verbessert IVF-Outcomes (Lebensgeburt-Rate +66 %)[8]</li><li><strong>Folsäure 400 µg/Tag</strong> ab 3 Monate vor geplanter Konzeption</li><li><strong>Omega-3 (200 mg DHA)</strong> verbessert Eizell-Qualität</li><li><strong>Vermeiden:</strong> trans-Fette (Frittiertes, Industriebackwaren) — reduzieren Fruchtbarkeit signifikant (Nurses Health Study)</li><li><strong>Männliche Fruchtbarkeit:</strong> Partnerinnen-Studien zeigen Spermienqualität profitiert ebenso von mediterraner Kost</li></ul>"),
            ("Häufige Fehler", "<ol><li><strong>Crash-Diäten bei PCOS:</strong> verschlechtern die hormonelle Balance — langfristige Anpassung wirkt besser</li><li><strong>Glutenfrei essen ohne Zöliakie:</strong> bei Endometriose oft als Wundermittel gehypet, Evidenz schwach</li><li><strong>Soja meiden ‚wegen Östrogenen':</strong> Phytoöstrogene wirken modulierend, nicht zwingend ungünstig — Studien neutral</li><li><strong>Inositol ohne ärztliche Abklärung hochdosiert:</strong> Wirkung auf Schilddrüse beachten</li><li><strong>Ernährung als Ersatz für Medikamente:</strong> bei schwerem PCOS / Endometriose bleiben Hormonelle Therapien und ggf. OP unverzichtbar</li></ol>"),
            ("Wann professionelle Begleitung?", "Bei Diagnose, Kinderwunsch, Insulinresistenz, deutlicher Gewichtsproblematik oder ausgeprägten Endometriose-Schmerzen. Bei PCOS / Endometriose ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Hilft Ernährung wirklich bei PCOS?", "Ja. Mediterrane, kohlenhydrat-bewusste Ernährung verbessert Zyklus, Insulinwerte, Hautbild und Fruchtbarkeit. In Kombination mit Bewegung sind die Effekte mit Metformin vergleichbar."),
            ("Brauche ich Inositol?", "Bei PCOS mit Insulinresistenz haben Studien moderate Effekte gezeigt (Myo-Inositol + D-Chiro im Verhältnis 40:1, 4 g/Tag). Vor Einnahme ärztlich abklären."),
            ("Welche Ernährung hilft bei Endometriose-Schmerzen?", "Anti-entzündlich, Omega-3-reich, mediterran. Reduktion von rotem Fleisch und trans-Fetten. Beobachtungsstudien zeigen Schmerz-Reduktion."),
            ("Glykämische Last vs. glykämischer Index — was zählt?", "Bei PCOS die glykämische Last (GL). Sie kombiniert glykämischen Index mit Portion und ist alltagstauglicher. Ziel: tägliche GL < 100. Beispiel: 1 Apfel hat GI 38, GL 6 — sehr günstig. 1 Cola hat GI 63, GL 16 — schlecht."),
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
            ("Moran LJ et al.", "(2013): „Dietary composition in restoring reproductive and metabolic physiology in overweight women with PCOS.\" J Clin Endocrinol Metab, 88:812–819.", "https://academic.oup.com/jcem/article/88/2/812/2845221"),
            ("Karayiannis D et al.", "(2018): „Adherence to the Mediterranean diet and IVF success rate.\" Hum Reprod, 33:494–502.", "https://academic.oup.com/humrep/article/33/3/494/4828630"),
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
            ("Gestationsdiabetes — was tun?", "Etwa 6–10 % der Schwangeren entwickeln einen Gestationsdiabetes (GDM). Ernährung ist die Erst-Therapie:<ul><li><strong>3 Hauptmahlzeiten + 2–3 Snacks</strong> — gleichmäßige BZ-Kurve</li><li><strong>Komplexe Kohlenhydrate</strong> (Vollkorn, Hülsenfrüchte) statt Weißmehl & Zucker</li><li><strong>Eiweiß zu jeder Mahlzeit</strong> — sättigt und glättet Blutzucker</li><li><strong>Gemüse zuerst essen</strong> (Tellerprinzip — Glukose-Spitzen ↓ 30 %)</li><li><strong>Spazierengehen 10 Min nach jeder Mahlzeit</strong></li><li><strong>BZ-Selbstmessung</strong> nüchtern und 1 h postprandial — Werte mit Diabetolog:in besprechen</li></ul>Nach Geburt klärt sich GDM meist — aber 50 % entwickeln innerhalb 10 Jahren Typ-2-Diabetes. Nachsorge ist wichtig.[7]"),
            ("Praktische Tagespläne", "<strong>Beispiel-Tag 2. Trimester:</strong><ul><li><strong>Frühstück:</strong> Vollkornbrot mit Frischkäse + Tomate, Apfel, kleines Glas Milch (≈ 450 kcal)</li><li><strong>Snack:</strong> Skyr mit Beeren + Mandeln (≈ 250 kcal)</li><li><strong>Mittag:</strong> Lachsfilet mit Quinoa, Brokkoli, Olivenöl (≈ 600 kcal, DHA + Eisen)</li><li><strong>Snack:</strong> Banane mit Erdnussmus (≈ 250 kcal)</li><li><strong>Abend:</strong> Linsen-Eintopf mit Süßkartoffeln & Vollkornbrot (≈ 500 kcal)</li><li><strong>Supplement:</strong> Folsäure + Jod (in der Frühschwangerschaft), DHA-Algenöl, Vit D (Winter)</li></ul>Gesamt ≈ 2050 kcal — Bedarf 2. Trimester (vorher 1800 + 250)."),
            ("Häufige Fehler", "<ol><li><strong>‚Essen für zwei':</strong> übermäßiger Gewichtszuwachs (> IOM-Empfehlung) erhöht Risiko für GDM und Komplikationen</li><li><strong>Folsäure erst ab positivem Test:</strong> Neuralrohr schließt in den ersten 4 Wochen — also schon vor positiver Diagnose nötig</li><li><strong>Fisch komplett meiden:</strong> die DHA aus 2× Lachs/Woche ist wertvoll — nur Quecksilber-reiche Sorten meiden</li><li><strong>Heißhunger-Falle:</strong> nicht jeder Heißhunger ist Nährstoff-Signal — Wasser trinken, kleine Eiweiß-Snacks helfen</li><li><strong>Stillzeit-Diäten:</strong> beim Abnehmen langsam (max. 0,5 kg/Woche) — Milchproduktion und Hormonbalance beachten</li></ol>"),
            ("Wann professionelle Begleitung?", "Bei Gestationsdiabetes, übermäßigem Gewichtszuwachs / -verlust, veganer Ernährung, Mehrlingsschwangerschaft, Vorerkrankungen (PCOS, Schilddrüse). Die Beratung in Schwangerschaft / Stillzeit ist bei medizinischer Notwendigkeit über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Wie viel mehr muss ich essen?", "Im 2. Trimester +250 kcal/Tag, in der Stillzeit +500 kcal/Tag. Das entspricht ca. einer zusätzlichen Hauptmahlzeit oder mehreren Snacks."),
            ("Brauche ich Nahrungsergänzungsmittel?", "Folsäure ist klar empfohlen (400 µg/Tag), Jod wird oft kombiniert. Vitamin D ganzjährig sinnvoll. Bei veganer Ernährung B12 obligat. Eisen nach Laborwerten."),
            ("Welche Lebensmittel sollte ich meiden?", "Rohmilchprodukte, rohes Fleisch, roher Fisch, quecksilberreicher Fisch, Alkohol, übermäßig Koffein. Leber nur sparsam."),
            ("Heißhunger — okay nachgeben?", "In moderaten Mengen ja — strikte Verbote führen oft zu Schuldgefühlen. Strategie: 1 Stück Schokolade nach dem Essen statt halbe Tafel solo am Nachmittag. Heißhunger auf Ungesundes oft Stress- oder Schlafsignal — nicht Nährstoffmangel."),
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
            ("Schäfer-Graf U et al.", "(2024): „S3-Leitlinie Gestationsdiabetes.\" AWMF-Register 057/008.", "https://www.awmf.org/leitlinien/detail/ll/057-008.html"),
            ("Bookhart LH et al.", "(2022): „Maternal Diet and Birth Outcomes — Mediterranean Diet Adherence.\" JAMA Netw Open, 5:e2243349.", "https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2798994"),
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
            ("Ausdauer vs. Kraft — anderer Bedarf", "<strong>Ausdauer-Sportler:innen</strong> brauchen Kohlenhydrate als Hauptenergiequelle:<ul><li>Glykogen-Speicher füllen: 5–7 g KH/kg KG normal, 8–10 g vor langen Einheiten</li><li>Carb-Loading 36–48 h vor Wettkampf (Marathon, Triathlon): bis 10–12 g/kg</li><li>Während Wettkampf (> 90 Min): 30–60 g KH/h (Gels, Riegel, Bananen)</li><li>Eiweiß: 1,2–1,6 g/kg KG für Erhalt der Muskelmasse</li></ul><strong>Kraft-Sportler:innen</strong> brauchen mehr Eiweiß, weniger KH-Schwankungen:<ul><li>Eiweiß: 1,6–2,2 g/kg, verteilt auf 4–5 Portionen à 0,4 g/kg</li><li>KH: 3–5 g/kg ausreichend (außer Wettkampftag)</li><li>Kreatin 3–5 g/Tag: Kraft- und Power-Output ↑ 5–10 %[7]</li><li>Fett nicht unter 0,8 g/kg — Hormonbalance beachten</li></ul>"),
            ("Hydration & Elektrolyte — praktische Tipps", "<strong>Vor dem Training:</strong> 5–10 ml/kg KG in den 2–4 h davor (also 350–700 ml). Urin sollte hellgelb sein.<br><strong>Während:</strong><ul><li>< 60 Min: Wasser reicht</li><li>60–90 Min: 6–8 % KH-Lösung (Sportgetränk)</li><li>> 90 Min: KH + Natrium 0,3–0,7 g/l</li><li>Hitze: zusätzlich Magnesium und Kalium</li></ul><strong>Nach dem Training:</strong> 1,5 l Flüssigkeit pro kg Gewichtsverlust durch Schwitzen (wiegen vorher/nachher!).[8]<br><strong>Hyponatriämie-Risiko</strong> bei sehr langen Belastungen mit zu viel reinem Wasser (Marathon, Ironman) — Salz unbedingt mit reinnehmen."),
            ("Häufige Fehler", "<ol><li><strong>Zu viel Eiweiß ohne Kohlenhydrate:</strong> Glykogen-Speicher leer → Trainingsqualität sinkt</li><li><strong>Carb-Cutting auch an Trainingstagen:</strong> Performance ↓ 20–30 %</li><li><strong>Recovery-Fenster ignorieren:</strong> in den 60 Min nach Training fehlt der Anabolen-Reiz</li><li><strong>Supplements vor Basis-Ernährung:</strong> erst Naturkost optimieren, dann Kreatin & Co.</li><li><strong>RED-S unterschätzen:</strong> Energie-Mangel-Syndrom (besonders bei Läuferinnen) — Zyklus, Stimmung und Performance sind Marker. Sofort handeln.</li></ol>"),
            ("Wann professionelle Begleitung?", "Vor Wettkampf-Vorbereitungen, in Diätphasen, bei Energie-Mangel-Syndromen (RED-S), Performance-Plateaus oder Übertraining-Symptomen. Bei Sportverletzungen kann die Beratung als ergänzende Maßnahme über §43 SGB V erstattungsfähig sein — typisch 80 %. Reine Performance-Beratung meist privat."),
        ],
        "faqs": [
            ("Wie viel Eiweiß brauche ich wirklich?", "Kraft: 1,6–2,0 g/kg KG. Ausdauer: 1,4 g/kg. Mehr als 2,2 g/kg bringt keinen Mehrwert. Verteilt auf 4 Mahlzeiten."),
            ("Brauche ich Eiweißshakes?", "Nicht zwingend. Sie sind praktisch nach dem Training. Naturbelassene Quellen (Quark, Eier, Fisch, Hülsenfrüchte) sind gleichwertig."),
            ("Was ist die beste Recovery-Mahlzeit?", "Innerhalb von 60 Min nach dem Training: 20–30 g Eiweiß + 60–100 g Kohlenhydrate. Beispiele: Quark mit Banane und Haferflocken; Sandwich mit Putenbrust."),
            ("Kohlenhydrate vor dem Schlaf?", "Ja, für intensive Trainings-Tage: 30–50 g langsame KH (Haferflocken, Vollkornbrot) + 30 g Casein-Eiweiß (Quark) vor dem Schlaf — füllt Glykogen, fördert Recovery. An Ruhetagen oder Diätphasen weglassen."),
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
            ("Kreider RB et al.", "(2017): „ISSN exercise & sports nutrition review on creatine supplementation.\" J Int Soc Sports Nutr, 14:18.", "https://jissn.biomedcentral.com/articles/10.1186/s12970-017-0173-z"),
            ("Sawka MN et al.", "(2007): „American College of Sports Medicine position stand: exercise and fluid replacement.\" Med Sci Sports Exerc, 39:377–390.", "https://journals.lww.com/acsm-msse/Fulltext/2007/02000/Exercise_and_Fluid_Replacement.22.aspx"),
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
            ("Was passiert in den Wechseljahren?", "Die Wechseljahre umfassen Prä-, Peri- und Postmenopause. Östrogen sinkt — mit Folgen für Körperzusammensetzung (mehr viszerales Fett), Knochendichte, Lipidprofil, Insulinwirkung und Stimmung. Hauptsymptome: Hitzewallungen, Schlafstörungen, Gewichtszunahme.[1] In Deutschland sind ca. 9 Millionen Frauen aktuell in den Wechseljahren — viele unzureichend versorgt."),
            ("Ernährung als Schutz", "<ul><li><strong>Mediterrane Ernährung:</strong> reduziert kardiovaskuläres Risiko und unterstützt Gewichts-Stabilisierung</li><li><strong>Eiweiß 1,2 g/kg KG:</strong> erhält Muskelmasse (entscheidend für Stoffwechsel und Sturzprävention)</li><li><strong>Kalzium 1000 mg + Vitamin D 800–1000 IE:</strong> Osteoporose-Prävention</li><li><strong>Phytoöstrogene</strong> (Soja, Leinsamen): Studien zeigen moderate Reduktion von Hitzewallungen</li><li><strong>Reduktion: Zucker, Alkohol, Koffein</strong> — verstärken Hitzewallungen und Schlafprobleme</li><li><strong>Omega-3:</strong> 2× fetter Fisch/Woche für Herz und Stimmung</li></ul>"),
            ("Gewichtsmanagement — anders als vor 40", "Der Grundumsatz sinkt um 1–2 % pro Jahrzehnt. Kombination aus geringerem Energiebedarf, hormonellen Veränderungen und veränderter Fettverteilung. Lösung: <strong>weniger Kohlenhydrate, mehr Eiweiß, regelmäßiges Krafttraining</strong> — die Kombination ist entscheidend.[2]"),
            ("Schlafqualität & Ernährung", "Schlafstörungen sind eines der belastendsten Wechseljahres-Symptome — 40–60 % der Frauen betroffen. Was Ernährung beitragen kann:<ul><li><strong>Tryptophan-reiche Lebensmittel</strong> abends (Quark, Banane, Hafer): Vorstufe von Melatonin</li><li><strong>Magnesium 300–400 mg/Tag</strong> (Nüsse, Vollkorn): entspannt Muskulatur, fördert Tiefschlaf[7]</li><li><strong>Vitamin B6</strong> als Cofaktor für Melatoninsynthese</li><li><strong>Letzte Mahlzeit 3 h vor Schlaf</strong> — Verdauung stört REM-Phasen</li><li><strong>Alkohol meiden</strong> nach 18 Uhr — fragmentiert Schlaf, verstärkt Hitzewallungen</li><li><strong>Koffein-Stopp ab 14 Uhr</strong> — Halbwertszeit verlängert sich in der Menopause</li><li><strong>Schlafzimmer-Temperatur:</strong> 16–18 °C — wichtig bei Hitzewallungen</li></ul>"),
            ("Sport-Kombination — der wahre Game-Changer", "Ernährung allein reicht nicht — die Kombination mit gezieltem Sport ist entscheidend:<ul><li><strong>Krafttraining 2× pro Woche:</strong> erhält Muskelmasse und Knochendichte. Daley (2014) zeigt Schmerz-/Symptom-Reduktion durch Sport vergleichbar mit HRT[8]</li><li><strong>HIIT (High-Intensity Interval Training) 1× pro Woche:</strong> verbessert Insulinwirkung und Fettverteilung</li><li><strong>Yoga / Pilates 1–2× pro Woche:</strong> Stressreduktion, Schlaf, Beweglichkeit</li><li><strong>Walking 30 Min täglich:</strong> baseline für Herz-Kreislauf</li></ul><strong>Wichtig:</strong> Ohne Sport verliert die Frau in den Wechseljahren 0,5–1 % Muskelmasse pro Jahr. Mit Krafttraining ist Muskelaufbau auch nach der Menopause möglich."),
            ("Häufige Fehler", "<ol><li><strong>Crash-Diäten:</strong> Östrogenmangel + Kalorienrestriktion = Muskel-Verlust statt Fett-Verlust</li><li><strong>Fettarmes Essen:</strong> gesunde Fette (Olivenöl, Nüsse) sind essenziell für Hormonbalance</li><li><strong>Alkohol verharmlosen:</strong> bereits 1 Glas Wein/Tag verstärkt Hitzewallungen und Schlafstörungen messbar</li><li><strong>Sport ‚nur Ausdauer':</strong> ohne Krafttraining geht Muskelmasse</li><li><strong>Soja meiden ‚wegen Östrogenen':</strong> bei den meisten Frauen sicher und sogar protektiv (Messina 2016)[9]</li></ol>"),
            ("Wann professionelle Begleitung?", "Bei deutlicher Gewichtszunahme, Osteoporose-Risiko, Hitzewallungen, in Vorbereitung auf eine Hormonersatztherapie. Wechseljahre-Beratung ist mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Helfen Soja und Phytoöstrogene wirklich bei Hitzewallungen?", "In Meta-Analysen zeigt Soja moderate Effekte (Reduktion um etwa 20 %). Konsequente tägliche Zufuhr nötig. Bei Brustkrebs-Vorgeschichte vorher ärztlich abklären."),
            ("Wie viel Eiweiß brauche ich in der Menopause?", "1,2 g/kg KG — also etwa 70–80 g pro Tag bei einer 60-kg-Frau. Verteilt auf 3–4 Mahlzeiten."),
            ("Warum nehme ich plötzlich zu?", "Östrogenmangel verändert Fettverteilung (mehr Bauchfett), Grundumsatz sinkt, oft auch Muskelabbau. Lösung: weniger einfache Kohlenhydrate, mehr Eiweiß, Krafttraining."),
            ("Ist Soja sicher bei Brustkrebs-Risiko?", "Messina (2016) und große Folgestudien zeigen: Moderater Soja-Konsum (1–2 Portionen/Tag) ist auch bei Brustkrebs-Vorgeschichte sicher und teils protektiv. Bei Tamoxifen-Therapie vor Beginn ärztlich abklären — vorsichtige Empfehlung."),
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
            ("Cao Y et al.", "(2020): „Magnesium intake and sleep disorder symptoms.\" Nutrients, 12:1349.", "https://www.mdpi.com/2072-6643/12/5/1349"),
            ("Daley A et al.", "(2014): „Exercise for vasomotor menopausal symptoms.\" Cochrane Database Syst Rev, CD006108.", "https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD006108.pub4/full"),
            ("Messina M", "(2016): „Impact of soy foods on the development of breast cancer and the prognosis of breast cancer patients.\" Forsch Komplementmed, 23:75–80.", "https://www.karger.com/Article/Abstract/444735"),
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
            ("Pflanzlich essen — die Studienlage", "Vegetarische und vegane Ernährung ist in der Mehrzahl der Studien mit niedrigerem Risiko für Typ-2-Diabetes, Herzinfarkt, Bluthochdruck und einigen Krebsarten verbunden. Vegane Ernährung führt zu niedrigerem LDL und systolischem Blutdruck. Voraussetzung: gute Planung.[1] In Deutschland leben etwa 8 Millionen Vegetarier:innen und 1,5 Millionen Veganer:innen — Tendenz steigend."),
            ("Die kritischen Nährstoffe", "<ul><li><strong>Vitamin B12:</strong> bei veganer Ernährung <em>obligat supplementieren</em> (z. B. 25 µg/Tag oder 2000 µg/Woche). Bei lakto-ovo-vegetarisch kontrollieren</li><li><strong>Eisen:</strong> pflanzliche Quellen (Hülsenfrüchte, Vollkorn, Tofu) — Aufnahme verbessern durch Vitamin C zur Mahlzeit, Kaffee/Tee versetzt</li><li><strong>Zink:</strong> Hülsenfrüchte, Nüsse, Vollkorn — Phytat reduzieren durch Einweichen und Keimen</li><li><strong>Omega-3 (DHA/EPA):</strong> aus Algenöl-Kapseln; Lein- und Walnussöl liefern nur Vorstufe (ALA)</li><li><strong>Jod:</strong> Jodsalz oder Seealgen (nur Nori in kleinen Mengen — andere Algen oft überjodiert)</li><li><strong>Vitamin D:</strong> Eigensynthese + Supplementierung im Winter</li><li><strong>Kalzium:</strong> Mineralwasser (> 400 mg/l), Brokkoli, Grünkohl, Mandeln, angereicherte Pflanzendrinks</li></ul>"),
            ("Eiweißbedarf einfach decken", "Empfehlung: 0,8–1,0 g/kg KG (mehr bei Sportler:innen, Schwangerschaft, Alter). Pflanzliche Eiweißquellen:<ul><li>Hülsenfrüchte (Linsen, Kichererbsen, Bohnen, Lupine)</li><li>Soja & Soja-Produkte (Tofu, Tempeh, Edamame)</li><li>Vollkorn-Getreide (Hafer, Quinoa, Dinkel)</li><li>Nüsse und Samen</li><li>Optional Eiweißpulver auf Erbsen-/Reisbasis</li></ul>Wichtig: <strong>Variation</strong> — verschiedene Quellen kombinieren ergänzt die Aminosäure-Profile."),
            ("Eisen-Resorption optimieren — der Trick mit Vitamin C", "Pflanzliches Eisen (Nicht-Häm-Eisen) wird schlechter resorbiert als tierisches. Die gute Nachricht: Vitamin C steigert die Aufnahme um den Faktor 3–5.[7] Praktisch:<ul><li><strong>Eisenreiche Mahlzeit + Orangensaft / Paprika / Zitrone:</strong> Beispiel: Linsensuppe mit Zitronenspritzer, Hafer mit Beeren, Tofu mit Paprika</li><li><strong>Kaffee/Tee 1 h vor und nach Mahlzeit meiden:</strong> Tannine hemmen Eisenaufnahme um 60–80 %</li><li><strong>Eisenkochtöpfe</strong> (Lucky Iron Fish, gusseiserne Pfanne): einfach effektiv, 1–2 mg pro Mahlzeit</li><li><strong>Phytate reduzieren</strong> durch Einweichen, Keimen, Sauerteig-Gärung</li><li><strong>Eisen-Status prüfen</strong>: Ferritin alle 6–12 Monate, Ziel > 30 µg/l</li></ul>Bei nachgewiesenem Mangel: gezielte Substitution unter ärztlicher Begleitung."),
            ("Familie & Kinder — sicher pflanzlich aufwachsen", "Vegetarische Ernährung ist für Kinder unproblematisch — vegan erfordert mehr Aufmerksamkeit. DGE-Position 2024 und ESPGHAN sind zurückhaltend, ProVeg und AAP halten vegane Ernährung bei strukturierter Begleitung für möglich.[8] Schlüssel:<ul><li><strong>B12 obligat supplementieren</strong> — kein Spielraum</li><li><strong>Vitamin D 400–600 IE/Tag</strong> im 1. Lebensjahr, danach 600–1000 IE</li><li><strong>Hochkalorische Energie:</strong> Nüsse, Avocado, Olivenöl — Kinder können Volumen nicht so leicht erreichen</li><li><strong>Eisen-Status</strong> bei jeder Vorsorge-Untersuchung</li><li><strong>Stillen oder angereicherte Säuglingsnahrung</strong> im 1. Jahr — Soja-Drink als Hauptmilch ist <em>nicht</em> ausreichend</li><li><strong>Kinderarzt einbeziehen</strong> — nicht alle sind vegan-erfahren, ggf. Spezialist:in suchen</li></ul>"),
            ("Häufige Fehler", "<ol><li><strong>B12 ‚aus Algen' / ‚aus Sauerkraut':</strong> nicht ausreichend bioverfügbar — Supplementierung obligat</li><li><strong>Eiweißmangel durch zu wenig Hülsenfrüchte:</strong> tägliche Portion nötig</li><li><strong>Hochverarbeitete vegane Fertigprodukte:</strong> oft viel Salz, Zucker, Zusatzstoffe — frisch kochen bevorzugen</li><li><strong>Kein Eisen-Test:</strong> alle 6–12 Monate Ferritin prüfen</li><li><strong>Vegan ohne Plan im Sport / Schwangerschaft / Kinder:</strong> hier braucht es zwingend professionelle Begleitung</li></ol>"),
            ("Wann professionelle Begleitung?", "Vor der Umstellung, in Schwangerschaft/Stillzeit, bei Kindern, Senioren, Leistungssportler:innen, bei chronischen Erkrankungen oder Mangelzuständen. Bei nachgewiesenem Mangel ist die Beratung mit ärztlicher Bescheinigung über §43 SGB V erstattungsfähig — typisch 80 %."),
        ],
        "faqs": [
            ("Muss ich als Veganer B12 supplementieren?", "Ja, immer. Es gibt keine zuverlässig veganen B12-Quellen. Supplementierung ist nicht optional, sondern obligat."),
            ("Bekomme ich genug Eiweiß ohne Fleisch?", "Ja. Hülsenfrüchte, Soja, Vollkorn, Nüsse decken den Bedarf gut. Wichtig: Vielfalt und ausreichende Menge."),
            ("Welches Omega-3 ist am besten?", "Für DHA/EPA: Algenöl-Kapseln. Lein- und Walnussöl liefern nur die Vorstufe ALA, die nur zu 5–15 % umgewandelt wird."),
            ("Was, wenn meine Werte schlecht sind?", "Ferritin < 30 µg/l, B12 < 250 pg/ml oder Vitamin D < 20 ng/ml → ärztlich abklären, gezielt substituieren. Häufig reicht 3-Monats-Substitution + Anpassung der Ernährung. Bei wiederholtem Mangel ggf. Diagnostik auf Resorptionsstörung (Zöliakie, Helicobacter)."),
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
            ("Hallberg L, Hulthén L", "(2000): „Prediction of dietary iron absorption.\" Am J Clin Nutr, 71:1147–1160.", "https://academic.oup.com/ajcn/article/71/5/1147/4729333"),
            ("Baroni L et al.", "(2018): „Vegan Nutrition for Mothers and Children.\" Nutrients, 11:5.", "https://www.mdpi.com/2072-6643/11/1/5"),
        ],
        "related": ["schwangerschaft-stillzeit-ernaehrung", "sport-performance-ernaehrung", "diabetes-typ-2-ernaehrung"],
    },
]


# ============================================================
# HTML-TEMPLATE
# ============================================================

def slugify(s):
    """Make a section ID from a section title."""
    import re as _re
    s = s.lower()
    s = s.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    s = _re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:40] or "sektion"


def add_citation_links(text):
    """Wandele [1], [2] etc. in klickbare Links zu den Quellen-IDs um (genau wie bei Fettleber)."""
    import re as _re
    return _re.sub(r'\[(\d+)\]', r'<a href="#q\1">[\1]</a>', text)


def estimate_reading_time(ind):
    """Estimate reading time in minutes from word count of sections + quick."""
    import re as _re
    text = ind.get("quick", "") + " " + " ".join(b for _, b in ind.get("sections", []))
    text = _re.sub(r"<[^>]+>", " ", text)  # strip HTML tags
    words = len(text.split())
    return max(5, round(words / 220))


def render_article(ind):
    """Render kompletten HTML-Artikel für eine Indikation."""
    section_ids = [slugify(t) for t, _ in ind["sections"]]
    sections_html = "\n".join(
        f'        <h2 id="{section_ids[i]}">{html.escape(title)}</h2>\n        <p>{add_citation_links(body)}</p>'
        for i, (title, body) in enumerate(ind["sections"])
    )
    # Auch Quick-Answer mit klickbaren Zitaten versehen, falls vorhanden
    ind = {**ind, "quick": add_citation_links(ind["quick"])}
    toc_html = "\n".join(
        f'            <li><a href="#{section_ids[i]}" class="hover:text-brand-700">{html.escape(title)}</a></li>'
        for i, (title, _) in enumerate(ind["sections"])
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
    reading_time = estimate_reading_time(ind)
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
        <div class="mt-6 flex flex-wrap gap-x-6 gap-y-2 text-xs text-white/60"><span>📅 Stand: 18. Mai 2026</span><span>⏱ {reading_time} Min Lesezeit</span><span>🔬 {len(ind["quellen"])} wissenschaftliche Quellen</span></div>
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

        <nav aria-label="Inhalt" class="rounded-2xl bg-ink-50 ring-1 ring-ink-100 p-6 mb-10 text-sm">
          <p class="text-xs font-semibold uppercase tracking-wider text-brand-600 mb-3">Inhalt</p>
          <ol class="grid sm:grid-cols-2 gap-y-1.5 gap-x-6 list-decimal list-inside text-ink-900">
{toc_html}
          </ol>
        </nav>

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
