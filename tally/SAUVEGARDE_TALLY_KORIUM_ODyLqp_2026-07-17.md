# TALLY KORIUM — Sauvegarde avant segmentation V2 — 17-07-2026

- Formulaire original : **Vos habitudes en cuisine du quotidien**
- Form ID : `ODyLqp` — URL : https://tally.so/r/ODyLqp
- Statut : PUBLIÉ, 322 blocs, 36 pages, 14 règles logiques, 4 champs cachés (source, canal, version_questionnaire, concept_order), 1 champ calculé (concept_order_final=v1).
- Ce fichier est l'export intégral de l'état au 17/07/2026 avant création de la V2 pilote. L'original n'est PAS modifié.

# Form ledger

## Blocks

| # | text/html | blockUuid | type | questionUuid | page | insertAfterBlockUuid_BEFORE | properties |
| - | - | - | - | - | - | - | - |
| 1 | Vos habitudes en cuisine du quotidien | e480e8a2-9e3d-4f68-bb26-48ad0edcea79 | FORM_TITLE | - | 1 | - | button={"label":"Continuer"} |
| 2 | - | e316701b-91ce-46e7-bbe9-60e94cbfab14 | CALCULATED_FIELDS | 34e3e3c1-4712-4213-baba-378b1d478e9b | 1 | e480e8a2-9e3d-4f68-bb26-48ad0edcea79 | 61ae70d8-bcf2-465c-b6f1-2bca6c2a6992=concept_order_final(TEXT,value="v1") |
| 3 | - | 731ffc40-0401-4576-a6a1-7d19f8fe94c8 | HIDDEN_FIELDS | cab71906-e580-470b-98a8-aa796ce16102 | 1 | e316701b-91ce-46e7-bbe9-60e94cbfab14 | 831b88a7-52ae-4004-a637-6227142a9524=source, df8e6ac8-b22e-4223-92d4-d63a29271018=canal, 2119d981-eecc-4516-a021-cf0ab78dd12e=version_questionnaire, 8982344d-db02-40d0-98f3-aee4bf6e1676=concept_order |
| 4 | Cette enquête s’adresse à des personnes majeures et vise à mieux comprendre des habitudes de cuisine, les usages autour des bases alimentaires et les réactions à de nouvelles idées de produits culinaires. Les réponses sont analysées de façon anonyme. La participation est facultative et vous pouvez quitter le questionnaire à tout moment. | 1ec52077-8d9f-4b88-85a6-1c0e1a78726d | TEXT | - | 1 | 731ffc40-0401-4576-a6a1-7d19f8fe94c8 | - |
| 5 | J’ai pris connaissance de ces informations. | aa445078-a99e-4899-9ac9-317e218116d9 | TITLE | 88ffdb41-c3c0-4c85-9b52-848a7956c043 | 1 | 1ec52077-8d9f-4b88-85a6-1c0e1a78726d | - |
| 6 | Je participe | f5db52af-2052-4a9c-8234-d4c11ded23c8 | MULTIPLE_CHOICE_OPTION | 88ffdb41-c3c0-4c85-9b52-848a7956c043 | 1 | aa445078-a99e-4899-9ac9-317e218116d9 | - |
| 7 | - | 36a59911-e71f-4210-aff2-62bcd1810698 | CONDITIONAL_LOGIC | - | 1 | f5db52af-2052-4a9c-8234-d4c11ded23c8 | see `## Logic rules` below |
| 8 | - | 6fc41bfd-7bf7-4f46-af9d-7ffdffd8b3d6 | CONDITIONAL_LOGIC | - | 1 | 36a59911-e71f-4210-aff2-62bcd1810698 | see `## Logic rules` below |
| 9 | - | fece5c35-c2b3-4b0c-a3b0-549457d9dec2 | CONDITIONAL_LOGIC | - | 1 | 6fc41bfd-7bf7-4f46-af9d-7ffdffd8b3d6 | see `## Logic rules` below |
| 10 | - | d8442457-3204-4398-a3a7-e63e7b90c31a | CONDITIONAL_LOGIC | - | 1 | fece5c35-c2b3-4b0c-a3b0-549457d9dec2 | see `## Logic rules` below |
| 11 | - | 957a307e-dedd-4330-a8af-ccc8c9b89ee6 | CONDITIONAL_LOGIC | - | 1 | d8442457-3204-4398-a3a7-e63e7b90c31a | see `## Logic rules` below |
| 12 | - | fba2bb57-b5b3-4f5b-91aa-0fa48e075221 | CONDITIONAL_LOGIC | - | 1 | 957a307e-dedd-4330-a8af-ccc8c9b89ee6 | see `## Logic rules` below |
| 13 | - | 8b91f018-7dca-4dd6-aae4-5514b56ae109 | CONDITIONAL_LOGIC | - | 1 | fba2bb57-b5b3-4f5b-91aa-0fa48e075221 | see `## Logic rules` below |
| 14 | Si vous acceptez d’être recontacté(e) en fin de questionnaire, votre email sera conservé séparément de vos réponses, pendant 6 mois maximum, et utilisé uniquement à cette fin. | d432f3cc-b416-4889-9189-de2ef494feaa | TEXT | - | 1 | 8b91f018-7dca-4dd6-aae4-5514b56ae109 | - |
| 15 | Écran 1 – Profil | 516fb961-a9bd-4778-bd2d-36b2b88086db | PAGE_BREAK | - | 2 | d432f3cc-b416-4889-9189-de2ef494feaa | - |
| 16 | Quelques éléments sur vous, pour situer les réponses. | 113c269e-214d-44da-ae70-3c12d918f297 | TEXT | - | 2 | 516fb961-a9bd-4778-bd2d-36b2b88086db | - |
| 17 | Composition de votre foyer | 9338eb89-52b8-4e44-a709-0eac8ffa1dad | TITLE | de2fe870-4946-48e7-a6b2-03bd67969d51 | 2 | 113c269e-214d-44da-ae70-3c12d918f297 | - |
| 18 | Seul(e) | bd4cc3f4-f2b5-43ef-9da5-7c28059313bc | MULTIPLE_CHOICE_OPTION | de2fe870-4946-48e7-a6b2-03bd67969d51 | 2 | 9338eb89-52b8-4e44-a709-0eac8ffa1dad | hasOtherOption=true |
| 19 | Couple | 5158d0bb-2c76-4819-825e-ecb077b492ed | MULTIPLE_CHOICE_OPTION | de2fe870-4946-48e7-a6b2-03bd67969d51 | 2 | bd4cc3f4-f2b5-43ef-9da5-7c28059313bc | hasOtherOption=true |
| 20 | Famille avec enfants | 6fda3020-1d30-43ba-89c8-80beaaeaebd4 | MULTIPLE_CHOICE_OPTION | de2fe870-4946-48e7-a6b2-03bd67969d51 | 2 | 5158d0bb-2c76-4819-825e-ecb077b492ed | hasOtherOption=true |
| 21 | Colocation | 9c548f22-70f4-4b9b-b8db-91379e44ec65 | MULTIPLE_CHOICE_OPTION | de2fe870-4946-48e7-a6b2-03bd67969d51 | 2 | 6fda3020-1d30-43ba-89c8-80beaaeaebd4 | hasOtherOption=true |
| 22 | Autre | 7d99dd62-ed0a-4693-8310-7da58c3d6609 | MULTIPLE_CHOICE_OPTION | de2fe870-4946-48e7-a6b2-03bd67969d51 | 2 | 9c548f22-70f4-4b9b-b8db-91379e44ec65 | hasOtherOption=true, isOtherOption=true |
| 23 | Votre tranche d’âge | 076a43c6-1268-4e8d-91a1-296b7b80d834 | TITLE | 3310a62c-ac96-4c13-aaf6-2e140e7481eb | 2 | 7d99dd62-ed0a-4693-8310-7da58c3d6609 | - |
| 24 | 18–24 | ddd47e9b-ebc6-468a-9cfa-ebed7c32999f | MULTIPLE_CHOICE_OPTION | 3310a62c-ac96-4c13-aaf6-2e140e7481eb | 2 | 076a43c6-1268-4e8d-91a1-296b7b80d834 | - |
| 25 | 25–34 | ebc8031f-32ee-4431-92b6-94859f84e5a1 | MULTIPLE_CHOICE_OPTION | 3310a62c-ac96-4c13-aaf6-2e140e7481eb | 2 | ddd47e9b-ebc6-468a-9cfa-ebed7c32999f | - |
| 26 | 35–44 | a6353839-1b81-45cc-b1ca-09411954637c | MULTIPLE_CHOICE_OPTION | 3310a62c-ac96-4c13-aaf6-2e140e7481eb | 2 | ebc8031f-32ee-4431-92b6-94859f84e5a1 | - |
| 27 | 45–54 | f4e9e4cc-1607-4233-bd62-0a079aa41e48 | MULTIPLE_CHOICE_OPTION | 3310a62c-ac96-4c13-aaf6-2e140e7481eb | 2 | a6353839-1b81-45cc-b1ca-09411954637c | - |
| 28 | 55–64 | 25717fa7-5552-40d8-89c7-c1dd5d0ca68a | MULTIPLE_CHOICE_OPTION | 3310a62c-ac96-4c13-aaf6-2e140e7481eb | 2 | f4e9e4cc-1607-4233-bd62-0a079aa41e48 | - |
| 29 | 65+ | 111b4b07-af26-40d8-b192-ffdf5289741d | MULTIPLE_CHOICE_OPTION | 3310a62c-ac96-4c13-aaf6-2e140e7481eb | 2 | 25717fa7-5552-40d8-89c7-c1dd5d0ca68a | - |
| 30 | Pour vous, cuisiner au quotidien est plutôt… | d548e489-7e82-4dab-a223-f0db1a594b80 | TITLE | 2d74fadc-25c1-4617-8d45-7284047806a0 | 2 | 111b4b07-af26-40d8-b192-ffdf5289741d | - |
| 31 | - | cc36d31a-c894-4335-abd1-5f89a24820bd | LINEAR_SCALE | 2d74fadc-25c1-4617-8d45-7284047806a0 | 2 | d548e489-7e82-4dab-a223-f0db1a594b80 | start=1, end=5, leftLabel="Une corvée", rightLabel="Un plaisir" |
| 32 | Écran 2 – Habitudes générales | 8ed2287d-7ac5-4681-b330-794299b71e4f | PAGE_BREAK | - | 3 | cc36d31a-c894-4335-abd1-5f89a24820bd | - |
| 33 | À quelle fréquence mangez-vous dans un fast-food ou commandez-vous un repas de type fast-food ? | b9a8a359-be99-44e6-91a6-71d0642dc570 | TITLE | 69e41df5-7ada-446a-9a47-88ca9e09d9d9 | 3 | 8ed2287d-7ac5-4681-b330-794299b71e4f | - |
| 34 | Jamais ou presque jamais | 0f69fb6c-aa0d-45a2-98b3-d7744632b581 | MULTIPLE_CHOICE_OPTION | 69e41df5-7ada-446a-9a47-88ca9e09d9d9 | 3 | b9a8a359-be99-44e6-91a6-71d0642dc570 | - |
| 35 | Moins d’une fois par semaine | 8780a78e-220c-45f1-ad52-36bea393e14f | MULTIPLE_CHOICE_OPTION | 69e41df5-7ada-446a-9a47-88ca9e09d9d9 | 3 | 0f69fb6c-aa0d-45a2-98b3-d7744632b581 | - |
| 36 | 1 fois par semaine | b754d33a-4c0b-4a0f-92ef-e5a3e2038620 | MULTIPLE_CHOICE_OPTION | 69e41df5-7ada-446a-9a47-88ca9e09d9d9 | 3 | 8780a78e-220c-45f1-ad52-36bea393e14f | - |
| 37 | 2–3 fois par semaine | f39fec55-49d0-4f5c-ab85-dc5cc2545b54 | MULTIPLE_CHOICE_OPTION | 69e41df5-7ada-446a-9a47-88ca9e09d9d9 | 3 | b754d33a-4c0b-4a0f-92ef-e5a3e2038620 | - |
| 38 | 4 fois ou plus par semaine | 3e9c30ea-f6b4-4790-a752-80e03de8bbb7 | MULTIPLE_CHOICE_OPTION | 69e41df5-7ada-446a-9a47-88ca9e09d9d9 | 3 | f39fec55-49d0-4f5c-ab85-dc5cc2545b54 | - |
| 39 | À quelle fréquence cuisinez-vous vous-même un repas ? | 04b9dc3c-31cb-4e87-9b2e-a3d26d843c70 | TITLE | 402ddfe0-16b1-444c-90d5-ddf107d7b953 | 3 | 3e9c30ea-f6b4-4790-a752-80e03de8bbb7 | - |
| 40 | Jamais | 04871e70-32bc-41de-8ac2-68612a007213 | MULTIPLE_CHOICE_OPTION | 402ddfe0-16b1-444c-90d5-ddf107d7b953 | 3 | 04b9dc3c-31cb-4e87-9b2e-a3d26d843c70 | - |
| 41 | 1–2 fois par semaine | 8b01e9c5-94d0-42e1-a98a-4bf84d69ff0c | MULTIPLE_CHOICE_OPTION | 402ddfe0-16b1-444c-90d5-ddf107d7b953 | 3 | 04871e70-32bc-41de-8ac2-68612a007213 | - |
| 42 | 3–4 fois par semaine | 9ba14a7a-c221-4a1e-9e14-14a876fa9a9b | MULTIPLE_CHOICE_OPTION | 402ddfe0-16b1-444c-90d5-ddf107d7b953 | 3 | 8b01e9c5-94d0-42e1-a98a-4bf84d69ff0c | - |
| 43 | 5 fois ou plus par semaine | e88b1de9-44c2-4cb4-bf8e-68bddc2b2e4a | MULTIPLE_CHOICE_OPTION | 402ddfe0-16b1-444c-90d5-ddf107d7b953 | 3 | 9ba14a7a-c221-4a1e-9e14-14a876fa9a9b | - |
| 44 | - | ae219951-ec90-4826-ba13-fb6a78985ad4 | CONDITIONAL_LOGIC | - | 3 | e88b1de9-44c2-4cb4-bf8e-68bddc2b2e4a | see `## Logic rules` below |
| 45 | Écran 3 – Influences culinaires | 8c7f9c42-c778-4fec-98c3-3183a96c6f6e | PAGE_BREAK | - | 4 | ae219951-ec90-4826-ba13-fb6a78985ad4 | - |
| 46 | Quelles influences culinaires retrouvez-vous le plus dans votre façon de cuisiner ? | ac99fc61-fb72-46cc-aac6-3a9081c8dc45 | TITLE | bd6676a6-3cd7-4045-8a6a-3aa1361f7e6a | 4 | 8c7f9c42-c778-4fec-98c3-3183a96c6f6e | - |
| 47 | Cuisine française / européenne | 5f896c5c-1681-448b-9594-e248194142da | CHECKBOX | bd6676a6-3cd7-4045-8a6a-3aa1361f7e6a | 4 | ac99fc61-fb72-46cc-aac6-3a9081c8dc45 | hasOtherOption=true, maxChoices=3 |
| 48 | Cuisine antillaise / caribéenne | 53043dbe-e55c-4ba1-859b-825d01277339 | CHECKBOX | bd6676a6-3cd7-4045-8a6a-3aa1361f7e6a | 4 | 5f896c5c-1681-448b-9594-e248194142da | hasOtherOption=true, maxChoices=3 |
| 49 | Cuisine africaine | 00f94632-4dd4-49d2-8dae-45b169a116ad | CHECKBOX | bd6676a6-3cd7-4045-8a6a-3aa1361f7e6a | 4 | 53043dbe-e55c-4ba1-859b-825d01277339 | hasOtherOption=true, maxChoices=3 |
| 50 | Cuisine maghrébine | 647d797c-eede-4c30-a146-12658ed16ff5 | CHECKBOX | bd6676a6-3cd7-4045-8a6a-3aa1361f7e6a | 4 | 00f94632-4dd4-49d2-8dae-45b169a116ad | hasOtherOption=true, maxChoices=3 |
| 51 | Cuisine moyen-orientale | d3dd9790-7f53-419a-9f0c-c81b9687c64c | CHECKBOX | bd6676a6-3cd7-4045-8a6a-3aa1361f7e6a | 4 | 647d797c-eede-4c30-a146-12658ed16ff5 | hasOtherOption=true, maxChoices=3 |
| 52 | Cuisine asiatique | 1d9ec1b4-f0bf-4868-a9f9-b9fe92319a3d | CHECKBOX | bd6676a6-3cd7-4045-8a6a-3aa1361f7e6a | 4 | d3dd9790-7f53-419a-9f0c-c81b9687c64c | hasOtherOption=true, maxChoices=3 |
| 53 | Cuisine indienne / sud-asiatique | b19002b8-1ea7-4871-b122-5379821a3282 | CHECKBOX | bd6676a6-3cd7-4045-8a6a-3aa1361f7e6a | 4 | 1d9ec1b4-f0bf-4868-a9f9-b9fe92319a3d | hasOtherOption=true, maxChoices=3 |
| 54 | Cuisine latino-américaine | 829bdd27-b8d6-468d-9dc5-b6ea51de5771 | CHECKBOX | bd6676a6-3cd7-4045-8a6a-3aa1361f7e6a | 4 | b19002b8-1ea7-4871-b122-5379821a3282 | hasOtherOption=true, maxChoices=3 |
| 55 | Cuisine familiale traditionnelle | 1d5ef7ec-ae85-4f34-a3c7-087b1e2bd795 | CHECKBOX | bd6676a6-3cd7-4045-8a6a-3aa1361f7e6a | 4 | 829bdd27-b8d6-468d-9dc5-b6ea51de5771 | hasOtherOption=true, maxChoices=3 |
| 56 | Cuisine végétarienne / végétale | ff38e721-3e4b-4773-b163-7d59cb028a2f | CHECKBOX | bd6676a6-3cd7-4045-8a6a-3aa1361f7e6a | 4 | 1d5ef7ec-ae85-4f34-a3c7-087b1e2bd795 | hasOtherOption=true, maxChoices=3 |
| 57 | Je ne sais pas | 4d848b0a-2d96-4264-91a9-9a414a180cb6 | CHECKBOX | bd6676a6-3cd7-4045-8a6a-3aa1361f7e6a | 4 | ff38e721-3e4b-4773-b163-7d59cb028a2f | hasOtherOption=true, maxChoices=3 |
| 58 | Autre | 2a9c9bd5-93f9-425c-8e45-07cdaaf45b4f | CHECKBOX | bd6676a6-3cd7-4045-8a6a-3aa1361f7e6a | 4 | 4d848b0a-2d96-4264-91a9-9a414a180cb6 | hasOtherOption=true, isOtherOption=true, maxChoices=3 |
| 59 | Écran 4 – Méthode de cuisson du riz | 29e15d12-abf2-490d-b696-0f708a0763e5 | PAGE_BREAK | - | 5 | 2a9c9bd5-93f9-425c-8e45-07cdaaf45b4f | - |
| 60 | Le plus souvent, comment cuisinez-vous le riz ? | 706fd436-2333-4f72-a258-af55c477f74b | TITLE | d0a8ac2f-1197-41a4-bc4b-6d0d4efaf56a | 5 | 29e15d12-abf2-490d-b696-0f708a0763e5 | - |
| 61 | À grande eau puis égoutté, comme des pâtes | fd45c8fc-5022-48bc-8680-7031963c02ca | MULTIPLE_CHOICE_OPTION | d0a8ac2f-1197-41a4-bc4b-6d0d4efaf56a | 5 | 706fd436-2333-4f72-a258-af55c477f74b | hasOtherOption=true |
| 62 | Par absorption, avec un volume d’eau à hauteur du riz | d5337828-a1ea-42c5-af06-aa334a9e0666 | MULTIPLE_CHOICE_OPTION | d0a8ac2f-1197-41a4-bc4b-6d0d4efaf56a | 5 | fd45c8fc-5022-48bc-8680-7031963c02ca | hasOtherOption=true |
| 63 | Pilaf | 7cc9785c-2dd6-4c4e-9554-58cc283363af | MULTIPLE_CHOICE_OPTION | d0a8ac2f-1197-41a4-bc4b-6d0d4efaf56a | 5 | d5337828-a1ea-42c5-af06-aa334a9e0666 | hasOtherOption=true |
| 64 | Au rice cooker, ou cuiseur à riz | 12ee6561-0274-4bae-85e1-640f5b6d7149 | MULTIPLE_CHOICE_OPTION | d0a8ac2f-1197-41a4-bc4b-6d0d4efaf56a | 5 | 7cc9785c-2dd6-4c4e-9554-58cc283363af | hasOtherOption=true |
| 65 | En sachet de cuisson rapide / riz instantané | 465e46c7-cdc2-4278-8fba-dfefe51df27b | MULTIPLE_CHOICE_OPTION | d0a8ac2f-1197-41a4-bc4b-6d0d4efaf56a | 5 | 12ee6561-0274-4bae-85e1-640f5b6d7149 | hasOtherOption=true |
| 66 | Je cuisine rarement du riz | ab9fdc26-4d03-42b9-b8f8-496b9b9a52eb | MULTIPLE_CHOICE_OPTION | d0a8ac2f-1197-41a4-bc4b-6d0d4efaf56a | 5 | 465e46c7-cdc2-4278-8fba-dfefe51df27b | hasOtherOption=true |
| 67 | Autre | 796eefc4-a45f-42fe-a4ea-4e492a631d35 | MULTIPLE_CHOICE_OPTION | d0a8ac2f-1197-41a4-bc4b-6d0d4efaf56a | 5 | ab9fdc26-4d03-42b9-b8f8-496b9b9a52eb | hasOtherOption=true, isOtherOption=true |
| 68 | Écran 5 – Ajouts au riz pendant cuisson | c4f16a04-99ce-4d7d-8dc6-e7438f9c5e29 | PAGE_BREAK | - | 6 | 796eefc4-a45f-42fe-a4ea-4e492a631d35 | - |
| 69 | Pendant la cuisson, ajoutez-vous quelque chose à l’eau ou au riz ? | 34af547f-aa4e-49f8-b8ff-0f9020eb6730 | TITLE | febb43cf-f222-44f6-8915-4db1471c89b6 | 6 | c4f16a04-99ce-4d7d-8dc6-e7438f9c5e29 | - |
| 70 | Rien | 8dc54f0b-9a0a-4a07-b389-14d13b275547 | CHECKBOX | febb43cf-f222-44f6-8915-4db1471c89b6 | 6 | 34af547f-aa4e-49f8-b8ff-0f9020eb6730 | hasOtherOption=true |
| 71 | Sel | 7cfcfe86-6390-4e32-bfdc-5a5eabe00859 | CHECKBOX | febb43cf-f222-44f6-8915-4db1471c89b6 | 6 | 8dc54f0b-9a0a-4a07-b389-14d13b275547 | hasOtherOption=true |
| 72 | Bouillon-cube | 33e4d553-6560-4d5b-b5af-7f7dbb5b2387 | CHECKBOX | febb43cf-f222-44f6-8915-4db1471c89b6 | 6 | 7cfcfe86-6390-4e32-bfdc-5a5eabe00859 | hasOtherOption=true |
| 73 | Épices | cf4840b6-02ae-4bb4-9da4-be2792a38d31 | CHECKBOX | febb43cf-f222-44f6-8915-4db1471c89b6 | 6 | 33e4d553-6560-4d5b-b5af-7f7dbb5b2387 | hasOtherOption=true |
| 74 | Herbes fraîches | 4cf01dd1-2527-4577-9a4c-01467c6fc47b | CHECKBOX | febb43cf-f222-44f6-8915-4db1471c89b6 | 6 | cf4840b6-02ae-4bb4-9da4-be2792a38d31 | hasOtherOption=true |
| 75 | Bouquet garni | 4ea40a66-81ca-44be-8e86-9aa0da1ce44b | CHECKBOX | febb43cf-f222-44f6-8915-4db1471c89b6 | 6 | 4cf01dd1-2527-4577-9a4c-01467c6fc47b | hasOtherOption=true |
| 76 | Ail / oignon / échalote | 3dc22683-44ba-42cf-8cb6-3eea1c5bd246 | CHECKBOX | febb43cf-f222-44f6-8915-4db1471c89b6 | 6 | 4ea40a66-81ca-44be-8e86-9aa0da1ce44b | hasOtherOption=true |
| 77 | Huile | 8c0b775c-b5de-4ec2-8a0a-fa98c970b8e8 | CHECKBOX | febb43cf-f222-44f6-8915-4db1471c89b6 | 6 | 3dc22683-44ba-42cf-8cb6-3eea1c5bd246 | hasOtherOption=true |
| 78 | Beurre | 9e3b8adc-81a9-48f5-88c0-38a1bcfe9092 | CHECKBOX | febb43cf-f222-44f6-8915-4db1471c89b6 | 6 | 8c0b775c-b5de-4ec2-8a0a-fa98c970b8e8 | hasOtherOption=true |
| 79 | Lait de coco | ea2fc9dd-e16c-4b89-9767-4aacfffb355a | CHECKBOX | febb43cf-f222-44f6-8915-4db1471c89b6 | 6 | 9e3b8adc-81a9-48f5-88c0-38a1bcfe9092 | hasOtherOption=true |
| 80 | Tomate / concentré de tomate | 26c62720-67b8-487e-973a-f87e24304859 | CHECKBOX | febb43cf-f222-44f6-8915-4db1471c89b6 | 6 | ea2fc9dd-e16c-4b89-9767-4aacfffb355a | hasOtherOption=true |
| 81 | Légumes | 8ff7f80c-f83b-429a-a53c-5d29a102a46a | CHECKBOX | febb43cf-f222-44f6-8915-4db1471c89b6 | 6 | 26c62720-67b8-487e-973a-f87e24304859 | hasOtherOption=true |
| 82 | Citron / vinaigre | f1b7b7ac-4cc1-4f98-82b0-c04806213872 | CHECKBOX | febb43cf-f222-44f6-8915-4db1471c89b6 | 6 | 8ff7f80c-f83b-429a-a53c-5d29a102a46a | hasOtherOption=true |
| 83 | Autre | 5442d30c-9d52-402f-a077-beb419e0fb96 | CHECKBOX | febb43cf-f222-44f6-8915-4db1471c89b6 | 6 | f1b7b7ac-4cc1-4f98-82b0-c04806213872 | hasOtherOption=true, isOtherOption=true |
| 84 | Écran 6 – Ajouts aux légumineuses pendant cuisson | 97338f57-4231-4489-ac43-68b6897ecb68 | PAGE_BREAK | - | 7 | 5442d30c-9d52-402f-a077-beb419e0fb96 | - |
| 85 | Pendant la cuisson, ajoutez-vous quelque chose à l’eau ou aux légumineuses ? | 012432e4-1899-45fd-b3ec-fac4392ec333 | TITLE | f474a6de-bdf2-44bd-9c80-70c26bcef806 | 7 | 97338f57-4231-4489-ac43-68b6897ecb68 | - |
| 86 | Exemples : lentilles, pois chiches, haricots, pois cassés… | b4a092bd-50c7-41a8-8f3a-6887f87fb846 | TEXT | f474a6de-bdf2-44bd-9c80-70c26bcef806 | 7 | 012432e4-1899-45fd-b3ec-fac4392ec333 | - |
| 87 | Rien | bb689e0b-8ee1-4931-a57c-5de0b00a658c | CHECKBOX | f474a6de-bdf2-44bd-9c80-70c26bcef806 | 7 | b4a092bd-50c7-41a8-8f3a-6887f87fb846 | hasOtherOption=true |
| 88 | Sel | 45c2fa03-36fe-4599-a8b2-79b4dc13fd3e | CHECKBOX | f474a6de-bdf2-44bd-9c80-70c26bcef806 | 7 | bb689e0b-8ee1-4931-a57c-5de0b00a658c | hasOtherOption=true |
| 89 | Bouillon-cube | ca1f7953-c3e2-46cf-9de9-b5ab4250906a | CHECKBOX | f474a6de-bdf2-44bd-9c80-70c26bcef806 | 7 | 45c2fa03-36fe-4599-a8b2-79b4dc13fd3e | hasOtherOption=true |
| 90 | Épices | b47649fd-36ae-41d8-97a1-ece5d1f8ef39 | CHECKBOX | f474a6de-bdf2-44bd-9c80-70c26bcef806 | 7 | ca1f7953-c3e2-46cf-9de9-b5ab4250906a | hasOtherOption=true |
| 91 | Herbes fraîches | bedd2006-16c8-40d8-8d01-d25449b35f94 | CHECKBOX | f474a6de-bdf2-44bd-9c80-70c26bcef806 | 7 | b47649fd-36ae-41d8-97a1-ece5d1f8ef39 | hasOtherOption=true |
| 92 | Bouquet garni | 16dd96ca-c3bb-4a7a-91a4-877396523321 | CHECKBOX | f474a6de-bdf2-44bd-9c80-70c26bcef806 | 7 | bedd2006-16c8-40d8-8d01-d25449b35f94 | hasOtherOption=true |
| 93 | Ail / oignon / échalote | aabb5f3e-4e0f-470d-9633-783b8bd0038a | CHECKBOX | f474a6de-bdf2-44bd-9c80-70c26bcef806 | 7 | 16dd96ca-c3bb-4a7a-91a4-877396523321 | hasOtherOption=true |
| 94 | Huile | 52231889-01ca-4aef-8c3c-79ed187d8796 | CHECKBOX | f474a6de-bdf2-44bd-9c80-70c26bcef806 | 7 | aabb5f3e-4e0f-470d-9633-783b8bd0038a | hasOtherOption=true |
| 95 | Beurre | f1921ef6-2df4-4136-b28a-64f68a8e1743 | CHECKBOX | f474a6de-bdf2-44bd-9c80-70c26bcef806 | 7 | 52231889-01ca-4aef-8c3c-79ed187d8796 | hasOtherOption=true |
| 96 | Tomate / concentré de tomate | 8f28d8dd-5f1b-471f-b830-c3d28ceb4ef9 | CHECKBOX | f474a6de-bdf2-44bd-9c80-70c26bcef806 | 7 | f1921ef6-2df4-4136-b28a-64f68a8e1743 | hasOtherOption=true |
| 97 | Légumes | 9b253976-d6ba-4575-9007-4a6ea2eccf2a | CHECKBOX | f474a6de-bdf2-44bd-9c80-70c26bcef806 | 7 | 8f28d8dd-5f1b-471f-b830-c3d28ceb4ef9 | hasOtherOption=true |
| 98 | Citron / vinaigre | 62902043-2314-435c-bce2-189ccbdc8d15 | CHECKBOX | f474a6de-bdf2-44bd-9c80-70c26bcef806 | 7 | 9b253976-d6ba-4575-9007-4a6ea2eccf2a | hasOtherOption=true |
| 99 | Autre | d31b10b2-8c5d-422e-85f0-40e94466ea86 | CHECKBOX | f474a6de-bdf2-44bd-9c80-70c26bcef806 | 7 | 62902043-2314-435c-bce2-189ccbdc8d15 | hasOtherOption=true, isOtherOption=true |
| 100 | Écran 7 – Ajouts aux féculents et graines pendant cuisson | a2ac1259-48c5-4a18-b006-cc760d768823 | PAGE_BREAK | - | 8 | d31b10b2-8c5d-422e-85f0-40e94466ea86 | - |
| 101 | Pendant la cuisson, ajoutez-vous quelque chose à l’eau ou aux féculents/graines ? | 817edb38-f2f6-4b2b-8785-161795b46f2a | TITLE | 173f1791-b375-4d7a-878b-00c7bd14fd61 | 8 | a2ac1259-48c5-4a18-b006-cc760d768823 | - |
| 102 | Exemples : pâtes, semoule, boulgour, quinoa… | 86168024-4fc2-4119-9caa-b521e21130d0 | TEXT | 173f1791-b375-4d7a-878b-00c7bd14fd61 | 8 | 817edb38-f2f6-4b2b-8785-161795b46f2a | - |
| 103 | Rien | a07c8093-e4b7-48d6-801d-6af69f56894b | CHECKBOX | 173f1791-b375-4d7a-878b-00c7bd14fd61 | 8 | 86168024-4fc2-4119-9caa-b521e21130d0 | hasOtherOption=true |
| 104 | Sel | 39b0ff87-3b12-4912-8cc0-58e0919f456a | CHECKBOX | 173f1791-b375-4d7a-878b-00c7bd14fd61 | 8 | a07c8093-e4b7-48d6-801d-6af69f56894b | hasOtherOption=true |
| 105 | Bouillon-cube | 2b66abf1-87ef-4378-98b8-67a923348bb1 | CHECKBOX | 173f1791-b375-4d7a-878b-00c7bd14fd61 | 8 | 39b0ff87-3b12-4912-8cc0-58e0919f456a | hasOtherOption=true |
| 106 | Épices | 2cdb6b52-5444-4ff7-a49c-5fde54721feb | CHECKBOX | 173f1791-b375-4d7a-878b-00c7bd14fd61 | 8 | 2b66abf1-87ef-4378-98b8-67a923348bb1 | hasOtherOption=true |
| 107 | Herbes fraîches | 9315e5f4-376d-4f78-9224-fc262af2b42a | CHECKBOX | 173f1791-b375-4d7a-878b-00c7bd14fd61 | 8 | 2cdb6b52-5444-4ff7-a49c-5fde54721feb | hasOtherOption=true |
| 108 | Bouquet garni | dd3594e4-d18d-4ee3-9e9c-afd7a4244548 | CHECKBOX | 173f1791-b375-4d7a-878b-00c7bd14fd61 | 8 | 9315e5f4-376d-4f78-9224-fc262af2b42a | hasOtherOption=true |
| 109 | Ail / oignon / échalote | 583925a1-52d8-462e-be03-c3ded96b5bf3 | CHECKBOX | 173f1791-b375-4d7a-878b-00c7bd14fd61 | 8 | dd3594e4-d18d-4ee3-9e9c-afd7a4244548 | hasOtherOption=true |
| 110 | Huile | c0d3e986-a748-42aa-b2fd-dcbec42a4a11 | CHECKBOX | 173f1791-b375-4d7a-878b-00c7bd14fd61 | 8 | 583925a1-52d8-462e-be03-c3ded96b5bf3 | hasOtherOption=true |
| 111 | Beurre | 25beab24-27a7-459b-abe6-374715d2a825 | CHECKBOX | 173f1791-b375-4d7a-878b-00c7bd14fd61 | 8 | c0d3e986-a748-42aa-b2fd-dcbec42a4a11 | hasOtherOption=true |
| 112 | Tomate / concentré de tomate | 31cc7bba-5bfd-41c3-b200-f52e5e7b78f0 | CHECKBOX | 173f1791-b375-4d7a-878b-00c7bd14fd61 | 8 | 25beab24-27a7-459b-abe6-374715d2a825 | hasOtherOption=true |
| 113 | Légumes | a13f3bab-9b47-4634-8b60-0dcf61399afd | CHECKBOX | 173f1791-b375-4d7a-878b-00c7bd14fd61 | 8 | 31cc7bba-5bfd-41c3-b200-f52e5e7b78f0 | hasOtherOption=true |
| 114 | Citron / vinaigre | bf87261f-08c2-4117-87bd-fa61a49d3524 | CHECKBOX | 173f1791-b375-4d7a-878b-00c7bd14fd61 | 8 | a13f3bab-9b47-4634-8b60-0dcf61399afd | hasOtherOption=true |
| 115 | Autre | 749ab35f-fc4f-4f22-b120-aaf035bcc836 | CHECKBOX | 173f1791-b375-4d7a-878b-00c7bd14fd61 | 8 | bf87261f-08c2-4117-87bd-fa61a49d3524 | hasOtherOption=true, isOtherOption=true |
| 116 | Écran 8 – Ajouts après cuisson | af5ed868-8a78-4825-8a7f-c1e264278aa5 | PAGE_BREAK | - | 9 | 749ab35f-fc4f-4f22-b120-aaf035bcc836 | - |
| 117 | Après cuisson, ajoutez-vous quelque chose à vos bases pour leur donner plus de goût ou d’intérêt ? | 0aeeed0c-2b6a-432c-8816-f1ebe0356939 | TITLE | 7687e6a9-ccf3-42f8-a09c-8de77ef2691d | 9 | af5ed868-8a78-4825-8a7f-c1e264278aa5 | - |
| 118 | Rien | a7e15308-b8be-47e1-bffa-9e411d70cd3e | CHECKBOX | 7687e6a9-ccf3-42f8-a09c-8de77ef2691d | 9 | 0aeeed0c-2b6a-432c-8816-f1ebe0356939 | hasOtherOption=true |
| 119 | Sel / poivre | e3dc9dca-9013-41c6-a314-c767c690fe09 | CHECKBOX | 7687e6a9-ccf3-42f8-a09c-8de77ef2691d | 9 | a7e15308-b8be-47e1-bffa-9e411d70cd3e | hasOtherOption=true |
| 120 | Épices | 89f69d8e-4e44-480a-96f3-12d81bec01a9 | CHECKBOX | 7687e6a9-ccf3-42f8-a09c-8de77ef2691d | 9 | e3dc9dca-9013-41c6-a314-c767c690fe09 | hasOtherOption=true |
| 121 | Herbes fraîches | c800612b-f320-40b0-878d-3a561dee56ed | CHECKBOX | 7687e6a9-ccf3-42f8-a09c-8de77ef2691d | 9 | 89f69d8e-4e44-480a-96f3-12d81bec01a9 | hasOtherOption=true |
| 122 | Huile | 0f9ac342-cbfa-435e-b11d-1fe680caac15 | CHECKBOX | 7687e6a9-ccf3-42f8-a09c-8de77ef2691d | 9 | c800612b-f320-40b0-878d-3a561dee56ed | hasOtherOption=true |
| 123 | Beurre | dfface76-ef4d-4242-922d-c231c2b181e7 | CHECKBOX | 7687e6a9-ccf3-42f8-a09c-8de77ef2691d | 9 | 0f9ac342-cbfa-435e-b11d-1fe680caac15 | hasOtherOption=true |
| 124 | Vinaigre | 66f39f0c-9e06-425d-9321-1c5f9779e4a0 | CHECKBOX | 7687e6a9-ccf3-42f8-a09c-8de77ef2691d | 9 | dfface76-ef4d-4242-922d-c231c2b181e7 | hasOtherOption=true |
| 125 | Citron | e1bfe67e-8a8a-4ef2-81f3-e9c3ce388484 | CHECKBOX | 7687e6a9-ccf3-42f8-a09c-8de77ef2691d | 9 | 66f39f0c-9e06-425d-9321-1c5f9779e4a0 | hasOtherOption=true |
| 126 | Levure de bière / levure maltée | e385e94a-daaa-472b-baca-81b1fb837581 | CHECKBOX | 7687e6a9-ccf3-42f8-a09c-8de77ef2691d | 9 | e1bfe67e-8a8a-4ef2-81f3-e9c3ce388484 | hasOtherOption=true |
| 127 | Graines | 837b060f-4984-403b-b9d6-2dab497a6f3b | CHECKBOX | 7687e6a9-ccf3-42f8-a09c-8de77ef2691d | 9 | e385e94a-daaa-472b-baca-81b1fb837581 | hasOtherOption=true |
| 128 | Fruits secs / oléagineux | 65f78c9e-4ea9-431c-b0fc-de4cdf01f5aa | CHECKBOX | 7687e6a9-ccf3-42f8-a09c-8de77ef2691d | 9 | 837b060f-4984-403b-b9d6-2dab497a6f3b | hasOtherOption=true |
| 129 | Fromage râpé | 68f0273c-1b09-4466-baec-52227ed18deb | CHECKBOX | 7687e6a9-ccf3-42f8-a09c-8de77ef2691d | 9 | 65f78c9e-4ea9-431c-b0fc-de4cdf01f5aa | hasOtherOption=true |
| 130 | Condiments | bf1efb0e-a5c6-4c77-b294-7ddfd4b646df | CHECKBOX | 7687e6a9-ccf3-42f8-a09c-8de77ef2691d | 9 | 68f0273c-1b09-4466-baec-52227ed18deb | hasOtherOption=true |
| 131 | Autre | 7d29d1f9-fc11-46b1-ac0d-ed6d19a85965 | CHECKBOX | 7687e6a9-ccf3-42f8-a09c-8de77ef2691d | 9 | bf1efb0e-a5c6-4c77-b294-7ddfd4b646df | hasOtherOption=true, isOtherOption=true |
| 132 | - | acb9d5b8-6b05-4775-85dc-799d72390e01 | CONDITIONAL_LOGIC | - | 9 | 7d29d1f9-fc11-46b1-ac0d-ed6d19a85965 | see `## Logic rules` below |
| 133 | - | cb7b432b-52c0-49fb-bda0-529c7569fb41 | CONDITIONAL_LOGIC | - | 9 | acb9d5b8-6b05-4775-85dc-799d72390e01 | see `## Logic rules` below |
| 134 | - | d51ba6c6-3c96-4497-a276-350534b8be90 | CONDITIONAL_LOGIC | - | 9 | cb7b432b-52c0-49fb-bda0-529c7569fb41 | see `## Logic rules` below |
| 135 | Ces ajouts après cuisson servent surtout à… | 426e8179-8421-4b3b-9419-c63349c45e51 | TITLE | 32f34299-01e3-441c-bfec-854759960489 | 9 | d51ba6c6-3c96-4497-a276-350534b8be90 | isHidden=true |
| 136 | Donner plus de goût | 2b2a999a-9a88-4659-b07f-93d8a13158f9 | CHECKBOX | 32f34299-01e3-441c-bfec-854759960489 | 9 | 426e8179-8421-4b3b-9419-c63349c45e51 | hasOtherOption=true, isHidden=true |
| 137 | Ajouter de la texture | 8ca6d904-94d9-4220-9363-dc68b44b20fc | CHECKBOX | 32f34299-01e3-441c-bfec-854759960489 | 9 | 2b2a999a-9a88-4659-b07f-93d8a13158f9 | hasOtherOption=true, isHidden=true |
| 138 | Rendre le plat moins sec | abca4ab3-f1fa-4bf8-b597-c16f95ae9238 | CHECKBOX | 32f34299-01e3-441c-bfec-854759960489 | 9 | 8ca6d904-94d9-4220-9363-dc68b44b20fc | hasOtherOption=true, isHidden=true |
| 139 | Ajouter une touche plus naturelle | 7bebee10-d73e-445d-bab3-5a00162b4f1d | CHECKBOX | 32f34299-01e3-441c-bfec-854759960489 | 9 | abca4ab3-f1fa-4bf8-b597-c16f95ae9238 | hasOtherOption=true, isHidden=true |
| 140 | Ajouter une dimension nutritionnelle | f65ef1a6-0854-4387-b1e6-6074197c867c | CHECKBOX | 32f34299-01e3-441c-bfec-854759960489 | 9 | 7bebee10-d73e-445d-bab3-5a00162b4f1d | hasOtherOption=true, isHidden=true |
| 141 | Faire comme d’habitude / par réflexe | c4d7089f-c58a-4871-9af8-38f1e6a076b0 | CHECKBOX | 32f34299-01e3-441c-bfec-854759960489 | 9 | f65ef1a6-0854-4387-b1e6-6074197c867c | hasOtherOption=true, isHidden=true |
| 142 | Autre | 1ec385dc-1976-4853-b6a4-7f833812c10c | CHECKBOX | 32f34299-01e3-441c-bfec-854759960489 | 9 | c4d7089f-c58a-4871-9af8-38f1e6a076b0 | hasOtherOption=true, isOtherOption=true, isHidden=true |
| 143 | Écran 9 – Épices et herbes (conditionnel) | aa1a5b2e-fbdc-4f6d-851e-8f125a221418 | PAGE_BREAK | - | 10 | 1ec385dc-1976-4853-b6a4-7f833812c10c | - |
| 144 | Quelles épices ou herbes utilisez-vous le plus souvent ? | 76feff44-3c16-44d5-993e-842418110367 | TITLE | c9f2eed4-a8cb-4c0b-a62b-8dcb7a1565a1 | 10 | aa1a5b2e-fbdc-4f6d-851e-8f125a221418 | - |
| 145 | Poivre | a9f069a5-31fb-45dd-a5a9-d62caa57e2ee | CHECKBOX | c9f2eed4-a8cb-4c0b-a62b-8dcb7a1565a1 | 10 | 76feff44-3c16-44d5-993e-842418110367 | hasOtherOption=true |
| 146 | Curry | 48821a72-ccc7-48dd-a468-635c125fc4f9 | CHECKBOX | c9f2eed4-a8cb-4c0b-a62b-8dcb7a1565a1 | 10 | a9f069a5-31fb-45dd-a5a9-d62caa57e2ee | hasOtherOption=true |
| 147 | Paprika | 6d5c0cb4-ee01-496d-87f3-a7234cee6b3a | CHECKBOX | c9f2eed4-a8cb-4c0b-a62b-8dcb7a1565a1 | 10 | 48821a72-ccc7-48dd-a468-635c125fc4f9 | hasOtherOption=true |
| 148 | Curcuma | 9ba295fd-0a3b-4e39-a7f1-e72fe8519d4e | CHECKBOX | c9f2eed4-a8cb-4c0b-a62b-8dcb7a1565a1 | 10 | 6d5c0cb4-ee01-496d-87f3-a7234cee6b3a | hasOtherOption=true |
| 149 | Cumin | 182cdcb7-fc19-4e1e-a244-04212ad8b386 | CHECKBOX | c9f2eed4-a8cb-4c0b-a62b-8dcb7a1565a1 | 10 | 9ba295fd-0a3b-4e39-a7f1-e72fe8519d4e | hasOtherOption=true |
| 150 | Gingembre | 46943ac6-e495-4ce3-9b2a-df1abf69665c | CHECKBOX | c9f2eed4-a8cb-4c0b-a62b-8dcb7a1565a1 | 10 | 182cdcb7-fc19-4e1e-a244-04212ad8b386 | hasOtherOption=true |
| 151 | Cannelle | 716d5a0a-b625-4fe6-98f9-f3a6890b1ca0 | CHECKBOX | c9f2eed4-a8cb-4c0b-a62b-8dcb7a1565a1 | 10 | 46943ac6-e495-4ce3-9b2a-df1abf69665c | hasOtherOption=true |
| 152 | Piment | 5cfaeae8-87a2-4928-be76-0eaeac70bace | CHECKBOX | c9f2eed4-a8cb-4c0b-a62b-8dcb7a1565a1 | 10 | 716d5a0a-b625-4fe6-98f9-f3a6890b1ca0 | hasOtherOption=true |
| 153 | Thym | 251913f5-93e2-4179-87a3-edd245bb2ff9 | CHECKBOX | c9f2eed4-a8cb-4c0b-a62b-8dcb7a1565a1 | 10 | 5cfaeae8-87a2-4928-be76-0eaeac70bace | hasOtherOption=true |
| 154 | Laurier | 246ff89c-33f7-4872-9006-59b557925822 | CHECKBOX | c9f2eed4-a8cb-4c0b-a62b-8dcb7a1565a1 | 10 | 251913f5-93e2-4179-87a3-edd245bb2ff9 | hasOtherOption=true |
| 155 | Persil | 1feee737-91aa-4603-a2a4-0be79701c184 | CHECKBOX | c9f2eed4-a8cb-4c0b-a62b-8dcb7a1565a1 | 10 | 246ff89c-33f7-4872-9006-59b557925822 | hasOtherOption=true |
| 156 | Coriandre | d4c59645-9f59-43d1-9f5c-1a804c18ab1e | CHECKBOX | c9f2eed4-a8cb-4c0b-a62b-8dcb7a1565a1 | 10 | 1feee737-91aa-4603-a2a4-0be79701c184 | hasOtherOption=true |
| 157 | Basilic | 7bfc3c39-f0df-4a52-b06d-e896b602f3f4 | CHECKBOX | c9f2eed4-a8cb-4c0b-a62b-8dcb7a1565a1 | 10 | d4c59645-9f59-43d1-9f5c-1a804c18ab1e | hasOtherOption=true |
| 158 | Herbes de Provence | dd44f8a6-193e-4a70-b5a7-7741a7eb37dc | CHECKBOX | c9f2eed4-a8cb-4c0b-a62b-8dcb7a1565a1 | 10 | 7bfc3c39-f0df-4a52-b06d-e896b602f3f4 | hasOtherOption=true |
| 159 | Mélanges tout prêts | 4414f4e9-7371-4acd-9a6a-872cd92c7a75 | CHECKBOX | c9f2eed4-a8cb-4c0b-a62b-8dcb7a1565a1 | 10 | dd44f8a6-193e-4a70-b5a7-7741a7eb37dc | hasOtherOption=true |
| 160 | Autre | 0f6708b8-4b96-48f2-8301-ddbe9f77f243 | CHECKBOX | c9f2eed4-a8cb-4c0b-a62b-8dcb7a1565a1 | 10 | 4414f4e9-7371-4acd-9a6a-872cd92c7a75 | hasOtherOption=true, isOtherOption=true |
| 161 | Écran 10 – Découverte de nouvelles saveurs (conditionnel) | 564722c8-80b4-4eee-b899-c9c0f83bf34e | PAGE_BREAK | - | 11 | 0f6708b8-4b96-48f2-8301-ddbe9f77f243 | - |
| 162 | Vous arrive-t-il de découvrir de nouvelles épices du monde ou de nouvelles saveurs pour agrémenter vos plats ? | a90b564c-8a5e-4e8d-b8d5-a8aea81ad4a1 | TITLE | 0399325e-3085-4983-ac45-415433dab7c5 | 11 | 564722c8-80b4-4eee-b899-c9c0f83bf34e | - |
| 163 | Oui, souvent | 8626b933-707f-4ed5-bf0a-e4a4c394b81f | MULTIPLE_CHOICE_OPTION | 0399325e-3085-4983-ac45-415433dab7c5 | 11 | a90b564c-8a5e-4e8d-b8d5-a8aea81ad4a1 | - |
| 164 | Oui, parfois | adaaa312-842f-42d0-8c9c-af7d584a01c2 | MULTIPLE_CHOICE_OPTION | 0399325e-3085-4983-ac45-415433dab7c5 | 11 | 8626b933-707f-4ed5-bf0a-e4a4c394b81f | - |
| 165 | Rarement | ea791a5c-0222-4070-87aa-a134e4807c76 | MULTIPLE_CHOICE_OPTION | 0399325e-3085-4983-ac45-415433dab7c5 | 11 | adaaa312-842f-42d0-8c9c-af7d584a01c2 | - |
| 166 | Non | fbf46159-c5db-422b-a201-d7d9d020ad03 | MULTIPLE_CHOICE_OPTION | 0399325e-3085-4983-ac45-415433dab7c5 | 11 | ea791a5c-0222-4070-87aa-a134e4807c76 | - |
| 167 | Je ne sais pas | 63b57095-d660-411a-9e73-4d1919f0f07a | MULTIPLE_CHOICE_OPTION | 0399325e-3085-4983-ac45-415433dab7c5 | 11 | fbf46159-c5db-422b-a201-d7d9d020ad03 | - |
| 168 | Écran 11 – Satisfaction actuelle | f49a6495-5209-4d18-8fba-33408d8b7485 | PAGE_BREAK | - | 12 | 63b57095-d660-411a-9e73-4d1919f0f07a | - |
| 169 | Êtes-vous satisfait(e) des solutions actuelles pour donner du goût à vos bases ? | ee1813ae-afa1-4cda-8812-cbba3c789431 | TITLE | cf172272-6491-4032-98ef-2c169cdfa25b | 12 | f49a6495-5209-4d18-8fba-33408d8b7485 | - |
| 170 | - | 237dedcc-1854-4b43-b7dd-3b103d62930c | LINEAR_SCALE | cf172272-6491-4032-98ef-2c169cdfa25b | 12 | ee1813ae-afa1-4cda-8812-cbba3c789431 | start=1, end=5, leftLabel="Pas du tout satisfait(e)", rightLabel="Très satisfait(e)" |
| 171 | Écran 12 – Variation des saveurs | d6fc477a-6ce9-438e-83aa-d60ed27bc94f | PAGE_BREAK | - | 13 | 237dedcc-1854-4b43-b7dd-3b103d62930c | - |
| 172 | Variez-vous la façon d’ajouter du goût à vos bases, ou utilisez-vous régulièrement les mêmes ingrédients ? | 7b328042-e501-4a7c-a1e7-86169c98546d | TITLE | d5427ab2-e6e5-43a6-9bc1-97101f9d430a | 13 | d6fc477a-6ce9-438e-83aa-d60ed27bc94f | - |
| 173 | Je varie souvent | f34698a0-45c4-48a1-9219-d5d9cb4b7d51 | MULTIPLE_CHOICE_OPTION | d5427ab2-e6e5-43a6-9bc1-97101f9d430a | 13 | 7b328042-e501-4a7c-a1e7-86169c98546d | - |
| 174 | Je varie parfois | f6b4e832-1afa-4eca-9223-35d19650fd5f | MULTIPLE_CHOICE_OPTION | d5427ab2-e6e5-43a6-9bc1-97101f9d430a | 13 | f34698a0-45c4-48a1-9219-d5d9cb4b7d51 | - |
| 175 | J’utilise souvent les mêmes ingrédients | dbc856e9-1ad9-4f91-9990-c402aef787e4 | MULTIPLE_CHOICE_OPTION | d5427ab2-e6e5-43a6-9bc1-97101f9d430a | 13 | f6b4e832-1afa-4eca-9223-35d19650fd5f | - |
| 176 | Je ne me pose pas vraiment la question | e373b95d-05bc-46c3-8e60-204104ff843d | MULTIPLE_CHOICE_OPTION | d5427ab2-e6e5-43a6-9bc1-97101f9d430a | 13 | dbc856e9-1ad9-4f91-9990-c402aef787e4 | - |
| 177 | - | 602e98d5-8ad6-4353-a43b-bf3b228de21c | CONDITIONAL_LOGIC | - | 13 | e373b95d-05bc-46c3-8e60-204104ff843d | see `## Logic rules` below |
| 178 | - | be8fbeb9-7020-4d7c-a361-f28da136a649 | CONDITIONAL_LOGIC | - | 13 | 602e98d5-8ad6-4353-a43b-bf3b228de21c | see `## Logic rules` below |
| 179 | Pourquoi utilisez-vous souvent les mêmes ingrédients ? | 12e52159-19f0-49b9-8616-3acc1f0ff9f6 | TITLE | 64ed3c17-6a59-44f1-914d-18d051579ceb | 13 | be8fbeb9-7020-4d7c-a361-f28da136a649 | isHidden=true |
| 180 | - | 03638caf-ebd9-4651-9058-9f012ac3c754 | TEXTAREA | 64ed3c17-6a59-44f1-914d-18d051579ceb | 13 | 12e52159-19f0-49b9-8616-3acc1f0ff9f6 | isRequired=false, isHidden=true |
| 181 | Écran 13 – Frictions actuelles | 4ca5a801-2f82-4064-b96f-888e43b23310 | PAGE_BREAK | - | 14 | 03638caf-ebd9-4651-9058-9f012ac3c754 | - |
| 182 | Qu’est-ce qui vous gêne le plus dans les bouillons ou condiments actuels ? | 1bf091d3-2b87-4a7e-94c7-6c6251dc765b | TITLE | be969b21-7600-46a8-9e57-df2e889f9dbf | 14 | 4ca5a801-2f82-4064-b96f-888e43b23310 | - |
| 183 | Trop salés | 90066813-6baa-451f-ae5c-2684bd088f17 | CHECKBOX | be969b21-7600-46a8-9e57-df2e889f9dbf | 14 | 1bf091d3-2b87-4a7e-94c7-6c6251dc765b | hasOtherOption=true |
| 184 | Additifs | 9ba5a8a1-2556-4d1d-aa16-108bae7a250c | CHECKBOX | be969b21-7600-46a8-9e57-df2e889f9dbf | 14 | 90066813-6baa-451f-ae5c-2684bd088f17 | hasOtherOption=true |
| 185 | Exhausteurs de goût | 56fd0863-52b3-445c-bb8f-a4440ae53485 | CHECKBOX | be969b21-7600-46a8-9e57-df2e889f9dbf | 14 | 9ba5a8a1-2556-4d1d-aa16-108bae7a250c | hasOtherOption=true |
| 186 | Goût redondant | 42baf333-b33b-41e9-a73d-f7edc5ff92d5 | CHECKBOX | be969b21-7600-46a8-9e57-df2e889f9dbf | 14 | 56fd0863-52b3-445c-bb8f-a4440ae53485 | hasOtherOption=true |
| 187 | Prix | d9bfc8ff-167f-4b66-95c1-ccca0387fdb3 | CHECKBOX | be969b21-7600-46a8-9e57-df2e889f9dbf | 14 | 42baf333-b33b-41e9-a73d-f7edc5ff92d5 | hasOtherOption=true |
| 188 | Composition peu claire | daf5eb02-b8e3-4150-815d-99b6e9f4f18b | CHECKBOX | be969b21-7600-46a8-9e57-df2e889f9dbf | 14 | d9bfc8ff-167f-4b66-95c1-ccca0387fdb3 | hasOtherOption=true |
| 189 | Rien ne me gêne | 09d73ff4-9fca-4072-93c1-51b6be5bb866 | CHECKBOX | be969b21-7600-46a8-9e57-df2e889f9dbf | 14 | daf5eb02-b8e3-4150-815d-99b6e9f4f18b | hasOtherOption=true |
| 190 | Cela me provoque des symptômes quand j’en consomme | 87df6e0a-4a48-4d11-a5f8-475b2928328c | CHECKBOX | be969b21-7600-46a8-9e57-df2e889f9dbf | 14 | 09d73ff4-9fca-4072-93c1-51b6be5bb866 | hasOtherOption=true |
| 191 | Autre | b968cb2d-26f2-48da-aa97-1e44c93f2f6a | CHECKBOX | be969b21-7600-46a8-9e57-df2e889f9dbf | 14 | 87df6e0a-4a48-4d11-a5f8-475b2928328c | hasOtherOption=true, isOtherOption=true |
| 192 | Écran 14 – Ouverture au changement : sachet / goût | beabe22a-93d3-4310-85b9-33a28882c386 | PAGE_BREAK | - | 15 | b968cb2d-26f2-48da-aa97-1e44c93f2f6a | - |
| 193 | Seriez-vous ouvert(e) à essayer un nouveau geste pendant la cuisson de vos bases, par exemple déposer un sachet d’épices, d’aromates et d’ingrédients végétaux dans l’eau de cuisson pour apporter plus de goût et de nouvelles saveurs ? | b9c9c8e3-38d3-41ca-a022-1b12f37fbbba | TITLE | 92c3d699-a17a-494f-b064-d1dad6fdc024 | 15 | beabe22a-93d3-4310-85b9-33a28882c386 | - |
| 194 | - | 2abffd2d-2184-4827-b36e-586112d108fe | LINEAR_SCALE | 92c3d699-a17a-494f-b064-d1dad6fdc024 | 15 | b9c9c8e3-38d3-41ca-a022-1b12f37fbbba | start=1, leftLabel="Pas du tout", centerLabel="Pourquoi pas", rightLabel="Tout à fait" |
| 195 | Des suggestions ou réflexions à ce sujet ? | 70d1fef9-7986-46a7-b220-b5c9ae6db0d2 | TITLE | 1afa34e2-0811-444f-8471-ff274c09a576 | 15 | 2abffd2d-2184-4827-b36e-586112d108fe | - |
| 196 | - | 5056b150-3c82-476a-9f31-0f0711121212 | TEXTAREA | 1afa34e2-0811-444f-8471-ff274c09a576 | 15 | 70d1fef9-7986-46a7-b220-b5c9ae6db0d2 | isRequired=false |
| 197 | Écran 15 – Ouverture au changement : préparation végétale | b7355e56-0f7c-4345-ac8c-4d98ee57a594 | PAGE_BREAK | - | 16 | 5056b150-3c82-476a-9f31-0f0711121212 | - |
| 198 | Autre possibilité : certains produits culinaires peuvent aussi se mélanger directement à la base pendant la cuisson. | 02f63847-3fcf-4519-bd26-02ecb9201ace | TEXT | - | 16 | b7355e56-0f7c-4345-ac8c-4d98ee57a594 | - |
| 199 | Seriez-vous ouvert(e) à essayer un nouveau geste pendant la cuisson de vos bases, par exemple ajouter deux cuillères d’une préparation végétale contenant des épices, des graines, des légumes ou des superaliments pour apporter plus de variété et une dimension nutritionnelle au plat ? | 811305b3-4599-4354-8c0d-7e4c61f1c647 | TITLE | e53ad5ea-e629-4131-a07c-e9ba8e11e9c3 | 16 | 02f63847-3fcf-4519-bd26-02ecb9201ace | - |
| 200 | - | 12d41b42-d4de-4daa-b808-94acaf4a8e03 | LINEAR_SCALE | e53ad5ea-e629-4131-a07c-e9ba8e11e9c3 | 16 | 811305b3-4599-4354-8c0d-7e4c61f1c647 | start=1, leftLabel="Pas du tout", centerLabel="Pourquoi pas", rightLabel="Tout à fait" |
| 201 | Des suggestions ou réflexions à ce sujet ? | a4b49889-97ca-44f0-83a3-4a981014ed46 | TITLE | ea6f19df-70ff-4938-9e5a-6dc757312aa5 | 16 | 12d41b42-d4de-4daa-b808-94acaf4a8e03 | - |
| 202 | - | eac8e7cb-2f26-44ca-9787-b69ccfda93a5 | TEXTAREA | ea6f19df-70ff-4938-9e5a-6dc757312aa5 | 16 | a4b49889-97ca-44f0-83a3-4a981014ed46 | isRequired=false |
| 203 | Écran 16 – Priorités | aa0adbd2-ded0-43a5-a7ad-4eb744567763 | PAGE_BREAK | - | 17 | eac8e7cb-2f26-44ca-9787-b69ccfda93a5 | - |
| 204 | Qu’est-ce qui compte le plus pour vous dans un produit qui accompagne la cuisson ? Classez du plus au moins important. | 975cab17-00d5-4b3e-a2ad-9c2c3e656c08 | TITLE | 4d36e475-4500-46bb-9392-612556ec52b1 | 17 | aa0adbd2-ded0-43a5-a7ad-4eb744567763 | - |
| 205 | Goût | 0686de6f-51f6-4125-8e75-622df1ca6d67 | RANKING_OPTION | 4d36e475-4500-46bb-9392-612556ec52b1 | 17 | 975cab17-00d5-4b3e-a2ad-9c2c3e656c08 | - |
| 206 | Naturalité, sans additif ni exhausteur de goût | 3b65c894-a868-4a36-a3ff-c80c3386b4dd | RANKING_OPTION | 4d36e475-4500-46bb-9392-612556ec52b1 | 17 | 0686de6f-51f6-4125-8e75-622df1ca6d67 | - |
| 207 | Praticité | 0c3a35fa-cefb-4b26-9506-a83345a0ba26 | RANKING_OPTION | 4d36e475-4500-46bb-9392-612556ec52b1 | 17 | 3b65c894-a868-4a36-a3ff-c80c3386b4dd | - |
| 208 | Apport nutritionnel | de272fcc-4b27-4cf2-b54e-5688ced0cbe7 | RANKING_OPTION | 4d36e475-4500-46bb-9392-612556ec52b1 | 17 | 0c3a35fa-cefb-4b26-9506-a83345a0ba26 | - |
| 209 | Écran 17 – Contextualisation avant concept | 68d2dfdb-79ec-4b4b-9a2e-3d86a2fb590b | PAGE_BREAK | - | 18 | de272fcc-4b27-4cf2-b54e-5688ced0cbe7 | - |
| 210 | Les bases alimentaires comme le riz, les pâtes ou les graines sont souvent choisies pour leur simplicité et leur apport en énergie au cœur des repas. L’idée explorée ici est de voir si le moment de cuisson peut aussi devenir une occasion d’apporter plus de goût, de variété et d’ingrédients végétaux à valeur nutritionnelle. Nous étudions deux façons possibles de travailler ce moment de cuisson. | 4a5d617e-af3b-4d94-a806-434c60e87f66 | TEXT | - | 18 | 68d2dfdb-79ec-4b4b-9a2e-3d86a2fb590b | - |
| 211 | Écran 18 – Présentation du concept (randomisé) | e7002fb7-ecb1-49c5-97e8-96c0a121be53 | PAGE_BREAK | - | 19 | 4a5d617e-af3b-4d94-a806-434c60e87f66 | - |
| 212 | Nous étudions une nouvelle idée de produit culinaire. Il en existe deux versions. Prenez le temps de lire les deux — il n’y a pas de bonne réponse. | d40a7af7-8923-4666-a029-1df965f4424e | TEXT | - | 19 | e7002fb7-ecb1-49c5-97e8-96c0a121be53 | - |
| 213 | <b>Option A</b><br>Un sachet à déposer dans l’eau de cuisson de votre riz, de vos féculents/graines ou de vos légumineuses, puis à retirer en fin de cuisson — comme une infusion culinaire. Il contient un mélange d’épices, d’aromates et d’ingrédients végétaux sélectionnés pour parfumer la cuisson. Il apporte du goût sans avoir à doser ni à mélanger : on retire le sachet et on sert. | 6b155792-f1b1-4c7a-bb3c-b50d65db86f0 | TEXT | - | 19 | d40a7af7-8923-4666-a029-1df965f4424e | isHidden=true |
| 214 | <b>Option A</b><br>Une préparation végétale à ajouter directement dans l’eau de cuisson de votre riz, de vos féculents/graines ou de vos légumineuses. Elle contient un mélange d’épices, d’aromates, de légumes, de graines ou de superaliments. Elle cuit avec la base et se mange avec le plat. On la dose à la cuillerée. | c75eff6b-1061-4f18-9a79-1ef0bb288fce | TEXT | - | 19 | 6b155792-f1b1-4c7a-bb3c-b50d65db86f0 | isHidden=true |
| 215 | <b>Option B</b><br>Une préparation végétale à ajouter directement dans l’eau de cuisson de votre riz, de vos féculents/graines ou de vos légumineuses. Elle contient un mélange d’épices, d’aromates, de légumes, de graines ou de superaliments. Elle cuit avec la base et se mange avec le plat. On la dose à la cuillerée. | df4b24d0-76be-40c8-8395-1a7a455d5115 | TEXT | - | 19 | c75eff6b-1061-4f18-9a79-1ef0bb288fce | isHidden=true |
| 216 | <b>Option B</b><br>Un sachet à déposer dans l’eau de cuisson de votre riz, de vos féculents/graines ou de vos légumineuses, puis à retirer en fin de cuisson — comme une infusion culinaire. Il contient un mélange d’épices, d’aromates et d’ingrédients végétaux sélectionnés pour parfumer la cuisson. Il apporte du goût sans avoir à doser ni à mélanger : on retire le sachet et on sert. | d7ce898e-658b-4f98-bf1a-701e34ea6df0 | TEXT | - | 19 | df4b24d0-76be-40c8-8395-1a7a455d5115 | isHidden=true |
| 217 | Écran 19 – Acceptabilité des ingrédients | c6263e0c-be59-41f1-8832-1365573203ed | PAGE_BREAK | - | 20 | d7ce898e-658b-4f98-bf1a-701e34ea6df0 | - |
| 218 | Dans ce type de produit culinaire, la présence de certains ingrédients vous semblerait-elle acceptable ? | 77732a33-969c-4195-95fa-42b04699a893 | TITLE | df7325ce-8757-4c79-bb88-9c0df92154d4 | 20 | c6263e0c-be59-41f1-8832-1365573203ed | - |
| 219 | - | e057826f-f054-40e4-8942-8de7898360b2 | MATRIX | df7325ce-8757-4c79-bb88-9c0df92154d4 | 20 | 77732a33-969c-4195-95fa-42b04699a893 | randomizeRows=false |
| 220 | Oui, cela me paraît intéressant | 9358ca0d-4c20-4e1e-9bc1-66ef6fbf39fa | MATRIX_COLUMN | df7325ce-8757-4c79-bb88-9c0df92154d4 | 20 | e057826f-f054-40e4-8942-8de7898360b2 | randomizeRows=false |
| 221 | Pourquoi pas | ca27e584-e049-4f80-8d9d-2adb02845b3c | MATRIX_COLUMN | df7325ce-8757-4c79-bb88-9c0df92154d4 | 20 | 9358ca0d-4c20-4e1e-9bc1-66ef6fbf39fa | randomizeRows=false |
| 222 | Cela me surprend, mais je pourrais essayer | d20f1225-ce49-439a-8e6f-b07875e66d91 | MATRIX_COLUMN | df7325ce-8757-4c79-bb88-9c0df92154d4 | 20 | ca27e584-e049-4f80-8d9d-2adb02845b3c | randomizeRows=false |
| 223 | Cela me paraît étrange | c4b3d1b8-f960-4a8e-91e6-efc1f3a96bdc | MATRIX_COLUMN | df7325ce-8757-4c79-bb88-9c0df92154d4 | 20 | d20f1225-ce49-439a-8e6f-b07875e66d91 | randomizeRows=false |
| 224 | Non, cela ne me donne pas envie | 675ab135-0a78-47eb-819a-913c628969f6 | MATRIX_COLUMN | df7325ce-8757-4c79-bb88-9c0df92154d4 | 20 | c4b3d1b8-f960-4a8e-91e6-efc1f3a96bdc | randomizeRows=false |
| 225 | Je ne sais pas | 73e02fbf-b75a-4496-99a7-0b70ca4a1a72 | MATRIX_COLUMN | df7325ce-8757-4c79-bb88-9c0df92154d4 | 20 | 675ab135-0a78-47eb-819a-913c628969f6 | randomizeRows=false |
| 226 | Algues | 1acd88ff-4171-495e-80c7-f1512239f855 | MATRIX_ROW | df7325ce-8757-4c79-bb88-9c0df92154d4 | 20 | 73e02fbf-b75a-4496-99a7-0b70ca4a1a72 | randomizeRows=false |
| 227 | Légumes séchés | 5820f429-077e-4dfd-bc30-be0afac53755 | MATRIX_ROW | df7325ce-8757-4c79-bb88-9c0df92154d4 | 20 | 1acd88ff-4171-495e-80c7-f1512239f855 | randomizeRows=false |
| 228 | Légumes lyophilisés | e47ca057-e534-4c0d-beba-bda7d2207e81 | MATRIX_ROW | df7325ce-8757-4c79-bb88-9c0df92154d4 | 20 | 5820f429-077e-4dfd-bc30-be0afac53755 | randomizeRows=false |
| 229 | Écran 20 – Compréhension / inspiration ouverte | 4880a929-dd3d-466f-bc5a-da62b02d4ceb | PAGE_BREAK | - | 21 | e47ca057-e534-4c0d-beba-bda7d2207e81 | - |
| 230 | En une phrase, qu’est-ce que ce produit et son utilisation vous inspirent ? | 3f644466-ce55-4b83-98d4-7f290b372046 | TITLE | 3e9978d4-8d14-4d0a-ba49-1bf2814bd2ed | 21 | 4880a929-dd3d-466f-bc5a-da62b02d4ceb | - |
| 231 | - | e142edea-969b-47bd-b353-237347919753 | TEXTAREA | 3e9978d4-8d14-4d0a-ba49-1bf2814bd2ed | 21 | 3f644466-ce55-4b83-98d4-7f290b372046 | - |
| 232 | Écran 21 – Clarté | 340f693b-e0cf-49c9-8f14-b42c2af2746b | PAGE_BREAK | - | 22 | e142edea-969b-47bd-b353-237347919753 | - |
| 233 | Les deux options vous paraissent-elles faciles à comprendre ? | e464a9b2-921c-40c2-8293-318cddea1e78 | TITLE | 459d8453-8572-48c4-b370-518ee1d3f296 | 22 | 340f693b-e0cf-49c9-8f14-b42c2af2746b | - |
| 234 | - | 6dbb334c-82f8-4eb1-9bee-12936b0868a2 | LINEAR_SCALE | 459d8453-8572-48c4-b370-518ee1d3f296 | 22 | e464a9b2-921c-40c2-8293-318cddea1e78 | start=1, end=5, leftLabel="Pas du tout claires", rightLabel="Très claires" |
| 235 | Écran 22 – Nouveauté | 15cac7d1-71f3-40c8-838e-e9a7080d2039 | PAGE_BREAK | - | 23 | 6dbb334c-82f8-4eb1-9bee-12936b0868a2 | - |
| 236 | Ce produit vous paraît-il nouveau ou différent de ce qui existe ? | 8bcd5889-3dec-433d-bcf7-b920bd549459 | TITLE | ba3dca6c-b72e-4886-ba24-721de6280331 | 23 | 15cac7d1-71f3-40c8-838e-e9a7080d2039 | - |
| 237 | - | ef944a7a-d16d-48f6-9d42-bb8de65b9e37 | LINEAR_SCALE | ba3dca6c-b72e-4886-ba24-721de6280331 | 23 | 8bcd5889-3dec-433d-bcf7-b920bd549459 | start=1, end=5, leftLabel="Déjà vu", rightLabel="Très nouveau" |
| 238 | Écran 23 – Catégorie ouverte | 7ddb0e0a-201d-4849-9c1a-02e46a054aa2 | PAGE_BREAK | - | 24 | ef944a7a-d16d-48f6-9d42-bb8de65b9e37 | - |
| 239 | À quelle catégorie de produit cela vous fait-il penser ? | fa77593b-492a-4b92-a08e-141cf9e109e0 | TITLE | 25363464-c659-4624-8393-2f3f9ab38cba | 24 | 7ddb0e0a-201d-4849-9c1a-02e46a054aa2 | - |
| 240 | - | fc68d42b-06e4-47f9-b2ef-841b14b1d9ff | TEXTAREA | 25363464-c659-4624-8393-2f3f9ab38cba | 24 | fa77593b-492a-4b92-a08e-141cf9e109e0 | - |
| 241 | Écran 24 – Perception catégorie fermée | 8a36d774-90b8-4c46-8231-4c2f95c42bc1 | PAGE_BREAK | - | 25 | fc68d42b-06e4-47f9-b2ef-841b14b1d9ff | - |
| 242 | Si vous deviez le ranger dans un rayon ou une famille de produits, où le mettriez-vous plutôt ? | 93d216f5-7ce3-4a27-8137-434f1be95c6a | TITLE | b47a7d09-b3d8-4238-a6b7-353990f98f33 | 25 | 8a36d774-90b8-4c46-8231-4c2f95c42bc1 | - |
| 243 | Épices / assaisonnements | 2f41081a-2a57-4736-b46f-2bd1d5167935 | MULTIPLE_CHOICE_OPTION | b47a7d09-b3d8-4238-a6b7-353990f98f33 | 25 | 93d216f5-7ce3-4a27-8137-434f1be95c6a | hasOtherOption=true |
| 244 | Bouillons / aides culinaires | 03fda77c-e307-40cb-8df0-d42acc45b8f2 | MULTIPLE_CHOICE_OPTION | b47a7d09-b3d8-4238-a6b7-353990f98f33 | 25 | 2f41081a-2a57-4736-b46f-2bd1d5167935 | hasOtherOption=true |
| 245 | Condiments | 1ae0e226-7909-494e-a396-189f78198147 | MULTIPLE_CHOICE_OPTION | b47a7d09-b3d8-4238-a6b7-353990f98f33 | 25 | 03fda77c-e307-40cb-8df0-d42acc45b8f2 | hasOtherOption=true |
| 246 | Produit culinaire innovant | 1239a4f6-dd15-4bbb-b048-c62e247ae3ec | MULTIPLE_CHOICE_OPTION | b47a7d09-b3d8-4238-a6b7-353990f98f33 | 25 | 1ae0e226-7909-494e-a396-189f78198147 | hasOtherOption=true |
| 247 | Produit nutritionnel | caf922e2-96a4-4e64-854b-f7bd836af785 | MULTIPLE_CHOICE_OPTION | b47a7d09-b3d8-4238-a6b7-353990f98f33 | 25 | 1239a4f6-dd15-4bbb-b048-c62e247ae3ec | hasOtherOption=true |
| 248 | Complément alimentaire | 9329b5b3-da29-4767-b60e-0221e2df52d7 | MULTIPLE_CHOICE_OPTION | b47a7d09-b3d8-4238-a6b7-353990f98f33 | 25 | caf922e2-96a4-4e64-854b-f7bd836af785 | hasOtherOption=true |
| 249 | Je ne saurais pas où le ranger | 163b9c94-0da5-4505-85ab-d1ba15fdb54d | MULTIPLE_CHOICE_OPTION | b47a7d09-b3d8-4238-a6b7-353990f98f33 | 25 | 9329b5b3-da29-4767-b60e-0221e2df52d7 | hasOtherOption=true |
| 250 | Autre | 78292572-000f-465e-8f04-d122df81448a | MULTIPLE_CHOICE_OPTION | b47a7d09-b3d8-4238-a6b7-353990f98f33 | 25 | 163b9c94-0da5-4505-85ab-d1ba15fdb54d | hasOtherOption=true, isOtherOption=true |
| 251 | Écran 25 – Préférence concept | 9671d940-c8c6-48fe-949b-8cd17a8317b5 | PAGE_BREAK | - | 26 | 78292572-000f-465e-8f04-d122df81448a | - |
| 252 | Si vous deviez n’en garder qu’une, quelle option vous parle le plus ? | 091ece95-e4ba-4110-b810-11e20ed4f1f1 | TITLE | 8011f8d3-a30b-485a-b529-0723ac3ae7f1 | 26 | 9671d940-c8c6-48fe-949b-8cd17a8317b5 | - |
| 253 | Option A | 25407749-8d31-4c04-be73-9a7db52919dd | MULTIPLE_CHOICE_OPTION | 8011f8d3-a30b-485a-b529-0723ac3ae7f1 | 26 | 091ece95-e4ba-4110-b810-11e20ed4f1f1 | - |
| 254 | Option B | 6c5058e4-3f34-4ecb-9fed-62a2bc0ed6d0 | MULTIPLE_CHOICE_OPTION | 8011f8d3-a30b-485a-b529-0723ac3ae7f1 | 26 | 25407749-8d31-4c04-be73-9a7db52919dd | - |
| 255 | Les deux | 42b5c896-c08a-4566-a65e-67f42f44a5a2 | MULTIPLE_CHOICE_OPTION | 8011f8d3-a30b-485a-b529-0723ac3ae7f1 | 26 | 6c5058e4-3f34-4ecb-9fed-62a2bc0ed6d0 | - |
| 256 | Aucune | 0df57214-b88e-44f2-8b43-05f64e25104a | MULTIPLE_CHOICE_OPTION | 8011f8d3-a30b-485a-b529-0723ac3ae7f1 | 26 | 42b5c896-c08a-4566-a65e-67f42f44a5a2 | - |
| 257 | Écran 26 – Raison du choix | e75f88cd-e783-435b-af03-48a758c1b82b | PAGE_BREAK | - | 27 | 0df57214-b88e-44f2-8b43-05f64e25104a | - |
| 258 | Pourquoi ce choix ? | b0609321-2eb1-4ef9-932a-d37952071344 | TITLE | 37e32f51-b4d2-4b7a-a3ba-d3fc22167385 | 27 | e75f88cd-e783-435b-af03-48a758c1b82b | - |
| 259 | - | 35c5b5f7-efa1-4c1f-b972-ad2434b31e5d | TEXTAREA | 37e32f51-b4d2-4b7a-a3ba-d3fc22167385 | 27 | b0609321-2eb1-4ef9-932a-d37952071344 | isRequired=false |
| 260 | Écran 27 – Intention d’essai | 7e0b50ea-085d-4ade-93e9-e09e6813cd39 | PAGE_BREAK | - | 28 | 35c5b5f7-efa1-4c1f-b972-ad2434b31e5d | - |
| 261 | Quelle serait la probabilité que vous essayiez ce type de produit au moins une fois ? | 56490ccf-780c-4569-aa3d-e2975d68d476 | TITLE | bfe2f724-ce34-4d36-ad6b-2ce7d2073e9b | 28 | 7e0b50ea-085d-4ade-93e9-e09e6813cd39 | - |
| 262 | - | 5885561f-6376-464e-b6f3-3343d612a7eb | LINEAR_SCALE | bfe2f724-ce34-4d36-ad6b-2ce7d2073e9b | 28 | 56490ccf-780c-4569-aa3d-e2975d68d476 | start=1, leftLabel="Très faible", centerLabel="Pourquoi pas", rightLabel="Très forte" |
| 263 | Écran 28 – Objections | 9481194d-4d36-4e1d-87c8-5149476a669a | PAGE_BREAK | - | 29 | 5885561f-6376-464e-b6f3-3343d612a7eb | - |
| 264 | Qu’est-ce qui vous ferait le plus hésiter à essayer ? | 8f3dd9c4-a5a4-48d1-b4b5-ac9ff4c68653 | TITLE | f231b030-8df9-4c9b-a251-33fd018382e4 | 29 | 9481194d-4d36-4e1d-87c8-5149476a669a | - |
| 265 | Le prix | 1fcebb2d-1805-44fc-96db-fbd58ef0f37a | CHECKBOX | f231b030-8df9-4c9b-a251-33fd018382e4 | 29 | 8f3dd9c4-a5a4-48d1-b4b5-ac9ff4c68653 | hasOtherOption=true |
| 266 | Un doute sur l’utilité | e09a4e27-c0db-4662-b129-791ea29a92df | CHECKBOX | f231b030-8df9-4c9b-a251-33fd018382e4 | 29 | 1fcebb2d-1805-44fc-96db-fbd58ef0f37a | hasOtherOption=true |
| 267 | Trop proche d’un complément | 72d82182-fd97-47e5-92b2-06b7e2f14214 | CHECKBOX | f231b030-8df9-4c9b-a251-33fd018382e4 | 29 | e09a4e27-c0db-4662-b129-791ea29a92df | hasOtherOption=true |
| 268 | Un goût inconnu | 9e3b2a35-48dc-4bdb-8031-15a535da4d6e | CHECKBOX | f231b030-8df9-4c9b-a251-33fd018382e4 | 29 | 72d82182-fd97-47e5-92b2-06b7e2f14214 | hasOtherOption=true |
| 269 | Un geste trop compliqué | 2526c965-fde8-4a66-81fe-b962b5063b98 | CHECKBOX | f231b030-8df9-4c9b-a251-33fd018382e4 | 29 | 9e3b2a35-48dc-4bdb-8031-15a535da4d6e | hasOtherOption=true |
| 270 | Une composition qui ne me parle pas | 3b2777c5-7b07-483f-ad8b-136223ad0d10 | CHECKBOX | f231b030-8df9-4c9b-a251-33fd018382e4 | 29 | 2526c965-fde8-4a66-81fe-b962b5063b98 | hasOtherOption=true |
| 271 | Le fait de l’ajouter pendant la cuisson | 2bca467e-f30f-49db-9417-1bd76da983c9 | CHECKBOX | f231b030-8df9-4c9b-a251-33fd018382e4 | 29 | 3b2777c5-7b07-483f-ad8b-136223ad0d10 | hasOtherOption=true |
| 272 | Rien | bd3d3966-ac05-4c1c-b380-c45fec3562de | CHECKBOX | f231b030-8df9-4c9b-a251-33fd018382e4 | 29 | 2bca467e-f30f-49db-9417-1bd76da983c9 | hasOtherOption=true |
| 273 | Autre | 3bd51b90-6bf0-44f5-8572-29c7e0a26c3b | CHECKBOX | f231b030-8df9-4c9b-a251-33fd018382e4 | 29 | bd3d3966-ac05-4c1c-b380-c45fec3562de | hasOtherOption=true, isOtherOption=true |
| 274 | Écran 29 – Prix Van Westendorp | 63385f19-d069-48da-bfda-48a73cad5186 | PAGE_BREAK | - | 30 | 3bd51b90-6bf0-44f5-8572-29c7e0a26c3b | - |
| 275 | Ce produit se présenterait sous forme d’un pot d’environ 200 g, soit environ 12 à 16 utilisations. Indiquez les prix qui vous semblent justes selon vous. | eb599f33-91c5-4458-b13e-06fdb2bc5432 | TEXT | - | 30 | 63385f19-d069-48da-bfda-48a73cad5186 | - |
| 276 | À quel prix ce pot vous semblerait-il trop cher pour que vous l’achetiez ? | 1698e84b-4f5d-4645-9141-f0ab82fb782d | TITLE | dea95eef-ece5-4c1b-a260-8add7e45436e | 30 | eb599f33-91c5-4458-b13e-06fdb2bc5432 | - |
| 277 | - | 00f787bb-d5ad-4cbb-9909-51a1fcf92850 | INPUT_NUMBER | dea95eef-ece5-4c1b-a260-8add7e45436e | 30 | 1698e84b-4f5d-4645-9141-f0ab82fb782d | suffix=" €", format="CUSTOM" |
| 278 | À quel prix le trouveriez-vous cher, mais encore envisageable ? | 8cc2fe7f-5d00-46a6-bc14-57f7de6ebdf9 | TITLE | 42422c1b-73d0-4eaa-a53c-91aab3e5b540 | 30 | 00f787bb-d5ad-4cbb-9909-51a1fcf92850 | - |
| 279 | - | a560d592-9b0d-499d-b834-d4a51d963782 | INPUT_NUMBER | 42422c1b-73d0-4eaa-a53c-91aab3e5b540 | 30 | 8cc2fe7f-5d00-46a6-bc14-57f7de6ebdf9 | suffix=" €", format="CUSTOM" |
| 280 | À quel prix le trouveriez-vous bon marché, une bonne affaire ? | 399b337e-26b1-4967-92a3-5e926d5254d6 | TITLE | 3048c45d-c572-459b-8856-4b949765a0ba | 30 | a560d592-9b0d-499d-b834-d4a51d963782 | - |
| 281 | - | 1d27f63a-b07e-4151-8a4f-4539a155d6a2 | INPUT_NUMBER | 3048c45d-c572-459b-8856-4b949765a0ba | 30 | 399b337e-26b1-4967-92a3-5e926d5254d6 | suffix=" €", format="CUSTOM" |
| 282 | À quel prix vous diriez-vous qu’il est si peu cher que vous douteriez de sa qualité ? | 0c07cbac-0e55-4192-8cb3-e5131d4a9e13 | TITLE | f4678b29-d937-4838-9534-a0aab5ba00ed | 30 | 1d27f63a-b07e-4151-8a4f-4539a155d6a2 | - |
| 283 | - | 3ec15c5b-2182-4e82-96fa-a0357fc7a250 | INPUT_NUMBER | f4678b29-d937-4838-9534-a0aab5ba00ed | 30 | 0c07cbac-0e55-4192-8cb3-e5131d4a9e13 | suffix=" €", format="CUSTOM" |
| 284 | Écran 30 – Acceptabilité du prix 24,90 € | 6eac2ea6-ddfc-45b0-87fa-34c08577f667 | PAGE_BREAK | - | 31 | 3ec15c5b-2182-4e82-96fa-a0357fc7a250 | - |
| 285 | À titre indicatif, imaginons un pot de 200 g, contenant environ 12 à 16 utilisations, avec une composition à base d’épices, d’aromates et d’ingrédients végétaux sélectionnés. | 5af07aa5-21b1-4c36-a7af-2ba4e33e85f9 | TEXT | - | 31 | 6eac2ea6-ddfc-45b0-87fa-34c08577f667 | - |
| 286 | À 24,90 €, ce produit vous semblerait… | 1c08a971-e74d-4d6c-8edd-563369ab69cf | TITLE | 8dff0597-a12c-48c0-a7c3-d3260b73d330 | 31 | 5af07aa5-21b1-4c36-a7af-2ba4e33e85f9 | - |
| 287 | Beaucoup trop cher | e43a958a-6aff-4f2d-9520-28773c570e8f | MULTIPLE_CHOICE_OPTION | 8dff0597-a12c-48c0-a7c3-d3260b73d330 | 31 | 1c08a971-e74d-4d6c-8edd-563369ab69cf | - |
| 288 | Plutôt cher | e682dd3b-fef3-4663-a65d-b14243c81c5f | MULTIPLE_CHOICE_OPTION | 8dff0597-a12c-48c0-a7c3-d3260b73d330 | 31 | e43a958a-6aff-4f2d-9520-28773c570e8f | - |
| 289 | Acceptable si la qualité et le goût sont au rendez-vous | b5ff0c43-4e3e-49ee-ab1b-ced451ab3d51 | MULTIPLE_CHOICE_OPTION | 8dff0597-a12c-48c0-a7c3-d3260b73d330 | 31 | e682dd3b-fef3-4663-a65d-b14243c81c5f | - |
| 290 | Bon rapport qualité/prix | d5dedc8f-776c-4bf4-b060-f4cc22728356 | MULTIPLE_CHOICE_OPTION | 8dff0597-a12c-48c0-a7c3-d3260b73d330 | 31 | b5ff0c43-4e3e-49ee-ab1b-ced451ab3d51 | - |
| 291 | Je ne sais pas | 8693095a-be2d-4855-8a46-238133a939ce | MULTIPLE_CHOICE_OPTION | 8dff0597-a12c-48c0-a7c3-d3260b73d330 | 31 | d5dedc8f-776c-4bf4-b060-f4cc22728356 | - |
| 292 | Qu’est-ce qui pourrait rendre ce prix acceptable pour vous ? | 451f22a8-cc0e-4cba-af19-6b955020cb83 | TITLE | 0cdaf7d6-1adf-41fa-b79e-e0a3ab9a2103 | 31 | 8693095a-be2d-4855-8a46-238133a939ce | - |
| 293 | Un goût vraiment différent | 8256aa8f-9c11-4854-bd83-c8ef3285daa0 | CHECKBOX | 0cdaf7d6-1adf-41fa-b79e-e0a3ab9a2103 | 31 | 451f22a8-cc0e-4cba-af19-6b955020cb83 | hasOtherOption=true |
| 294 | Une composition claire | fe1a723e-c186-4d82-bb46-58812e6484c9 | CHECKBOX | 0cdaf7d6-1adf-41fa-b79e-e0a3ab9a2103 | 31 | 8256aa8f-9c11-4854-bd83-c8ef3285daa0 | hasOtherOption=true |
| 295 | Des ingrédients de qualité | adb91cf7-929d-45ef-a895-b3472fdc5931 | CHECKBOX | 0cdaf7d6-1adf-41fa-b79e-e0a3ab9a2103 | 31 | fe1a723e-c186-4d82-bb46-58812e6484c9 | hasOtherOption=true |
| 296 | Un usage simple | 691f525f-923e-423b-ac35-42fd56f443df | CHECKBOX | 0cdaf7d6-1adf-41fa-b79e-e0a3ab9a2103 | 31 | adb91cf7-929d-45ef-a895-b3472fdc5931 | hasOtherOption=true |
| 297 | Plusieurs utilisations par pot | acf4d65a-45e2-4177-924f-2265c7041af3 | CHECKBOX | 0cdaf7d6-1adf-41fa-b79e-e0a3ab9a2103 | 31 | 691f525f-923e-423b-ac35-42fd56f443df | hasOtherOption=true |
| 298 | Une fabrication française ou locale | c39174d8-2251-4cee-99ab-f835d454fa80 | CHECKBOX | 0cdaf7d6-1adf-41fa-b79e-e0a3ab9a2103 | 31 | acf4d65a-45e2-4177-924f-2265c7041af3 | hasOtherOption=true |
| 299 | Une preuve concrète de l’intérêt du produit | ba249eda-e6aa-4057-a286-aad1ce03d016 | CHECKBOX | 0cdaf7d6-1adf-41fa-b79e-e0a3ab9a2103 | 31 | c39174d8-2251-4cee-99ab-f835d454fa80 | hasOtherOption=true |
| 300 | Rien, ce prix me semble trop élevé | c18134b2-519d-4752-8c87-2a2d2d13f270 | CHECKBOX | 0cdaf7d6-1adf-41fa-b79e-e0a3ab9a2103 | 31 | ba249eda-e6aa-4057-a286-aad1ce03d016 | hasOtherOption=true |
| 301 | Autre | 301e7b6b-23c2-44eb-875f-759eff7c43fa | CHECKBOX | 0cdaf7d6-1adf-41fa-b79e-e0a3ab9a2103 | 31 | c18134b2-519d-4752-8c87-2a2d2d13f270 | hasOtherOption=true, isOtherOption=true |
| 302 | Écran 31 – Focus fonctionnel prudent | fc8fd93b-ac5d-45bd-be66-ec004b7fac8b | PAGE_BREAK | - | 32 | 301e7b6b-23c2-44eb-875f-759eff7c43fa | - |
| 303 | Dans ce type de produit, la présence d’ingrédients végétaux comme des légumes séchés, graines, algues ou superaliments vous paraît-elle… | a036bf10-e684-4589-a1b8-be55666089f6 | TITLE | 52259084-79ae-4402-84b7-0bdc7c2351b0 | 32 | fc8fd93b-ac5d-45bd-be66-ec004b7fac8b | - |
| 304 | Très intéressante | a79eda8f-9c94-4cd2-ba57-1ebda134c72c | MULTIPLE_CHOICE_OPTION | 52259084-79ae-4402-84b7-0bdc7c2351b0 | 32 | a036bf10-e684-4589-a1b8-be55666089f6 | - |
| 305 | Plutôt intéressante | ce6e8019-89e0-4e40-a407-3c10742445b8 | MULTIPLE_CHOICE_OPTION | 52259084-79ae-4402-84b7-0bdc7c2351b0 | 32 | a79eda8f-9c94-4cd2-ba57-1ebda134c72c | - |
| 306 | Peu importante | 941f6ec3-f502-44a0-87b6-50283f00f450 | MULTIPLE_CHOICE_OPTION | 52259084-79ae-4402-84b7-0bdc7c2351b0 | 32 | ce6e8019-89e0-4e40-a407-3c10742445b8 | - |
| 307 | Pas importante | de12436e-194f-4876-a805-7c4d51206f22 | MULTIPLE_CHOICE_OPTION | 52259084-79ae-4402-84b7-0bdc7c2351b0 | 32 | 941f6ec3-f502-44a0-87b6-50283f00f450 | - |
| 308 | Cela me rend méfiant(e) | c9952d21-4828-4061-a3d6-3a9a7b47f802 | MULTIPLE_CHOICE_OPTION | 52259084-79ae-4402-84b7-0bdc7c2351b0 | 32 | de12436e-194f-4876-a805-7c4d51206f22 | - |
| 309 | Je ne sais pas | dedb7998-bba8-43ae-a01a-963e372df9d1 | MULTIPLE_CHOICE_OPTION | 52259084-79ae-4402-84b7-0bdc7c2351b0 | 32 | c9952d21-4828-4061-a3d6-3a9a7b47f802 | - |
| 310 | Écran 32 – Recontact | 7529d9bf-05ef-4af8-9adb-ce4114b30494 | PAGE_BREAK | - | 33 | dedb7998-bba8-43ae-a01a-963e372df9d1 | - |
| 311 | Puis-je conserver votre contact pour vous adresser des questions personnalisées ou vous proposer un futur test produit ? | d010cc1f-5030-4e5d-aa87-a6ce2d077aeb | TITLE | 9e5361d1-1024-435f-af8a-24e52b066ddf | 33 | 7529d9bf-05ef-4af8-9adb-ce4114b30494 | - |
| 312 | Oui | 65ca8eab-3fe8-4d2b-979a-792f7589a866 | MULTIPLE_CHOICE_OPTION | 9e5361d1-1024-435f-af8a-24e52b066ddf | 33 | d010cc1f-5030-4e5d-aa87-a6ce2d077aeb | - |
| 313 | Non | 5f951d6c-ac18-4566-98dd-accb5d5e7242 | MULTIPLE_CHOICE_OPTION | 9e5361d1-1024-435f-af8a-24e52b066ddf | 33 | 65ca8eab-3fe8-4d2b-979a-792f7589a866 | - |
| 314 | - | 644b7fe8-e1eb-4d19-aaa4-7ad120f97f16 | CONDITIONAL_LOGIC | - | 33 | 5f951d6c-ac18-4566-98dd-accb5d5e7242 | see `## Logic rules` below |
| 315 | Écran 33 – Email conditionnel | 4af51a48-6f56-4296-9e3b-6511d35aec70 | PAGE_BREAK | - | 34 | 644b7fe8-e1eb-4d19-aaa4-7ad120f97f16 | - |
| 316 | Votre email servira uniquement à vous recontacter au sujet de cette enquête ou d’un futur test produit. Il sera conservé séparément de vos réponses. | b17c3453-9714-4b1c-b72a-a4fe59e91f07 | TEXT | - | 34 | 4af51a48-6f56-4296-9e3b-6511d35aec70 | - |
| 317 | Votre email | 780403b4-19ad-486d-8496-fbd77965361f | TITLE | 2c1c1bef-e3e3-4654-b1b0-aaad2efea876 | 34 | b17c3453-9714-4b1c-b72a-a4fe59e91f07 | - |
| 318 | - | 4d7a80f8-b0fd-42f5-990c-f6878effd45f | INPUT_EMAIL | 2c1c1bef-e3e3-4654-b1b0-aaad2efea876 | 34 | 780403b4-19ad-486d-8496-fbd77965361f | - |
| 319 | Écran 34 – Remerciement | b24da3d3-2f74-4449-91a2-9d7cfb7349fc | PAGE_BREAK | - | 35 | 4d7a80f8-b0fd-42f5-990c-f6878effd45f | isThankYouPage=true, isQualifiedForThankYouPage=true |
| 320 | Merci — vos réponses sont enregistrées. Elles vont directement aider à mieux comprendre les usages culinaires du quotidien. | bed59f66-5a56-4fe2-b36c-bbfb8dfec1fe | TEXT | - | 35 | b24da3d3-2f74-4449-91a2-9d7cfb7349fc | - |
| 321 | Disqualification | c99483a6-2d0b-44f9-98ca-2e795ee59466 | PAGE_BREAK | - | 36 | bed59f66-5a56-4fe2-b36c-bbfb8dfec1fe | isThankYouPage=true, isQualifiedForThankYouPage=true |
| 322 | Merci de votre intérêt. Cette enquête cible les personnes qui cuisinent au moins occasionnellement — vos réponses ne sont pas requises cette fois-ci. | ce72e814-fa42-4661-abed-faf8f1de9ffa | TEXT | - | 36 | c99483a6-2d0b-44f9-98ca-2e795ee59466 | - |

