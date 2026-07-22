# V3 `81gebo` — Grille d'arbitrage des questions

But : préparer la **version quantitative finale** *après* la séquence méthodologique
(10–15 entretiens quali → pilote V3 15–30 → mesure temps/abandons/incompréhensions/pouvoir
discriminant → quanti final). **Aucune modification du Tally à ce stade.**

Codes recommandation : **I** = indispensable · **U** = utile · **S** = supprimable / déplaçable vers le quali.
Temps = temps répondant estimé par question.

---

## 1. Grille d'arbitrage (par bloc)

### Profil
| Variable | Objectif décisionnel | Type de donnée | Utilité analyse | Redondance | Déplaçable quali | Temps | Reco |
|---|---|---|---|---|---|---|---|
| `age_range` | Réceptivité aux ingrédients nouveaux + sensibilité prix + quota de représentativité | Ordinal (bandes) | Croisement transversal clé | Non | Non | 10 s | **I** |
| `household` | Pertinence format/portion (pot multi-usages vs solo), contexte repas | Nominal | Segmentation légère + quota | Faible | Non | 15 s | **U** |
| *(à ajouter)* `dietary_constraints` | Viabilité de formulation, taille du marché adressable, claims autorisés | Multi nominal | **Décision R&D + ciblage** | Non | Non | 15 s | **I** |

### Habitudes de cuisine
| Variable | Objectif décisionnel | Type | Utilité | Redondance | Quali | Temps | Reco |
|---|---|---|---|---|---|---|---|
| `cook_relation` (plaisir/corvée) | Axe « implication culinaire » (segment) | Échelle 1–5 | Segmentation forte | Partielle (cook_freq) | Non | 10 s | **I** |
| `cook_freq` | Filtre cuisinier / non-cuisinier + segment | Ordinal | Branche + segment | Partielle (cook_relation) | Non | 10 s | **I** |
| `bases_cooked` | Quelles bases enrichir en priorité | Multi nominal | Ciblage produit | Non | Non | 20 s | **I** |
| `addins_during` (pendant cuisson) | Comprendre la routine de cuisson | Multi | Contexte | **Forte** (addins_after) | Oui | 25 s | **S** |
| `addins_after` (après cuisson) | Usage actuel d'enrichissement → base de substituabilité | Multi | Moyenne-forte | Partielle (addins_during) | Partiel | 25 s | **U** |
| `after_add_motivation` (goût/nutrition) | Driver dominant → **promesse** | Nominal unique | Forte (positionnement) | Non | Non | 10 s | **I** |
| `friction_current` | Point de douleur → angle d'attaque / messaging | Multi | Forte | Faible | Partiel | 20 s | **U** |
| `better_eating` (échelle santé) | Motivation « manger mieux » (segment sensibilité) | Échelle | Moyenne-forte | Partielle (primary_value) | Non | 10 s | **U** |
| `practical_know` (savoir quoi ajouter) | Déficit de savoir-faire adressé par le produit | Échelle | Moyenne (nice-to-know) | Faible | Oui | 10 s | **S** |
| `cooking_change_profile` | **Ouverture au changement — axe de segmentation majeur** | Nominal ordonné | Très forte (segment cible) | Partielle (cook_relation) | Non | 15 s | **I** |
| `time_pressure` (jours sans temps) | Contexte d'usage / solution actuelle | Nominal | Moyenne | **Forte** (usage_context) | Non | 15 s | **S** |

### Concept & évaluation
| Variable | Objectif décisionnel | Type | Utilité | Redondance | Quali | Temps | Reco |
|---|---|---|---|---|---|---|---|
| `concept_first_impressions` (11 items, max 3) | Accueil spontané / registres (nouveauté, crédibilité, rejet) | Multi (top-of-mind) | Moyenne (bruité) | Partielle (matrices) | **Oui** | 30 s | **U** *(réduire 11→6 items)* |
| `spontaneous_product_name` (ouvert) | Catégorisation mentale + piste de naming | Texte ouvert | Forte mais codage | Non | **Oui** | 30 s | **U** *(le seul ouvert à conserver)* |
| `expected_product_category` (rayon) | **Positionnement merchandising / distribution** | Nominal | Forte | Faible | Non | 15 s | **I** |
| `eval_A` (matrice 5 lignes) | Diagnostic concept A (compréhension, intégration, simplicité, appétence, essai) | 5 échelles | Très forte | Ligne « essai » ≈ preference | Non | 40 s | **I** *(réduire 5→3-4 lignes)* |
| `eval_B` (matrice 5 lignes) | Diagnostic concept B | 5 échelles | Très forte | idem | Non | 40 s | **I** *(idem)* |
| `preference` (A/B/2/aucune) | **Arbitrage principal entre concepts** | Nominal forcé | Décisive | first_purchase | Non | 10 s | **I** |
| `first_purchase` (essayer/acheter en 1er) | Préférence à connotation comportementale | Nominal | Moyenne | **Forte** (preference) | Non | 10 s | **S** |
| `preference_reason` (ouvert, facultatif) | Pourquoi de la préférence | Texte ouvert | Codage | Non | **Oui** | 20 s | **S** |

