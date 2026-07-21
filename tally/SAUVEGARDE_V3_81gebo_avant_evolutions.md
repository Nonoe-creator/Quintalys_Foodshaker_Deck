# Form ledger

## Blocks

| # | text/html | blockUuid | type | questionUuid | page | insertAfterBlockUuid_BEFORE | properties |
| - | - | - | - | - | - | - | - |
| 1 | KORIUM — Questionnaire quantitatif V3 pilote | 49dcf54b-3019-4282-ae7a-b84dbc0190ee | FORM_TITLE | - | 1 | - | button={"label":"Continuer"} |
| 2 | - | 015a4e84-26e0-4f0d-9c72-8263dbfc9b57 | CALCULATED_FIELDS | 2937c066-b043-47da-8f53-e2ec558e426f | 1 | 49dcf54b-3019-4282-ae7a-b84dbc0190ee | 0f6debe2-fc6c-4a48-9492-394832aa0066=concept_order_final(TEXT,value="v1"), f8498a80-213c-4d04-9afa-86a519c6552e=cooking_path(TEXT,value="regular_cooking") |
| 3 | - | 9cd0ed9a-3455-4e65-a6e9-4ef663ee6c40 | HIDDEN_FIELDS | e557a03a-8ced-4d5d-a2a5-d02551bb2d79 | 1 | 015a4e84-26e0-4f0d-9c72-8263dbfc9b57 | 2d63fb1a-05b3-440e-aef3-a69ecbea1d18=source, 064f9493-cc20-41ae-9ef2-4f174375c911=canal, 30d8cd81-5b98-4ef2-9451-936fc77cf884=version_questionnaire, 285cfee7-4eb0-4935-ac3d-43e4701d18f3=concept_order |
| 4 | Cette enquête s’adresse à des personnes majeures et vise à mieux comprendre des habitudes de cuisine, les usages autour des bases alimentaires et les réactions à de nouvelles idées de produits culinaires. Les réponses sont analysées de façon anonyme. La participation est facultative et vous pouvez quitter le questionnaire à tout moment. | 828bb741-7002-4d5e-bccb-a81d604a6be4 | TEXT | - | 1 | 9cd0ed9a-3455-4e65-a6e9-4ef663ee6c40 | - |
| 5 | J’ai pris connaissance de ces informations. | ba217e22-70f4-4c80-af5f-994b82a9e6ba | TITLE | 9f6e6906-86da-45eb-b58d-06d698683735 | 1 | 828bb741-7002-4d5e-bccb-a81d604a6be4 | - |
| 6 | Je participe | 8f2cdf95-e30a-4d0a-a4de-6852c4af32fe | MULTIPLE_CHOICE_OPTION | 9f6e6906-86da-45eb-b58d-06d698683735 | 1 | ba217e22-70f4-4c80-af5f-994b82a9e6ba | - |
| 7 | - | 8dfbf196-9971-4c55-8fda-c102b018b49b | CONDITIONAL_LOGIC | - | 1 | 8f2cdf95-e30a-4d0a-a4de-6852c4af32fe | see `## Logic rules` below |
| 8 | - | 5c94b2e0-0c75-4b71-bd36-94214189f46b | CONDITIONAL_LOGIC | - | 1 | 8dfbf196-9971-4c55-8fda-c102b018b49b | see `## Logic rules` below |
| 9 | - | 7970afaf-d6ee-4921-80ba-161a02fa4281 | CONDITIONAL_LOGIC | - | 1 | 5c94b2e0-0c75-4b71-bd36-94214189f46b | see `## Logic rules` below |
| 10 | - | a1cecc9d-0904-4f0e-892e-e4aece266dda | CONDITIONAL_LOGIC | - | 1 | 7970afaf-d6ee-4921-80ba-161a02fa4281 | see `## Logic rules` below |
| 11 | - | 5870d415-0933-443b-9476-8884ccb1e85c | CONDITIONAL_LOGIC | - | 1 | a1cecc9d-0904-4f0e-892e-e4aece266dda | see `## Logic rules` below |
| 12 | Si vous acceptez d’être recontacté(e) en fin de questionnaire, votre email sera utilisé uniquement à cette fin et ne sera pas utilisé à des fins commerciales sans votre accord. | a694dfa2-f8b3-48a7-a27f-d28d1675a0fd | TEXT | - | 1 | 5870d415-0933-443b-9476-8884ccb1e85c | - |
| 13 | É2 – Profil | 93392df0-a9c9-43bc-8ca0-d49cb7cc30c2 | PAGE_BREAK | - | 2 | a694dfa2-f8b3-48a7-a27f-d28d1675a0fd | - |
| 14 | Composition de votre foyer | aed9209d-566f-4ba6-9d29-5743aa82d15a | TITLE | 40f82127-93ab-4bdc-a233-dcd9690beeba | 2 | 93392df0-a9c9-43bc-8ca0-d49cb7cc30c2 | - |
| 15 | Seul(e) | db5b7648-8c3b-4ede-9b7a-7f35fb08760b | MULTIPLE_CHOICE_OPTION | 40f82127-93ab-4bdc-a233-dcd9690beeba | 2 | aed9209d-566f-4ba6-9d29-5743aa82d15a | hasOtherOption=true |
| 16 | Couple | 857bae66-3dcd-44c9-9ba5-4b728c08501a | MULTIPLE_CHOICE_OPTION | 40f82127-93ab-4bdc-a233-dcd9690beeba | 2 | db5b7648-8c3b-4ede-9b7a-7f35fb08760b | hasOtherOption=true |
| 17 | Famille avec enfants | f01d3a4e-3656-4db0-ab45-a321d5ee30e0 | MULTIPLE_CHOICE_OPTION | 40f82127-93ab-4bdc-a233-dcd9690beeba | 2 | 857bae66-3dcd-44c9-9ba5-4b728c08501a | hasOtherOption=true |
| 18 | Colocation | e5c7fd24-9842-4755-b0f8-e467fcb8fdda | MULTIPLE_CHOICE_OPTION | 40f82127-93ab-4bdc-a233-dcd9690beeba | 2 | f01d3a4e-3656-4db0-ab45-a321d5ee30e0 | hasOtherOption=true |
| 19 | Autre | a20403fb-04cf-4af7-b199-a9e40a7afda3 | MULTIPLE_CHOICE_OPTION | 40f82127-93ab-4bdc-a233-dcd9690beeba | 2 | e5c7fd24-9842-4755-b0f8-e467fcb8fdda | hasOtherOption=true, isOtherOption=true |
| 20 | Votre tranche d’âge | 38ef2d3f-3eba-4075-bc12-5755e72addf6 | TITLE | 3691e1c3-daf1-4ed4-9378-e158a691b24b | 2 | a20403fb-04cf-4af7-b199-a9e40a7afda3 | - |
| 21 | 18–24 | 7e646f62-a818-4d07-b08a-182eb08b708a | MULTIPLE_CHOICE_OPTION | 3691e1c3-daf1-4ed4-9378-e158a691b24b | 2 | 38ef2d3f-3eba-4075-bc12-5755e72addf6 | - |
| 22 | 25–34 | 6061e08f-dec0-403a-b9d6-fd81b629b641 | MULTIPLE_CHOICE_OPTION | 3691e1c3-daf1-4ed4-9378-e158a691b24b | 2 | 7e646f62-a818-4d07-b08a-182eb08b708a | - |
| 23 | 35–44 | fcdafdc4-9d56-4293-98fb-4f4ec5c55732 | MULTIPLE_CHOICE_OPTION | 3691e1c3-daf1-4ed4-9378-e158a691b24b | 2 | 6061e08f-dec0-403a-b9d6-fd81b629b641 | - |
| 24 | 45–54 | 907aca00-d9a3-4821-a4db-e8cd707d8733 | MULTIPLE_CHOICE_OPTION | 3691e1c3-daf1-4ed4-9378-e158a691b24b | 2 | fcdafdc4-9d56-4293-98fb-4f4ec5c55732 | - |
| 25 | 55–64 | 3e091cc5-65dd-4b0c-bd66-9a8f49791c43 | MULTIPLE_CHOICE_OPTION | 3691e1c3-daf1-4ed4-9378-e158a691b24b | 2 | 907aca00-d9a3-4821-a4db-e8cd707d8733 | - |
| 26 | 65+ | 60ef6e0d-3b97-4426-aef7-76795f2bb361 | MULTIPLE_CHOICE_OPTION | 3691e1c3-daf1-4ed4-9378-e158a691b24b | 2 | 3e091cc5-65dd-4b0c-bd66-9a8f49791c43 | - |
| 27 | É3 – Rapport à la cuisine | 352a4d12-d3d2-489e-8609-43be8a1d449e | PAGE_BREAK | - | 3 | 60ef6e0d-3b97-4426-aef7-76795f2bb361 | - |
| 28 | Pour vous, cuisiner au quotidien est plutôt… | 63bf2f6a-21b5-4ed8-95e4-8bff1e4f6534 | TITLE | 919572f3-ab17-43e5-88b9-973826014a5f | 3 | 352a4d12-d3d2-489e-8609-43be8a1d449e | - |
| 29 | - | 3a5c3789-e44d-4842-a227-d535400e0ab6 | LINEAR_SCALE | 919572f3-ab17-43e5-88b9-973826014a5f | 3 | 63bf2f6a-21b5-4ed8-95e4-8bff1e4f6534 | start=1, end=5, leftLabel="Une corvée", rightLabel="Un plaisir" |
| 30 | À quelle fréquence cuisinez-vous vous-même un repas ? | 64b396e5-22a1-4166-af60-d675a2096267 | TITLE | 56528099-3033-433f-8bd4-124cf4d0f82a | 3 | 3a5c3789-e44d-4842-a227-d535400e0ab6 | - |
| 31 | Jamais | 8d84b4b8-1974-4b57-9582-5541572bb971 | MULTIPLE_CHOICE_OPTION | 56528099-3033-433f-8bd4-124cf4d0f82a | 3 | 64b396e5-22a1-4166-af60-d675a2096267 | - |
| 32 | 1–2 fois par semaine | 98755dcd-3ec6-4217-8546-b78fb42065fb | MULTIPLE_CHOICE_OPTION | 56528099-3033-433f-8bd4-124cf4d0f82a | 3 | 8d84b4b8-1974-4b57-9582-5541572bb971 | - |
| 33 | 3–4 fois par semaine | 8384f0e0-cdc7-4d97-8205-c26077c7e03e | MULTIPLE_CHOICE_OPTION | 56528099-3033-433f-8bd4-124cf4d0f82a | 3 | 98755dcd-3ec6-4217-8546-b78fb42065fb | - |
| 34 | 5 fois ou plus par semaine | 5fca5e61-b631-49bd-8c39-326d200dd2bb | MULTIPLE_CHOICE_OPTION | 56528099-3033-433f-8bd4-124cf4d0f82a | 3 | 8384f0e0-cdc7-4d97-8205-c26077c7e03e | - |
| 35 | - | 93302922-917c-4371-a158-fa313f9951f1 | CONDITIONAL_LOGIC | - | 3 | 5fca5e61-b631-49bd-8c39-326d200dd2bb | see `## Logic rules` below |
| 36 | - | b3729b35-8495-4532-ba6f-8ca0d09782fc | CONDITIONAL_LOGIC | - | 3 | 93302922-917c-4371-a158-fa313f9951f1 | see `## Logic rules` below |
| 37 | - | c8338ccb-e5a4-4807-871c-55949071fbb8 | CONDITIONAL_LOGIC | - | 3 | b3729b35-8495-4532-ba6f-8ca0d09782fc | see `## Logic rules` below |
| 38 | - | 2757ca71-3e00-47e5-97bc-b5c748e612ae | CONDITIONAL_LOGIC | - | 3 | c8338ccb-e5a4-4807-871c-55949071fbb8 | see `## Logic rules` below |
| 39 | É4 – Bases cuisinées | 249e4ae7-5354-4352-8e49-3191d302bd0d | PAGE_BREAK | - | 4 | 2757ca71-3e00-47e5-97bc-b5c748e612ae | - |
| 40 | Parmi ces bases, lesquelles cuisinez-vous au moins occasionnellement ? | 1c79afaf-15a4-4f32-a9cf-e08fbabe75a5 | TITLE | 98cc417e-10e7-483d-9751-79050d7c4a2b | 4 | 249e4ae7-5354-4352-8e49-3191d302bd0d | - |
| 41 | Riz | 709867b7-4f68-4738-9776-8c1bb906e614 | CHECKBOX | 98cc417e-10e7-483d-9751-79050d7c4a2b | 4 | 1c79afaf-15a4-4f32-a9cf-e08fbabe75a5 | hasOtherOption=true |
| 42 | Légumineuses : lentilles, pois chiches, haricots, pois cassés… | 55494128-1086-404d-8482-3f5bad3d8d92 | CHECKBOX | 98cc417e-10e7-483d-9751-79050d7c4a2b | 4 | 709867b7-4f68-4738-9776-8c1bb906e614 | hasOtherOption=true |
| 43 | Pâtes, semoule, boulgour, quinoa ou autres céréales | 581ae6af-2582-4723-82ab-5953323eb06f | CHECKBOX | 98cc417e-10e7-483d-9751-79050d7c4a2b | 4 | 55494128-1086-404d-8482-3f5bad3d8d92 | hasOtherOption=true |
| 44 | Pommes de terre ou autres féculents | 94119472-2d3a-4e73-8d4e-d1a9a828ace7 | CHECKBOX | 98cc417e-10e7-483d-9751-79050d7c4a2b | 4 | 581ae6af-2582-4723-82ab-5953323eb06f | hasOtherOption=true |
| 45 | Je cuisine rarement ces types de bases | cb00d7a8-6d1c-4c34-956c-d25a19d756ad | CHECKBOX | 98cc417e-10e7-483d-9751-79050d7c4a2b | 4 | 94119472-2d3a-4e73-8d4e-d1a9a828ace7 | hasOtherOption=true |
| 46 | Autre | 170c235b-8ff5-4ed7-90e8-aa69d24d480d | CHECKBOX | 98cc417e-10e7-483d-9751-79050d7c4a2b | 4 | cb00d7a8-6d1c-4c34-956c-d25a19d756ad | hasOtherOption=true, isOtherOption=true |
| 47 | - | f24344ea-0a25-468a-b072-15f82ea61fbf | CONDITIONAL_LOGIC | - | 4 | 170c235b-8ff5-4ed7-90e8-aa69d24d480d | see `## Logic rules` below |
| 48 | Parmi ces bases, laquelle cuisinez-vous le plus souvent ? | 2f8fd1b6-a304-4015-9e7d-2de77cee80d6 | TITLE | bc43430c-e159-4caf-8a9c-f837aa531f36 | 4 | f24344ea-0a25-468a-b072-15f82ea61fbf | - |
| 49 | Riz | 06f64fc9-79a6-4905-ac5a-4ef2ff74901e | MULTIPLE_CHOICE_OPTION | bc43430c-e159-4caf-8a9c-f837aa531f36 | 4 | 2f8fd1b6-a304-4015-9e7d-2de77cee80d6 | - |
| 50 | Légumineuses | e9d1c890-646d-4412-a20f-56e057f03664 | MULTIPLE_CHOICE_OPTION | bc43430c-e159-4caf-8a9c-f837aa531f36 | 4 | 06f64fc9-79a6-4905-ac5a-4ef2ff74901e | - |
| 51 | Pâtes, semoule, boulgour, quinoa ou autres céréales | 6079a957-374b-49b1-9160-6becb0f2f8f4 | MULTIPLE_CHOICE_OPTION | bc43430c-e159-4caf-8a9c-f837aa531f36 | 4 | e9d1c890-646d-4412-a20f-56e057f03664 | - |
| 52 | Pommes de terre ou autres féculents | 53c26203-122f-4c07-95ae-402cd80a9333 | MULTIPLE_CHOICE_OPTION | bc43430c-e159-4caf-8a9c-f837aa531f36 | 4 | 6079a957-374b-49b1-9160-6becb0f2f8f4 | - |
| 53 | Cela varie vraiment selon les semaines | f72e2539-e38b-4dc7-816c-91a67d75672f | MULTIPLE_CHOICE_OPTION | bc43430c-e159-4caf-8a9c-f837aa531f36 | 4 | 53c26203-122f-4c07-95ae-402cd80a9333 | - |
| 54 | É5 – Ajouts pendant la cuisson | 53ce4723-8147-4927-a9bc-5e075122c92a | PAGE_BREAK | - | 5 | f72e2539-e38b-4dc7-816c-91a67d75672f | - |
| 55 | Pendant la cuisson de vos bases (riz, légumineuses, pâtes, céréales…), ajoutez-vous généralement quelque chose à l’eau ou à la base ? | 4c26451b-accc-497f-8d7f-6de3787ffe0d | TITLE | afa753a4-232a-4128-a04b-a31c0a4f1985 | 5 | 53ce4723-8147-4927-a9bc-5e075122c92a | - |
| 56 | Rien | 670186c9-c917-4e1c-ad7a-8b044ae8ba11 | CHECKBOX | afa753a4-232a-4128-a04b-a31c0a4f1985 | 5 | 4c26451b-accc-497f-8d7f-6de3787ffe0d | hasOtherOption=true |
| 57 | Sel | 2a7897a2-413b-4868-8e72-99066e526c9c | CHECKBOX | afa753a4-232a-4128-a04b-a31c0a4f1985 | 5 | 670186c9-c917-4e1c-ad7a-8b044ae8ba11 | hasOtherOption=true |
| 58 | Bouillon-cube | 00b9e60c-64d6-4dff-9406-40bb132be255 | CHECKBOX | afa753a4-232a-4128-a04b-a31c0a4f1985 | 5 | 2a7897a2-413b-4868-8e72-99066e526c9c | hasOtherOption=true |
| 59 | Épices | f16abbcb-0412-4295-92ab-6e3905cdfad2 | CHECKBOX | afa753a4-232a-4128-a04b-a31c0a4f1985 | 5 | 00b9e60c-64d6-4dff-9406-40bb132be255 | hasOtherOption=true |
| 60 | Herbes ou aromates (frais ou secs) | 7806910c-6f38-45b7-8b79-6a4fedd3ce1d | CHECKBOX | afa753a4-232a-4128-a04b-a31c0a4f1985 | 5 | f16abbcb-0412-4295-92ab-6e3905cdfad2 | hasOtherOption=true |
| 61 | Ail, oignon ou échalote | f03edc28-13db-4b12-833d-5cc23a81f89f | CHECKBOX | afa753a4-232a-4128-a04b-a31c0a4f1985 | 5 | 7806910c-6f38-45b7-8b79-6a4fedd3ce1d | hasOtherOption=true |
| 62 | Huile ou beurre | 7c31acef-f6a1-4484-84c4-df3c1ab1a043 | CHECKBOX | afa753a4-232a-4128-a04b-a31c0a4f1985 | 5 | f03edc28-13db-4b12-833d-5cc23a81f89f | hasOtherOption=true |
| 63 | Lait de coco | fb4e776e-5d62-4918-930d-b73d6dce0a1f | CHECKBOX | afa753a4-232a-4128-a04b-a31c0a4f1985 | 5 | 7c31acef-f6a1-4484-84c4-df3c1ab1a043 | hasOtherOption=true |
| 64 | Tomate ou concentré | 9f7ed104-e947-4a21-a2be-78edcd93c139 | CHECKBOX | afa753a4-232a-4128-a04b-a31c0a4f1985 | 5 | fb4e776e-5d62-4918-930d-b73d6dce0a1f | hasOtherOption=true |
| 65 | Légumes | 10b97dbe-e3d5-4480-a50e-0cb149dddfcd | CHECKBOX | afa753a4-232a-4128-a04b-a31c0a4f1985 | 5 | 9f7ed104-e947-4a21-a2be-78edcd93c139 | hasOtherOption=true |
| 66 | Citron ou vinaigre | c491b400-5f7a-4448-8448-c68294620f77 | CHECKBOX | afa753a4-232a-4128-a04b-a31c0a4f1985 | 5 | 10b97dbe-e3d5-4480-a50e-0cb149dddfcd | hasOtherOption=true |
| 67 | Autre | c82246b7-f296-4504-aba6-750d2398ad77 | CHECKBOX | afa753a4-232a-4128-a04b-a31c0a4f1985 | 5 | c491b400-5f7a-4448-8448-c68294620f77 | hasOtherOption=true, isOtherOption=true |
| 68 | É6 – Ajouts après la cuisson | a7fca26d-0514-4653-929f-5e3468f177f8 | PAGE_BREAK | - | 6 | c82246b7-f296-4504-aba6-750d2398ad77 | - |
| 69 | Et après la cuisson, ajoutez-vous quelque chose pour donner plus de goût ou d’intérêt à vos bases ? | c61d2c09-1dcc-403c-83cd-0c7ccc2cd927 | TITLE | e6caf72e-b6e8-40f4-9811-64c76fc045fa | 6 | a7fca26d-0514-4653-929f-5e3468f177f8 | - |
| 70 | Rien | d38983da-7c0c-4ace-b271-c3ca59b8f6b1 | CHECKBOX | e6caf72e-b6e8-40f4-9811-64c76fc045fa | 6 | c61d2c09-1dcc-403c-83cd-0c7ccc2cd927 | hasOtherOption=true |
| 71 | Sel, poivre | 23be8470-6e61-483e-961a-2bdcb4056d5f | CHECKBOX | e6caf72e-b6e8-40f4-9811-64c76fc045fa | 6 | d38983da-7c0c-4ace-b271-c3ca59b8f6b1 | hasOtherOption=true |
| 72 | Épices | 2a8fe28b-9cb1-402c-905b-4ffd356e6fbe | CHECKBOX | e6caf72e-b6e8-40f4-9811-64c76fc045fa | 6 | 23be8470-6e61-483e-961a-2bdcb4056d5f | hasOtherOption=true |
| 73 | Herbes fraîches | 70c0c9a6-42b0-489c-a04f-24792d15f737 | CHECKBOX | e6caf72e-b6e8-40f4-9811-64c76fc045fa | 6 | 2a8fe28b-9cb1-402c-905b-4ffd356e6fbe | hasOtherOption=true |
| 74 | Huile ou beurre | 761f8868-8b92-45e0-90d4-a0128959e97c | CHECKBOX | e6caf72e-b6e8-40f4-9811-64c76fc045fa | 6 | 70c0c9a6-42b0-489c-a04f-24792d15f737 | hasOtherOption=true |
| 75 | Citron ou vinaigre | 32ff8437-8dee-445a-beae-294fb4256463 | CHECKBOX | e6caf72e-b6e8-40f4-9811-64c76fc045fa | 6 | 761f8868-8b92-45e0-90d4-a0128959e97c | hasOtherOption=true |
| 76 | Levure maltée | 79753fa0-30e0-4361-a1a5-3f18fe73b61e | CHECKBOX | e6caf72e-b6e8-40f4-9811-64c76fc045fa | 6 | 32ff8437-8dee-445a-beae-294fb4256463 | hasOtherOption=true |
| 77 | Graines ou oléagineux | 513e85c4-fca6-4ae6-abe9-37220a9d21c1 | CHECKBOX | e6caf72e-b6e8-40f4-9811-64c76fc045fa | 6 | 79753fa0-30e0-4361-a1a5-3f18fe73b61e | hasOtherOption=true |
| 78 | Fromage râpé | dc30535c-cb9b-4c6d-acdd-178ede30aeee | CHECKBOX | e6caf72e-b6e8-40f4-9811-64c76fc045fa | 6 | 513e85c4-fca6-4ae6-abe9-37220a9d21c1 | hasOtherOption=true |
| 79 | Condiments ou sauces | e1fbe4d6-1b90-4055-9698-6f660086c56a | CHECKBOX | e6caf72e-b6e8-40f4-9811-64c76fc045fa | 6 | dc30535c-cb9b-4c6d-acdd-178ede30aeee | hasOtherOption=true |
| 80 | Autre | f2319c54-6bfd-44a4-ac14-3d85389925a2 | CHECKBOX | e6caf72e-b6e8-40f4-9811-64c76fc045fa | 6 | e1fbe4d6-1b90-4055-9698-6f660086c56a | hasOtherOption=true, isOtherOption=true |
| 81 | É7 – Solutions actuelles | 4e12803d-23bf-45ac-827a-b784e24f70e4 | PAGE_BREAK | - | 7 | f2319c54-6bfd-44a4-ac14-3d85389925a2 | - |
| 82 | Êtes-vous satisfait(e) des solutions actuelles pour donner du goût à vos bases ? | 033d01a0-0cbf-490c-85e3-a01e6e558c8f | TITLE | 676c7d78-cce2-44a0-94d1-e718dfde986f | 7 | 4e12803d-23bf-45ac-827a-b784e24f70e4 | - |
| 83 | - | 07470717-a1a4-43f3-b2e9-c450de842505 | LINEAR_SCALE | 676c7d78-cce2-44a0-94d1-e718dfde986f | 7 | 033d01a0-0cbf-490c-85e3-a01e6e558c8f | start=1, end=5, leftLabel="Pas du tout satisfait(e)", rightLabel="Très satisfait(e)" |
| 84 | Qu’est-ce qui vous gêne le plus dans les bouillons ou condiments actuels ? | 51433fb8-691a-425c-a1fa-e7dbb7b88312 | TITLE | d7639c23-2196-426b-8c5d-fbc21e60bc97 | 7 | 07470717-a1a4-43f3-b2e9-c450de842505 | - |
| 85 | Trop salés | 02c2002d-51ef-43ce-a52f-e1bdf649a1dd | CHECKBOX | d7639c23-2196-426b-8c5d-fbc21e60bc97 | 7 | 51433fb8-691a-425c-a1fa-e7dbb7b88312 | hasOtherOption=true |
| 86 | Additifs | 4b8752e5-e970-4d8d-bc1d-eb797dac26b9 | CHECKBOX | d7639c23-2196-426b-8c5d-fbc21e60bc97 | 7 | 02c2002d-51ef-43ce-a52f-e1bdf649a1dd | hasOtherOption=true |
| 87 | Exhausteurs de goût | 05596661-fa17-4249-83a4-351a9a476dbf | CHECKBOX | d7639c23-2196-426b-8c5d-fbc21e60bc97 | 7 | 4b8752e5-e970-4d8d-bc1d-eb797dac26b9 | hasOtherOption=true |
| 88 | Goût redondant | 6c9dd929-a7bd-4b04-8d52-e2d4d8dd467d | CHECKBOX | d7639c23-2196-426b-8c5d-fbc21e60bc97 | 7 | 05596661-fa17-4249-83a4-351a9a476dbf | hasOtherOption=true |
| 89 | Composition peu claire | 55711616-8f70-4de6-b0c1-809983003ba9 | CHECKBOX | d7639c23-2196-426b-8c5d-fbc21e60bc97 | 7 | 6c9dd929-a7bd-4b04-8d52-e2d4d8dd467d | hasOtherOption=true |
| 90 | Certains ingrédients ne correspondent pas à mes contraintes ou préférences alimentaires | 43b6d1e1-f732-4192-90e6-2b25335eef6a | CHECKBOX | d7639c23-2196-426b-8c5d-fbc21e60bc97 | 7 | 55711616-8f70-4de6-b0c1-809983003ba9 | hasOtherOption=true |
| 91 | Rien ne me gêne | 1161b24d-79f3-4a5f-a69a-f06e8bed7cbd | CHECKBOX | d7639c23-2196-426b-8c5d-fbc21e60bc97 | 7 | 43b6d1e1-f732-4192-90e6-2b25335eef6a | hasOtherOption=true |
| 92 | Autre | 8ce7b54c-ddc7-44e1-b1e6-ec293118acde | CHECKBOX | d7639c23-2196-426b-8c5d-fbc21e60bc97 | 7 | 1161b24d-79f3-4a5f-a69a-f06e8bed7cbd | hasOtherOption=true, isOtherOption=true |
| 93 | Lorsque vous cuisinez une base simple, êtes-vous disposé(e) à modifier légèrement votre façon de faire pour un résultat qui vous convient davantage ? | 48a4afa0-8653-430c-8f39-04aa987e8585 | TITLE | 428b17ff-5272-46d1-90df-c85dfad57528 | 7 | 8ce7b54c-ddc7-44e1-b1e6-ec293118acde | - |
| 94 | - | 5c4e1dce-901b-483c-ace6-ba627575ea6f | LINEAR_SCALE | 428b17ff-5272-46d1-90df-c85dfad57528 | 7 | 48a4afa0-8653-430c-8f39-04aa987e8585 | start=1, end=5, leftLabel="Pas du tout", rightLabel="Tout à fait" |
| 95 | É8 – Votre manière d’améliorer vos repas | da04d29d-130e-42eb-a6f7-1442722f3794 | PAGE_BREAK | - | 8 | 5c4e1dce-901b-483c-ace6-ba627575ea6f | - |
| 96 | Dans quelle mesure cherchez-vous à améliorer la qualité de vos repas au quotidien ? | d52a5c66-df63-4120-9847-57b4306c78fb | TITLE | a3b3ca4d-ef17-4091-94f9-01c3874abe67 | 8 | da04d29d-130e-42eb-a6f7-1442722f3794 | - |
| 97 | - | b617e648-1a84-490a-9e88-696f9ee83944 | LINEAR_SCALE | a3b3ca4d-ef17-4091-94f9-01c3874abe67 | 8 | d52a5c66-df63-4120-9847-57b4306c78fb | start=1, end=5, leftLabel="Très peu", rightLabel="Beaucoup" |
| 98 | Quand vous voulez améliorer un plat simple, savez-vous généralement quoi ajouter et comment l’utiliser ? | fb99b3fc-441e-4dc9-a4f0-edc887f9fc0e | TITLE | e747c92a-65d1-4313-b73a-e3c7211fdb1f | 8 | b617e648-1a84-490a-9e88-696f9ee83944 | - |
| 99 | - | 21a25000-3461-4317-be4b-cad0a53893a5 | LINEAR_SCALE | e747c92a-65d1-4313-b73a-e3c7211fdb1f | 8 | fb99b3fc-441e-4dc9-a4f0-edc887f9fc0e | start=1, end=5, leftLabel="Pas du tout", rightLabel="Tout à fait" |
| 100 | Pour améliorer une base simple, quel geste supplémentaire accepteriez-vous le plus facilement ? | 488f67f7-edce-4452-8adb-f693468bb159 | TITLE | 67281037-0a4b-4037-902d-0a814dd7a695 | 8 | 21a25000-3461-4317-be4b-cad0a53893a5 | - |
| 101 | Aucun geste supplémentaire | 34201c02-2409-4eed-ab3f-41862ddde267 | MULTIPLE_CHOICE_OPTION | 67281037-0a4b-4037-902d-0a814dd7a695 | 8 | 488f67f7-edce-4452-8adb-f693468bb159 | - |
| 102 | Ajouter un format déjà pré-dosé | 0fd74eae-2b40-4a62-88c9-b01bce78e169 | MULTIPLE_CHOICE_OPTION | 67281037-0a4b-4037-902d-0a814dd7a695 | 8 | 34201c02-2409-4eed-ab3f-41862ddde267 | - |
| 103 | Ajouter une cuillère d’un produit | bf213726-1b0f-4493-b5ff-57762110e8a1 | MULTIPLE_CHOICE_OPTION | 67281037-0a4b-4037-902d-0a814dd7a695 | 8 | 0fd74eae-2b40-4a62-88c9-b01bce78e169 | - |
| 104 | Suivre une instruction très courte | e9f950f6-11fa-414e-9626-d9b372521cb8 | MULTIPLE_CHOICE_OPTION | 67281037-0a4b-4037-902d-0a814dd7a695 | 8 | bf213726-1b0f-4493-b5ff-57762110e8a1 | - |
| 105 | Adapter légèrement ma façon de cuire | 76acd414-7b1d-41f6-acf7-4e53fb41162a | MULTIPLE_CHOICE_OPTION | 67281037-0a4b-4037-902d-0a814dd7a695 | 8 | e9f950f6-11fa-414e-9626-d9b372521cb8 | - |
| 106 | Cela dépend du résultat attendu | 4dde2e50-cf31-4deb-9d60-326a05ff81ff | MULTIPLE_CHOICE_OPTION | 67281037-0a4b-4037-902d-0a814dd7a695 | 8 | 76acd414-7b1d-41f6-acf7-4e53fb41162a | - |
| 107 | Les jours où vous manquez de temps, que faites-vous le plus souvent pour les repas ? | 979bc3ac-0c2c-4db8-b27f-90b1b288da95 | TITLE | ce0f7375-9773-4d3a-9b1e-20e226009bef | 8 | 4dde2e50-cf31-4deb-9d60-326a05ff81ff | - |
| 108 | Je cuisine quand même quelque chose de rapide | 389c122b-d2ba-4f32-adaa-7b9d7749b657 | MULTIPLE_CHOICE_OPTION | ce0f7375-9773-4d3a-9b1e-20e226009bef | 8 | 979bc3ac-0c2c-4db8-b27f-90b1b288da95 | - |
| 109 | J’improvise avec ce que j’ai | 78946078-44e3-42d2-b436-d9c987dd9903 | MULTIPLE_CHOICE_OPTION | ce0f7375-9773-4d3a-9b1e-20e226009bef | 8 | 389c122b-d2ba-4f32-adaa-7b9d7749b657 | - |
| 110 | Je choisis un plat préparé ou prêt à l’emploi | c43c2b66-6628-457a-9116-58309c1d7347 | MULTIPLE_CHOICE_OPTION | ce0f7375-9773-4d3a-9b1e-20e226009bef | 8 | 78946078-44e3-42d2-b436-d9c987dd9903 | - |
| 111 | Je commande ou prends à emporter | 538180e3-3f3c-428e-a324-691b41447bcb | MULTIPLE_CHOICE_OPTION | ce0f7375-9773-4d3a-9b1e-20e226009bef | 8 | c43c2b66-6628-457a-9116-58309c1d7347 | - |
| 112 | Je simplifie fortement ou je saute le repas | bd6f36e7-edbe-4c20-86f0-73d69330cc9f | MULTIPLE_CHOICE_OPTION | ce0f7375-9773-4d3a-9b1e-20e226009bef | 8 | 538180e3-3f3c-428e-a324-691b41447bcb | - |
| 113 | Je ne manque pas réellement de temps pour les repas | 7ae494ea-ae51-4439-ba0b-dea654a11bcf | MULTIPLE_CHOICE_OPTION | ce0f7375-9773-4d3a-9b1e-20e226009bef | 8 | bd6f36e7-edbe-4c20-86f0-73d69330cc9f | - |
| 114 | É9 – Présentation du concept | 4dd42485-a1cb-47b6-98f5-e9baec528cac | PAGE_BREAK | - | 9 | 7ae494ea-ae51-4439-ba0b-dea654a11bcf | - |
| 115 | Nous étudions deux façons d’utiliser pendant la cuisson une même préparation culinaire composée d’épices, d’aromates et d’autres ingrédients végétaux. Les deux options se distinguent par leur mode d’utilisation et par ce qui reste dans le plat. Prenez le temps de lire les deux — il n’y a pas de bonne réponse. | f0a7c7af-4d3c-4734-a536-ea0bd956a04b | TEXT | - | 9 | 4dd42485-a1cb-47b6-98f5-e9baec528cac | - |
| 116 | <b>Option A</b><br>Cette préparation est placée dans l’eau de cuisson sous forme de sachet.<br>Elle est ajoutée au début ou pendant la cuisson.<br>Les ingrédients restent dans le sachet, qui est retiré avant de servir.<br>Le format est pré-dosé : on ajoute le sachet, on le laisse agir pendant la cuisson, puis on le retire.<br>La préparation agit pendant la cuisson, mais la matière contenue dans le sachet n’est pas consommée et ne reste pas visible dans l’assiette. | 0b2ba077-c403-4b8d-820d-c64467cf86c5 | TEXT | - | 9 | f0a7c7af-4d3c-4734-a536-ea0bd956a04b | isHidden=true |
| 117 | <b>Option A</b><br>Cette préparation est ajoutée directement dans l’eau de cuisson.<br>Elle est ajoutée au début ou pendant la cuisson.<br>Les ingrédients cuisent avec la base et restent intégrés dans le plat au moment de servir.<br>Le format se dose selon les indications : on ajoute la quantité recommandée, on mélange et on laisse cuire.<br>La matière contenue dans la préparation est consommée avec le repas et peut rester visible dans l’assiette. | ed849ce0-9f87-4711-a52c-6b007a0eae9f | TEXT | - | 9 | 0b2ba077-c403-4b8d-820d-c64467cf86c5 | isHidden=true |
| 118 | <b>Option B</b><br>Cette préparation est ajoutée directement dans l’eau de cuisson.<br>Elle est ajoutée au début ou pendant la cuisson.<br>Les ingrédients cuisent avec la base et restent intégrés dans le plat au moment de servir.<br>Le format se dose selon les indications : on ajoute la quantité recommandée, on mélange et on laisse cuire.<br>La matière contenue dans la préparation est consommée avec le repas et peut rester visible dans l’assiette. | d3cfe418-4c63-497d-a318-39efb76d8c1b | TEXT | - | 9 | ed849ce0-9f87-4711-a52c-6b007a0eae9f | isHidden=true |
| 119 | <b>Option B</b><br>Cette préparation est placée dans l’eau de cuisson sous forme de sachet.<br>Elle est ajoutée au début ou pendant la cuisson.<br>Les ingrédients restent dans le sachet, qui est retiré avant de servir.<br>Le format est pré-dosé : on ajoute le sachet, on le laisse agir pendant la cuisson, puis on le retire.<br>La préparation agit pendant la cuisson, mais la matière contenue dans le sachet n’est pas consommée et ne reste pas visible dans l’assiette. | 654cca42-9548-4849-8143-ad2194eaf3bd | TEXT | - | 9 | d3cfe418-4c63-497d-a318-39efb76d8c1b | isHidden=true |
| 120 | É10 – Compréhension | 3914e8a8-1ad1-4e1b-852e-d7193ac6576f | PAGE_BREAK | - | 10 | 654cca42-9548-4849-8143-ad2194eaf3bd | - |
| 121 | En quelques mots, qu’avez-vous compris de cette idée de produit et de son utilisation ? | 3465fd81-21c4-4a9e-a393-0982624d6925 | TITLE | 575de4e1-38ef-4588-836c-abf0fd1b7e52 | 10 | 3914e8a8-1ad1-4e1b-852e-d7193ac6576f | - |
| 122 | - | 93c10ceb-cdb4-4b49-b561-2b7edbc35540 | TEXTAREA | 575de4e1-38ef-4588-836c-abf0fd1b7e52 | 10 | 3465fd81-21c4-4a9e-a393-0982624d6925 | - |
| 123 | É11 – Catégorie spontanée | 25e0e41b-4016-4828-bb29-b7469b0e9cbc | PAGE_BREAK | - | 11 | 93c10ceb-cdb4-4b49-b561-2b7edbc35540 | - |
| 124 | En un ou deux mots, à quelle catégorie de produit cette idée vous fait-elle penser ? | 990c8884-0c9c-42f4-be1f-771dcc2c649d | TITLE | b3b80a8c-ee30-48a4-af75-ca2e20d3a2c3 | 11 | 25e0e41b-4016-4828-bb29-b7469b0e9cbc | - |
| 125 | - | 2d903b9b-bfa0-43f3-901a-646ec3ffdf59 | TEXTAREA | b3b80a8c-ee30-48a4-af75-ca2e20d3a2c3 | 11 | 990c8884-0c9c-42f4-be1f-771dcc2c649d | - |
| 126 | É12 – Catégorie assistée | efab05aa-3716-4f70-945f-14df5f855ef2 | PAGE_BREAK | - | 12 | 2d903b9b-bfa0-43f3-901a-646ec3ffdf59 | - |
| 127 | Si vous deviez ranger ce produit dans un rayon ou une famille de produits, où le placeriez-vous plutôt ? | 0e7b010a-23cf-4e20-8d64-5864d7c15425 | TITLE | 8dc9569d-c2f3-4880-8e11-fb9b1e862265 | 12 | efab05aa-3716-4f70-945f-14df5f855ef2 | - |
| 128 | Épices et assaisonnements | 405544e9-08d3-4f5a-99ce-5745f233b767 | MULTIPLE_CHOICE_OPTION | 8dc9569d-c2f3-4880-8e11-fb9b1e862265 | 12 | 0e7b010a-23cf-4e20-8d64-5864d7c15425 | hasOtherOption=true |
| 129 | Bouillons et aides culinaires | fb87badc-666b-4ffe-92e1-eb0a7f181aea | MULTIPLE_CHOICE_OPTION | 8dc9569d-c2f3-4880-8e11-fb9b1e862265 | 12 | 405544e9-08d3-4f5a-99ce-5745f233b767 | hasOtherOption=true |
| 130 | Condiments | 00818a9c-0f8d-4613-bfc1-71552f2053c0 | MULTIPLE_CHOICE_OPTION | 8dc9569d-c2f3-4880-8e11-fb9b1e862265 | 12 | fb87badc-666b-4ffe-92e1-eb0a7f181aea | hasOtherOption=true |
| 131 | Préparations culinaires | 4a10e40e-6dee-498c-9430-cf8ad57daa14 | MULTIPLE_CHOICE_OPTION | 8dc9569d-c2f3-4880-8e11-fb9b1e862265 | 12 | 00818a9c-0f8d-4613-bfc1-71552f2053c0 | hasOtherOption=true |
| 132 | Produits nutritionnels | a462b700-df88-43e3-90e2-775c731a4eb8 | MULTIPLE_CHOICE_OPTION | 8dc9569d-c2f3-4880-8e11-fb9b1e862265 | 12 | 4a10e40e-6dee-498c-9430-cf8ad57daa14 | hasOtherOption=true |
| 133 | Compléments alimentaires | 5b3696ae-aef9-4ef2-8d01-b56ec0f0437f | MULTIPLE_CHOICE_OPTION | 8dc9569d-c2f3-4880-8e11-fb9b1e862265 | 12 | a462b700-df88-43e3-90e2-775c731a4eb8 | hasOtherOption=true |
| 134 | Je ne saurais pas où le ranger | b7a7435a-0f1f-4512-93b1-f4fc10fc0b1a | MULTIPLE_CHOICE_OPTION | 8dc9569d-c2f3-4880-8e11-fb9b1e862265 | 12 | 5b3696ae-aef9-4ef2-8d01-b56ec0f0437f | hasOtherOption=true |
| 135 | Autre | fb4b6936-2e34-46c5-8fdc-998424144faa | MULTIPLE_CHOICE_OPTION | 8dc9569d-c2f3-4880-8e11-fb9b1e862265 | 12 | b7a7435a-0f1f-4512-93b1-f4fc10fc0b1a | hasOtherOption=true, isOtherOption=true |
| 136 | É13 – Évaluation Option A | b15b21ae-d9f5-47de-ae5f-3265db5fcc2a | PAGE_BREAK | - | 13 | fb4b6936-2e34-46c5-8fdc-998424144faa | - |
| 137 | Votre avis sur l’Option A | 7c6b837d-05d2-4236-966f-94ccdf2222b4 | TITLE | 04cec261-f9ce-41e5-9106-d6d8d1854a8c | 13 | b15b21ae-d9f5-47de-ae5f-3265db5fcc2a | - |
| 138 | - | 39e22e6a-5ab9-47c8-9bef-214315ca14b1 | MATRIX | 04cec261-f9ce-41e5-9106-d6d8d1854a8c | 13 | 7c6b837d-05d2-4236-966f-94ccdf2222b4 | randomizeRows=false |
| 139 | 1 — Pas du tout d’accord | 962602fd-8028-4d48-b483-25ef028c4346 | MATRIX_COLUMN | 04cec261-f9ce-41e5-9106-d6d8d1854a8c | 13 | 39e22e6a-5ab9-47c8-9bef-214315ca14b1 | randomizeRows=false |
| 140 | 2 | e6744675-27d4-4da6-8ef8-44f8bd12485e | MATRIX_COLUMN | 04cec261-f9ce-41e5-9106-d6d8d1854a8c | 13 | 962602fd-8028-4d48-b483-25ef028c4346 | randomizeRows=false |
| 141 | 3 | 9009aaee-7644-4bb7-bda3-7579dea8c760 | MATRIX_COLUMN | 04cec261-f9ce-41e5-9106-d6d8d1854a8c | 13 | e6744675-27d4-4da6-8ef8-44f8bd12485e | randomizeRows=false |
| 142 | 4 | 2e40131f-ee77-4cd5-a6c2-3de9c91700ee | MATRIX_COLUMN | 04cec261-f9ce-41e5-9106-d6d8d1854a8c | 13 | 9009aaee-7644-4bb7-bda3-7579dea8c760 | randomizeRows=false |
| 143 | 5 — Tout à fait d’accord | bfe41606-5e1e-4df9-98e7-cb8dd27a28cd | MATRIX_COLUMN | 04cec261-f9ce-41e5-9106-d6d8d1854a8c | 13 | 2e40131f-ee77-4cd5-a6c2-3de9c91700ee | randomizeRows=false |
| 144 | Je comprends comment cette option s’utilise | 8bf8a647-cc48-45e3-b8f3-b292e8e7895c | MATRIX_ROW | 04cec261-f9ce-41e5-9106-d6d8d1854a8c | 13 | bfe41606-5e1e-4df9-98e7-cb8dd27a28cd | randomizeRows=false |
| 145 | Cette option pourrait s’intégrer à ma façon de cuisiner | e939ff62-d06d-4713-ba57-65b1a8fae8d8 | MATRIX_ROW | 04cec261-f9ce-41e5-9106-d6d8d1854a8c | 13 | 8bf8a647-cc48-45e3-b8f3-b292e8e7895c | randomizeRows=false |
| 146 | Cette option me paraît simple à utiliser | 4995b524-ac1b-423b-bf60-ec9ef3c1b01c | MATRIX_ROW | 04cec261-f9ce-41e5-9106-d6d8d1854a8c | 13 | e939ff62-d06d-4713-ba57-65b1a8fae8d8 | randomizeRows=false |
| 147 | Le résultat attendu me paraît appétissant | f41f70e7-36af-4d89-8f0a-c076eaacb8e8 | MATRIX_ROW | 04cec261-f9ce-41e5-9106-d6d8d1854a8c | 13 | 4995b524-ac1b-423b-bf60-ec9ef3c1b01c | randomizeRows=false |
| 148 | Je serais disposé(e) à essayer cette option au moins une fois | ef492349-eca1-4b0e-bfa8-06c706eb476b | MATRIX_ROW | 04cec261-f9ce-41e5-9106-d6d8d1854a8c | 13 | f41f70e7-36af-4d89-8f0a-c076eaacb8e8 | randomizeRows=false |
| 149 | É14 – Évaluation Option B | 368e1eac-c0ed-46d8-843c-4ce22bdfcc54 | PAGE_BREAK | - | 14 | ef492349-eca1-4b0e-bfa8-06c706eb476b | - |
| 150 | Votre avis sur l’Option B | b63a8692-d2cf-4dff-aab4-b8059fe36b28 | TITLE | 1e0f4e76-ce85-47cf-b09c-83ebfe41607b | 14 | 368e1eac-c0ed-46d8-843c-4ce22bdfcc54 | - |
| 151 | - | 47a26383-f15f-4b98-a0a8-8a8af5ed696b | MATRIX | 1e0f4e76-ce85-47cf-b09c-83ebfe41607b | 14 | b63a8692-d2cf-4dff-aab4-b8059fe36b28 | randomizeRows=false |
| 152 | 1 — Pas du tout d’accord | 78023276-290b-4ac8-adee-3433c4088d8e | MATRIX_COLUMN | 1e0f4e76-ce85-47cf-b09c-83ebfe41607b | 14 | 47a26383-f15f-4b98-a0a8-8a8af5ed696b | randomizeRows=false |
| 153 | 2 | 1b0459c5-e21e-4b10-a00a-00dc4f45986a | MATRIX_COLUMN | 1e0f4e76-ce85-47cf-b09c-83ebfe41607b | 14 | 78023276-290b-4ac8-adee-3433c4088d8e | randomizeRows=false |
| 154 | 3 | 9ea5720e-3a97-4135-a093-7819f84cd8fa | MATRIX_COLUMN | 1e0f4e76-ce85-47cf-b09c-83ebfe41607b | 14 | 1b0459c5-e21e-4b10-a00a-00dc4f45986a | randomizeRows=false |
| 155 | 4 | 11d54508-d483-4135-bb67-6346c27e1d16 | MATRIX_COLUMN | 1e0f4e76-ce85-47cf-b09c-83ebfe41607b | 14 | 9ea5720e-3a97-4135-a093-7819f84cd8fa | randomizeRows=false |
| 156 | 5 — Tout à fait d’accord | d7565511-3d74-46dd-9761-b87c2426f19d | MATRIX_COLUMN | 1e0f4e76-ce85-47cf-b09c-83ebfe41607b | 14 | 11d54508-d483-4135-bb67-6346c27e1d16 | randomizeRows=false |
| 157 | Je comprends comment cette option s’utilise | 620129a6-0ef0-4592-9ca7-9af237cbae0f | MATRIX_ROW | 1e0f4e76-ce85-47cf-b09c-83ebfe41607b | 14 | d7565511-3d74-46dd-9761-b87c2426f19d | randomizeRows=false |
| 158 | Cette option pourrait s’intégrer à ma façon de cuisiner | b48f5633-29be-4887-82b4-bf7d23d5adb4 | MATRIX_ROW | 1e0f4e76-ce85-47cf-b09c-83ebfe41607b | 14 | 620129a6-0ef0-4592-9ca7-9af237cbae0f | randomizeRows=false |
| 159 | Cette option me paraît simple à utiliser | b55fa7c3-2c22-4fbe-acd4-0a2298f8df1a | MATRIX_ROW | 1e0f4e76-ce85-47cf-b09c-83ebfe41607b | 14 | b48f5633-29be-4887-82b4-bf7d23d5adb4 | randomizeRows=false |
| 160 | Le résultat attendu me paraît appétissant | eb8664ac-3e26-4578-8ea5-7ead840bcfbc | MATRIX_ROW | 1e0f4e76-ce85-47cf-b09c-83ebfe41607b | 14 | b55fa7c3-2c22-4fbe-acd4-0a2298f8df1a | randomizeRows=false |
| 161 | Je serais disposé(e) à essayer cette option au moins une fois | 7e19e95b-5ce7-4d2c-b912-9d901dc22f0b | MATRIX_ROW | 1e0f4e76-ce85-47cf-b09c-83ebfe41607b | 14 | eb8664ac-3e26-4578-8ea5-7ead840bcfbc | randomizeRows=false |
| 162 | É15 – Préférence | 0046d066-fb32-4ca5-885a-a23ee19cd956 | PAGE_BREAK | - | 15 | 7e19e95b-5ce7-4d2c-b912-9d901dc22f0b | - |
| 163 | Si vous deviez n’en garder qu’une, quelle option vous conviendrait le mieux ? | 1eac8ff9-3a1c-40a0-b0c5-34b0970d60ff | TITLE | 928bd7c4-6eec-4608-b960-6db6b6641973 | 15 | 0046d066-fb32-4ca5-885a-a23ee19cd956 | - |
| 164 | Option A | f2c1b5c3-11bb-44bf-875c-38ac0fd73c98 | MULTIPLE_CHOICE_OPTION | 928bd7c4-6eec-4608-b960-6db6b6641973 | 15 | 1eac8ff9-3a1c-40a0-b0c5-34b0970d60ff | - |
| 165 | Option B | bfa8d806-a460-47c1-9724-2cb463a5cba3 | MULTIPLE_CHOICE_OPTION | 928bd7c4-6eec-4608-b960-6db6b6641973 | 15 | f2c1b5c3-11bb-44bf-875c-38ac0fd73c98 | - |
| 166 | Les deux | 3ac09da9-599e-4ae4-ad19-121105f6da7b | MULTIPLE_CHOICE_OPTION | 928bd7c4-6eec-4608-b960-6db6b6641973 | 15 | bfa8d806-a460-47c1-9724-2cb463a5cba3 | - |
| 167 | Aucune | b38ee722-169a-4858-8bc9-13ec531970fb | MULTIPLE_CHOICE_OPTION | 928bd7c4-6eec-4608-b960-6db6b6641973 | 15 | 3ac09da9-599e-4ae4-ad19-121105f6da7b | - |
| 168 | - | 54fdc041-afbf-4526-9aa2-ea291c385182 | CONDITIONAL_LOGIC | - | 15 | b38ee722-169a-4858-8bc9-13ec531970fb | see `## Logic rules` below |
| 169 | Laquelle envisageriez-vous d’essayer ou d’acheter en premier ? | 3f5c0560-efc6-451b-a934-f7824937384c | TITLE | a9c61764-bdaa-4757-9f8d-353861c2cdac | 15 | 54fdc041-afbf-4526-9aa2-ea291c385182 | isHidden=true |
| 170 | Option A | 51813e71-404b-4643-bfdd-69cec5017a0c | MULTIPLE_CHOICE_OPTION | a9c61764-bdaa-4757-9f8d-353861c2cdac | 15 | 3f5c0560-efc6-451b-a934-f7824937384c | isHidden=true |
| 171 | Option B | 5bdabae9-0c3b-43bc-951b-64f985640df3 | MULTIPLE_CHOICE_OPTION | a9c61764-bdaa-4757-9f8d-353861c2cdac | 15 | 51813e71-404b-4643-bfdd-69cec5017a0c | isHidden=true |
| 172 | Cela dépendrait du goût proposé | 653e901b-f788-46b6-8b27-3a6caede636b | MULTIPLE_CHOICE_OPTION | a9c61764-bdaa-4757-9f8d-353861c2cdac | 15 | 5bdabae9-0c3b-43bc-951b-64f985640df3 | isHidden=true |
| 173 | Cela dépendrait du prix | 601befb3-a21b-48bc-a9a5-0d8782cdff87 | MULTIPLE_CHOICE_OPTION | a9c61764-bdaa-4757-9f8d-353861c2cdac | 15 | 653e901b-f788-46b6-8b27-3a6caede636b | isHidden=true |
| 174 | Je ne sais pas | 43378da9-4d9c-428b-9543-00363b020397 | MULTIPLE_CHOICE_OPTION | a9c61764-bdaa-4757-9f8d-353861c2cdac | 15 | 601befb3-a21b-48bc-a9a5-0d8782cdff87 | isHidden=true |
| 175 | - | 7c19f06f-0cf7-4966-a49e-3bb773385bfa | CONDITIONAL_LOGIC | - | 15 | 43378da9-4d9c-428b-9543-00363b020397 | see `## Logic rules` below |
| 176 | - | 9c751b70-da2b-4681-8805-9ef7c9ef2a80 | CONDITIONAL_LOGIC | - | 15 | 7c19f06f-0cf7-4966-a49e-3bb773385bfa | see `## Logic rules` below |
| 177 | - | 24addaa5-3f5b-49af-8561-e119142de723 | CONDITIONAL_LOGIC | - | 15 | 9c751b70-da2b-4681-8805-9ef7c9ef2a80 | see `## Logic rules` below |
| 178 | Quelle est la principale raison de votre choix ? | e98a58fa-f26e-4cce-8474-2aae373db971 | TITLE | ea3b444a-c300-4faa-a88c-336cae52307a | 15 | 24addaa5-3f5b-49af-8561-e119142de723 | - |
| 179 | - | ba5be04e-9217-4e44-b25a-fdaf7c18f6c5 | TEXTAREA | ea3b444a-c300-4faa-a88c-336cae52307a | 15 | e98a58fa-f26e-4cce-8474-2aae373db971 | isRequired=false |
| 180 | É16 – Valeur et substituabilité | 19e92dd9-187e-4ffe-99c9-06ede1d677a1 | PAGE_BREAK | - | 16 | ba5be04e-9217-4e44-b25a-fdaf7c18f6c5 | - |
| 181 | Au-delà du mode d’utilisation, quel aspect de cette idée vous intéresse le plus ? | 7ee22d34-643b-439d-880f-2a72efb8e038 | TITLE | ae8557be-4258-4f95-8670-c6ac1e83c1c1 | 16 | 19e92dd9-187e-4ffe-99c9-06ede1d677a1 | - |
| 182 | Apporter davantage de goût et de variété | 8f258be4-792d-4577-8a20-e2d57a4285ad | MULTIPLE_CHOICE_OPTION | ae8557be-4258-4f95-8670-c6ac1e83c1c1 | 16 | 7ee22d34-643b-439d-880f-2a72efb8e038 | hasOtherOption=true |
| 183 | Simplifier l’assaisonnement pendant la cuisson | 703e321d-6339-4afc-9054-33ed5f5179bf | MULTIPLE_CHOICE_OPTION | ae8557be-4258-4f95-8670-c6ac1e83c1c1 | 16 | 8f258be4-792d-4577-8a20-e2d57a4285ad | hasOtherOption=true |
| 184 | Intégrer des ingrédients végétaux directement au plat | 355f7f0b-a3e2-457b-8168-84e2b74fb716 | MULTIPLE_CHOICE_OPTION | ae8557be-4258-4f95-8670-c6ac1e83c1c1 | 16 | 703e321d-6339-4afc-9054-33ed5f5179bf | hasOtherOption=true |
| 185 | Ajouter un intérêt nutritionnel au repas | aeced8d1-f6bd-46dd-9983-fdbd90092e97 | MULTIPLE_CHOICE_OPTION | ae8557be-4258-4f95-8670-c6ac1e83c1c1 | 16 | 355f7f0b-a3e2-457b-8168-84e2b74fb716 | hasOtherOption=true |
| 186 | Aucun de ces aspects | 632b12d5-7ef0-4e90-b18a-2966ecd7664d | MULTIPLE_CHOICE_OPTION | ae8557be-4258-4f95-8670-c6ac1e83c1c1 | 16 | aeced8d1-f6bd-46dd-9983-fdbd90092e97 | hasOtherOption=true |
| 187 | Autre | 57691ae5-0a0d-4009-b76d-afd1c452117f | MULTIPLE_CHOICE_OPTION | ae8557be-4258-4f95-8670-c6ac1e83c1c1 | 16 | 632b12d5-7ef0-4e90-b18a-2966ecd7664d | hasOtherOption=true, isOtherOption=true |
| 188 | Avez-vous le sentiment que vous pourriez obtenir le même résultat avec ce que vous avez déjà dans vos placards ? | 5fca8d23-d186-4407-8b3a-9d7cf7919a53 | TITLE | 3c41552e-b6c7-4c60-a1d9-d197a5a9ccde | 16 | 57691ae5-0a0d-4009-b76d-afd1c452117f | - |
| 189 | Oui, facilement | f323e9ed-3328-49b5-b4af-dc94d182c4ca | MULTIPLE_CHOICE_OPTION | 3c41552e-b6c7-4c60-a1d9-d197a5a9ccde | 16 | 5fca8d23-d186-4407-8b3a-9d7cf7919a53 | - |
| 190 | Oui, mais avec davantage d’effort ou de connaissances | 90207d0d-0ed1-4d3a-ac41-838a4356705d | MULTIPLE_CHOICE_OPTION | 3c41552e-b6c7-4c60-a1d9-d197a5a9ccde | 16 | f323e9ed-3328-49b5-b4af-dc94d182c4ca | - |
| 191 | Non, pas vraiment | 78dbf594-b844-4995-b726-b11d0d185be2 | MULTIPLE_CHOICE_OPTION | 3c41552e-b6c7-4c60-a1d9-d197a5a9ccde | 16 | 90207d0d-0ed1-4d3a-ac41-838a4356705d | - |
| 192 | Je ne sais pas | 2020b381-dee0-4d4f-85ee-60c4d94facd6 | MULTIPLE_CHOICE_OPTION | 3c41552e-b6c7-4c60-a1d9-d197a5a9ccde | 16 | 78dbf594-b844-4995-b726-b11d0d185be2 | - |
| 193 | É17 – Axes nutritionnels | f88ae0cd-929f-407a-bfea-dddc1c74f352 | PAGE_BREAK | - | 17 | 2020b381-dee0-4d4f-85ee-60c4d94facd6 | - |
| 194 | Ces possibilités sont encore à l’étude. Elles dépendront de la formulation finale et de ce qui reste réellement dans le plat après cuisson. | a0befbd7-52cd-42aa-bd50-29db5f0c1f30 | TEXT | - | 17 | f88ae0cd-929f-407a-bfea-dddc1c74f352 | - |
| 195 | Dans quelle mesure chacune augmenterait-elle votre intérêt pour le produit ? | 4b6c49f4-6de0-4074-bbe9-83f9c5b37945 | TITLE | 79e933d0-ae20-4e9e-b8d0-45b461b2244d | 17 | a0befbd7-52cd-42aa-bd50-29db5f0c1f30 | - |
| 196 | - | 14fed82c-2ae9-4a04-8761-69338d2b9adf | MATRIX | 79e933d0-ae20-4e9e-b8d0-45b461b2244d | 17 | 4b6c49f4-6de0-4074-bbe9-83f9c5b37945 | randomizeRows=true |
| 197 | Pas du tout | 3fe1c4dc-8b57-4e81-a132-01868c6e3d20 | MATRIX_COLUMN | 79e933d0-ae20-4e9e-b8d0-45b461b2244d | 17 | 14fed82c-2ae9-4a04-8761-69338d2b9adf | randomizeRows=true |
| 198 | Un peu | c1854720-22a0-4ba1-9d9b-684b6f2b63c9 | MATRIX_COLUMN | 79e933d0-ae20-4e9e-b8d0-45b461b2244d | 17 | 3fe1c4dc-8b57-4e81-a132-01868c6e3d20 | randomizeRows=true |
| 199 | Assez | e50aa4bf-ff37-4a58-b76e-ea94dfe8a1e2 | MATRIX_COLUMN | 79e933d0-ae20-4e9e-b8d0-45b461b2244d | 17 | c1854720-22a0-4ba1-9d9b-684b6f2b63c9 | randomizeRows=true |
| 200 | Beaucoup | b7ce021e-2b09-4ad1-8857-dc961d0c0b0f | MATRIX_COLUMN | 79e933d0-ae20-4e9e-b8d0-45b461b2244d | 17 | e50aa4bf-ff37-4a58-b76e-ea94dfe8a1e2 | randomizeRows=true |
| 201 | Je ne comprends pas bien cet axe | 00b13cfb-c13c-495b-946f-c5d82152c584 | MATRIX_COLUMN | 79e933d0-ae20-4e9e-b8d0-45b461b2244d | 17 | b7ce021e-2b09-4ad1-8857-dc961d0c0b0f | randomizeRows=true |
| 202 | Un apport intéressant en fibres | 525efd5c-bf9e-4daa-82d5-d247dc74c833 | MATRIX_ROW | 79e933d0-ae20-4e9e-b8d0-45b461b2244d | 17 | 00b13cfb-c13c-495b-946f-c5d82152c584 | randomizeRows=true |
| 203 | Un apport intéressant en magnésium | e1fd69fb-a49d-42ea-85c0-52c5ade4abcc | MATRIX_ROW | 79e933d0-ae20-4e9e-b8d0-45b461b2244d | 17 | 525efd5c-bf9e-4daa-82d5-d247dc74c833 | randomizeRows=true |
| 204 | Un apport intéressant en fer | afc35041-11c6-4072-a2a4-9cfb25ada075 | MATRIX_ROW | 79e933d0-ae20-4e9e-b8d0-45b461b2244d | 17 | e1fd69fb-a49d-42ea-85c0-52c5ade4abcc | randomizeRows=true |
| 205 | Lequel de ces apports augmenterait le plus votre intérêt pour ce produit ? | 1b0221cb-ee29-4ce5-a37c-b3f87cc73259 | TITLE | ecbe5ee8-d129-48a5-a6dc-81b366cb4e4a | 17 | afc35041-11c6-4072-a2a4-9cfb25ada075 | - |
| 206 | Un apport en fibres | 942d27a0-70a8-4845-a059-f8a2fe850d6c | MULTIPLE_CHOICE_OPTION | ecbe5ee8-d129-48a5-a6dc-81b366cb4e4a | 17 | 1b0221cb-ee29-4ce5-a37c-b3f87cc73259 | - |
| 207 | Un apport en magnésium | f43122e2-a4c1-4cb3-bfbb-584b7b5dd22d | MULTIPLE_CHOICE_OPTION | ecbe5ee8-d129-48a5-a6dc-81b366cb4e4a | 17 | 942d27a0-70a8-4845-a059-f8a2fe850d6c | - |
| 208 | Un apport en fer | ea4c2095-fe3e-488c-8667-4f2e3482b8cf | MULTIPLE_CHOICE_OPTION | ecbe5ee8-d129-48a5-a6dc-81b366cb4e4a | 17 | f43122e2-a4c1-4cb3-bfbb-584b7b5dd22d | - |
| 209 | Aucun de ces apports | bdd637f4-1eed-48ce-ac98-7e10556cc889 | MULTIPLE_CHOICE_OPTION | ecbe5ee8-d129-48a5-a6dc-81b366cb4e4a | 17 | ea4c2095-fe3e-488c-8667-4f2e3482b8cf | - |
| 210 | Je ne sais pas | 7c0bdc38-144c-4106-90b5-10eda8cd339e | MULTIPLE_CHOICE_OPTION | ecbe5ee8-d129-48a5-a6dc-81b366cb4e4a | 17 | bdd637f4-1eed-48ce-ac98-7e10556cc889 | - |
| 211 | É18 – Minéraux ajoutés | 099137ab-75c5-4795-b18f-a6ccd657e105 | PAGE_BREAK | - | 18 | 7c0bdc38-144c-4106-90b5-10eda8cd339e | - |
| 212 | Certaines versions de ce type de produit pourraient contenir des minéraux ajoutés, comme du magnésium ou du fer, clairement indiqués dans la liste d’ingrédients. | 0cb07122-75f3-4276-a28a-f703f80d1d2b | TEXT | - | 18 | 099137ab-75c5-4795-b18f-a6ccd657e105 | - |
| 213 | Quelle serait votre réaction à la présence de ces minéraux ajoutés ? | 32c04694-3c31-497f-840b-10a92a1be077 | TITLE | 9dc61692-42ed-4ac5-af4d-0daaa5e50045 | 18 | 0cb07122-75f3-4276-a28a-f703f80d1d2b | - |
| 214 | Cela augmenterait mon intérêt | 144dc88a-e9c6-48ba-ae2b-a35d74ba15c5 | MULTIPLE_CHOICE_OPTION | 9dc61692-42ed-4ac5-af4d-0daaa5e50045 | 18 | 32c04694-3c31-497f-840b-10a92a1be077 | - |
| 215 | Cela ne changerait pas mon intérêt | 35498c63-bde7-44ae-8924-ebc426029d18 | MULTIPLE_CHOICE_OPTION | 9dc61692-42ed-4ac5-af4d-0daaa5e50045 | 18 | 144dc88a-e9c6-48ba-ae2b-a35d74ba15c5 | - |
| 216 | Cela me ferait hésiter | f4038ea2-3372-4f78-9bea-4cfeb7c8c2b6 | MULTIPLE_CHOICE_OPTION | 9dc61692-42ed-4ac5-af4d-0daaa5e50045 | 18 | 35498c63-bde7-44ae-8924-ebc426029d18 | - |
| 217 | Cela diminuerait fortement mon intérêt | 225ab8d5-b973-4588-aa09-6738d5e42f74 | MULTIPLE_CHOICE_OPTION | 9dc61692-42ed-4ac5-af4d-0daaa5e50045 | 18 | f4038ea2-3372-4f78-9bea-4cfeb7c8c2b6 | - |
| 218 | Je ne sais pas | a882804b-db68-492f-b63e-594d463d4c83 | MULTIPLE_CHOICE_OPTION | 9dc61692-42ed-4ac5-af4d-0daaa5e50045 | 18 | 225ab8d5-b973-4588-aa09-6738d5e42f74 | - |
| 219 | - | b0b2bb7a-086e-4776-ae81-ec0ab0ddf3ba | CONDITIONAL_LOGIC | - | 18 | a882804b-db68-492f-b63e-594d463d4c83 | see `## Logic rules` below |
| 220 | Pour quelle raison principalement ? | f0f30853-0df1-4864-a4ad-b43d6fc8e0b0 | TITLE | d969f67a-eda7-42c5-aebc-d501839feafe | 18 | b0b2bb7a-086e-4776-ae81-ec0ab0ddf3ba | isHidden=true |
| 221 | Le produit me semblerait trop transformé ou artificiel | 499e447b-1908-4d04-af87-ad82bc7a8501 | MULTIPLE_CHOICE_OPTION | d969f67a-eda7-42c5-aebc-d501839feafe | 18 | f0f30853-0df1-4864-a4ad-b43d6fc8e0b0 | hasOtherOption=true, isHidden=true |
| 222 | Il me ferait penser à un complément alimentaire | 68b7a3c7-427d-41af-87bc-847a2dbb0939 | MULTIPLE_CHOICE_OPTION | d969f67a-eda7-42c5-aebc-d501839feafe | 18 | 499e447b-1908-4d04-af87-ad82bc7a8501 | hasOtherOption=true, isHidden=true |
| 223 | Je douterais de l’utilité des quantités ajoutées | 5dda55fe-a95a-4232-af30-78c5575a9ecd | MULTIPLE_CHOICE_OPTION | d969f67a-eda7-42c5-aebc-d501839feafe | 18 | 68b7a3c7-427d-41af-87bc-847a2dbb0939 | hasOtherOption=true, isHidden=true |
| 224 | Je préférerais que les nutriments proviennent uniquement des ingrédients végétaux | d53df03f-c48f-4815-9631-272f3ea10b18 | MULTIPLE_CHOICE_OPTION | d969f67a-eda7-42c5-aebc-d501839feafe | 18 | 5dda55fe-a95a-4232-af30-78c5575a9ecd | hasOtherOption=true, isHidden=true |
| 225 | Je manquerais d’informations sur leur origine | 14730d92-ed30-48ca-8c75-9af94776d147 | MULTIPLE_CHOICE_OPTION | d969f67a-eda7-42c5-aebc-d501839feafe | 18 | d53df03f-c48f-4815-9631-272f3ea10b18 | hasOtherOption=true, isHidden=true |
| 226 | Je manquerais d’informations sur les quantités réellement apportées | 5828a5b2-307f-4acb-b469-a06ec7c76f62 | MULTIPLE_CHOICE_OPTION | d969f67a-eda7-42c5-aebc-d501839feafe | 18 | 14730d92-ed30-48ca-8c75-9af94776d147 | hasOtherOption=true, isHidden=true |
| 227 | Autre | 607956b2-52a4-485e-9046-66097ff8dc37 | MULTIPLE_CHOICE_OPTION | d969f67a-eda7-42c5-aebc-d501839feafe | 18 | 5828a5b2-307f-4acb-b469-a06ec7c76f62 | hasOtherOption=true, isOtherOption=true, isHidden=true |
| 228 | Après avoir vu ces possibilités nutritionnelles, ce produit vous semblerait plutôt… | 66b16a21-225e-4aee-be68-288a3e0ac0e6 | TITLE | f4c620da-02cd-4827-8f97-d6ba010390a3 | 18 | 607956b2-52a4-485e-9046-66097ff8dc37 | - |
| 229 | Un condiment ou une aide culinaire du quotidien | 8d619761-ede2-4b37-bce9-6fd145e90396 | MULTIPLE_CHOICE_OPTION | f4c620da-02cd-4827-8f97-d6ba010390a3 | 18 | 66b16a21-225e-4aee-be68-288a3e0ac0e6 | - |
| 230 | Un aliment du quotidien avec un intérêt nutritionnel | d46bc371-6b7f-4b53-9d01-0b0014e701ad | MULTIPLE_CHOICE_OPTION | f4c620da-02cd-4827-8f97-d6ba010390a3 | 18 | 8d619761-ede2-4b37-bce9-6fd145e90396 | - |
| 231 | Un produit nutritionnel spécialisé | d86cfa7c-20ca-4dec-84e0-7a77dc6994eb | MULTIPLE_CHOICE_OPTION | f4c620da-02cd-4827-8f97-d6ba010390a3 | 18 | d46bc371-6b7f-4b53-9d01-0b0014e701ad | - |
| 232 | Trop proche d’un complément alimentaire | 5070f2cb-1a90-48b2-b146-40dfb0cc3540 | MULTIPLE_CHOICE_OPTION | f4c620da-02cd-4827-8f97-d6ba010390a3 | 18 | d86cfa7c-20ca-4dec-84e0-7a77dc6994eb | - |
| 233 | Je ne sais pas | c8f49d7a-5bd4-4b03-afdd-e45b338202c5 | MULTIPLE_CHOICE_OPTION | f4c620da-02cd-4827-8f97-d6ba010390a3 | 18 | 5070f2cb-1a90-48b2-b146-40dfb0cc3540 | - |
| 234 | É19 – Les algues | a0b355ef-5c82-4e0d-9a9e-4cda589e823f | PAGE_BREAK | - | 19 | c8f49d7a-5bd4-4b03-afdd-e45b338202c5 | - |
| 235 | Consommez-vous actuellement des algues dans votre alimentation ? | 5b6ffcfe-6254-4778-affb-dc239ffb2e94 | TITLE | 2695d573-3f07-4c30-8f4d-5a85bf1dfdcc | 19 | a0b355ef-5c82-4e0d-9a9e-4cda589e823f | - |
| 236 | Oui, régulièrement | 32a5af2b-d435-4879-8b43-f54d528a48ef | MULTIPLE_CHOICE_OPTION | 2695d573-3f07-4c30-8f4d-5a85bf1dfdcc | 19 | 5b6ffcfe-6254-4778-affb-dc239ffb2e94 | - |
| 237 | Oui, occasionnellement | d1fdf625-a923-41c9-8906-d359c179689e | MULTIPLE_CHOICE_OPTION | 2695d573-3f07-4c30-8f4d-5a85bf1dfdcc | 19 | 32a5af2b-d435-4879-8b43-f54d528a48ef | - |
| 238 | J’en ai déjà goûté, mais très rarement | 080a9c21-0557-49b2-93f9-bec2328ebbee | MULTIPLE_CHOICE_OPTION | 2695d573-3f07-4c30-8f4d-5a85bf1dfdcc | 19 | d1fdf625-a923-41c9-8906-d359c179689e | - |
| 239 | Non, jamais | ddf50d21-fd4d-43ea-9808-8660fa392e62 | MULTIPLE_CHOICE_OPTION | 2695d573-3f07-4c30-8f4d-5a85bf1dfdcc | 19 | 080a9c21-0557-49b2-93f9-bec2328ebbee | - |
| 240 | Je ne sais pas | d1921024-c54d-4aa4-88dd-a90c58a73fd9 | MULTIPLE_CHOICE_OPTION | 2695d573-3f07-4c30-8f4d-5a85bf1dfdcc | 19 | ddf50d21-fd4d-43ea-9808-8660fa392e62 | - |
| 241 | Que penseriez-vous de l’utilisation d’une petite quantité d’algues dans une préparation ajoutée pendant la cuisson ? | 62aae197-a982-4f9c-a139-6a2c9c632d0a | TITLE | 0f9c2dd0-1528-4ac5-9dce-fe6f5fde5189 | 19 | d1921024-c54d-4aa4-88dd-a90c58a73fd9 | - |
| 242 | Cela augmenterait mon intérêt | 549b29f3-a52e-4387-b09a-5b2c9ce206bc | MULTIPLE_CHOICE_OPTION | 0f9c2dd0-1528-4ac5-9dce-fe6f5fde5189 | 19 | 62aae197-a982-4f9c-a139-6a2c9c632d0a | - |
| 243 | Cela pourrait m’intéresser selon le goût | 7f441cfb-0b7f-42a2-ab71-e79062e411dc | MULTIPLE_CHOICE_OPTION | 0f9c2dd0-1528-4ac5-9dce-fe6f5fde5189 | 19 | 549b29f3-a52e-4387-b09a-5b2c9ce206bc | - |
| 244 | Cela ne changerait pas mon intérêt | 966f8f3f-1a21-4c3c-bbab-fc40635b8914 | MULTIPLE_CHOICE_OPTION | 0f9c2dd0-1528-4ac5-9dce-fe6f5fde5189 | 19 | 7f441cfb-0b7f-42a2-ab71-e79062e411dc | - |
| 245 | Cela me ferait hésiter | 8ce2dbed-5ea6-439c-aeba-b656b95fbf61 | MULTIPLE_CHOICE_OPTION | 0f9c2dd0-1528-4ac5-9dce-fe6f5fde5189 | 19 | 966f8f3f-1a21-4c3c-bbab-fc40635b8914 | - |
| 246 | Je ne voudrais pas en consommer | 56858fe0-d696-4b22-b967-1e1f303523c0 | MULTIPLE_CHOICE_OPTION | 0f9c2dd0-1528-4ac5-9dce-fe6f5fde5189 | 19 | 8ce2dbed-5ea6-439c-aeba-b656b95fbf61 | - |
| 247 | Je ne sais pas | 5abbe61f-94a3-49b5-bec9-e0e741b1e45b | MULTIPLE_CHOICE_OPTION | 0f9c2dd0-1528-4ac5-9dce-fe6f5fde5189 | 19 | 56858fe0-d696-4b22-b967-1e1f303523c0 | - |
| 248 | - | 9c52fcb6-b912-44a2-952e-926e12bd6e1b | CONDITIONAL_LOGIC | - | 19 | 5abbe61f-94a3-49b5-bec9-e0e741b1e45b | see `## Logic rules` below |
| 249 | - | d5d85a42-67f4-4dfb-aacc-2c36ab9b70ea | CONDITIONAL_LOGIC | - | 19 | 9c52fcb6-b912-44a2-952e-926e12bd6e1b | see `## Logic rules` below |
| 250 | Une gamme de préparations culinaires principalement fondée sur les algues vous semblerait-elle intéressante ? | 81eee087-23b5-4fcb-bfd5-e306d3cc433e | TITLE | 23637cca-8634-42a3-a498-1608f8ea5eed | 19 | d5d85a42-67f4-4dfb-aacc-2c36ab9b70ea | - |
| 251 | Oui, très intéressante | fd49c514-ec59-4a4c-afde-f374f8f881b5 | MULTIPLE_CHOICE_OPTION | 23637cca-8634-42a3-a498-1608f8ea5eed | 19 | 81eee087-23b5-4fcb-bfd5-e306d3cc433e | - |
| 252 | Oui, selon les goûts proposés | 33a9f82f-2021-4c2c-a430-dcd46785fddc | MULTIPLE_CHOICE_OPTION | 23637cca-8634-42a3-a498-1608f8ea5eed | 19 | fd49c514-ec59-4a4c-afde-f374f8f881b5 | - |
| 253 | Peut-être, mais seulement si les algues restent discrètes | edef7e65-9ad7-440b-8859-9754548fb13d | MULTIPLE_CHOICE_OPTION | 23637cca-8634-42a3-a498-1608f8ea5eed | 19 | 33a9f82f-2021-4c2c-a430-dcd46785fddc | - |
| 254 | Non, je préférerais que les algues restent un ingrédient secondaire | ce8edb35-01c9-47a5-8375-37dfcf56a6ab | MULTIPLE_CHOICE_OPTION | 23637cca-8634-42a3-a498-1608f8ea5eed | 19 | edef7e65-9ad7-440b-8859-9754548fb13d | - |
| 255 | Non, cela ne m’intéresserait pas | 0c02ba7c-6953-4458-9b6f-90b184bdca74 | MULTIPLE_CHOICE_OPTION | 23637cca-8634-42a3-a498-1608f8ea5eed | 19 | ce8edb35-01c9-47a5-8375-37dfcf56a6ab | - |
| 256 | Je ne sais pas | fe3046d1-021d-4cd5-a871-5d3edecd9820 | MULTIPLE_CHOICE_OPTION | 23637cca-8634-42a3-a498-1608f8ea5eed | 19 | 0c02ba7c-6953-4458-9b6f-90b184bdca74 | - |
| 257 | Quel aspect vous semblerait le plus intéressant ? | 9d838a37-7c11-409c-b9a0-e5f0300312ee | TITLE | f894196e-2081-4f05-bf0d-3dea9334d9e2 | 19 | fe3046d1-021d-4cd5-a871-5d3edecd9820 | isHidden=true |
| 258 | Apporter davantage d’umami et de profondeur au goût | 32caa6b6-386e-4a7f-8216-2e0723c0a7d6 | MULTIPLE_CHOICE_OPTION | f894196e-2081-4f05-bf0d-3dea9334d9e2 | 19 | 9d838a37-7c11-409c-b9a0-e5f0300312ee | isHidden=true |
| 259 | Permettre d’utiliser moins de sel | 9e63996b-cbf1-453d-a295-04519b656ee2 | MULTIPLE_CHOICE_OPTION | f894196e-2081-4f05-bf0d-3dea9334d9e2 | 19 | 32caa6b6-386e-4a7f-8216-2e0723c0a7d6 | isHidden=true |
| 260 | Apporter naturellement certains minéraux | aafa0834-fe0c-4573-9ecc-6ed22be296e6 | MULTIPLE_CHOICE_OPTION | f894196e-2081-4f05-bf0d-3dea9334d9e2 | 19 | 9e63996b-cbf1-453d-a295-04519b656ee2 | isHidden=true |
| 261 | Introduire plus facilement les algues dans l’alimentation quotidienne | bdc5b499-373d-43dd-83cd-044032709959 | MULTIPLE_CHOICE_OPTION | f894196e-2081-4f05-bf0d-3dea9334d9e2 | 19 | aafa0834-fe0c-4573-9ecc-6ed22be296e6 | isHidden=true |
| 262 | Donner une identité originale au produit | 471b2021-cef2-4442-8c3f-536798f064d5 | MULTIPLE_CHOICE_OPTION | f894196e-2081-4f05-bf0d-3dea9334d9e2 | 19 | bdc5b499-373d-43dd-83cd-044032709959 | isHidden=true |
| 263 | Aucun de ces aspects | 9a9df5d1-cb83-4f6e-acdb-04c651008b46 | MULTIPLE_CHOICE_OPTION | f894196e-2081-4f05-bf0d-3dea9334d9e2 | 19 | 471b2021-cef2-4442-8c3f-536798f064d5 | isHidden=true |
| 264 | Je ne sais pas | c8f55cd6-4906-4cbe-b406-04077840a85a | MULTIPLE_CHOICE_OPTION | f894196e-2081-4f05-bf0d-3dea9334d9e2 | 19 | 9a9df5d1-cb83-4f6e-acdb-04c651008b46 | isHidden=true |
| 265 | Quel serait votre principal frein ? | f297187b-a463-480c-8b0e-44c24a7f7129 | TITLE | 122f7fc8-b993-4762-96d6-48f3647c035c | 19 | c8f55cd6-4906-4cbe-b406-04077840a85a | isHidden=true |
| 266 | Peur d’un goût trop marin | 568786f4-17cb-4edf-a941-50ba5b443c6c | MULTIPLE_CHOICE_OPTION | 122f7fc8-b993-4762-96d6-48f3647c035c | 19 | f297187b-a463-480c-8b0e-44c24a7f7129 | hasOtherOption=true, isHidden=true |
| 267 | Odeur | 96b1f9b9-ef3b-4438-832a-acf35be7139d | MULTIPLE_CHOICE_OPTION | 122f7fc8-b993-4762-96d6-48f3647c035c | 19 | 568786f4-17cb-4edf-a941-50ba5b443c6c | hasOtherOption=true, isHidden=true |
| 268 | Couleur ou aspect dans le plat | 61d280e1-87c2-40e8-9db1-5288c8a4d4d4 | MULTIPLE_CHOICE_OPTION | 122f7fc8-b993-4762-96d6-48f3647c035c | 19 | 96b1f9b9-ef3b-4438-832a-acf35be7139d | hasOtherOption=true, isHidden=true |
| 269 | Texture | ed68cfbe-debb-4e73-8642-c4b419218eae | MULTIPLE_CHOICE_OPTION | 122f7fc8-b993-4762-96d6-48f3647c035c | 19 | 61d280e1-87c2-40e8-9db1-5288c8a4d4d4 | hasOtherOption=true, isHidden=true |
| 270 | Manque d’habitude | 793d5ff8-a396-4ab6-92c6-e233145bf3ae | MULTIPLE_CHOICE_OPTION | 122f7fc8-b993-4762-96d6-48f3647c035c | 19 | ed68cfbe-debb-4e73-8642-c4b419218eae | hasOtherOption=true, isHidden=true |
| 271 | Présence d’iode | 1b5d0934-d2f6-4f62-b487-df4bfab377b9 | MULTIPLE_CHOICE_OPTION | 122f7fc8-b993-4762-96d6-48f3647c035c | 19 | 793d5ff8-a396-4ab6-92c6-e233145bf3ae | hasOtherOption=true, isHidden=true |
| 272 | Doute sur l’origine ou la sécurité | 26379fe2-f57a-4fd0-819d-472eb418f3d5 | MULTIPLE_CHOICE_OPTION | 122f7fc8-b993-4762-96d6-48f3647c035c | 19 | 1b5d0934-d2f6-4f62-b487-df4bfab377b9 | hasOtherOption=true, isHidden=true |
| 273 | Prix | 5483c0e1-6203-4b4a-b3cb-6223ec02d173 | MULTIPLE_CHOICE_OPTION | 122f7fc8-b993-4762-96d6-48f3647c035c | 19 | 26379fe2-f57a-4fd0-819d-472eb418f3d5 | hasOtherOption=true, isHidden=true |
| 274 | Autre | c2bae6a2-2c60-4870-9255-dc8e4ffccbd2 | MULTIPLE_CHOICE_OPTION | 122f7fc8-b993-4762-96d6-48f3647c035c | 19 | 5483c0e1-6203-4b4a-b3cb-6223ec02d173 | hasOtherOption=true, isOtherOption=true, isHidden=true |
| 275 | É20 – Critères d’achat et confiance | 56033f4c-76f3-4166-969c-42d67da946a8 | PAGE_BREAK | - | 20 | c2bae6a2-2c60-4870-9255-dc8e4ffccbd2 | - |
| 276 | Lorsque vous choisissez un produit de ce type, classez les critères suivants du plus important au moins important pour vous. Placez en premier le critère qui compterait le plus dans votre décision d’achat. | 88d12c3b-63ba-4bf6-abc6-3a63276816c9 | TITLE | 6059bd38-d261-4c33-b8a9-f71bb15cffa7 | 20 | 56033f4c-76f3-4166-969c-42d67da946a8 | - |
| 277 | Le goût | 9ba41f88-787b-47f0-9ed5-d5a9aa024937 | RANKING_OPTION | 6059bd38-d261-4c33-b8a9-f71bb15cffa7 | 20 | 88d12c3b-63ba-4bf6-abc6-3a63276816c9 | - |
| 278 | Le prix | 99712842-7a0d-4911-9a15-21e195b0319a | RANKING_OPTION | 6059bd38-d261-4c33-b8a9-f71bb15cffa7 | 20 | 9ba41f88-787b-47f0-9ed5-d5a9aa024937 | - |
| 279 | La facilité et la praticité d’utilisation | 5986edce-1836-41a2-94dc-a91f8bb04ff7 | RANKING_OPTION | 6059bd38-d261-4c33-b8a9-f71bb15cffa7 | 20 | 99712842-7a0d-4911-9a15-21e195b0319a | - |
| 280 | La composition et la qualité des ingrédients | d8ad2e2a-bf4b-49cd-b79b-9ecaa5f4cc3a | RANKING_OPTION | 6059bd38-d261-4c33-b8a9-f71bb15cffa7 | 20 | 5986edce-1836-41a2-94dc-a91f8bb04ff7 | - |
| 281 | L’intérêt nutritionnel | 50de311f-e745-481f-b748-c7ee894b7c4e | RANKING_OPTION | 6059bd38-d261-4c33-b8a9-f71bb15cffa7 | 20 | d8ad2e2a-bf4b-49cd-b79b-9ecaa5f4cc3a | - |
| 282 | La confiance dans les informations et les preuves apportées | 4878ae36-c754-4385-b482-ab806869e5b1 | RANKING_OPTION | 6059bd38-d261-4c33-b8a9-f71bb15cffa7 | 20 | 50de311f-e745-481f-b748-c7ee894b7c4e | - |
| 283 | Qu’est-ce qui vous donnerait le plus confiance dans ce type de produit ? | 087056b2-af30-4f39-b82f-408a56c5eb95 | TITLE | a8d79db4-a570-42e9-b191-83c20f4712bd | 20 | 4878ae36-c754-4385-b482-ab806869e5b1 | - |
| 284 | Une liste d’ingrédients claire | b13c487f-d512-477d-a4d3-cc6409a868c4 | CHECKBOX | a8d79db4-a570-42e9-b191-83c20f4712bd | 20 | 087056b2-af30-4f39-b82f-408a56c5eb95 | hasOtherOption=true, maxChoices=2 |
| 285 | Une composition courte | 7832f56b-b682-49ec-9edd-12c186f8aead | CHECKBOX | a8d79db4-a570-42e9-b191-83c20f4712bd | 20 | b13c487f-d512-477d-a4d3-cc6409a868c4 | hasOtherOption=true, maxChoices=2 |
| 286 | L’origine des ingrédients | f4178a1c-2284-4001-840c-442a560045cc | CHECKBOX | a8d79db4-a570-42e9-b191-83c20f4712bd | 20 | 7832f56b-b682-49ec-9edd-12c186f8aead | hasOtherOption=true, maxChoices=2 |
| 287 | Des quantités et instructions précises | f91d9ac2-291e-4e78-8921-70a3dd99cf40 | CHECKBOX | a8d79db4-a570-42e9-b191-83c20f4712bd | 20 | f4178a1c-2284-4001-840c-442a560045cc | hasOtherOption=true, maxChoices=2 |
| 288 | Des analyses ou preuves concrètes | f21e4d7d-a8f2-4104-a647-151ae3f06606 | CHECKBOX | a8d79db4-a570-42e9-b191-83c20f4712bd | 20 | f91d9ac2-291e-4e78-8921-70a3dd99cf40 | hasOtherOption=true, maxChoices=2 |
| 289 | La possibilité de goûter le produit | 431c5c7f-36ee-47e1-909f-6d68da479fe7 | CHECKBOX | a8d79db4-a570-42e9-b191-83c20f4712bd | 20 | f21e4d7d-a8f2-4104-a647-151ae3f06606 | hasOtherOption=true, maxChoices=2 |
| 290 | L’avis d’un professionnel | 1b11377d-68b1-44de-822f-b01f84dcbc02 | CHECKBOX | a8d79db4-a570-42e9-b191-83c20f4712bd | 20 | 431c5c7f-36ee-47e1-909f-6d68da479fe7 | hasOtherOption=true, maxChoices=2 |
| 291 | La réputation de la marque | 9599a5d6-40c0-414f-987c-1c43d73459ab | CHECKBOX | a8d79db4-a570-42e9-b191-83c20f4712bd | 20 | 1b11377d-68b1-44de-822f-b01f84dcbc02 | hasOtherOption=true, maxChoices=2 |
| 292 | Autre | 2ecbe7a0-ee95-4019-810b-7e6f13389e15 | CHECKBOX | a8d79db4-a570-42e9-b191-83c20f4712bd | 20 | 9599a5d6-40c0-414f-987c-1c43d73459ab | hasOtherOption=true, isOtherOption=true, maxChoices=2 |
| 293 | Au cours des deux dernières années, avez-vous consommé des compléments alimentaires ? | b56f89bc-d3b2-4d3b-b102-9e390af46c09 | TITLE | 01ca02d6-e6bf-4628-b065-9401e84fbc85 | 20 | 2ecbe7a0-ee95-4019-810b-7e6f13389e15 | - |
| 294 | Oui, régulièrement | 0d5d7acf-f015-4258-8c68-c414efd3e713 | MULTIPLE_CHOICE_OPTION | 01ca02d6-e6bf-4628-b065-9401e84fbc85 | 20 | b56f89bc-d3b2-4d3b-b102-9e390af46c09 | - |
| 295 | Oui, occasionnellement | 7862828c-92c3-457a-b856-7f9ff54ef248 | MULTIPLE_CHOICE_OPTION | 01ca02d6-e6bf-4628-b065-9401e84fbc85 | 20 | 0d5d7acf-f015-4258-8c68-c414efd3e713 | - |
| 296 | J’en ai déjà consommé mais j’ai arrêté | c3fd1080-5fdb-48ff-8285-9f71066f5f6a | MULTIPLE_CHOICE_OPTION | 01ca02d6-e6bf-4628-b065-9401e84fbc85 | 20 | 7862828c-92c3-457a-b856-7f9ff54ef248 | - |
| 297 | Non, jamais | 9940cb5c-af79-4022-b31a-3b366f9b5837 | MULTIPLE_CHOICE_OPTION | 01ca02d6-e6bf-4628-b065-9401e84fbc85 | 20 | c3fd1080-5fdb-48ff-8285-9f71066f5f6a | - |
| 298 | Je préfère ne pas répondre | 2833322a-b933-47df-863e-c9390a09f5e1 | MULTIPLE_CHOICE_OPTION | 01ca02d6-e6bf-4628-b065-9401e84fbc85 | 20 | 9940cb5c-af79-4022-b31a-3b366f9b5837 | - |
| 299 | É21 – Freins et pédagogie | 1a861f74-58e6-4bb3-b6d2-8f3beaba762e | PAGE_BREAK | - | 21 | 2833322a-b933-47df-863e-c9390a09f5e1 | - |
| 300 | Qu’est-ce qui pourrait le plus vous faire hésiter à essayer l’option que vous préférez ? | 15d2372f-9f92-4d83-8fd8-f600f7a5b137 | TITLE | e44151fd-c589-4932-9e80-b9e26e79b84d | 21 | 1a861f74-58e6-4bb3-b6d2-8f3beaba762e | - |
| 301 | Le prix | fc8a2604-983c-4a8c-a901-489585d3ed55 | CHECKBOX | e44151fd-c589-4932-9e80-b9e26e79b84d | 21 | 15d2372f-9f92-4d83-8fd8-f600f7a5b137 | hasOtherOption=true, maxChoices=3 |
| 302 | Un doute sur son utilité | ad598257-49c5-430c-ab5e-61a82e37a564 | CHECKBOX | e44151fd-c589-4932-9e80-b9e26e79b84d | 21 | fc8a2604-983c-4a8c-a901-489585d3ed55 | hasOtherOption=true, maxChoices=3 |
| 303 | Un goût qui ne me conviendrait pas | d14bf9c0-9ec5-4e99-ba8d-e001dad277fd | CHECKBOX | e44151fd-c589-4932-9e80-b9e26e79b84d | 21 | ad598257-49c5-430c-ab5e-61a82e37a564 | hasOtherOption=true, maxChoices=3 |
| 304 | Une modification de la couleur du plat | be38a900-1916-4300-aef8-e6adc4037829 | CHECKBOX | e44151fd-c589-4932-9e80-b9e26e79b84d | 21 | d14bf9c0-9ec5-4e99-ba8d-e001dad277fd | hasOtherOption=true, maxChoices=3 |
| 305 | Une texture ou des morceaux visibles | 20c68ea8-754e-4f20-bc4a-e891a419f0b0 | CHECKBOX | e44151fd-c589-4932-9e80-b9e26e79b84d | 21 | be38a900-1916-4300-aef8-e6adc4037829 | hasOtherOption=true, maxChoices=3 |
| 306 | Le geste pendant la cuisson | d0325476-caa5-45cf-a4e6-7c8f3d2927a6 | CHECKBOX | e44151fd-c589-4932-9e80-b9e26e79b84d | 21 | 20c68ea8-754e-4f20-bc4a-e891a419f0b0 | hasOtherOption=true, maxChoices=3 |
| 307 | Le fait de devoir retirer un sachet | 1cc60f04-4d6e-4fcd-ae13-c3c1e34c0011 | CHECKBOX | e44151fd-c589-4932-9e80-b9e26e79b84d | 21 | d0325476-caa5-45cf-a4e6-7c8f3d2927a6 | hasOtherOption=true, maxChoices=3 |
| 308 | Un positionnement trop proche d’un complément alimentaire | 64088fc5-4e46-4585-a149-5869fbce77f2 | CHECKBOX | e44151fd-c589-4932-9e80-b9e26e79b84d | 21 | 1cc60f04-4d6e-4fcd-ae13-c3c1e34c0011 | hasOtherOption=true, maxChoices=3 |
| 309 | Le manque de preuves ou d’informations | 5a9c7305-571d-4427-addc-be506e704c62 | CHECKBOX | e44151fd-c589-4932-9e80-b9e26e79b84d | 21 | 64088fc5-4e46-4585-a149-5869fbce77f2 | hasOtherOption=true, maxChoices=3 |
| 310 | Rien en particulier | 5a6c3890-2ef7-46a0-a30c-0cb7322c1fc8 | CHECKBOX | e44151fd-c589-4932-9e80-b9e26e79b84d | 21 | 5a9c7305-571d-4427-addc-be506e704c62 | hasOtherOption=true, maxChoices=3 |
| 311 | Autre | ca1d25f9-9b1d-496d-bcd1-4048b058dba8 | CHECKBOX | e44151fd-c589-4932-9e80-b9e26e79b84d | 21 | 5a6c3890-2ef7-46a0-a30c-0cb7322c1fc8 | hasOtherOption=true, isOtherOption=true, maxChoices=3 |
| 312 | Si ce produit nécessitait une courte explication sur ses ingrédients et son utilisation, vous diriez plutôt… | d6689166-5b55-49da-8aa7-dbd25cf4e15a | TITLE | 67ff5d63-ae62-4464-ac82-bbb18eff3535 | 21 | ca1d25f9-9b1d-496d-bcd1-4048b058dba8 | - |
| 313 | J’aimerais comprendre en détail | a8fe75dd-9ac7-449b-8ffb-63b5ab91c97b | MULTIPLE_CHOICE_OPTION | 67ff5d63-ae62-4464-ac82-bbb18eff3535 | 21 | d6689166-5b55-49da-8aa7-dbd25cf4e15a | - |
| 314 | Une explication courte me suffirait | 6881e5bb-e822-4a91-9973-305a00070395 | MULTIPLE_CHOICE_OPTION | 67ff5d63-ae62-4464-ac82-bbb18eff3535 | 21 | a8fe75dd-9ac7-449b-8ffb-63b5ab91c97b | - |
| 315 | Je n’ai pas besoin d’explication | 32d453ab-723d-4cea-bc91-ce2264567713 | MULTIPLE_CHOICE_OPTION | 67ff5d63-ae62-4464-ac82-bbb18eff3535 | 21 | 6881e5bb-e822-4a91-9973-305a00070395 | - |
| 316 | Trop d’explications me décourageraient | a6aa49d7-cf91-4748-80e2-461503b235d2 | MULTIPLE_CHOICE_OPTION | 67ff5d63-ae62-4464-ac82-bbb18eff3535 | 21 | 32d453ab-723d-4cea-bc91-ce2264567713 | - |
| 317 | - | 91ef7232-e81b-47ac-b397-14c3392889a0 | CONDITIONAL_LOGIC | - | 21 | a6aa49d7-cf91-4748-80e2-461503b235d2 | see `## Logic rules` below |
| 318 | - | 21952bb0-7e2b-48b3-849c-b107af547106 | CONDITIONAL_LOGIC | - | 21 | 91ef7232-e81b-47ac-b397-14c3392889a0 | see `## Logic rules` below |
| 319 | - | cb21bcc4-1682-4af5-bfe5-787d40216cd3 | CONDITIONAL_LOGIC | - | 21 | 21952bb0-7e2b-48b3-849c-b107af547106 | see `## Logic rules` below |
| 320 | - | 958ee7ad-f7cf-4355-b9af-d4415b801597 | CONDITIONAL_LOGIC | - | 21 | cb21bcc4-1682-4af5-bfe5-787d40216cd3 | see `## Logic rules` below |
| 321 | - | 516bffad-d94d-4c75-8a09-f036ea6121f2 | CONDITIONAL_LOGIC | - | 21 | 958ee7ad-f7cf-4355-b9af-d4415b801597 | see `## Logic rules` below |
| 322 | Pour répondre aux questions de prix, quel format souhaitez-vous évaluer ? | d622034f-0e52-4193-b0c6-0ec1ac19133a | TITLE | c4f08f85-0c90-42d9-9665-3219cd41c764 | 21 | 516bffad-d94d-4c75-8a09-f036ea6121f2 | isHidden=true |
| 323 | Le format en sachet à retirer | ea5addf9-2c9c-4591-a575-228ffd3afbbc | MULTIPLE_CHOICE_OPTION | c4f08f85-0c90-42d9-9665-3219cd41c764 | 21 | d622034f-0e52-4193-b0c6-0ec1ac19133a | isHidden=true |
| 324 | Le format à doser et consommer avec le plat | 52b82763-7a99-4c6b-a3cf-3a67cbae5ee6 | MULTIPLE_CHOICE_OPTION | c4f08f85-0c90-42d9-9665-3219cd41c764 | 21 | ea5addf9-2c9c-4591-a575-228ffd3afbbc | isHidden=true |
| 325 | Je ne souhaite pas évaluer le prix | c61c8b24-2205-46f7-a5cf-5230edaa0f88 | MULTIPLE_CHOICE_OPTION | c4f08f85-0c90-42d9-9665-3219cd41c764 | 21 | 52b82763-7a99-4c6b-a3cf-3a67cbae5ee6 | isHidden=true |
| 326 | - | e8601398-5bb2-4425-9666-6ae0e4c079e7 | CONDITIONAL_LOGIC | - | 21 | c61c8b24-2205-46f7-a5cf-5230edaa0f88 | see `## Logic rules` below |
| 327 | - | 43db6383-8763-471d-a7d8-da51544b890a | CONDITIONAL_LOGIC | - | 21 | e8601398-5bb2-4425-9666-6ae0e4c079e7 | see `## Logic rules` below |
| 328 | É22 – Prix (format à doser – Fusion) | cbddf0d8-7a9b-4476-8474-119b19c17d82 | PAGE_BREAK | - | 22 | 43db6383-8763-471d-a7d8-da51544b890a | - |
| 329 | Imaginez un pot permettant environ 12 à 16 utilisations, sous forme de préparation à doser et à consommer avec le plat. Ce conditionnement reste exploratoire. | 48b7b56b-3abb-415f-9c06-9bf99f0e053e | TEXT | - | 22 | cbddf0d8-7a9b-4476-8474-119b19c17d82 | - |
| 330 | Pour ce format, quel prix vous semblerait acceptable ? | bc282cee-0c7e-4b6c-992e-d61173b78d30 | TITLE | fd7d80de-b393-4de7-a191-8a44b8130f67 | 22 | 48b7b56b-3abb-415f-9c06-9bf99f0e053e | - |
| 331 | Moins de 10 € | 1aa41073-9773-4c83-af7a-3558c4bc519b | MULTIPLE_CHOICE_OPTION | fd7d80de-b393-4de7-a191-8a44b8130f67 | 22 | bc282cee-0c7e-4b6c-992e-d61173b78d30 | - |
| 332 | 10 à 14,99 € | 43ccecae-51d0-4b40-8918-1835d5e2efc4 | MULTIPLE_CHOICE_OPTION | fd7d80de-b393-4de7-a191-8a44b8130f67 | 22 | 1aa41073-9773-4c83-af7a-3558c4bc519b | - |
| 333 | 15 à 19,99 € | 165e5bc4-9798-45b1-8604-8933eb1ac083 | MULTIPLE_CHOICE_OPTION | fd7d80de-b393-4de7-a191-8a44b8130f67 | 22 | 43ccecae-51d0-4b40-8918-1835d5e2efc4 | - |
| 334 | 20 à 24,99 € | 5a791e4c-7120-4137-be5f-7b8c0d8a61e0 | MULTIPLE_CHOICE_OPTION | fd7d80de-b393-4de7-a191-8a44b8130f67 | 22 | 165e5bc4-9798-45b1-8604-8933eb1ac083 | - |
| 335 | 25 à 29,99 € | 14bee4d1-ed45-42f4-bc4f-32a669da6cbf | MULTIPLE_CHOICE_OPTION | fd7d80de-b393-4de7-a191-8a44b8130f67 | 22 | 5a791e4c-7120-4137-be5f-7b8c0d8a61e0 | - |
| 336 | 30 € ou plus | 1ee32a9f-e187-4f1e-8c18-791a598e0b72 | MULTIPLE_CHOICE_OPTION | fd7d80de-b393-4de7-a191-8a44b8130f67 | 22 | 14bee4d1-ed45-42f4-bc4f-32a669da6cbf | - |
| 337 | Je ne sais pas | 1fef5a50-21e7-4e68-bc44-1794d667b267 | MULTIPLE_CHOICE_OPTION | fd7d80de-b393-4de7-a191-8a44b8130f67 | 22 | 1ee32a9f-e187-4f1e-8c18-791a598e0b72 | - |
| 338 | - | d04fb2d6-ec89-4c90-bd90-868a02b9281c | CONDITIONAL_LOGIC | - | 22 | 1fef5a50-21e7-4e68-bc44-1794d667b267 | see `## Logic rules` below |
| 339 | À 24,90 € — soit environ 1,60 à 2,10 € par utilisation — ce produit vous semblerait… | 1e9ca023-8bf9-4a92-90b9-e09d1494c129 | TITLE | 087ec777-6398-4299-9868-2400fa1eba64 | 22 | d04fb2d6-ec89-4c90-bd90-868a02b9281c | - |
| 340 | Beaucoup trop cher | 3b2e18f3-6b3a-4521-a415-e12f9671d90e | MULTIPLE_CHOICE_OPTION | 087ec777-6398-4299-9868-2400fa1eba64 | 22 | 1e9ca023-8bf9-4a92-90b9-e09d1494c129 | - |
| 341 | Un peu trop cher | ae90b6d8-10ba-4a9f-9666-5e8f66e53021 | MULTIPLE_CHOICE_OPTION | 087ec777-6398-4299-9868-2400fa1eba64 | 22 | 3b2e18f3-6b3a-4521-a415-e12f9671d90e | - |
| 342 | Acceptable | bfa5f02d-699c-4ff0-a133-ccf35e86f426 | MULTIPLE_CHOICE_OPTION | 087ec777-6398-4299-9868-2400fa1eba64 | 22 | ae90b6d8-10ba-4a9f-9666-5e8f66e53021 | - |
| 343 | Plutôt avantageux | 87872f2c-3449-470b-a036-305046897dc7 | MULTIPLE_CHOICE_OPTION | 087ec777-6398-4299-9868-2400fa1eba64 | 22 | bfa5f02d-699c-4ff0-a133-ccf35e86f426 | - |
| 344 | Très avantageux | 874e9c54-602c-4074-8e0f-ba940fb7e238 | MULTIPLE_CHOICE_OPTION | 087ec777-6398-4299-9868-2400fa1eba64 | 22 | 87872f2c-3449-470b-a036-305046897dc7 | - |
| 345 | Je ne sais pas | 1e81814f-9189-408c-9211-0f47b3deeb6c | MULTIPLE_CHOICE_OPTION | 087ec777-6398-4299-9868-2400fa1eba64 | 22 | 874e9c54-602c-4074-8e0f-ba940fb7e238 | - |
| 346 | Concrètement, à 24,90 €, achèteriez-vous ce produit ? | 423e2b88-8845-4a8b-bfe0-42ceb7da3ae9 | TITLE | 6b4a6d3b-ad5f-47c9-9ab1-8f03fd2b5aed | 22 | 1e81814f-9189-408c-9211-0f47b3deeb6c | - |
| 347 | Oui, certainement | 88c353f0-ef9b-4f23-88c2-45816ebfa8a1 | MULTIPLE_CHOICE_OPTION | 6b4a6d3b-ad5f-47c9-9ab1-8f03fd2b5aed | 22 | 423e2b88-8845-4a8b-bfe0-42ceb7da3ae9 | - |
| 348 | Oui, probablement | 8c18b455-9e85-4591-93e7-75dc6f341dac | MULTIPLE_CHOICE_OPTION | 6b4a6d3b-ad5f-47c9-9ab1-8f03fd2b5aed | 22 | 88c353f0-ef9b-4f23-88c2-45816ebfa8a1 | - |
| 349 | Peut-être | ac014161-26f6-472e-9df3-ca494eafb0b2 | MULTIPLE_CHOICE_OPTION | 6b4a6d3b-ad5f-47c9-9ab1-8f03fd2b5aed | 22 | 8c18b455-9e85-4591-93e7-75dc6f341dac | - |
| 350 | Probablement pas | 7c7b7646-61bf-4c90-9591-3cc42751ba99 | MULTIPLE_CHOICE_OPTION | 6b4a6d3b-ad5f-47c9-9ab1-8f03fd2b5aed | 22 | ac014161-26f6-472e-9df3-ca494eafb0b2 | - |
| 351 | Certainement pas | cf367a4c-e24e-4412-9d5c-da8762815a5a | MULTIPLE_CHOICE_OPTION | 6b4a6d3b-ad5f-47c9-9ab1-8f03fd2b5aed | 22 | 7c7b7646-61bf-4c90-9591-3cc42751ba99 | - |
| 352 | É23 – Prix (format sachet – Essence) | 9b042f94-bf15-4e6b-95ae-8a983c52aa41 | PAGE_BREAK | - | 23 | cf367a4c-e24e-4412-9d5c-da8762815a5a | - |
| 353 | Imaginez une boîte permettant environ 12 à 16 utilisations, sous forme de sachets à retirer après cuisson. Ce conditionnement reste exploratoire. | 0570f45c-58cd-435a-bc6b-ae623fb297b9 | TEXT | - | 23 | 9b042f94-bf15-4e6b-95ae-8a983c52aa41 | - |
| 354 | Pour ce format, quel prix vous semblerait acceptable ? | 3735b0e3-9fce-44c4-9dbc-92c1d9f33a3d | TITLE | 7b91f35c-b478-406b-ba77-c11e33d457db | 23 | 0570f45c-58cd-435a-bc6b-ae623fb297b9 | - |
| 355 | Moins de 10 € | 9955d301-3e77-4b21-a033-6ab0cc8577ae | MULTIPLE_CHOICE_OPTION | 7b91f35c-b478-406b-ba77-c11e33d457db | 23 | 3735b0e3-9fce-44c4-9dbc-92c1d9f33a3d | - |
| 356 | 10 à 14,99 € | 723aa46b-776d-44bb-b73e-10c4e2d3f3da | MULTIPLE_CHOICE_OPTION | 7b91f35c-b478-406b-ba77-c11e33d457db | 23 | 9955d301-3e77-4b21-a033-6ab0cc8577ae | - |
| 357 | 15 à 19,99 € | 4ac06035-1cb2-41c1-b190-ef900a52c137 | MULTIPLE_CHOICE_OPTION | 7b91f35c-b478-406b-ba77-c11e33d457db | 23 | 723aa46b-776d-44bb-b73e-10c4e2d3f3da | - |
| 358 | 20 à 24,99 € | ee9593a2-2e08-47d5-a0d5-488efd24019b | MULTIPLE_CHOICE_OPTION | 7b91f35c-b478-406b-ba77-c11e33d457db | 23 | 4ac06035-1cb2-41c1-b190-ef900a52c137 | - |
| 359 | 25 à 29,99 € | a494ab86-b80b-4962-a569-9e9ff3c38057 | MULTIPLE_CHOICE_OPTION | 7b91f35c-b478-406b-ba77-c11e33d457db | 23 | ee9593a2-2e08-47d5-a0d5-488efd24019b | - |
| 360 | 30 € ou plus | 04f5c87a-31bd-40bd-bf40-7bf0cedc9174 | MULTIPLE_CHOICE_OPTION | 7b91f35c-b478-406b-ba77-c11e33d457db | 23 | a494ab86-b80b-4962-a569-9e9ff3c38057 | - |
| 361 | Je ne sais pas | e633f594-2593-4e53-b8a9-6ce85ad8f37e | MULTIPLE_CHOICE_OPTION | 7b91f35c-b478-406b-ba77-c11e33d457db | 23 | 04f5c87a-31bd-40bd-bf40-7bf0cedc9174 | - |
| 362 | À 24,90 € — soit environ 1,60 à 2,10 € par utilisation — ce produit vous semblerait… | 80e35252-d46f-4edf-ad7c-e439cd83679d | TITLE | 65c74ac4-26d9-45d3-8df6-6cebb79432de | 23 | e633f594-2593-4e53-b8a9-6ce85ad8f37e | - |
| 363 | Beaucoup trop cher | 305a25b8-85f8-465c-bdd7-c315125e098b | MULTIPLE_CHOICE_OPTION | 65c74ac4-26d9-45d3-8df6-6cebb79432de | 23 | 80e35252-d46f-4edf-ad7c-e439cd83679d | - |
| 364 | Un peu trop cher | 749775b9-d6cc-4e19-b673-a94aa055f0e8 | MULTIPLE_CHOICE_OPTION | 65c74ac4-26d9-45d3-8df6-6cebb79432de | 23 | 305a25b8-85f8-465c-bdd7-c315125e098b | - |
| 365 | Acceptable | 0e3c51e2-4a64-45d6-81ad-c30e5ecc67dd | MULTIPLE_CHOICE_OPTION | 65c74ac4-26d9-45d3-8df6-6cebb79432de | 23 | 749775b9-d6cc-4e19-b673-a94aa055f0e8 | - |
| 366 | Plutôt avantageux | f5461dc1-6f28-4e50-a5fe-608a714b4889 | MULTIPLE_CHOICE_OPTION | 65c74ac4-26d9-45d3-8df6-6cebb79432de | 23 | 0e3c51e2-4a64-45d6-81ad-c30e5ecc67dd | - |
| 367 | Très avantageux | bd5a9a32-bcd8-425f-bdd2-c298da08695f | MULTIPLE_CHOICE_OPTION | 65c74ac4-26d9-45d3-8df6-6cebb79432de | 23 | f5461dc1-6f28-4e50-a5fe-608a714b4889 | - |
| 368 | Je ne sais pas | 6d1b7b8c-20fc-45fb-8bba-363c5a648e31 | MULTIPLE_CHOICE_OPTION | 65c74ac4-26d9-45d3-8df6-6cebb79432de | 23 | bd5a9a32-bcd8-425f-bdd2-c298da08695f | - |
| 369 | Concrètement, à 24,90 €, achèteriez-vous ce produit ? | b662ef8b-6538-4369-84f0-3e6bdc35433f | TITLE | e59f58a2-288f-4dc3-a117-82ddebfd46dc | 23 | 6d1b7b8c-20fc-45fb-8bba-363c5a648e31 | - |
| 370 | Oui, certainement | 5d5c5a11-bfb0-4046-a3ab-00a8bf7e7f09 | MULTIPLE_CHOICE_OPTION | e59f58a2-288f-4dc3-a117-82ddebfd46dc | 23 | b662ef8b-6538-4369-84f0-3e6bdc35433f | - |
| 371 | Oui, probablement | d87633b8-9230-4cfb-9ffc-7392dd899953 | MULTIPLE_CHOICE_OPTION | e59f58a2-288f-4dc3-a117-82ddebfd46dc | 23 | 5d5c5a11-bfb0-4046-a3ab-00a8bf7e7f09 | - |
| 372 | Peut-être | 38bf9489-103c-455d-8e49-578f689e1f26 | MULTIPLE_CHOICE_OPTION | e59f58a2-288f-4dc3-a117-82ddebfd46dc | 23 | d87633b8-9230-4cfb-9ffc-7392dd899953 | - |
| 373 | Probablement pas | cbc20012-5e94-4420-aa26-413d4fe02f8a | MULTIPLE_CHOICE_OPTION | e59f58a2-288f-4dc3-a117-82ddebfd46dc | 23 | 38bf9489-103c-455d-8e49-578f689e1f26 | - |
| 374 | Certainement pas | bd3246ad-1d5d-43d7-8bda-b76327e6ff19 | MULTIPLE_CHOICE_OPTION | e59f58a2-288f-4dc3-a117-82ddebfd46dc | 23 | cbc20012-5e94-4420-aa26-413d4fe02f8a | - |
| 375 | É24 – Usage et recontact | ed1d4630-7d57-4a57-9754-92c5a6e15a11 | PAGE_BREAK | - | 24 | bd3246ad-1d5d-43d7-8bda-b76327e6ff19 | - |
| 376 | Si vous aviez ce produit chez vous, à quelle fréquence pensez-vous que vous l’utiliseriez réellement ? | 4bf9216c-b11b-4208-9c37-b2e8a4590f45 | TITLE | 49ccbeab-4b21-489b-b862-a47b293c4ec6 | 24 | ed1d4630-7d57-4a57-9754-92c5a6e15a11 | - |
| 377 | Plusieurs fois par semaine | a6c9d7b9-a7ee-4c0a-851d-2f4217d2e194 | MULTIPLE_CHOICE_OPTION | 49ccbeab-4b21-489b-b862-a47b293c4ec6 | 24 | 4bf9216c-b11b-4208-9c37-b2e8a4590f45 | - |
| 378 | Environ une fois par semaine | be99c7ee-b43f-4462-bce6-5108bbcb2816 | MULTIPLE_CHOICE_OPTION | 49ccbeab-4b21-489b-b862-a47b293c4ec6 | 24 | a6c9d7b9-a7ee-4c0a-851d-2f4217d2e194 | - |
| 379 | Quelques fois par mois | d81909fe-18a1-41c7-9442-a4a279017507 | MULTIPLE_CHOICE_OPTION | 49ccbeab-4b21-489b-b862-a47b293c4ec6 | 24 | be99c7ee-b43f-4462-bce6-5108bbcb2816 | - |
| 380 | Plus rarement | 3a1ac373-a9ee-4f4d-8e2b-2a10c657eb8d | MULTIPLE_CHOICE_OPTION | 49ccbeab-4b21-489b-b862-a47b293c4ec6 | 24 | d81909fe-18a1-41c7-9442-a4a279017507 | - |
| 381 | Je l’essaierais par curiosité, mais je ne pense pas l’utiliser durablement | 74c74534-7a20-4c98-8781-15b78236d453 | MULTIPLE_CHOICE_OPTION | 49ccbeab-4b21-489b-b862-a47b293c4ec6 | 24 | 3a1ac373-a9ee-4f4d-8e2b-2a10c657eb8d | - |
| 382 | Je ne pense pas l’utiliser | a6f892b7-e8f1-4ef9-8e2f-0b5367370668 | MULTIPLE_CHOICE_OPTION | 49ccbeab-4b21-489b-b862-a47b293c4ec6 | 24 | 74c74534-7a20-4c98-8781-15b78236d453 | - |
| 383 | Puis-je conserver votre contact pour vous adresser des questions personnalisées ou vous proposer un futur test produit ? | ef299a2b-dddd-455c-a66c-2dc09043105d | TITLE | 50442e5c-4ebd-4184-88c5-d705083c6b0f | 24 | a6f892b7-e8f1-4ef9-8e2f-0b5367370668 | - |
| 384 | Oui | 4661cdec-31b0-4ca5-931a-6fa69fd0e67b | MULTIPLE_CHOICE_OPTION | 50442e5c-4ebd-4184-88c5-d705083c6b0f | 24 | ef299a2b-dddd-455c-a66c-2dc09043105d | - |
| 385 | Non | 42b1b03c-00ed-467a-922e-a10515b1b86a | MULTIPLE_CHOICE_OPTION | 50442e5c-4ebd-4184-88c5-d705083c6b0f | 24 | 4661cdec-31b0-4ca5-931a-6fa69fd0e67b | - |
| 386 | - | 13374597-ca88-4e7c-aed3-b26b284882be | CONDITIONAL_LOGIC | - | 24 | 42b1b03c-00ed-467a-922e-a10515b1b86a | see `## Logic rules` below |
| 387 | É25 – Email | 8a47dd59-8af6-4579-8c37-f36dc22ec00d | PAGE_BREAK | - | 25 | 13374597-ca88-4e7c-aed3-b26b284882be | - |
| 388 | Votre email sera utilisé uniquement pour vous recontacter au sujet de cette enquête ou d’un futur test produit. Il ne sera pas utilisé à des fins commerciales sans votre accord. | 5ebbc6d3-05e3-4812-a3b6-e8d009ee1022 | TEXT | - | 25 | 8a47dd59-8af6-4579-8c37-f36dc22ec00d | - |
| 389 | Votre email | 46d1ede9-285e-438d-8981-9268787a7482 | TITLE | ff4a3253-6a31-46e0-b45b-5c48a5cf0531 | 25 | 5ebbc6d3-05e3-4812-a3b6-e8d009ee1022 | - |
| 390 | - | 2d534671-3d88-4531-95a8-b67843f2bb8f | INPUT_EMAIL | ff4a3253-6a31-46e0-b45b-5c48a5cf0531 | 25 | 46d1ede9-285e-438d-8981-9268787a7482 | - |
| 391 | É26 – Remerciement | 5d775073-f2a2-4442-90e2-d9fcbc32694b | PAGE_BREAK | - | 26 | 2d534671-3d88-4531-95a8-b67843f2bb8f | isThankYouPage=true, isQualifiedForThankYouPage=true |
| 392 | Merci — vos réponses sont enregistrées. Elles vont directement aider à mieux comprendre les usages culinaires du quotidien. | ed196cca-c94a-464f-bc9f-b7a574b661b5 | TEXT | - | 26 | 5d775073-f2a2-4442-90e2-d9fcbc32694b | - |

