# Notes de design et d'architecture

## Choix de la base

Le fichier `QUINTALYS_Pitch_Foodshaker_Phase3.html` a été retenu comme base. Raisons :
- Design system complet déjà intégré (palette 7 familles, typographie 3 polices)
- Structure cohérente avec le brief Foodshaker
- Support print/PDF natif

## Condensation 13 → 11 slides

| Phase 3 (13 slides) | V1 finale (11 slides) | Action |
|---|---|---|
| Slides 2+3 (marché) | Slide 2 | Fusionnées — 2 chiffres-clés + quote |
| Slides 5+6 (solution + science) | Slides 4+5 | Séparées mais allégées |
| Slide 10 (exécution) + 11 (roadmap) | Slide 9 | Fusionnées — stats + timeline compacte |

## Architecture technique

**Single-file HTML** — délibéré pour la stabilité en présentation live :
- Pas de dépendance à un framework (Reveal.js, Impress, etc.)
- Pas de build nécessaire
- Fonctionne offline (seules les Google Fonts nécessitent le réseau)
- Un seul fichier à ouvrir = zéro risque de chemin cassé

**Navigation :** vanilla JS, ~40 lignes. Supporte clavier, tactile, clic.

**Responsive :** la slide-inner se centre et se dimensionne en conservant le ratio 16:9 quelle que soit la fenêtre.

## Principes visuels

- Max 3-4 blocs visuels par slide (pas de tableaux denses)
- Typographie comme hiérarchie principale (pas d'icônes décoratifs)
- Quote-blocks pour les phrases-mémoire (ancrage émotionnel)
- Transition fade-only (360ms) — pas de slide/zoom/parallax
- Contraste renforcé pour projection (backgrounds sombres + or/crème)

## Positionnement respecté

- Aucune allégation santé directe
- Vocabulaire : "formulation culinaire fonctionnelle", "condiments", "food science appliquée"
- Pas de "boost", "super-aliment", "détox", "miracle"
- Positionnement : levier culinaire intelligent ≠ complément alimentaire
