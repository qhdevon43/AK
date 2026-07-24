#!/usr/bin/env python3
"""Assemble HANDOFF.md from per-video artifacts. Run from church-verification/."""
import json, os, glob

VIDEOS = [
    ("movement-church-celina", "4F7R_XFsAHU"),
    ("movement-church-celina", "V2KhD7yrmTM"),
    ("movement-church-celina", "S5hmFAr6iUs"),
    ("consumed-church", "zaQ4mUHUBdA"),
    ("consumed-church", "UR1Jwm4gC4E"),
]

def hms_to_s(t):
    p = [int(x) for x in t.split(":")]
    return p[0] * 3600 + p[1] * 60 + p[2]

def bucket_bounds(line):
    rng = line.split("|")[0].strip()
    lo, hi = rng.split("–")
    def cv(x):
        p = [int(v) for v in x.strip().split(":")]
        return p[0] * 60 + p[1] if len(p) == 2 else p[0] * 3600 + p[1] * 60 + p[2]
    return cv(lo), cv(hi)

out = ["# HANDOFF.md — Church Worship-Culture Verification (extraction only)",
       "",
       "Frame grids: ALL timestamps burned into tiles are TRUE video time (grids were",
       "composed from YouTube storyboard frames with absolute timing) — no offsets needed.",
       "Baseline grids: 1 frame/60s. Dense grids: 1 frame/~10s (native storyboard interval).",
       "Transcripts are YouTube 'en-orig' auto-captions (ASR), not Whisper — see PIPELINE_REPORT.md.",
       ""]

for slug, vid in VIDEOS:
    d = f"{slug}/{vid}"
    man = json.load(open(f"{d}/manifest.json"))
    seg = json.load(open(f"{d}/segments.json"))
    out.append(f"\n---\n\n## {man['church']} — {man['title']} ({vid})\n")
    out.append("### 1. Manifest\n```json\n" + json.dumps(man, indent=2) + "\n```\n")
    out.append("### 2. Segments\n```json\n" + json.dumps(seg, indent=2) + "\n```\n")

    # density restricted to worship + ministry segments
    wins = [(hms_to_s(s["start"]), hms_to_s(s["end"])) for s in seg["segments"]
            if s["label"] in ("worship", "ministry_time")]
    kept = []
    for line in open(f"{d}/speech_density.txt"):
        lo, hi = bucket_bounds(line)
        if any(lo < e and hi > s for s, e in wins):
            kept.append(line.rstrip())
    out.append("### 3. Speech density (worship + ministry buckets only; 5-min buckets, ASR word counts)\n```")
    out.extend(kept)
    out.append("```\n")

    grids = sorted(os.path.basename(p) for p in glob.glob(f"{d}/grid_*.jpg"))
    out.append("### 4. Contact sheets (timestamps in tiles are true video time)\n```")
    out.extend(grids)
    out.append("```\n")

    def add_excerpt(title, fname, note=""):
        path = f"{d}/{fname}"
        out.append(f"### {title}\n")
        if note:
            out.append(f"_{note}_\n")
        if os.path.exists(path) and os.path.getsize(path) > 0:
            out.append("```\n" + open(path).read().rstrip() + "\n```\n")
        else:
            out.append("_(no transcript content in this window — see PIPELINE_REPORT.md)_\n")

    add_excerpt("5a. Transcript excerpt — final 10 min of worship", "excerpt_worship_tail.txt")
    add_excerpt("5b. Transcript excerpt — ministry time (entirety)", "excerpt_ministry.txt")
    add_excerpt("5c. Transcript excerpt — prophetic/ministry language matches",
                "excerpt_keywords.txt",
                "keyword regex: prophesy/prophetic, word from the Lord, healing, lay hands, tongues, fire, presence, altar, come forward, receive, impartation, deliverance")

out.append("\n---\n\n## Bonus: movement-church-celina/dCWJhrpKUrc (Jul 20 service)\n")
out.append("Frames-only entry: no captions exist for this video, so no transcript/segments/density.")
out.append("Baseline grids grid_baseline_01..07.jpg provided as visual evidence only.\n")
out.append("\nSee PIPELINE_REPORT.md for failures, fallbacks, and reliability caveats.\n")

open("HANDOFF.md", "w").write("\n".join(out))
print("HANDOFF.md written:", os.path.getsize("HANDOFF.md"), "bytes")
