#!/usr/bin/env python3
"""Build transcript.srt and speech_density.txt from YouTube json3 auto-captions.

json3 ASR events carry word-level segments (tStartMs + tOffsetMs) without the
rolling-line duplication of the srt/vtt exports. We reconstruct a word stream,
group it into readable cues (max ~12 words or 7s, split on >2.5s gaps), and
bucket word counts per 5 minutes over the full duration so instrumental /
selah stretches show up as low-word buckets.

Usage: captions_build.py <dir> <duration_seconds>
Reads <dir>/cap.en.json3, writes <dir>/transcript.srt and <dir>/speech_density.txt
"""
import json, sys

def hms_srt(ms):
    s, ms = divmod(int(ms), 1000)
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def fmt_mmss(sec):
    sec = int(sec)
    return f"{sec // 60:02d}:{sec % 60:02d}" if sec < 3600 else f"{sec // 3600}:{(sec % 3600) // 60:02d}:{sec % 60:02d}"

def words_from_json3(path):
    d = json.load(open(path, encoding="utf-8"))
    words = []
    for ev in d.get("events", []):
        t0 = ev.get("tStartMs", 0)
        for seg in ev.get("segs", []) or []:
            txt = (seg.get("utf8") or "").strip()
            if not txt or txt == "\n":
                continue
            words.append((t0 + seg.get("tOffsetMs", 0), txt))
    words.sort(key=lambda w: w[0])
    return words

def main():
    dirpath, duration = sys.argv[1], float(sys.argv[2])
    words = words_from_json3(f"{dirpath}/cap.en.json3")

    # --- transcript.srt
    cues, cur, cur_start = [], [], None
    for t, w in words:
        if cur and (len(cur) >= 12 or t - cur_start > 7000 or t - cur[-1][0] > 2500):
            cues.append((cur_start, cur[-1][0] + 600, " ".join(x[1] for x in cur)))
            cur, cur_start = [], None
        if cur_start is None:
            cur_start = t
        cur.append((t, w))
    if cur:
        cues.append((cur_start, cur[-1][0] + 600, " ".join(x[1] for x in cur)))

    with open(f"{dirpath}/transcript.srt", "w", encoding="utf-8") as f:
        for i, (a, b, text) in enumerate(cues, 1):
            f.write(f"{i}\n{hms_srt(a)} --> {hms_srt(b)}\n{text}\n\n")

    # --- speech_density.txt (5-minute buckets over full duration)
    bucket = 300
    n = int(duration // bucket) + (1 if duration % bucket else 0)
    counts = [0] * n
    for t, _w in words:
        idx = min(int((t / 1000) // bucket), n - 1)
        counts[idx] += 1
    with open(f"{dirpath}/speech_density.txt", "w", encoding="utf-8") as f:
        for i, c in enumerate(counts):
            lo, hi = i * bucket, min((i + 1) * bucket, duration)
            f.write(f"{fmt_mmss(lo)}–{fmt_mmss(hi)} | {c} words\n")

    print(f"{dirpath}: {len(words)} words, {len(cues)} cues, {n} density buckets")

if __name__ == "__main__":
    main()