## Logic rules

| logicRule_blockUuid | when | then |
| - | - | - |
| 36a59911-e71f-4210-aff2-62bcd1810698 | 88ffdb41-c3c0-4c85-9b52-848a7956c043 IS f5db52af-2052-4a9c-8234-d4c11ded23c8 AND 8982344d-db02-40d0-98f3-aee4bf6e1676 IS "v2" | CALCULATE 61ae70d8-bcf2-465c-b6f1-2bca6c2a6992 = "v2" |
| 6fc41bfd-7bf7-4f46-af9d-7ffdffd8b3d6 | 88ffdb41-c3c0-4c85-9b52-848a7956c043 IS f5db52af-2052-4a9c-8234-d4c11ded23c8 AND 61ae70d8-bcf2-465c-b6f1-2bca6c2a6992 IS "v1" | SHOW 6b155792-f1b1-4c7a-bb3c-b50d65db86f0 |
| fece5c35-c2b3-4b0c-a3b0-549457d9dec2 | 88ffdb41-c3c0-4c85-9b52-848a7956c043 IS f5db52af-2052-4a9c-8234-d4c11ded23c8 AND 61ae70d8-bcf2-465c-b6f1-2bca6c2a6992 IS "v1" | SHOW df4b24d0-76be-40c8-8395-1a7a455d5115 |
| d8442457-3204-4398-a3a7-e63e7b90c31a | 88ffdb41-c3c0-4c85-9b52-848a7956c043 IS f5db52af-2052-4a9c-8234-d4c11ded23c8 AND 61ae70d8-bcf2-465c-b6f1-2bca6c2a6992 IS "v1" | HIDE c75eff6b-1061-4f18-9a79-1ef0bb288fce |
| 957a307e-dedd-4330-a8af-ccc8c9b89ee6 | 88ffdb41-c3c0-4c85-9b52-848a7956c043 IS f5db52af-2052-4a9c-8234-d4c11ded23c8 AND 61ae70d8-bcf2-465c-b6f1-2bca6c2a6992 IS "v1" | HIDE d7ce898e-658b-4f98-bf1a-701e34ea6df0 |
| fba2bb57-b5b3-4f5b-91aa-0fa48e075221 | 88ffdb41-c3c0-4c85-9b52-848a7956c043 IS f5db52af-2052-4a9c-8234-d4c11ded23c8 AND 61ae70d8-bcf2-465c-b6f1-2bca6c2a6992 IS "v2" | SHOW c75eff6b-1061-4f18-9a79-1ef0bb288fce |
| 8b91f018-7dca-4dd6-aae4-5514b56ae109 | 88ffdb41-c3c0-4c85-9b52-848a7956c043 IS f5db52af-2052-4a9c-8234-d4c11ded23c8 AND 61ae70d8-bcf2-465c-b6f1-2bca6c2a6992 IS "v2" | SHOW d7ce898e-658b-4f98-bf1a-701e34ea6df0 |
| ae219951-ec90-4826-ba13-fb6a78985ad4 | 402ddfe0-16b1-444c-90d5-ddf107d7b953 IS 04871e70-32bc-41de-8ac2-68612a007213 | JUMP TO PAGE 36 |
| acb9d5b8-6b05-4775-85dc-799d72390e01 | 7687e6a9-ccf3-42f8-a09c-8de77ef2691d IS ANY OF (e3dc9dca-9013-41c6-a314-c767c690fe09, 89f69d8e-4e44-480a-96f3-12d81bec01a9, c800612b-f320-40b0-878d-3a561dee56ed, 0f9ac342-cbfa-435e-b11d-1fe680caac15, dfface76-ef4d-4242-922d-c231c2b181e7, 66f39f0c-9e06-425d-9321-1c5f9779e4a0, e1bfe67e-8a8a-4ef2-81f3-e9c3ce388484, e385e94a-daaa-472b-baca-81b1fb837581, 837b060f-4984-403b-b9d6-2dab497a6f3b, 65f78c9e-4ea9-431c-b0fc-de4cdf01f5aa, 68f0273c-1b09-4466-baec-52227ed18deb, bf1efb0e-a5c6-4c77-b294-7ddfd4b646df, 7d29d1f9-fc11-46b1-ac0d-ed6d19a85965) | SHOW 32f34299-01e3-441c-bfec-854759960489 |
| cb7b432b-52c0-49fb-bda0-529c7569fb41 | 7687e6a9-ccf3-42f8-a09c-8de77ef2691d IS NOT ANY OF (e3dc9dca-9013-41c6-a314-c767c690fe09, 89f69d8e-4e44-480a-96f3-12d81bec01a9, c800612b-f320-40b0-878d-3a561dee56ed, 0f9ac342-cbfa-435e-b11d-1fe680caac15, dfface76-ef4d-4242-922d-c231c2b181e7, 66f39f0c-9e06-425d-9321-1c5f9779e4a0, e1bfe67e-8a8a-4ef2-81f3-e9c3ce388484, e385e94a-daaa-472b-baca-81b1fb837581, 837b060f-4984-403b-b9d6-2dab497a6f3b, 65f78c9e-4ea9-431c-b0fc-de4cdf01f5aa, 68f0273c-1b09-4466-baec-52227ed18deb, bf1efb0e-a5c6-4c77-b294-7ddfd4b646df, 7d29d1f9-fc11-46b1-ac0d-ed6d19a85965) | HIDE 32f34299-01e3-441c-bfec-854759960489 |
| d51ba6c6-3c96-4497-a276-350534b8be90 | febb43cf-f222-44f6-8915-4db1471c89b6 IS NOT ANY OF (cf4840b6-02ae-4bb4-9da4-be2792a38d31, 4cf01dd1-2527-4577-9a4c-01467c6fc47b) AND f474a6de-bdf2-44bd-9c80-70c26bcef806 IS NOT ANY OF (b47649fd-36ae-41d8-97a1-ece5d1f8ef39, bedd2006-16c8-40d8-8d01-d25449b35f94) AND 173f1791-b375-4d7a-878b-00c7bd14fd61 IS NOT ANY OF (2cdb6b52-5444-4ff7-a49c-5fde54721feb, 9315e5f4-376d-4f78-9224-fc262af2b42a) AND 7687e6a9-ccf3-42f8-a09c-8de77ef2691d IS NOT ANY OF (89f69d8e-4e44-480a-96f3-12d81bec01a9, c800612b-f320-40b0-878d-3a561dee56ed) | JUMP TO PAGE 12 |
| 602e98d5-8ad6-4353-a43b-bf3b228de21c | d5427ab2-e6e5-43a6-9bc1-97101f9d430a IS dbc856e9-1ad9-4f91-9990-c402aef787e4 | SHOW 64ed3c17-6a59-44f1-914d-18d051579ceb |
| be8fbeb9-7020-4d7c-a361-f28da136a649 | d5427ab2-e6e5-43a6-9bc1-97101f9d430a IS NOT dbc856e9-1ad9-4f91-9990-c402aef787e4 | HIDE 64ed3c17-6a59-44f1-914d-18d051579ceb |
| 644b7fe8-e1eb-4d19-aaa4-7ad120f97f16 | 9e5361d1-1024-435f-af8a-24e52b066ddf IS 5f951d6c-ac18-4566-98dd-accb5d5e7242 | JUMP TO PAGE 35 |

## Page flow

Page 1 -> Page 2 -> Page 3 -> Page 4 -> Page 5 -> Page 6 -> Page 7 -> Page 8 -> Page 9 -> Page 10 -> Page 11 -> Page 12 -> Page 13 -> Page 14 -> Page 15 -> Page 16 -> Page 17 -> Page 18 -> Page 19 -> Page 20 -> Page 21 -> Page 22 -> Page 23 -> Page 24 -> Page 25 -> Page 26 -> Page 27 -> Page 28 -> Page 29 -> Page 30 -> Page 31 -> Page 32 -> Page 33 -> Page 34 -> Page 35 (Thank You) -> Page 36 (Thank You)
  - Rule: Page 3 may jump to Page 36 (Thank You)
  - Rule: Page 9 may jump to Page 12
  - Rule: Page 33 may jump to Page 35 (Thank You)
