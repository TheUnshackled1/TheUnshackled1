"""
prep_photo.py — Step 3a
Removes background, boosts local contrast (CLAHE), composites onto white.
Output: scripts/source-prepped.png

Usage:
    python scripts/prep_photo.py
    python scripts/prep_photo.py path/to/photo.jpg   # optional override
"""

import sys
from pathlib import Path
import numpy as np
from PIL import Image
import cv2
from rembg import remove

# ── paths ──────────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).parent.parent
DEFAULT_INPUT = REPO_ROOT / "tyrone.jpg"
OUTPUT = Path(__file__).parent / "source-prepped.png"


def remove_background(img_bytes: bytes) -> Image.Image:
    """Strip background with rembg → returns RGBA PIL image."""
    out_bytes = remove(img_bytes)
    return Image.open(__import__("io").BytesIO(out_bytes)).convert("RGBA")


def clahe_boost(rgba: Image.Image) -> Image.Image:
    """
    Boost local contrast with CLAHE on the L channel (LAB colour space).
    Works on the RGB channels, ignores alpha.
    """
    rgb = np.array(rgba.convert("RGB"))
    lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB)

    # Apply CLAHE to L channel only
    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
    lab[:, :, 0] = clahe.apply(lab[:, :, 0])

    rgb_boosted = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)

    # Put alpha back
    result = np.dstack([rgb_boosted, np.array(rgba)[:, :, 3]])
    return Image.fromarray(result.astype(np.uint8), "RGBA")


def composite_white(rgba: Image.Image) -> Image.Image:
    """Alpha-composite onto pure white background → RGB."""
    bg = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
    bg.paste(rgba, mask=rgba.split()[3])
    return bg.convert("RGB")


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if not src.exists():
        print(f"[prep_photo] ERROR: source not found: {src}")
        sys.exit(1)

    print(f"[prep_photo] Reading  {src}")
    img_bytes = src.read_bytes()

    print("[prep_photo] Removing background …")
    rgba = remove_background(img_bytes)

    print("[prep_photo] Boosting contrast (CLAHE) …")
    rgba = clahe_boost(rgba)

    print("[prep_photo] Compositing onto white …")
    result = composite_white(rgba)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    result.save(OUTPUT)
    print(f"[prep_photo] Saved → {OUTPUT}")


if __name__ == "__main__":
    main()
