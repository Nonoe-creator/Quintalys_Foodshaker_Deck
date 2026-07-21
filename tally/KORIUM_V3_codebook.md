# KORIUM — Questionnaire quantitatif V3 pilote — Codebook & logique
Form ID : 81gebo · URL : https://tally.so/r/81gebo · 26 pages · 392 blocs · 26 règles
V1 (ODyLqp) et V2 (2EyQrb) conservées intactes. Construit le 17-07-2026.

## Liens
- Public (=v1 par défaut) : https://tally.so/r/81gebo
- v1 : https://tally.so/r/81gebo?concept_order=v1&version_questionnaire=v3_pilote
- v2 : https://tally.so/r/81gebo?concept_order=v2&version_questionnaire=v3_pilote

## Champs cachés : source, canal, version_questionnaire, concept_order
## Champs calculés : concept_order_final (défaut v1), cooking_path (défaut regular_cooking)

## Variables par page
P1 consent_ok | P2 household, age_band | P3 cook_relation(1-5), cook_freq | P4 bases_cooked, dominant_base(cond)
P5 cooking_addins_during | P6 addins_after_cooking | P7 sat_current(1-5), friction_current, routine_change_openness(1-5)
P8 better_eating_intent(1-5), practical_food_knowhow(1-5), effort_accepted, time_pressure_solution
P9 concept (cartes A/B) | P10 concept_understanding_open(ouvert obl) | P11 category_association(ouvert obl) | P12 category_perception
P13 option_a_* (matrice 5x5) | P14 option_b_* (matrice 5x5)
P15 concept_pref_displayed, first_purchase_displayed(cond), pref_reason(facult)
P16 primary_value_entry(6 opt), substitutability
P17 nutrition_axis fibres/magnesium/fer (matrice, lignes randomisées), nutrition_axis_top1
P18 added_minerals_reaction, added_minerals_concern(cond), post_nutrition_categorization
P19 seaweed_consumption, seaweed_korium_interest, seaweed_range_interest, seaweed_primary_benefit(cond), seaweed_main_barrier(cond)
P20 purchase_driver_ranking(6), trust_drivers(max 2), supplement_experience
P21 objections(max 3), pedagogy_tolerance, price_format_choice(cond)
P22 price_bracket_pot, price_2490_pot, purchase_intent_pot  (format Fusion)
P23 price_bracket_boite, price_2490_boite, purchase_intent_boite  (format Essence)
P24 projected_frequency, recontact_ok | P25 email(cond) | P26 Merci

## 26 règles conditionnelles
1 cook_freq=Jamais -> cooking_path=low_or_no_cooking
2 concept_order=v2 (+consent) -> concept_order_final=v2
3 cook_freq=Jamais -> JUMP P7 (saute bases + ajouts)
4 cook_freq=Jamais -> HIDE sat_current
5 cook_freq=Jamais -> HIDE routine_change_openness
6 bases_cooked sans base nommée -> HIDE dominant_base
7-10 cartes concept SHOW selon v1/v2 (A_essence,B_fusion si v1 ; A_fusion,B_essence si v2) - cachées par défaut
11 minerals reaction=hésiter/diminuerait -> SHOW added_minerals_concern
12 seaweed interest positif/neutre/nsp -> SHOW seaweed_primary_benefit
13 seaweed interest hésiter/ne voudrais -> SHOW seaweed_main_barrier
14 pref=Les deux -> SHOW first_purchase_displayed
15-17 pref=Les deux + first∈{goût,prix,nsp} -> SHOW price_format_choice
18-22 route Essence -> JUMP P21->P23 : (v1&pref A)|(v2&pref B)|(v1&first A)|(v2&first B)|(price_format=sachet)
23 pref=Aucune -> JUMP P21->P24 (pas de prix)
24 price_format=ne souhaite pas -> JUMP P21->P24
25 pot bracket répondu -> JUMP P22->P24 (saute page boîte)
26 recontact=Non -> JUMP P24->P26 (saute email)
Flux Fusion : naturel P21->P22 (aucun saut).

## Recodage Sheets (rappel)
concept_pref_real : =SI(C2="Les deux";"Les deux";SI(C2="Aucune";"Aucune";SI(ET(OU(B2="v1";B2="");C2="Option A");"Essence";SI(ET(OU(B2="v1";B2="");C2="Option B");"Fusion";SI(ET(B2="v2";C2="Option A");"Fusion";SI(ET(B2="v2";C2="Option B");"Essence";"À vérifier"))))))
price_concept_real : colonnes *_pot remplies => Fusion ; *_boite remplies => Essence.
concept_order vide = TOUJOURS v1.
