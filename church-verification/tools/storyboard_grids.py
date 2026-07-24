#!/usr/bin/env python3
"""Compose contact-sheet grids from a YouTube sb0 storyboard mhtml.

The sb0 storyboard is a sequence of JPEG mosaics (rows x cols tiles); each
tile is one video frame sampled at 1/fps seconds. We rebuild individual
frames with their true timestamps, then emit:
  - grid_baseline_NN.jpg : 4x4 grids, one frame per ~60s, whole video
  - grid_dense_<tag>_NN.jpg : 4x4 grids, every storyboard frame (~10s step)
    within requested windows

Timestamps are burned into each tile (true video time, no offset needed).

Usage:
  storyboard_grids.py <dir> <duration_s> <fps> <rows> <cols> [dense windows...]
  dense window syntax: tag:start_s:end_s   (e.g. worship_tail:1800:2700)
Reads <dir>/storyboard.mhtml, writes grids into <dir>/.
"""
import re, sys, math, io
from PIL import Image, ImageDraw, ImageFont

FONT = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)

def hms(t):
    t = int(t)
    return f"{t//3600}:{(t%3600)//60:02d}:{t%60:02d}"

def extract_jpegs(path):
    data = open(path, "rb").read()
    out = []
    for m in re.finditer(rb"Content-Type:\s*image/jpeg.*?\r?\n\r?\n", data, re.S | re.I):
        start = m.end()
        soi = data.find(b"\xff\xd8", start)
        eoi = data.find(b"\xff\xd9", soi)
        if soi == -1 or eoi == -1:
            continue
        out.append(data[soi:eoi + 2])
    return out

def load_frames(dirpath, duration, fps, rows, cols):
    import glob, os
    frag_files = sorted(glob.glob(f"{dirpath}/sb/frag_*.jpg"))
    if frag_files:
        jpegs = [open(p, "rb").read() for p in frag_files]
    else:
        jpegs = extract_jpegs(f"{dirpath}/storyboard.mhtml")
    step = 1.0 / fps
    total = min(int(math.ceil(duration * fps)), len(jpegs) * rows * cols)
    frames = []  # (timestamp_s, PIL image)
    for i, blob in enumerate(jpegs):
        mosaic = Image.open(io.BytesIO(blob)).convert("RGB")
        tw, th = mosaic.width // cols, mosaic.height // rows
        for r in range(rows):
            for c in range(cols):
                idx = i * rows * cols + r * cols + c
                if idx >= total:
                    break
                ts = idx * step
                if ts > duration:
                    break
                frames.append((ts, mosaic.crop((c * tw, r * th, (c + 1) * tw, (r + 1) * th))))
    return frames

def stamp(img, ts):
    img = img.copy()
    d = ImageDraw.Draw(img)
    text = hms(ts)
    x, y = 6, 4
    tb = d.textbbox((x, y), text, font=FONT)
    d.rectangle((tb[0] - 3, tb[1] - 2, tb[2] + 3, tb[3] + 2), fill=(0, 0, 0))
    d.text((x, y), text, font=FONT, fill=(255, 255, 0))
    return img

def write_grids(frames, out_prefix, per_row=4):
    if not frames:
        return 0
    tw, th = frames[0][1].width, frames[0][1].height
    per_grid = per_row * per_row
    n_grids = math.ceil(len(frames) / per_grid)
    for g in range(n_grids):
        chunk = frames[g * per_grid:(g + 1) * per_grid]
        sheet = Image.new("RGB", (tw * per_row, th * math.ceil(len(chunk) / per_row)), (16, 16, 16))
        for i, (ts, img) in enumerate(chunk):
            sheet.paste(stamp(img, ts), ((i % per_row) * tw, (i // per_row) * th))
        sheet.save(f"{out_prefix}{g + 1:02d}.jpg", quality=85)
    return n_grids

def main():
    dirpath, duration, fps, rows, cols = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    frames = load_frames(dirpath, duration, fps, rows, cols)
    print(f"frames reconstructed: {len(frames)} (interval {1/fps:.1f}s)")

    # baseline: nearest frame to each 60s boundary
    baseline, next_t = [], 0.0
    for ts, img in frames:
        if ts + 1e-6 >= next_t:
            baseline.append((ts, img))
            next_t += 60.0
    n = write_grids(baseline, f"{dirpath}/grid_baseline_")
    print(f"baseline grids: {n} ({len(baseline)} frames @60s)")

    for spec in sys.argv[6:]:
        tag, lo, hi = spec.split(":")
        lo, hi = float(lo), float(hi)
        sel = [(ts, img) for ts, img in frames if lo <= ts <= hi]
        n = write_grids(sel, f"{dirpath}/grid_dense_{tag}_")
        print(f"dense[{tag}] {hms(lo)}-{hms(hi)}: {n} grids ({len(sel)} frames)")

if __name__ == "__main__":
    main()
