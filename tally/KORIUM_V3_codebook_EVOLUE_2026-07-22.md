# Codebook V3 `81gebo` — version évoluée (reconstruction du 2026-07-22)

Formulaire : **« Vos habitudes en cuisine du quotidien »** — https://tally.so/r/81gebo
Statut : **PUBLISHED** · 39 pages · 430 blocs · workspace `wgJgyK`

> Reconstruction complète du parcours (pages 2 à 26 supprimées puis reconstruites en
> pages 2 à 39), page 1 conservée à l'identique. Sauvegarde de l'état antérieur :
> `tally/SAUVEGARDE_V3_81gebo_avant_evolutions.md` + copie de forme Tally `Np9YLG` (DRAFT).
> V1 `ODyLqp` et V2 `2EyQrb` non modifiées.

## Page 1 — conservée (variables techniques)

| Élément | UUID | Détail |
| - | - | - |
| Titre du formulaire | `49dcf54b` | « Vos habitudes en cuisine du quotidien » (KORIUM retiré) |
| Calc `concept_order_final` | `0f6debe2` | TEXT, défaut `v1` |
| Calc `cooking_path` | `f8498a80` | TEXT, défaut `regular_cooking` |
| Hidden `source` / `canal` / `version_questionnaire` / `concept_order` | `2d63fb1a` / `064f9493` / `30d8cd81` / `285cfee7` | inchangés |
| Consentement Q / « Je participe » | `9f6e6906` / `8f2cdf95` | inchangé |
| Règle KEEP `8dfbf196` | — | `concept_order IS v2 → CALCULATE concept_order_final = v2` |

## Ordre des pages (parcours validé)

1 Consentement · 2 Profil (foyer, âge) · 3 Rapport à la cuisine (échelle + fréquence) ·
4 Bases cuisinées · 5 Ajouts pendant la cuisson · 6 Ajouts après la cuisson ·
7 Motivation des ajouts · 8 Frictions actuelles · 9 Ouverture au changement
(2 échelles + profil de changement + solution manque de temps) · 10 Présentation du concept
(intro + 4 cartes conditionnelles) · 11 Premières impressions · 12 Nom spontané ·
13 Rayon attendu · 14 Évaluation Option A · 15 Évaluation Option B · 16 Préférence
(préférence + 1er essai + raison) · 17 Valeur perçue · 18 Intégration/substituabilité ·
19 Intérêt nutritionnel naturel · 20 Apports (fibres/magnésium/fer) · 21 Priorité nutritionnelle ·
22 Réaction aux apports (+ méfiance conditionnelle) · 23 Familles d'ingrédients ·
24 Approfondissement algues · 25 champignons · 26 légumes séchés · 27 fleurs comestibles ·
28 Classement des critères · 29 Leviers de confiance · 30 Freins ·
31 Expérience produits comparables · 32 Prix : choix du format · 33 Prix : format pot (VW) ·
34 Prix : format boîte (VW) · 35 Intention d'achat (24,90 €) · 36 Usage projeté ·
37 Recontact · 38 Email · 39 Merci.

## Variables (questionUuid) créées