### Valeur & substituabilité
| Variable | Objectif décisionnel | Type | Utilité | Redondance | Quali | Temps | Reco |
|---|---|---|---|---|---|---|---|
| `primary_value` | **Promesse principale à mettre en avant** | Nominal unique | Forte | Partielle (criteria_ranking) | Non | 15 s | **I** |
| `integration_mode` (remplace/complète/nouveau) | Positionnement d'usage (substitution vs complément) | Nominal | Forte — *données quanti nettes* | Partielle (addins_after) | Non | 15 s | **U** |

### Nutrition
| Variable | Objectif décisionnel | Type | Utilité | Redondance | Quali | Temps | Reco |
|---|---|---|---|---|---|---|---|
| `nutrition_natural_interest` (échelle) | Réceptivité à l'argument « naturellement riche » | Échelle | Moyenne-forte | Partielle (primary_value) | Non | 10 s | **U** |
| `nutrition_matrix` (fibres/mag/fer) | Intensité d'intérêt par apport | 3 échelles | Forte | **Forte** (nutrition_priority) | Non | 25 s | **S** *(garder priority OU matrice, pas les deux)* |
| `nutrition_priority` (top 1) | **Apport à valoriser en claim** | Nominal | Forte (net) | **Forte** (matrix) | Non | 10 s | **I** |
| `minerals_reaction` (atout/méfiance) | Risque de rejet de l'« enrichi » | Nominal | Moyenne-forte | Faible | Non | 10 s | **U** |
| `minerals_concern` (ouvert, conditionnel) | Nature de la méfiance | Texte ouvert | Codage, faible volume | Non | **Oui** | 15 s | **S** |

### Familles d'ingrédients
| Variable | Objectif décisionnel | Type | Utilité | Redondance | Quali | Temps | Reco |
|---|---|---|---|---|---|---|---|
| `ingredient_families` (multi + « Aucune ») | Intérêt R&D par famille | Multi | Forte | Non | Non | 20 s | **I** |
| `deepdive_*` × 8 (bénéfice/frein × 4 familles) | Raisons d'attrait/frein par famille | Multi | Riche mais très lourd | **Élevée entre elles** | **Oui** | ~60 s cumulés | **S** *(→ voir bloc allégé §3)* |

### Critères, confiance, freins, comparables
| Variable | Objectif décisionnel | Type | Utilité | Redondance | Quali | Temps | Reco |
|---|---|---|---|---|---|---|---|
| `criteria_ranking` (6 items) | **Hiérarchie des drivers d'essai** | Classement | Forte | Partielle (primary_value) | Non | 30 s | **I** |
| `trust_levers` (max 3) | Éléments de réassurance → packaging / comm | Multi limité | Forte | Faible | Non | 20 s | **I** |
| `barriers` (max 3) | Freins à lever → comm / produit | Multi limité | Forte | Partielle (minerals_reaction, friction) | Non | 20 s | **I** |
| `comparable_experience` | Maturité marché / expérience préalable | Nominal | Moyenne (contexte) | Faible | Non | 10 s | **U** |

### Prix & clôture
| Variable | Objectif décisionnel | Type | Utilité | Redondance | Quali | Temps | Reco |
|---|---|---|---|---|---|---|---|
| `price_format_choice` | **Format préféré** + route le VW | Nominal | Forte | Non | Non | 10 s | **I** |
| `vw_pot` × 4 | Sensibilité prix format pot | 4 numériques € | Forte *(si volume)* | Deux VW = split échantillon | Non | 40 s | **U** |
| `vw_box` × 4 | Sensibilité prix format boîte | 4 numériques € | Forte *(si volume)* | idem | Non | 40 s | **U** |
| `purchase_intent_2490` | **Intention au prix cible → go/no-go prix** | Échelle intention | Forte | Partielle (VW) | Non | 10 s | **I** |
| `usage_context` | Occasions d'usage → positionnement | Multi | Forte | Partielle (time_pressure) | Non | 15 s | **I** |
| `recontact_consent` | Recrutement panel qual | Nominal | Opérationnelle | Non | Non | 5 s | **U** |
| `email` (conditionnel) | Contact | Email | Opérationnelle | Non | Non | 15 s | **U** |

**Synthèse : ~20 I · ~13 U · ~8 S.** Le retrait des **S** (`addins_during`, `practical_know`,
`time_pressure`, `first_purchase`, `preference_reason`, `nutrition_matrix`, `minerals_concern`,
deep-dives ×8) économise ≈ **4 à 5 minutes** sans toucher au pouvoir décisionnel.

---

## 2. Variables de profil — justifiées par la décision

> Principe : une variable de profil ne se garde que si une **décision** ou une **segmentation utile** en dépend.

