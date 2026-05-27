#!/usr/bin/env python3
"""QUINTALYS × Foodshaker ISARA 2026 — Premium Pitch Deck Generator"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from pptx.oxml import parse_xml

# ═══════════════════════════════════════════════════════════════
# DESIGN SYSTEM — QUINTALYS Premium Dark
# ═══════════════════════════════════════════════════════════════
BG      = RGBColor(0x0A, 0x0B, 0x0F)
BG2     = RGBColor(0x12, 0x13, 0x1C)
BG3     = RGBColor(0x1A, 0x1C, 0x2E)
GOLD    = RGBColor(0xC9, 0xA9, 0x6E)
GOLD_L  = RGBColor(0xE8, 0xD5, 0xA3)
GOLD_D  = RGBColor(0x7A, 0x62, 0x3A)
GREEN   = RGBColor(0x14, 0x26, 0x1C)
GREEN_M = RGBColor(0x20, 0x40, 0x30)
GREEN_L = RGBColor(0x35, 0x6A, 0x52)
PHARM   = RGBColor(0x0C, 0x0E, 0x22)
COLD    = RGBColor(0x48, 0x58, 0x9E)
WHITE_W = RGBColor(0xF0, 0xEB, 0xE1)
CREAM   = RGBColor(0xF5, 0xF0, 0xE8)
GREY    = RGBColor(0x82, 0x82, 0x82)
GREY_D  = RGBColor(0x28, 0x28, 0x38)

FH = "Palatino Linotype"
FB = "Calibri"
FL = "Calibri Light"

SW, SH = Inches(13.33), Inches(7.5)
ML = Inches(0.85)

prs = Presentation()
prs.slide_width = SW
prs.slide_height = SH
BLANK = prs.slide_layouts[6]

_c = [500]

def nid(n=1):
    r = list(range(_c[0], _c[0] + n))
    _c[0] += n
    return r if n > 1 else r[0]


# ── Primitives ─────────────────────────────────────────────────

def sl():
    s = prs.slides.add_slide(BLANK)
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = BG
    return s

def set_bg(s, c):
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = c

def R(s, l, t, w, h, f=BG2, lc=None, lw=Pt(0.5)):
    sp = s.shapes.add_shape(1, l, t, w, h)
    if f:
        sp.fill.solid()
        sp.fill.fore_color.rgb = f
    else:
        sp.fill.background()
    if lc:
        sp.line.color.rgb = lc
        sp.line.width = lw
    else:
        sp.line.fill.background()
    return sp

def O(s, l, t, w, h, f=GREEN, lc=None, lw=Pt(0.5)):
    sp = s.shapes.add_shape(9, l, t, w, h)
    if f:
        sp.fill.solid()
        sp.fill.fore_color.rgb = f
    else:
        sp.fill.background()
    if lc:
        sp.line.color.rgb = lc
        sp.line.width = lw
    else:
        sp.line.fill.background()
    return sp

def T(s, txt, l, t, w, h, fn=FB, fs=Pt(12), fc=WHITE_W,
      b=False, it=False, al=PP_ALIGN.LEFT, wrap=True):
    box = s.shapes.add_textbox(l, t, w, h)
    tf = box.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = al
    r = p.add_run()
    r.text = txt
    r.font.name = fn
    r.font.size = fs
    r.font.color.rgb = fc
    r.font.bold = b
    r.font.italic = it
    return box

def TL(s, lines, l, t, w, h, al=PP_ALIGN.LEFT, wrap=True):
    """Multi-line. lines = [(text, font, size, color, bold), ...]"""
    box = s.shapes.add_textbox(l, t, w, h)
    tf = box.text_frame
    tf.word_wrap = wrap
    for i, (txt2, fn, fs, fc, b) in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = al
        if txt2:
            r = p.add_run()
            r.text = txt2
            r.font.name = fn
            r.font.size = fs
            r.font.color.rgb = fc
            r.font.bold = b
    return box

def LN(s, x1, y1, x2, y2, c=GOLD, w=Pt(0.75)):
    cn = s.shapes.add_connector(1, x1, y1, x2, y2)
    cn.line.color.rgb = c
    cn.line.width = w
    return cn

def get_sid(shape):
    try:
        return shape._element.nvSpPr.cNvPr.id
    except Exception:
        try:
            return shape._element.nvCxnSpPr.cNvPr.id
        except Exception:
            return None

def NOTE(s, t):
    s.notes_slide.notes_text_frame.text = t

def ANIM(s, shapes, dur=700):
    """Fade-in on click for each shape in list (one click per shape)."""
    pars, blds = [], []
    for i, sh in enumerate(shapes):
        spid = get_sid(sh)
        if not spid:
            continue
        c, pe, st, ai = nid(4)
        pars.append(
            f'<p:par>'
            f'<p:cTn id="{c}" fill="hold">'
            f'<p:stCondLst><p:cond delay="indefinite"/></p:stCondLst>'
            f'<p:childTnLst><p:par>'
            f'<p:cTn id="{pe}" presetID="10" presetClass="entr" presetSubtype="0"'
            f' fill="hold" grpId="{i}" nodeType="clickEffect">'
            f'<p:stCondLst><p:cond delay="0"/></p:stCondLst>'
            f'<p:childTnLst>'
            f'<p:set><p:cBhvr>'
            f'<p:cTn id="{st}" dur="1" fill="hold"/>'
            f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl>'
            f'<p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst>'
            f'</p:cBhvr><p:to><p:strVal val="visible"/></p:to></p:set>'
            f'<p:animEffect transition="in" filter="fade">'
            f'<p:cBhvr><p:cTn id="{ai}" dur="{dur}"/>'
            f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl>'
            f'</p:cBhvr></p:animEffect>'
            f'</p:childTnLst>'
            f'</p:cTn>'
            f'</p:par></p:childTnLst>'
            f'</p:cTn></p:par>'
        )
        blds.append(f'<p:bldP spid="{spid}" grpId="{i}" uiExpand="1" build="p"/>')

    if not pars:
        return
    root, seq = nid(2)
    xml = (
        f'<p:timing'
        f' xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"'
        f' xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"'
        f' xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        f'<p:tnLst><p:par>'
        f'<p:cTn id="{root}" dur="indefinite" restart="whenNotActive" nodeType="tmRoot">'
        f'<p:childTnLst>'
        f'<p:seq concurrent="1" nextAc="seek">'
        f'<p:cTn id="{seq}" dur="indefinite" nodeType="mainSeq">'
        f'<p:childTnLst>{"".join(pars)}</p:childTnLst>'
        f'</p:cTn>'
        f'<p:prevCondLst>'
        f'<p:cond evt="onPrevClick" delay="0"><p:tn/></p:cond>'
        f'</p:prevCondLst>'
        f'</p:seq>'
        f'</p:childTnLst>'
        f'</p:cTn>'
        f'</p:par></p:tnLst>'
        f'<p:bldLst>{"".join(blds)}</p:bldLst>'
        f'</p:timing>'
    )
    try:
        el = parse_xml(xml)
        se = s._element
        ex = se.find(qn('p:timing'))
        if ex is not None:
            se.remove(ex)
        se.append(el)
    except Exception as e:
        print(f'  [anim] {e}')


# ═══════════════════════════════════════════════════════════════
# SLIDE 1 — COUVERTURE
# ═══════════════════════════════════════════════════════════════
s1 = sl()

# Background botanical mass (right side)
s1_blob1 = O(s1, Inches(6.8), Inches(-0.8), Inches(7.5), Inches(6.2), f=GREEN)
s1_blob2 = O(s1, Inches(8.5), Inches(0.8), Inches(5.5), Inches(7.2), f=GREEN_M)
s1_warm  = R(s1, Inches(6.5), Inches(0), Inches(6.83), SH,
             f=RGBColor(0x16, 0x12, 0x08))

# Left gold vertical accent
s1_vline = LN(s1, Inches(0.58), Inches(1.1), Inches(0.58), Inches(6.4),
              c=GOLD, w=Pt(2))

# QUINTALYS title
s1_title = T(s1, "QUINTALYS",
             Inches(0.9), Inches(1.3), Inches(8), Inches(1.7),
             fn=FH, fs=Pt(72), fc=GOLD_L, b=True)

# Gold divider
s1_div = LN(s1, Inches(0.9), Inches(3.15), Inches(5.8), Inches(3.15),
            c=GOLD, w=Pt(0.75))

# Subtitle
s1_sub = TL(s1, [
    ("Réhabiliter la cuisine", FH, Pt(26), WHITE_W, False),
    ("comme terrain de formulation culinaire", FH, Pt(26), GOLD_L, False),
], Inches(0.9), Inches(3.3), Inches(8.2), Inches(1.6))

# Name tag
s1_name = T(s1, "Noelly Sterlin  ·  ISARA Foodshaker 2026",
            Inches(0.9), Inches(5.6), Inches(7), Inches(0.55),
            fn=FL, fs=Pt(13), fc=GREY, it=True)

# Logo mark
s1_logo_bg = O(s1, Inches(11.6), Inches(5.85), Inches(0.88), Inches(0.88), f=GOLD)
s1_logo_t  = T(s1, "Q",
               Inches(11.6), Inches(5.8), Inches(0.88), Inches(0.9),
               fn=FH, fs=Pt(36), fc=BG, b=True, al=PP_ALIGN.CENTER)

NOTE(s1, "ANIMATION: Entrée lente atmosphérique. "
         "Blob vert → ligne or → titre → divider + sous-titre → nom → logo. "
         "Durée: 800ms/élément. Ton immersif.")

ANIM(s1, [s1_blob1, s1_blob2, s1_warm,
          s1_vline, s1_title, s1_div, s1_sub,
          s1_name, s1_logo_bg, s1_logo_t], dur=800)


# ═══════════════════════════════════════════════════════════════
# SLIDE 2 — CONSTATS + PARADOXE
# ═══════════════════════════════════════════════════════════════
s2 = sl()

# Left panel (pharmaceutical / cold)
s2_left  = R(s2, Inches(0), Inches(0), Inches(6.3), SH, f=PHARM)
# Right panel (botanical / warm)
s2_right = R(s2, Inches(6.9), Inches(0), Inches(6.43), SH, f=GREEN)
# Center vertical divider
s2_cdiv  = LN(s2, Inches(6.665), Inches(0.3), Inches(6.665), Inches(7.2),
              c=GOLD, w=Pt(1))

# Left: pharmaceutical shapes (capsule ovals)
s2_pill1 = O(s2, Inches(1.0), Inches(1.2), Inches(1.4), Inches(0.55), f=COLD)
s2_pill2 = O(s2, Inches(2.8), Inches(1.0), Inches(1.4), Inches(0.55), f=COLD)
s2_pill3 = O(s2, Inches(1.6), Inches(2.0), Inches(1.4), Inches(0.55), f=COLD)
s2_pill4 = O(s2, Inches(3.5), Inches(2.2), Inches(0.9), Inches(0.9),
             f=RGBColor(0x30, 0x3A, 0x78))
s2_pill5 = O(s2, Inches(0.8), Inches(3.1), Inches(1.1), Inches(1.1),
             f=RGBColor(0x2A, 0x34, 0x68))

# Left labels
s2_llbl = TL(s2, [
    ("COMPLÉMENT", FL, Pt(11), COLD, False),
    ("ALIMENTAIRE", FL, Pt(11), COLD, False),
    ("", FL, Pt(6), COLD, False),
    ("gélules · poudres · routine", FL, Pt(10), GREY, False),
], Inches(0.7), Inches(4.5), Inches(5.5), Inches(1.8),
   al=PP_ALIGN.CENTER)

# Right: botanical / food shapes
s2_veg1 = O(s2, Inches(7.3), Inches(0.8), Inches(2.2), Inches(2.2), f=GREEN_M)
s2_veg2 = O(s2, Inches(9.8), Inches(1.2), Inches(1.6), Inches(1.6), f=GREEN_M)
s2_veg3 = O(s2, Inches(8.2), Inches(2.8), Inches(1.8), Inches(1.8), f=GREEN_L)
s2_veg4 = O(s2, Inches(10.8), Inches(2.5), Inches(2.2), Inches(2.2), f=GREEN_M)

# Right labels
s2_rlbl = TL(s2, [
    ("CUISINE", FL, Pt(11), GREEN_L, False),
    ("FONCTIONNELLE", FL, Pt(11), GREEN_L, False),
    ("", FL, Pt(6), GREEN_L, False),
    ("repas · cuisson · végétal", FL, Pt(10), GREY, False),
], Inches(7.0), Inches(4.5), Inches(6.0), Inches(1.8),
   al=PP_ALIGN.CENTER)

# Central question overlay
s2_qbg  = R(s2, Inches(2.2), Inches(5.1), Inches(8.9), Inches(1.9),
            f=RGBColor(0x08, 0x09, 0x12),
            lc=GOLD, lw=Pt(0.5))
s2_qtxt = T(s2,
            "Et si la fonctionnalité était progressivement sortie du repas ?",
            Inches(2.5), Inches(5.3), Inches(8.3), Inches(1.4),
            fn=FH, fs=Pt(20), fc=GOLD_L, al=PP_ALIGN.CENTER, wrap=True)

NOTE(s2, "ANIMATION: Panneau gauche (pharma) → Panneau droit (food) → "
         "Formes pharmaceutiques → Formes végétales → "
         "Divider central → Question finale. Émotion: questionnement.")

ANIM(s2, [s2_left, s2_right,
          s2_pill1, s2_pill2, s2_pill3, s2_pill4, s2_pill5, s2_llbl,
          s2_veg1, s2_veg2, s2_veg3, s2_veg4, s2_rlbl,
          s2_cdiv, s2_qbg, s2_qtxt], dur=600)


# ═══════════════════════════════════════════════════════════════
# SLIDE 3 — CUISINE = FORMULATION
# ═══════════════════════════════════════════════════════════════
s3 = sl()

# Title
s3_title = T(s3, "La cuisine n'est pas neutre",
             Inches(0.85), Inches(0.35), Inches(11.63), Inches(0.9),
             fn=FH, fs=Pt(38), fc=GOLD_L, b=False, al=PP_ALIGN.CENTER)
s3_titdiv = LN(s3, Inches(3.5), Inches(1.35), Inches(9.83), Inches(1.35),
               c=GOLD, w=Pt(0.5))

# Center hub (matrice alimentaire)
cx, cy = Inches(6.05), Inches(3.25)
cw, ch = Inches(2.3), Inches(2.3)
s3_hub_bg = O(s3, cx - cw/2, cy - ch/2, cw, ch, f=GREEN_M,
              lc=GOLD, lw=Pt(1.2))
s3_hub_t  = T(s3, "MATRICE\nALIMENTAIRE",
              cx - cw/2, cy - Inches(0.42), cw, Inches(0.84),
              fn=FL, fs=Pt(11), fc=GOLD_L, b=True,
              al=PP_ALIGN.CENTER, wrap=True)

# 5 satellites — positions around center
import math
satellites = [
    ("Chaleur",       2.0,  2.0),
    ("Eau",           4.2,  1.0),
    ("Broyage",       8.5,  1.2),
    ("Associations", 10.0,  3.4),
    ("Cuisson",       3.5,  5.4),
]
s3_sats, s3_lines, s3_slbls = [], [], []
for label, lx, ly in satellites:
    sx, sy = Inches(lx), Inches(ly)
    sw2, sh2 = Inches(1.5), Inches(0.8)
    # line from center to satellite
    ln = LN(s3, cx, cy, sx + sw2/2, sy + sh2/2, c=GOLD_D, w=Pt(0.6))
    sp = O(s3, sx, sy, sw2, sh2, f=GREEN, lc=GOLD, lw=Pt(0.75))
    lb = T(s3, label, sx, sy, sw2, sh2,
           fn=FL, fs=Pt(13), fc=CREAM, b=False, al=PP_ALIGN.CENTER)
    s3_lines.append(ln)
    s3_sats.append(sp)
    s3_slbls.append(lb)

# Subtitle
s3_sub = T(s3,
           "Chaque paramètre de préparation module la disponibilité fonctionnelle des composés.",
           Inches(1.5), Inches(6.7), Inches(10.33), Inches(0.6),
           fn=FL, fs=Pt(12), fc=GREY, it=True, al=PP_ALIGN.CENTER)

NOTE(s3, "ANIMATION: Titre → Hub central → Chaque satellite séquentiellement (clic par clic). "
         "Le schéma respire. Style éditorial scientifique.")

anim_shapes_s3 = [s3_title, s3_titdiv, s3_hub_bg, s3_hub_t]
for ln, sp, lb in zip(s3_lines, s3_sats, s3_slbls):
    anim_shapes_s3 += [ln, sp, lb]
anim_shapes_s3.append(s3_sub)
ANIM(s3, anim_shapes_s3, dur=600)


# ═══════════════════════════════════════════════════════════════
# SLIDE 4 — INFUSION-CUISSON (3 étapes)
# ═══════════════════════════════════════════════════════════════
s4 = sl()

s4_title = T(s4, "Infuser  ·  Cuire  ·  Agrémenter",
             Inches(0.85), Inches(0.4), Inches(11.63), Inches(0.9),
             fn=FH, fs=Pt(36), fc=GOLD_L, al=PP_ALIGN.CENTER)
s4_titdiv = LN(s4, Inches(3.0), Inches(1.35), Inches(10.33), Inches(1.35),
               c=GOLD, w=Pt(0.5))

steps = [
    ("01", "KORIUM + Eau",
     "Versez dans l'eau\nde cuisson froide"),
    ("02", "Infusion-Cuisson",
     "Chaleur progressive\n→ diffusion des composés"),
    ("03", "Matrice Imprégnée",
     "Céréales · légumineuses\n· légumes enrichis"),
]

step_colors = [GREEN, GREEN_M, RGBColor(0x28, 0x50, 0x3C)]
sx_positions = [Inches(1.0), Inches(5.0), Inches(9.0)]
bw, bh = Inches(3.3), Inches(4.2)
by = Inches(1.7)

s4_boxes, s4_nums, s4_headers, s4_descs, s4_arrows = [], [], [], [], []

for i, ((num, header, desc), col, bx) in enumerate(zip(steps, step_colors, sx_positions)):
    box = R(s4, bx, by, bw, bh, f=col, lc=GOLD, lw=Pt(0.75))
    num_t = T(s4, num, bx, by + Inches(0.25), bw, Inches(0.8),
              fn=FH, fs=Pt(36), fc=GOLD, b=True, al=PP_ALIGN.CENTER)
    head_t = T(s4, header, bx, by + Inches(1.1), bw, Inches(0.8),
               fn=FH, fs=Pt(18), fc=GOLD_L, b=False, al=PP_ALIGN.CENTER)
    desc_t = T(s4, desc, bx + Inches(0.2), by + Inches(2.0), bw - Inches(0.4), Inches(1.8),
               fn=FL, fs=Pt(14), fc=WHITE_W, al=PP_ALIGN.CENTER, wrap=True)
    s4_boxes.append(box)
    s4_nums.append(num_t)
    s4_headers.append(head_t)
    s4_descs.append(desc_t)
    if i < 2:
        ax = bx + bw + Inches(0.05)
        arr = LN(s4, ax, by + bh/2, ax + Inches(0.55), by + bh/2,
                 c=GOLD, w=Pt(2))
        s4_arrows.append(arr)

NOTE(s4, "ANIMATION: Titre → Étape 1 (box+num+header+desc) → Flèche → Étape 2 → Flèche → Étape 3. "
         "Progression gauche→droite stricte. Très démonstratif.")

s4_anim = [s4_title, s4_titdiv]
for i in range(3):
    s4_anim += [s4_boxes[i], s4_nums[i], s4_headers[i], s4_descs[i]]
    if i < 2:
        s4_anim.append(s4_arrows[i])
ANIM(s4, s4_anim, dur=550)


# ═══════════════════════════════════════════════════════════════
# SLIDE 5 — KORIUM PRODUIT
# ═══════════════════════════════════════════════════════════════
s5 = sl()

# Hero zone (left 58%)
s5_hero = R(s5, Inches(0), Inches(0), Inches(7.7), SH, f=GREEN)
s5_hero2 = O(s5, Inches(-1), Inches(-1), Inches(7), Inches(6), f=GREEN_M)

# Product granule pattern (abstract texture in hero)
for row in range(4):
    for col in range(6):
        gx = Inches(0.5 + col * 1.0)
        gy = Inches(5.0 + row * 0.45)
        O(s5, gx, gy, Inches(0.18), Inches(0.18),
          f=RGBColor(0x30, 0x60, 0x48))

# KORIUM hero text
s5_k = T(s5, "KORIUM",
         Inches(0.3), Inches(1.8), Inches(7.2), Inches(2.2),
         fn=FH, fs=Pt(88), fc=GOLD_L, b=True)
s5_ksub = T(s5, "Le condiment de formulation culinaire",
            Inches(0.5), Inches(3.8), Inches(6.8), Inches(0.7),
            fn=FL, fs=Pt(17), fc=CREAM, it=True)
s5_kdiv = LN(s5, Inches(0.5), Inches(4.65), Inches(5.5), Inches(4.65),
             c=GOLD, w=Pt(0.6))
s5_ktag = T(s5, "by QUINTALYS",
            Inches(0.5), Inches(4.8), Inches(4), Inches(0.5),
            fn=FL, fs=Pt(12), fc=GREY, it=True)

# Right: 3 callout cards
callouts = [
    ("INFUSION-CUISSON",
     "Actif pendant la préparation,\nnon après."),
    ("MATRICE VÉGÉTALE",
     "Céréales · légumineuses\n· végétaux de cuisson"),
    ("CONDIMENT",
     "Geste simple intégré\nau quotidien culinaire"),
]
cy_start = Inches(1.0)
for j, (ctitle, cdesc) in enumerate(callouts):
    cy = cy_start + j * Inches(2.05)
    cbg = R(s5, Inches(8.1), cy, Inches(4.9), Inches(1.7),
            f=BG2, lc=GOLD_D, lw=Pt(0.5))
    cln = LN(s5, Inches(8.1), cy + Inches(0.02),
             Inches(8.1), cy + Inches(1.66), c=GOLD, w=Pt(3))
    ct  = T(s5, ctitle,
            Inches(8.45), cy + Inches(0.18), Inches(4.4), Inches(0.5),
            fn=FB, fs=Pt(12), fc=GOLD_L, b=True)
    cd  = T(s5, cdesc,
            Inches(8.45), cy + Inches(0.68), Inches(4.4), Inches(0.9),
            fn=FL, fs=Pt(12), fc=WHITE_W, wrap=True)

NOTE(s5, "ANIMATION: Hero zone → KORIUM grand texte → Sous-titre → "
         "Callout 1 → Callout 2 → Callout 3. Focus progressif sur le produit.")

ANIM(s5, [s5_hero, s5_hero2, s5_k, s5_ksub, s5_kdiv, s5_ktag], dur=700)


# ═══════════════════════════════════════════════════════════════
# SLIDE 6 — USAGE + ACCESSIBILITÉ
# ═══════════════════════════════════════════════════════════════
s6 = sl()

s6_title = T(s6, "Un usage accessible, un geste intégré",
             ML, Inches(0.4), Inches(11.63), Inches(0.8),
             fn=FH, fs=Pt(32), fc=GOLD_L, al=PP_ALIGN.CENTER)
s6_titdiv = LN(s6, Inches(3.5), Inches(1.25), Inches(9.83), Inches(1.25),
               c=GOLD, w=Pt(0.5))

cards_data = [
    ("200 g", "par format", "Conditionnement standard\npour 1 à 2 semaines d'usage"),
    ("12–16", "plats / format", "Rendement optimal par\ncuisson courante"),
    ("1,5–2 €", "par plat", "Accessible au quotidien,\ncomparable au condiment"),
]
col_w = Inches(3.8)
col_gap = Inches(0.47)
col_y = Inches(1.5)
col_h = Inches(5.5)

s6_cards, s6_nums, s6_units, s6_descs = [], [], [], []
for i, (num, unit, desc) in enumerate(cards_data):
    cx = ML + i * (col_w + col_gap)
    card = R(s6, cx, col_y, col_w, col_h, f=BG2, lc=GREY_D, lw=Pt(0.5))
    # Top gold bar
    top_bar = R(s6, cx, col_y, col_w, Inches(0.08), f=GOLD)
    num_t = T(s6, num, cx, col_y + Inches(0.5), col_w, Inches(1.5),
              fn=FH, fs=Pt(54), fc=GOLD_L, b=True, al=PP_ALIGN.CENTER)
    unit_t = T(s6, unit, cx, col_y + Inches(1.95), col_w, Inches(0.55),
               fn=FL, fs=Pt(14), fc=GREY, al=PP_ALIGN.CENTER)
    div = LN(s6, cx + Inches(0.6), col_y + Inches(2.65),
             cx + col_w - Inches(0.6), col_y + Inches(2.65),
             c=GOLD_D, w=Pt(0.4))
    desc_t = T(s6, desc, cx + Inches(0.3), col_y + Inches(2.9),
               col_w - Inches(0.6), Inches(1.6),
               fn=FL, fs=Pt(13), fc=WHITE_W, al=PP_ALIGN.CENTER, wrap=True)
    s6_cards.append((card, top_bar, num_t, unit_t, div, desc_t))

NOTE(s6, "ANIMATION: Titre → Carte 1 → Carte 2 → Carte 3. "
         "Révélation colonne par colonne, très lisible.")

s6_anim = [s6_title, s6_titdiv]
for group in s6_cards:
    for sh in group:
        s6_anim.append(sh)
ANIM(s6, s6_anim, dur=600)


# ═══════════════════════════════════════════════════════════════
# SLIDE 7 — MATRICE CONCURRENTIELLE
# ═══════════════════════════════════════════════════════════════
s7 = sl()

s7_title = T(s7, "Un territoire existant, mais fragmenté",
             ML, Inches(0.35), Inches(11.63), Inches(0.8),
             fn=FH, fs=Pt(32), fc=GOLD_L, al=PP_ALIGN.CENTER)

# Axes
ax_cx, ax_cy = Inches(6.665), Inches(4.1)
ax_len_h, ax_len_v = Inches(5.5), Inches(2.6)

s7_xaxis = LN(s7, ax_cx - ax_len_h, ax_cy, ax_cx + ax_len_h, ax_cy,
              c=GREY_D, w=Pt(1))
s7_yaxis = LN(s7, ax_cx, ax_cy + ax_len_v, ax_cx, ax_cy - ax_len_v,
              c=GREY_D, w=Pt(1))

# Axis labels
s7_xl1 = T(s7, "Post-préparation",
           Inches(8.8), ax_cy + Inches(0.15), Inches(2.3), Inches(0.45),
           fn=FL, fs=Pt(11), fc=GREY)
s7_xl2 = T(s7, "Cuisson",
           ax_cx - ax_len_h - Inches(0.1), ax_cy + Inches(0.15), Inches(1.1), Inches(0.45),
           fn=FL, fs=Pt(11), fc=GREY)
s7_yl1 = T(s7, "Formulation\ncontextualisée",
           ax_cx + Inches(0.15), ax_cy - ax_len_v - Inches(0.1), Inches(2.0), Inches(0.7),
           fn=FL, fs=Pt(11), fc=GREY, wrap=True)
s7_yl2 = T(s7, "Agrémentation",
           ax_cx + Inches(0.15), ax_cy + ax_len_v - Inches(0.1), Inches(2.0), Inches(0.4),
           fn=FL, fs=Pt(11), fc=GREY)

# Quadrant background hints
Q1 = R(s7, ax_cx - ax_len_h, ax_cy - ax_len_v,
       ax_len_h, ax_len_v, f=RGBColor(0x14, 0x20, 0x18))  # top-left
Q2 = R(s7, ax_cx, ax_cy - ax_len_v,
       ax_len_h, ax_len_v, f=RGBColor(0x18, 0x26, 0x1E))  # top-right (KORIUM zone)
Q3 = R(s7, ax_cx - ax_len_h, ax_cy,
       ax_len_h, ax_len_v, f=RGBColor(0x12, 0x12, 0x1C))  # bottom-left
Q4 = R(s7, ax_cx, ax_cy, ax_len_h, ax_len_v,
       f=RGBColor(0x12, 0x14, 0x1C))  # bottom-right

# Competitor dots (small, grey)
competitors = [
    ("Maggi",        ax_cx - Inches(3.0), ax_cy + Inches(0.8)),
    ("Épices BIO",   ax_cx - Inches(1.5), ax_cy + Inches(1.8)),
    ("Actifry",      ax_cx + Inches(1.0), ax_cy + Inches(1.5)),
    ("Yooji",        ax_cx + Inches(2.5), ax_cy + Inches(0.5)),
    ("Overstims",    ax_cx - Inches(2.0), ax_cy - Inches(0.8)),
]
s7_cdots, s7_clbls = [], []
for name, dx, dy in competitors:
    dot = O(s7, dx - Inches(0.2), dy - Inches(0.2), Inches(0.4), Inches(0.4),
            f=GREY_D, lc=GREY, lw=Pt(0.4))
    lbl = T(s7, name, dx + Inches(0.15), dy - Inches(0.28), Inches(1.5), Inches(0.4),
            fn=FL, fs=Pt(9), fc=GREY)
    s7_cdots.append(dot)
    s7_clbls.append(lbl)

# KORIUM dominant dot
korium_x, korium_y = ax_cx + Inches(2.8), ax_cy - Inches(1.8)
s7_kdot  = O(s7, korium_x - Inches(0.42), korium_y - Inches(0.42),
             Inches(0.84), Inches(0.84), f=GOLD, lc=GOLD_L, lw=Pt(1))
s7_klbl  = TL(s7, [
    ("KORIUM", FH, Pt(14), GOLD_L, True),
    ("by QUINTALYS", FL, Pt(9), GREY, False),
], korium_x + Inches(0.5), korium_y - Inches(0.35), Inches(2.5), Inches(0.7))

NOTE(s7, "ANIMATION: Titre → Quadrants → Axes → Concurrents → KORIUM (dernier, dominant). "
         "Le blanc autour de KORIUM = espace stratégique libre.")

s7_anim = ([s7_title] + [Q1, Q2, Q3, Q4] +
           [s7_xaxis, s7_yaxis] +
           [s7_xl1, s7_xl2, s7_yl1, s7_yl2] +
           s7_cdots + s7_clbls +
           [s7_kdot, s7_klbl])
ANIM(s7, s7_anim, dur=500)


# ═══════════════════════════════════════════════════════════════
# SLIDE 8 — BENCHMARK ASPIRATIONNEL
# ═══════════════════════════════════════════════════════════════
s8 = sl()

s8_title = T(s8, "Des briques séparées — aucune convergence",
             ML, Inches(0.35), Inches(11.63), Inches(0.8),
             fn=FH, fs=Pt(32), fc=GOLD_L, al=PP_ALIGN.CENTER)
s8_titdiv = LN(s8, Inches(2.5), Inches(1.25), Inches(10.83), Inches(1.25),
               c=GOLD, w=Pt(0.5))

columns = [
    ("SAUPOUDRAGE",
     ["Épices Ducros", "Fleur de sel", "Mélanges aromatiques"],
     COLD),
    ("PRÊT-À-CUIRE",
     ["Yooji", "Bonduelle Vapeur", "Kit légumes"],
     GREEN_M),
    ("AROMATIQUE",
     ["Herbes fraîches", "Bouillons Maggi", "Concentrés"],
     RGBColor(0x3A, 0x28, 0x12)),
    ("FOOD-SCIENCE",
     ["Nutraceutique", "Overstims", "Protéines fonct."],
     RGBColor(0x28, 0x20, 0x3C)),
]

col_w8 = Inches(2.8)
col_h8 = Inches(4.6)
col_y8 = Inches(1.45)
col_gap8 = Inches(0.41)

s8_cols = []
for i, (header, brands, col_color) in enumerate(columns):
    cx = ML + i * (col_w8 + col_gap8)
    hbg = R(s8, cx, col_y8, col_w8, Inches(0.7), f=col_color)
    ht  = T(s8, header, cx, col_y8 + Inches(0.05), col_w8, Inches(0.6),
            fn=FB, fs=Pt(11), fc=CREAM, b=True, al=PP_ALIGN.CENTER)
    cbg = R(s8, cx, col_y8 + Inches(0.7), col_w8, col_h8 - Inches(0.7),
            f=BG2, lc=GREY_D, lw=Pt(0.4))
    group = [hbg, ht, cbg]
    for j, brand in enumerate(brands):
        bt = T(s8, "· " + brand,
               cx + Inches(0.25), col_y8 + Inches(1.1) + j * Inches(0.75),
               col_w8 - Inches(0.3), Inches(0.55),
               fn=FL, fs=Pt(12), fc=WHITE_W)
        group.append(bt)
    s8_cols.append(group)

# Final phrase
s8_final_bg = R(s8, ML, Inches(6.3), Inches(11.63), Inches(0.85),
                f=RGBColor(0x14, 0x10, 0x06), lc=GOLD, lw=Pt(0.4))
s8_final = T(s8,
             "KORIUM est la première solution qui intègre ces dimensions dans un geste culinaire unique.",
             ML + Inches(0.3), Inches(6.4), Inches(11.03), Inches(0.7),
             fn=FH, fs=Pt(16), fc=GOLD_L, al=PP_ALIGN.CENTER, wrap=True)

NOTE(s8, "ANIMATION: Titre → Colonne 1 → 2 → 3 → 4 → Phrase finale forte. "
         "Lecture guidée, pas de surcharge.")

s8_anim = [s8_title, s8_titdiv]
for group in s8_cols:
    for sh in group:
        s8_anim.append(sh)
s8_anim += [s8_final_bg, s8_final]
ANIM(s8, s8_anim, dur=550)


# ═══════════════════════════════════════════════════════════════
# SLIDE 9 — VIABILITÉ + MARCHÉ
# ═══════════════════════════════════════════════════════════════
s9 = sl()

s9_title = T(s9, "Un marché existant, une cible identifiée",
             ML, Inches(0.35), Inches(11.63), Inches(0.8),
             fn=FH, fs=Pt(32), fc=GOLD_L, al=PP_ALIGN.CENTER)
s9_titdiv = LN(s9, Inches(3.0), Inches(1.25), Inches(10.33), Inches(1.25),
               c=GOLD, w=Pt(0.5))

market_cards = [
    ("MARCHÉ",
     "3,2 Md€",
     "Condiments & épices France",
     "+4,7 % / an depuis 2019",
     GREEN),
    ("CIBLE",
     "Cuisiniers actifs",
     "28–55 ans, urbains\nsensibles à la nutrition",
     "~12 M de ménages concernés",
     GREEN_M),
    ("USAGE",
     "1,5–2 €/plat",
     "Budget condiment habituel",
     "Intégration sans rupture\nde comportement",
     RGBColor(0x20, 0x3A, 0x2C)),
]
card_w9 = Inches(3.75)
card_h9 = Inches(5.2)
card_y9 = Inches(1.5)
card_gap9 = Inches(0.29)

s9_card_groups = []
for i, (label, num, sub, note9, col) in enumerate(market_cards):
    cx = ML + i * (card_w9 + card_gap9)
    cbg  = R(s9, cx, card_y9, card_w9, card_h9, f=col, lc=GOLD_D, lw=Pt(0.6))
    lbar = R(s9, cx, card_y9, Inches(0.07), card_h9, f=GOLD)
    ct   = T(s9, label, cx + Inches(0.25), card_y9 + Inches(0.2),
             card_w9 - Inches(0.3), Inches(0.5),
             fn=FL, fs=Pt(11), fc=CREAM, b=True)
    cn   = T(s9, num, cx + Inches(0.25), card_y9 + Inches(0.8),
             card_w9 - Inches(0.3), Inches(1.0),
             fn=FH, fs=Pt(32), fc=GOLD_L, b=True)
    cs   = T(s9, sub, cx + Inches(0.25), card_y9 + Inches(1.85),
             card_w9 - Inches(0.3), Inches(0.8),
             fn=FL, fs=Pt(14), fc=WHITE_W, wrap=True)
    cd   = LN(s9, cx + Inches(0.25), card_y9 + Inches(2.75),
              cx + card_w9 - Inches(0.25), card_y9 + Inches(2.75),
              c=GOLD_D, w=Pt(0.4))
    cn2  = T(s9, note9, cx + Inches(0.25), card_y9 + Inches(2.95),
             card_w9 - Inches(0.3), Inches(1.5),
             fn=FL, fs=Pt(12), fc=GREY, it=True, wrap=True)
    s9_card_groups.append([cbg, lbar, ct, cn, cs, cd, cn2])

NOTE(s9, "ANIMATION: Titre → Carte Marché → Carte Cible → Carte Usage. "
         "Business crédible, pas de graphique TAM/SAM/SOM.")

s9_anim = [s9_title, s9_titdiv]
for grp in s9_card_groups:
    for sh in grp:
        s9_anim.append(sh)
ANIM(s9, s9_anim, dur=600)


# ═══════════════════════════════════════════════════════════════
# SLIDE 10 — POURQUOI FOODSHAKER
# ═══════════════════════════════════════════════════════════════
s10 = sl()

s10_title = T(s10, "Foodshaker : l'accélérateur logique",
              ML, Inches(0.35), Inches(11.63), Inches(0.8),
              fn=FH, fs=Pt(34), fc=GOLD_L, al=PP_ALIGN.CENTER)
s10_titdiv = LN(s10, Inches(3.5), Inches(1.25), Inches(9.83), Inches(1.25),
                c=GOLD, w=Pt(0.5))
s10_sub = T(s10, "QUINTALYS × ISARA — 3 piliers de convergence",
            ML, Inches(1.4), Inches(11.63), Inches(0.5),
            fn=FL, fs=Pt(14), fc=GREY, al=PP_ALIGN.CENTER)

pillars = [
    ("01", "FORMULATION",
     "Accès au plateau technique\net aux compétences analytiques\npour documenter KORIUM"),
    ("02", "FOOD BUSINESS",
     "Réseau industriels, distributeurs\net expertise go-to-market\nspécifique food-tech"),
    ("03", "STRUCTURATION",
     "Accompagnement juridique,\nproduction et IP\npour passer de la formulation au produit"),
]

pil_w = Inches(3.5)
pil_h = Inches(4.8)
pil_y = Inches(1.95)
pil_gap = Inches(0.41)
pil_colors = [GREEN, GREEN_M, RGBColor(0x1E, 0x38, 0x2A)]

s10_pils = []
for i, ((num, head, desc), col) in enumerate(zip(pillars, pil_colors)):
    px = ML + i * (pil_w + pil_gap)
    pbg = R(s10, px, pil_y, pil_w, pil_h, f=col, lc=GOLD, lw=Pt(0.6))
    # Icon circle
    pic = O(s10, px + pil_w/2 - Inches(0.45), pil_y + Inches(0.3),
            Inches(0.9), Inches(0.9), f=GOLD)
    pnum = T(s10, num, px + pil_w/2 - Inches(0.45), pil_y + Inches(0.32),
             Inches(0.9), Inches(0.85),
             fn=FH, fs=Pt(22), fc=BG, b=True, al=PP_ALIGN.CENTER)
    pdiv = LN(s10, px + Inches(0.4), pil_y + Inches(1.4),
              px + pil_w - Inches(0.4), pil_y + Inches(1.4),
              c=GOLD_D, w=Pt(0.4))
    phead = T(s10, head, px, pil_y + Inches(1.55), pil_w, Inches(0.6),
              fn=FB, fs=Pt(14), fc=GOLD_L, b=True, al=PP_ALIGN.CENTER)
    pdesc = T(s10, desc,
              px + Inches(0.25), pil_y + Inches(2.25),
              pil_w - Inches(0.5), Inches(2.2),
              fn=FL, fs=Pt(13), fc=WHITE_W, al=PP_ALIGN.CENTER, wrap=True)
    s10_pils.append([pbg, pic, pnum, pdiv, phead, pdesc])

NOTE(s10, "ANIMATION: Titre → Sous-titre → Pilier 1 → Pilier 2 → Pilier 3. "
         "Apparition pilier par pilier. Design ISARA-compatible, sobre et institutionnel.")

s10_anim = [s10_title, s10_titdiv, s10_sub]
for group in s10_pils:
    for sh in group:
        s10_anim.append(sh)
ANIM(s10, s10_anim, dur=650)


# ═══════════════════════════════════════════════════════════════
# SLIDE 11 — CLÔTURE
# ═══════════════════════════════════════════════════════════════
s11 = sl()

# Large botanical background
s11_blob1 = O(s11, Inches(-1.5), Inches(-1.5), Inches(9), Inches(9), f=GREEN)
s11_blob2 = O(s11, Inches(7), Inches(2), Inches(8), Inches(8), f=GREEN_M)
# Dark overlay for readability
s11_overlay = R(s11, Inches(0), Inches(0), SW, SH,
                f=RGBColor(0x07, 0x08, 0x0C))

# Gold top line accent
s11_top = LN(s11, Inches(0.85), Inches(0.7), Inches(6.5), Inches(0.7),
             c=GOLD, w=Pt(0.75))

# Main closing text (3 paragraphs as per brief)
closing_lines = [
    ("Aujourd'hui, beaucoup de solutions fonctionnelles existent en dehors du repas.",
     FH, Pt(18), WHITE_W, False),
    ("", FB, Pt(8), WHITE_W, False),
    ("Avec QUINTALYS et KORIUM, mon ambition n'est pas de médicaliser l'assiette,",
     FH, Pt(18), CREAM, False),
    ("mais de réhabiliter la cuisine comme terrain de formulation culinaire,",
     FH, Pt(18), CREAM, False),
    ("à travers un geste simple, documenté et intégré au quotidien.",
     FH, Pt(18), CREAM, False),
    ("", FB, Pt(8), WHITE_W, False),
    ("KORIUM constitue cette première preuve produit.",
     FH, Pt(20), GOLD_L, True),
    ("", FB, Pt(8), WHITE_W, False),
    ("Et Foodshaker représente pour moi l'environnement capable",
     FH, Pt(18), CREAM, False),
    ("d'aider cette approche à devenir une réalité alimentaire concrète.",
     FH, Pt(18), CREAM, False),
]
s11_text = TL(s11, closing_lines,
              Inches(1.0), Inches(1.2), Inches(11.33), Inches(5.8),
              al=PP_ALIGN.LEFT)

# Gold bottom line + logo
s11_bot = LN(s11, Inches(1.0), Inches(6.8), Inches(5.5), Inches(6.8),
             c=GOLD, w=Pt(0.5))
s11_logo = T(s11, "QUINTALYS  ·  by QUINTEXOR",
             Inches(1.0), Inches(6.85), Inches(5), Inches(0.5),
             fn=FL, fs=Pt(11), fc=GREY, it=True)

NOTE(s11, "ANIMATION: Blobs botaniques → Overlay → Ligne top → Texte (très lente, 1200ms). "
         "Fin silencieuse. La dernière slide = signature émotionnelle.")

ANIM(s11, [s11_blob1, s11_blob2, s11_overlay,
           s11_top, s11_text,
           s11_bot, s11_logo], dur=1200)


# ═══════════════════════════════════════════════════════════════
# SAVE
# ═══════════════════════════════════════════════════════════════
output = "/home/user/Quintalys_Foodshaker_Deck/QUINTALYS_Foodshaker_Deck.pptx"
prs.save(output)
print(f"✓ Saved: {output}")
print(f"  Slides: {len(prs.slides)}")
