import os
from pathlib import Path
import textwrap

OUTPUT = Path(__file__).parent.parent / "info-card.svg"
STATIC = os.environ.get("STATIC", "0") == "1"

CARD_W      = 490
CARD_H      = 380
PAD_X       = 22
PAD_Y       = 22
LINE_H      = 22
FONT_SIZE   = 13

BG          = "#0d1117"
TITLE_BAR   = "#161b22"
BORDER      = "#30363d"
DOT_RED     = "#ff5f57"
DOT_YEL     = "#ffbd2e"
DOT_GRN     = "#28c840"

KEY_COLOR   = "#58a6ff"
VAL_COLOR   = "#c9d1d9"
DIM_COLOR   = "#8b949e"
HL_COLOR    = "#39d353"
PROMPT_COL  = "#58a6ff"

TITLE_BAR_H = 30

INFO_ROWS = [
    ("Name   ",   "John Tyrone P. Coronel",           KEY_COLOR,  VAL_COLOR),
    ("Status ",   "4th Year BSIS Student",              KEY_COLOR,  HL_COLOR),
    ("School ",   "Carlos Hilado Memorial State University",           KEY_COLOR,  VAL_COLOR),
    (None,        "─" * 28,                           DIM_COLOR,  DIM_COLOR),
    ("Stack  ",   "Python · Django · Django REST",    KEY_COLOR,  VAL_COLOR),
    ("        ",  "JavaScript · HTML/CSS/SCSS",       KEY_COLOR,  VAL_COLOR),
    ("        ",  "PostgreSQL · SQLite",              KEY_COLOR,  VAL_COLOR),
    (None,        "─" * 28,                           DIM_COLOR,  DIM_COLOR),
    ("Port   ",   "johntyroneportfolio.vercel.app",   KEY_COLOR,  HL_COLOR),
    ("Mail   ",   "jtcoronel.chmsu@gmail.com",        KEY_COLOR,  VAL_COLOR),
    ("GitHub ",   "github.com/TheUnshackled1",        KEY_COLOR,  VAL_COLOR),
    (None,        "─" * 28,                           DIM_COLOR,  DIM_COLOR),
    ("Goal   ",   "Building things that matter 🚀",  KEY_COLOR,  VAL_COLOR),
]

SWATCHES = ["#0e4429", "#006d32", "#26a641", "#39d353",
            "#58a6ff", "#79c0ff", "#e3b341", "#f78166"]


TARGET_DUR  = 4.0  # seconds total animation reveal
ANIM_DUR    = 0.35
TOTAL_ITEMS = len(INFO_ROWS) + len(SWATCHES)
STEP_DELAY  = (TARGET_DUR - ANIM_DUR) / max(1, TOTAL_ITEMS - 1)


def stagger(i: int, static: bool) -> str:
    if static:
        return 'style="opacity:1;transform:translateX(0)"'
    delay = f"{i * STEP_DELAY:.2f}s"
    return (f'class="reveal" style="animation-delay:{delay};'
            f'opacity:0;transform:translateX(-12px)"')


def build_svg() -> str:
    lines_svg = []
    content_start_y = TITLE_BAR_H + PAD_Y + LINE_H

    for i, (key, val, kc, vc) in enumerate(INFO_ROWS):
        y = content_start_y + i * LINE_H
        attr = stagger(i, STATIC)

        if key is None:
            lines_svg.append(
                f'  <text x="{PAD_X}" y="{y}" fill="{kc}" {attr}>'
                f'{val}</text>'
            )
        elif key == "":
            lines_svg.append(
                f'  <text x="{PAD_X}" y="{y}" fill="{kc}" '
                f'font-weight="bold" font-size="15" {attr}>'
                f'{val}</text>'
            )
        else:
            lines_svg.append(
                f'  <text x="{PAD_X}" y="{y}" {attr}>'
                f'<tspan fill="{kc}" font-weight="bold">{key}: </tspan>'
                f'<tspan fill="{vc}">{val}</tspan></text>'
            )

    swatch_y  = CARD_H - 30
    sw_w      = 18
    sw_gap    = 4
    swatch_total_w = len(SWATCHES) * (sw_w + sw_gap) - sw_gap
    sw_x_start = (CARD_W - swatch_total_w) // 2

    swatches_svg = []
    for j, color in enumerate(SWATCHES):
        sx = sw_x_start + j * (sw_w + sw_gap)
        delay_attr = (
            f'style="animation-delay:{(len(INFO_ROWS) + j) * STEP_DELAY:.2f}s;opacity:0"'
            f' class="reveal"'
            if not STATIC else 'style="opacity:1"'
        )
        swatches_svg.append(
            f'  <rect x="{sx}" y="{swatch_y}" width="{sw_w}" height="{sw_w}" '
            f'rx="4" fill="{color}" {delay_attr}/>'
        )

    anim_css = "" if STATIC else textwrap.dedent("""\
        @keyframes revealLine {
          from { opacity: 0; transform: translateX(-12px); }
          to   { opacity: 1; transform: translateX(0);     }
        }
        .reveal {
          animation: revealLine 0.35s ease forwards;
        }""")

    dots_y = TITLE_BAR_H // 2
    svg = textwrap.dedent(f"""\
        <svg xmlns="http://www.w3.org/2000/svg"
             width="{CARD_W}" height="{CARD_H}"
             viewBox="0 0 {CARD_W} {CARD_H}">

          <style>
            text {{
              font-family: 'Courier New', Courier, monospace;
              font-size: {FONT_SIZE}px;
            }}
            {anim_css}
          </style>

          <rect width="{CARD_W}" height="{CARD_H}" rx="10" ry="10"
                fill="{BG}" stroke="{BORDER}" stroke-width="1"/>

          <rect x="0" y="0" width="{CARD_W}" height="{TITLE_BAR_H}"
                rx="10" ry="10" fill="{TITLE_BAR}"/>
          <rect x="0" y="{TITLE_BAR_H // 2}" width="{CARD_W}" height="{TITLE_BAR_H // 2}"
                fill="{TITLE_BAR}"/>

          <circle cx="18" cy="{dots_y}" r="6" fill="{DOT_RED}"/>
          <circle cx="36" cy="{dots_y}" r="6" fill="{DOT_YEL}"/>
          <circle cx="54" cy="{dots_y}" r="6" fill="{DOT_GRN}"/>

          {"".join(chr(10) + l for l in lines_svg)}

          {"".join(chr(10) + s for s in swatches_svg)}

        </svg>""")

    return svg


def main():
    print("[make_info_card] Building SVG ...")
    svg = build_svg()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(svg, encoding="utf-8")
    print(f"[make_info_card] Saved -> {OUTPUT}")


if __name__ == "__main__":
    main()