| Variable | Décision / segmentation qui la justifie | Verdict |
|---|---|---|
| **Contraintes alimentaires** *(à ajouter)* | Détermine quels ingrédients sont **formulables** (algues, superaliments…), la **taille du marché adressable** et les **claims** possibles. Pour un produit d'ingrédients, c'est structurant. | **Prioritaire — ajouter** |
| **Habitudes de cuisine** (`cook_freq`, `cook_relation`, `bases_cooked`) | Constituent l'axe « implication culinaire » — segment cible n°1. Déjà présentes. | **Prioritaire — garder** |
| **Profils d'usage** (`usage_context`, `cooking_change_profile`) | Positionnement (semaine express vs plaisir) + ouverture au changement = segment cible n°2. | **Prioritaire — garder** |
| **Âge** | Réceptivité générationnelle aux ingrédients nouveaux + sensibilité au prix (24,90 € = premium) + quota minimal de représentativité. | **Garder (léger)** |
| **Foyer** | Pertinence du format/portion et du contexte repas. | **Garder si peu coûteux** |
| **Genre** | Décision réelle qui en dépend ? Faible. Utile surtout comme quota de représentativité et corrélat de « qui cuisine ». | **Optionnel — seulement en quota léger** |
| **CSP / revenu** | Le VW mesure déjà directement la disposition à payer ; le revenu est intrusif et fait chuter la complétion. À n'ajouter (bande grossière) que si un **prix différencié par segment** est une décision réelle. | **Optionnel — proxy grossier au besoin** |
| **Région** | Utile seulement si la **distribution** ou une différence de culture culinaire pilote une décision. Sur un pilote national : faible valeur. | **Écarter (sauf enjeu distribution)** |

**À ajouter en priorité : `dietary_constraints`** (multi) — végétarien / végétalien · sans gluten ·
sans lactose · allergies (préciser) · sans porc / halal / casher · aucune contrainte.

---

## 3. Bloc familles d'ingrédients — version allégée

**Actuel :** 1 sélection multi + **4 pages** d'approfondissement conditionnel (bénéfice *ou* frein
par famille) → lourd, redondant, très « quali ».

**Allégé (3 questions, 1 seule page conditionnelle) :**

1. **Sélection** — `ingredient_families` (multi, « Aucune » exclusive). *Inchangé.*
2. **Priorisation** — `family_top` (choix unique) : « Parmi celles que vous avez sélectionnées,
   laquelle vous attire le plus ? »
   → *Faisable proprement en n'affichant en Q2 que les familles cochées en Q1* (règle SHOW par
   option ; ~10 règles). À défaut, liste complète.
3. **Approfondissement unique conditionnel** — `family_deepdive`, une seule question générique
   dont le titre reprend la famille choisie via un *mention* Tally :
   « Concernant **{{family_top}}**, qu'est-ce qui vous attire le plus, et qu'est-ce qui vous
   retiendrait ? » (options génériques : curiosité / bienfaits / goût / naturel — vs — goût /
   trop inhabituel / doute nutritionnel / mal connu).

**Gain :** 8 questions → 3 · 4 pages → 2 · ~60 s → ~25 s · logique divisée par ~5.
La profondeur famille-par-famille (les 8 deep-dives) **migre vers le guide terrain quali**,
là où elle est la plus riche.

---

## 4. Volume minimal nécessaire

> Hypothèses : α = 5 % bilatéral, puissance 80 %, effets modérés. Le **pilote (15–30)** ne sert
> qu'à mesurer temps / abandons / incompréhensions / pouvoir discriminant — **il ne tranche rien**.

| Objectif d'analyse | Plancher (tendance) | Confortable (décision) | Note |
|---|---|---|---|
| **Comparer les 2 concepts** (préférence forcée + matrices A/B, en *within-subject*) | ~150 complétions | **250–300** | 150 ne détecte qu'un écart net (≥ 60/40) ; 300 capte un écart fin (≈ 55/45). Recodage A/B obligatoire. |
| **Un seul Van Westendorp** | ~100 | **150–200** | En dessous de ~75, les points d'intersection sont instables. |
| **Deux VW séparés pot/boîte** | ~250 au total | **350–450** | Chaque courbe exige ≥ 100–150 ; le choix de format n'est pas 50/50. Ex. split 60/40 → 100 ÷ 0,40 ≈ **250** ; split 70/30 → 100 ÷ 0,30 ≈ **335** rien que pour le plancher. C'est le coût chiffré du double VW. |
| **Croisements de segmentation (1 dimension)** — ex. préférence × profil d'ouverture | ~80/segment → **~300** | ~100/segment → **400–500** | Minimum absolu pour *rapporter* un %: 30/cellule (IC très larges). |
| **Croisements à 2 dimensions** (segment × format × préférence) | — | **800–1 200** | Les cellules se multiplient : à réserver si un budget de volume le permet. |

**Lecture pour décider :**
- Objectif « trancher entre les deux concepts + un prix » → viser **≈ 300** complétions.
- Objectif « garder les deux VW pot/boîte analysables séparément » → viser **≈ 400**.
- Objectif « segmenter finement » (2 dimensions) → **≈ 800+**, sinon se limiter aux croisements
  à une seule dimension.