## Logic rules

| logicRule_blockUuid | when | then |
| - | - | - |
| 8dfbf196-9971-4c55-8fda-c102b018b49b | 9f6e6906-86da-45eb-b58d-06d698683735 IS 8f2cdf95-e30a-4d0a-a4de-6852c4af32fe AND 285cfee7-4eb0-4935-ac3d-43e4701d18f3 IS "v2" | CALCULATE 0f6debe2-fc6c-4a48-9492-394832aa0066 = "v2" |
| 5c94b2e0-0c75-4b71-bd36-94214189f46b | 9f6e6906-86da-45eb-b58d-06d698683735 IS 8f2cdf95-e30a-4d0a-a4de-6852c4af32fe AND 0f6debe2-fc6c-4a48-9492-394832aa0066 IS "v1" | SHOW 0b2ba077-c403-4b8d-820d-c64467cf86c5 |
| 7970afaf-d6ee-4921-80ba-161a02fa4281 | 9f6e6906-86da-45eb-b58d-06d698683735 IS 8f2cdf95-e30a-4d0a-a4de-6852c4af32fe AND 0f6debe2-fc6c-4a48-9492-394832aa0066 IS "v1" | SHOW d3cfe418-4c63-497d-a318-39efb76d8c1b |
| a1cecc9d-0904-4f0e-892e-e4aece266dda | 9f6e6906-86da-45eb-b58d-06d698683735 IS 8f2cdf95-e30a-4d0a-a4de-6852c4af32fe AND 0f6debe2-fc6c-4a48-9492-394832aa0066 IS "v2" | SHOW ed849ce0-9f87-4711-a52c-6b007a0eae9f |
| 5870d415-0933-443b-9476-8884ccb1e85c | 9f6e6906-86da-45eb-b58d-06d698683735 IS 8f2cdf95-e30a-4d0a-a4de-6852c4af32fe AND 0f6debe2-fc6c-4a48-9492-394832aa0066 IS "v2" | SHOW 654cca42-9548-4849-8143-ad2194eaf3bd |
| 93302922-917c-4371-a158-fa313f9951f1 | 56528099-3033-433f-8bd4-124cf4d0f82a IS 8d84b4b8-1974-4b57-9582-5541572bb971 | CALCULATE f8498a80-213c-4d04-9afa-86a519c6552e = "low_or_no_cooking" |
| b3729b35-8495-4532-ba6f-8ca0d09782fc | 56528099-3033-433f-8bd4-124cf4d0f82a IS 8d84b4b8-1974-4b57-9582-5541572bb971 | JUMP TO PAGE 7 |
| c8338ccb-e5a4-4807-871c-55949071fbb8 | 56528099-3033-433f-8bd4-124cf4d0f82a IS 8d84b4b8-1974-4b57-9582-5541572bb971 | HIDE 676c7d78-cce2-44a0-94d1-e718dfde986f |
| 2757ca71-3e00-47e5-97bc-b5c748e612ae | 56528099-3033-433f-8bd4-124cf4d0f82a IS 8d84b4b8-1974-4b57-9582-5541572bb971 | HIDE 428b17ff-5272-46d1-90df-c85dfad57528 |
| f24344ea-0a25-468a-b072-15f82ea61fbf | 98cc417e-10e7-483d-9751-79050d7c4a2b IS NOT ANY OF (709867b7-4f68-4738-9776-8c1bb906e614, 55494128-1086-404d-8482-3f5bad3d8d92, 581ae6af-2582-4723-82ab-5953323eb06f, 94119472-2d3a-4e73-8d4e-d1a9a828ace7) | HIDE bc43430c-e159-4caf-8a9c-f837aa531f36 |
| 54fdc041-afbf-4526-9aa2-ea291c385182 | 928bd7c4-6eec-4608-b960-6db6b6641973 IS 3ac09da9-599e-4ae4-ad19-121105f6da7b | SHOW a9c61764-bdaa-4757-9f8d-353861c2cdac |
| 7c19f06f-0cf7-4966-a49e-3bb773385bfa | 928bd7c4-6eec-4608-b960-6db6b6641973 IS 3ac09da9-599e-4ae4-ad19-121105f6da7b AND a9c61764-bdaa-4757-9f8d-353861c2cdac IS 653e901b-f788-46b6-8b27-3a6caede636b | SHOW c4f08f85-0c90-42d9-9665-3219cd41c764 |
| 9c751b70-da2b-4681-8805-9ef7c9ef2a80 | 928bd7c4-6eec-4608-b960-6db6b6641973 IS 3ac09da9-599e-4ae4-ad19-121105f6da7b AND a9c61764-bdaa-4757-9f8d-353861c2cdac IS 601befb3-a21b-48bc-a9a5-0d8782cdff87 | SHOW c4f08f85-0c90-42d9-9665-3219cd41c764 |
| 24addaa5-3f5b-49af-8561-e119142de723 | 928bd7c4-6eec-4608-b960-6db6b6641973 IS 3ac09da9-599e-4ae4-ad19-121105f6da7b AND a9c61764-bdaa-4757-9f8d-353861c2cdac IS 43378da9-4d9c-428b-9543-00363b020397 | SHOW c4f08f85-0c90-42d9-9665-3219cd41c764 |
| b0b2bb7a-086e-4776-ae81-ec0ab0ddf3ba | 9dc61692-42ed-4ac5-af4d-0daaa5e50045 IS ANY OF (f4038ea2-3372-4f78-9bea-4cfeb7c8c2b6, 225ab8d5-b973-4588-aa09-6738d5e42f74) | SHOW d969f67a-eda7-42c5-aebc-d501839feafe |
| 9c52fcb6-b912-44a2-952e-926e12bd6e1b | 0f9c2dd0-1528-4ac5-9dce-fe6f5fde5189 IS ANY OF (549b29f3-a52e-4387-b09a-5b2c9ce206bc, 7f441cfb-0b7f-42a2-ab71-e79062e411dc, 966f8f3f-1a21-4c3c-bbab-fc40635b8914, 5abbe61f-94a3-49b5-bec9-e0e741b1e45b) | SHOW f894196e-2081-4f05-bf0d-3dea9334d9e2 |
| d5d85a42-67f4-4dfb-aacc-2c36ab9b70ea | 0f9c2dd0-1528-4ac5-9dce-fe6f5fde5189 IS ANY OF (8ce2dbed-5ea6-439c-aeba-b656b95fbf61, 56858fe0-d696-4b22-b967-1e1f303523c0) | SHOW 122f7fc8-b993-4762-96d6-48f3647c035c |
| 91ef7232-e81b-47ac-b397-14c3392889a0 | 0f6debe2-fc6c-4a48-9492-394832aa0066 IS "v1" AND 928bd7c4-6eec-4608-b960-6db6b6641973 IS f2c1b5c3-11bb-44bf-875c-38ac0fd73c98 AND 67ff5d63-ae62-4464-ac82-bbb18eff3535 IS NOT EMPTY | JUMP TO PAGE 23 |
| 21952bb0-7e2b-48b3-849c-b107af547106 | 0f6debe2-fc6c-4a48-9492-394832aa0066 IS "v2" AND 928bd7c4-6eec-4608-b960-6db6b6641973 IS bfa8d806-a460-47c1-9724-2cb463a5cba3 AND 67ff5d63-ae62-4464-ac82-bbb18eff3535 IS NOT EMPTY | JUMP TO PAGE 23 |
| cb21bcc4-1682-4af5-bfe5-787d40216cd3 | 0f6debe2-fc6c-4a48-9492-394832aa0066 IS "v1" AND a9c61764-bdaa-4757-9f8d-353861c2cdac IS 51813e71-404b-4643-bfdd-69cec5017a0c AND 67ff5d63-ae62-4464-ac82-bbb18eff3535 IS NOT EMPTY | JUMP TO PAGE 23 |
| 958ee7ad-f7cf-4355-b9af-d4415b801597 | 0f6debe2-fc6c-4a48-9492-394832aa0066 IS "v2" AND a9c61764-bdaa-4757-9f8d-353861c2cdac IS 5bdabae9-0c3b-43bc-951b-64f985640df3 AND 67ff5d63-ae62-4464-ac82-bbb18eff3535 IS NOT EMPTY | JUMP TO PAGE 23 |
| 516bffad-d94d-4c75-8a09-f036ea6121f2 | 928bd7c4-6eec-4608-b960-6db6b6641973 IS b38ee722-169a-4858-8bc9-13ec531970fb AND 67ff5d63-ae62-4464-ac82-bbb18eff3535 IS NOT EMPTY | JUMP TO PAGE 24 |
| e8601398-5bb2-4425-9666-6ae0e4c079e7 | c4f08f85-0c90-42d9-9665-3219cd41c764 IS ea5addf9-2c9c-4591-a575-228ffd3afbbc | JUMP TO PAGE 23 |
| 43db6383-8763-471d-a7d8-da51544b890a | c4f08f85-0c90-42d9-9665-3219cd41c764 IS c61c8b24-2205-46f7-a5cf-5230edaa0f88 | JUMP TO PAGE 24 |
| d04fb2d6-ec89-4c90-bd90-868a02b9281c | fd7d80de-b393-4de7-a191-8a44b8130f67 IS NOT EMPTY | JUMP TO PAGE 24 |
| 13374597-ca88-4e7c-aed3-b26b284882be | 50442e5c-4ebd-4184-88c5-d705083c6b0f IS 42b1b03c-00ed-467a-922e-a10515b1b86a | JUMP TO PAGE 26 |

## Page flow

Page 1 -> Page 2 -> Page 3 -> Page 4 -> Page 5 -> Page 6 -> Page 7 -> Page 8 -> Page 9 -> Page 10 -> Page 11 -> Page 12 -> Page 13 -> Page 14 -> Page 15 -> Page 16 -> Page 17 -> Page 18 -> Page 19 -> Page 20 -> Page 21 -> Page 22 -> Page 23 -> Page 24 -> Page 25 -> Page 26 (Thank You)
  - Rule: Page 3 may jump to Page 7
  - Rule: Page 21 may jump to Page 23
  - Rule: Page 21 may jump to Page 23
  - Rule: Page 21 may jump to Page 23
  - Rule: Page 21 may jump to Page 23
  - Rule: Page 21 may jump to Page 24
  - Rule: Page 21 may jump to Page 23
  - Rule: Page 21 may jump to Page 24
  - Rule: Page 22 may jump to Page 24
  - Rule: Page 24 may jump to Page 26 (Thank You)
