# KORIUM — V2 pilote (Tally 2EyQrb) — Codebook, logique et recodage
Date : 17-07-2026 · Original préservé : ODyLqp · Pilote : 2EyQrb

## Liens de diffusion (pilote uniquement — pas de diffusion large)
- v1 : https://tally.so/r/2EyQrb?concept_order=v1&version_questionnaire=v2_pilote
- v2 : https://tally.so/r/2EyQrb?concept_order=v2&version_questionnaire=v2_pilote
- Le lien nu https://tally.so/r/2EyQrb affiche v1 (défaut) — ne pas l'utiliser pour la collecte ; en données, concept_order vide = v1.

## Ordre final des écrans (28 pages)
P1 Consentement (consent_ok) + champs cachés + calculés
P2 Profil : household, age_band, cook_relation (1-5)
P3 Habitudes : fastfood_freq, cook_freq → si Jamais : cooking_path=low_or_no_cooking + saut vers P12
P4 Influences culinaires (max 3)
P5 bases_cooked → sauts vers P7/P8/P9 selon bases cochées
P6 Riz : rice_method + rice_addins_cooking (si Riz coché)
P7 legume_addins_cooking (si Légumineuses)
P8 starch_seed_addins_cooking (si céréales)
P9 addins_after_cooking + after_cooking_purpose (cond.) → saut P11 si aucune épice/herbe
P10 spices_herbs_used + spice_discovery (conditionnel)
P11 sat_current (1-5) + flavor_variation + flavor_repetition_reason (cond., facultatif)
P12 friction_current (option symptômes remplacée) + routine_change_openness (1-5, masquée si non-cuisinier)
P13 Mini-bloc segmentation : better_eating_intent, practical_food_knowhow, supplement_experience, effort_accepted
P14 Concept : intro commune + cartes A/B strictement parallèles (pilotées par concept_order_final)
P15 concept_understanding_open · P16 category_association · P17 category_perception (sans « Produit culinaire innovant », avec « Préparations culinaires »)
P18 Éval Option A (matrice 5 items ×1-5) · P19 Éval Option B (idem)
P20 concept_pref_displayed + first_purchase_displayed (cond. « Les deux ») + pref_reason (facultatif)
P21 primary_value_entry + trust_drivers (max 2)
P22 objections (max 3, nouvelle liste) → routage prix
P23 Prix POT (Fusion réel) : vw_*_pot ×4 + price_2490_pot → saut P26
P24 Prix BOÎTE (Essence réel) : vw_*_boite ×4 + price_2490_boite
P25 recontact_ok → si Non : saut P27
P26 email (texte RGPD corrigé) · P27 Merci

(Numéros de pages Tally : P1..P28 ci-dessus = pages 1..28 ; les « P » du tableau des sauts ci-dessous utilisent la numérotation Tally réelle : frictions=page 12, épices=page 10, satisfaction=page 11, prix pot=page 24, prix boîte=page 25, recontact=page 26, email=page 27, merci=page 28.)

## Logique conditionnelle finale (29 règles)
1. cook_freq=Jamais → CALCULATE cooking_path="low_or_no_cooking" (p.3)
2. cook_freq=Jamais → JUMP page 12 (frictions) — plus AUCUNE disqualification
3. concept_order(URL)="v2" → CALCULATE concept_order_final="v2" (défaut "v1")
4-7. Cartes concept : v1 → affiche A=Essence, B=Fusion ; v2 → affiche A=Fusion, B=Essence (cartes masquées par défaut, 4 règles SHOW)
8-9. after_cooking ≠ uniquement « Rien » → SHOW/HIDE after_cooking_purpose
10-11. flavor_variation=« mêmes ingrédients » → SHOW/HIDE flavor_repetition_reason
12. cook_freq=Jamais → HIDE routine_change_openness
13-14. concept_pref=« Les deux » → SHOW/HIDE first_purchase_displayed
15-17. Sauts bases (p.5) : pas Riz→p.7 ; pas Riz/Lég→p.8 ; aucune des 3→p.9
18-19. Sauts depuis p.6 : pas Lég mais céréales→p.8 ; ni Lég ni céréales→p.9
20. Saut depuis p.7 : pas céréales→p.9
21. Aucune épice/herbe dans les 4 questions d'ajouts → JUMP p.11
22. pref=Aucune → JUMP p.26 (pas de bloc prix)
23. pref=Les deux + first_purchase ∉ {A,B} → JUMP p.26
24-27. Routage Essence : (v1∧pref=A) ∨ (v2∧pref=B) ∨ (v1∧first=A) ∨ (v2∧first=B) → JUMP p.25 (boîte) ; sinon flux naturel → p.24 (pot)
28. Fin du bloc pot → JUMP p.26
29. recontact=Non → JUMP p.28 (merci)

## Formules CLEAN_DATA (Google Sheets FR) — adapter les références de colonnes après le 1er export
Convention : B=concept_order (caché), C=concept_pref_displayed, D=first_purchase_displayed, cook=cook_freq.
Champ vide de concept_order = TOUJOURS traité comme v1.

concept_pref_real :
=SI(C2="Les deux";"Les deux";SI(C2="Aucune";"Aucune";SI(ET(OU(B2="v1";B2="");C2="Option A");"Essence";SI(ET(OU(B2="v1";B2="");C2="Option B");"Fusion";SI(ET(B2="v2";C2="Option A");"Fusion";SI(ET(B2="v2";C2="Option B");"Essence";"À vérifier"))))))

first_purchase_real :
=SI(D2="";"";SI(D2="Option A";SI(B2="v2";"Fusion";"Essence");SI(D2="Option B";SI(B2="v2";"Essence";"Fusion");D2)))

cooking_path (si le champ calculé n'est pas exporté) :
=SI(cook2="Jamais";"low_or_no_cooking";"regular_cooking")

Évaluations par concept (E=item Option A, F=item Option B — répéter pour les 5 items) :
essence_item : =SI(OU(B2="v1";B2="");E2;F2)
fusion_item  : =SI(OU(B2="v1";B2="");F2;E2)

price_concept_real (déduit des colonnes remplies ou de la préférence) :
=SI(OU(C2="Option A";C2="Option B");concept_pref_real2;SI(C2="Les deux";first_purchase_real2;""))
Contrôle croisé : les colonnes vw_*_pot remplies ⇒ Fusion ; vw_*_boite remplies ⇒ Essence.

## Onglets Sheets à créer/maintenir : RAW_RESPONSES · CLEAN_DATA · CODEBOOK
Ne jamais modifier les données brutes déjà collectées. Filtre d'analyse : conserver TOUTES les lignes (les non-cuisiniers ne sont plus exclus) ; colonne cooking_path pour segmenter.
