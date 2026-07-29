from pathlib import Path
import textwrap
from PIL import Image

INPUT   = Path(__file__).parent / "source-prepped.png"
OUTPUT  = Path(__file__).parent.parent / "tyrone-ascii.svg"

COLS        = 100
FONT_W      = 6.0
FONT_H      = 10.5
FONT_SIZE   = 10

CHAR_COLOR  = "#c9d1d9"
CURSOR_COL  = "#58a6ff"
BG_COLOR    = "#0d1117"

RAMP = " .`':-=+*cs#%@"


def img_to_chars(path: Path, cols: int) -> list[str]:
    img = Image.open(path).convert("L")
    aspect = img.height / img.width
    rows = int(cols * aspect * FONT_W / FONT_H)
    img = img.resize((cols, rows), Image.LANCZOS)

    lines = []
    for y in range(rows):
        row = ""
        for x in range(cols):
            brightness = img.getpixel((x, y))
            idx = int(brightness / 255 * (len(RAMP) - 1))
            row += RAMP[idx]
        lines.append(row)
    return lines


def xml_escape(s: str) -> str:
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;"))


def build_svg(lines: list[str]) -> str:
    num_rows   = len(lines)
    num_cols   = max(len(l) for l in lines)
    svg_w      = num_cols * FONT_W
    svg_h      = num_rows * FONT_H + FONT_H

    ROW_DELAY  = 0.045
    WIPE_DUR   = 0.35
    CURSOR_DUR = 0.10

    total_dur  = num_rows * ROW_DELAY + WIPE_DUR + 0.5

    defs_parts = []
    text_parts = []

    for i, line in enumerate(lines):
        row_id     = f"r{i}"
        clip_id    = f"c{i}"
        begin_s    = i * ROW_DELAY
        end_s      = begin_s + WIPE_DUR
        freeze_s   = total_dur

        y_baseline = (i + 1) * FONT_H

        defs_parts.append(f"""
    <clipPath id="{clip_id}">
      <rect id="{clip_id}r" x="0" y="{i * FONT_H:.1f}" width="0" height="{FONT_H:.1f}">
        <animate
          attributeName="width"
          from="0" to="{svg_w:.1f}"
          begin="{begin_s:.3f}s" dur="{WIPE_DUR:.3f}s"
          fill="freeze"
          calcMode="linear"/>
      </rect>
    </clipPath>""")

        safe_line = xml_escape(line)
        text_parts.append(
            f'  <text clip-path="url(#{clip_id})" '
            f'x="0" y="{y_baseline:.1f}" '
            f'fill="{CHAR_COLOR}">'
            f'{safe_line}</text>'
        )

    cursor_parts = []
    for i in range(num_rows):
        begin_s  = i * ROW_DELAY
        end_s    = begin_s + WIPE_DUR
        y_top    = i * FONT_H

        cursor_parts.append(f"""
  <rect id="cur{i}" x="0" y="{y_top:.1f}" width="{FONT_W:.1f}" height="{FONT_H:.1f}"
        fill="{CURSOR_COL}" opacity="0.85">
    <animate attributeName="opacity"
      values="0;0.85;0.85;0"
      keyTimes="0;0.001;0.95;1"
      begin="{begin_s:.3f}s" dur="{WIPE_DUR + CURSOR_DUR:.3f}s"
      fill="freeze"/>
    <animate attributeName="x"
      from="0" to="{svg_w:.1f}"
      begin="{begin_s:.3f}s" dur="{WIPE_DUR:.3f}s"
      fill="freeze" calcMode="linear"/>
  </rect>""")

    defs_block = "<defs>" + "".join(defs_parts) + "\n</defs>"
    cursor_block = "".join(cursor_parts)
    text_block   = "\n".join(text_parts)

    svg = textwrap.dedent(f"""\
        <svg xmlns="http://www.w3.org/2000/svg"
             width="{svg_w:.0f}" height="{svg_h:.0f}"
             viewBox="0 0 {svg_w:.0f} {svg_h:.0f}">

          <style>
            text {{
              font-family: 'Courier New', Courier, monospace;
              font-size: {FONT_SIZE}px;
              white-space: pre;
            }}
          </style>

          <rect width="100%" height="100%" fill="{BG_COLOR}"/>

          {defs_block}

          {cursor_block}

          {text_block}

        </svg>""")

    return svg


def main():
    if not INPUT.exists():
        print(f"[make_ascii_svg] ERROR: {INPUT} not found. Run prep_photo.py first.")
        raise SystemExit(1)

    print(f"[make_ascii_svg] Reading {INPUT} ...")
    lines = img_to_chars(INPUT, COLS)
    print(f"[make_ascii_svg] Grid: {len(lines[0])}x{len(lines)} chars")

    print("[make_ascii_svg] Building SVG ...")
    svg = build_svg(lines)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(svg, encoding="utf-8")
    print(f"[make_ascii_svg] Saved -> {OUTPUT}")


if __name__ == "__main__":
    main()