| Var | Q UUID | Type | Page |
| - | - | - | - |
| household | `a77982d3` | choix unique | 2 |
| age_range | `fb548f5d` | choix unique | 2 |
| cook_relation | `8387f025` | échelle 1–5 (Une corvée→Un plaisir) | 3 |
| cook_freq | `69789b56` | choix unique (Jamais=`6e20bae9`) | 3 |
| bases_cooked | `d157c1ad` | cases (Riz blanc=`38124853`) | 4 |
| addins_during | `96b3a44f` | cases | 5 |
| addins_after | `6096db0f` | cases | 6 |
| after_add_motivation | `db7fa0a6` | choix unique | 7 |
| friction_current | `b805de0a` | cases | 8 |
| better_eating | `23c3c1a8` | échelle 1–5 (Pas du tout→Énormément) | 9 |
| practical_know | `a34f6e9d` | échelle 1–5 (Jamais→Toujours) | 9 |
| cooking_change_profile | `6b206780` | choix unique | 9 |
| time_pressure | `58614bac` | choix unique | 9 |
| concept_first_impressions | `3e09d355` | cases · max 3 | 11 |
| spontaneous_product_name | `21f9dab5` | texte court | 12 |
| expected_product_category | `9da35fee` | choix unique | 13 |
| eval_A (matrice) | `78db7b1c` | matrice 5×5 · ligne essai=`e9d98887` | 14 |
| eval_B (matrice) | `fff033b1` | matrice 5×5 · ligne essai=`2b12f835` | 15 |
| preference | `076b377a` | choix unique (A/B/Les deux/Aucune) | 16 |
| first_purchase | `80aecd89` | choix unique | 16 |
| preference_reason | `08c89133` | texte long · **facultatif** | 16 |
| primary_value | `230304ab` | choix unique (8 options) | 17 |
| integration_mode | `eaf7b32b` | choix unique (remplace/complète/nouveau/rien/nsp) | 18 |
| nutrition_natural_interest | `8538a5d2` | échelle 1–5 (Pas du tout→Beaucoup) | 19 |
| nutrition_matrix | `6f062515` | matrice 5×3 (fibres/magnésium/fer) · **lignes aléatoires** | 20 |
| nutrition_priority | `fe85a237` | choix unique | 21 |
| minerals_reaction | `9aa7ca82` | choix unique (méfiant=`70de1def`) | 22 |
| minerals_concern | `d5ff8c6c` | texte long · **facultatif** · conditionnel | 22 |
| ingredient_families | `88a7beb8` | cases · Aucune(excl)=`d8edfeda` | 23 |
| deepdive_algues_benefit / _barrier | `6f215446` / `5a309977` | cases · conditionnel | 24 |
| deepdive_champignons_benefit / _barrier | `5ab2ad6c` / `a510fd5a` | cases · conditionnel | 25 |
| deepdive_legumes_benefit / _barrier | `1409cb76` / `7cb257b8` | cases · conditionnel | 26 |
| deepdive_fleurs_benefit / _barrier | `3d5a133b` / `292a83bb` | cases · conditionnel | 27 |
| criteria_ranking | `a34343cf` | classement (6 items) | 28 |
| trust_levers | `cd45547d` | cases · max 3 | 29 |
| barriers | `4e10918f` | cases · max 3 · « pas de frein »(excl)=`4887047b` | 30 |
| comparable_experience | `983b998f` | choix unique | 31 |
| price_format_choice | `f6316932` | choix unique (pot=`126690a1` / boîte=`faea4553`) | 32 |
| vw_pot_too_cheap / _cheap / _expensive / _too_expensive | `e5145d7b` / `c8f565b7` / `4d570c79` / `fc94c669` | nombre € · conditionnel pot | 33 |
| vw_box_too_cheap / _cheap / _expensive / _too_expensive | `a5997cdf` / `e870431a` / `6c1fcf64` / `9ea7bb0c` | nombre € · conditionnel boîte | 34 |
| purchase_intent_2490 | `ba339255` | choix unique | 35 |
| usage_context | `a50986dd` | cases | 36 |
| recontact_consent | `2cb3bf73` | choix unique (Oui=`fe8ec80d` / Non=`b0311227`) | 37 |
| email | `7739cfed` | email · **facultatif** · conditionnel | 38 |

## Logique conditionnelle (48 règles)

- **Randomisation concept** (page 1, conservée) : `8dfbf196` calcule `concept_order_final=v2`.
- **Cartes concept** (4 règles re-câblées) : v1 → montre A=Infuser (`a4702ac3`) + B=Ajouter (`63084d55`) ;
  v2 → montre A=Ajouter (`cd334786`) + B=Infuser (`68e6791a`). Cartes masquées par défaut.
- **Branche non-cuisinier** : `cook_freq IS Jamais` → `CALCULATE cooking_path = "non_cooking"` **et** `JUMP TO PAGE 10`
  (saute bases/ajouts/motivation/frictions/ouverture).
- **Méfiance minéraux** : `minerals_reaction IS méfiant` → montre `minerals_concern`.
- **Approfondissements familles** (8 règles) : famille sélectionnée → question *bénéfice* ;
  famille non sélectionnée → question *frein* (jamais les deux).
- **Routage prix pot/boîte** (10 règles) : format pot → montre rappel + 4 seuils pot ;
  format boîte → montre rappel + 4 seuils boîte ; la page non retenue reste entièrement masquée (sautée).
- **Email** : `recontact_consent IS Oui` → montre le champ email.
- **Exclusivités** :
  - Familles : « Aucune de ces propositions » masque les 10 autres ; toute autre sélection masque « Aucune » (11 règles).
  - Freins : « Je n'ai pas de frein particulier » masque les 9 autres ; toute autre sélection le masque (10 règles).

## Limites techniques

1. **Van Westendorp** — Tally ne supporte pas les contrôles de cohérence inter-champs
   (qualité douteuse ≤ bon marché ≤ cher ≤ trop cher). Seul `min = 0` est posé ; l'ordre des
   seuils devra être vérifié en post-traitement.
2. **Exclusivités** — pas de fonction native « option exclusive » dans Tally ; reproduites par
   des règles HIDE (voir ci-dessus). Garde-fou efficace, mais une case déjà cochée puis rendue
   exclusive n'est pas automatiquement décochée.
3. **Pages conditionnelles pot/boîte** — reposent sur le saut automatique des pages
   entièrement masquées par Tally.
4. **Classement (ranking)** — l'ordre d'affichage aléatoire n'est pas pilotable via l'API MCP.

## Analyse

- Analyser **pot** et **boîte** séparément (ne pas fusionner les courbes Van Westendorp).
- L'intention d'achat à 24,90 € est commune et n'apparaît qu'**après** les 4 seuils (anti-ancrage).
