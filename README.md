# QUINTALYS · Pitch Foodshaker 2026

Présentation HTML premium pour le pitch de candidature au programme Foodshaker (ISARA Lyon, mai 2026).

## Lancer la présentation

Ouvrir `slides/index.html` dans un navigateur (Chrome recommandé pour le rendu typographique).

**Mode plein écran :** F11 dans le navigateur.

### Navigation

| Action | Contrôle |
|--------|----------|
| Slide suivante | → / Espace / Clic (droite 2/3) / Swipe gauche |
| Slide précédente | ← / Clic (gauche 1/3) / Swipe droite |
| Première slide | Home |
| Dernière slide | End |

## Structure du projet

```
quintalys-foodshaker-deck/
├── slides/
│   └── index.html          ← Présentation principale (11 slides)
├── assets/
│   ├── quintalys-logo.png
│   ├── quintalys-logo-transparent.png
│   └── quintexor-logo.png
├── design-system/
│   └── tokens.css          ← Variables couleurs, typo, spacing
├── scripts/
│   └── export-pdf.md       ← Instructions export PDF
├── export/
│   └── (fichier PDF généré)
└── README.md
```

## Exporter en PDF

### Méthode 1 — Chrome Print (recommandé)

1. Ouvrir `slides/index.html` dans Chrome
2. Ctrl+P (ou Cmd+P sur Mac)
3. Destination : "Enregistrer au format PDF"
4. Orientation : Paysage
5. Marges : Aucune
6. Cocher "Graphiques d'arrière-plan"
7. Enregistrer dans `export/`

### Méthode 2 — Impression directe

Le fichier intègre `@media print` qui force chaque slide en pleine page paysage.

## Modifier le contenu

Toutes les slides sont dans `slides/index.html`. Chaque slide est une `<section class="slide">` avec son thème (classe sur `.slide-inner`).

### Thèmes disponibles

- `theme-copper` — Fond cuivre (titre, positionnement)
- `theme-ivory` — Fond ivoire (marché, stratégie, exécution)
- `theme-science` — Fond violet nuit (science, preuve)
- `theme-ingredient` — Fond vert pâle (solution)
- `theme-structure` — Fond brun cacao (réglementaire, conclusion)
- `theme-tips` — Fond terracotta pâle (Foodshaker)

## Design system

Palette QUINTEXOR/QUINTALYS : 7 familles sémantiques × 3 niveaux (saturé/médian/pâle).
Typographie : Imperial Script (display) · Cormorant Garamond (corps) · Amiri (labels).
Animations : fade 360ms, cubic-bezier(0.22, 0.61, 0.36, 1).

## Positionnement (rappel)

QUINTALYS formule des condiments culinaires pensés pour activer le potentiel bioactif du repas, sans sortir du cadre alimentaire. Ce n'est pas une marque "santé" ni un complément alimentaire.
