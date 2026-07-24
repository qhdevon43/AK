#!/usr/bin/env python3
"""Generate speech_density.txt from an SRT transcript.

Counts transcribed words in fixed 5-minute buckets over the FULL video
duration (so silent/instrumental buckets appear as 0 words, never dropped).
Words are attributed to the bucket containing the midpoint of their cue.

Usage: speech_density.py transcript.srt duration_seconds > speech_density.txt
"""
import re, sys

def parse_srt(path):
    cues = []
    text = open(path, encoding="utf-8", errors="replace").read()
    pat = re.compile(
        r"(\d{2}):(\d{2}):(\d{2})[,.](\d{3})\s*-->\s*(\d{2}):(\d{2}):(\d{2})[,.](\d{3})\s*\n(.*?)(?=\n\s*\n|\Z)",
        re.S)
    for m in pat.finditer(text):
        h1, m1, s1, ms1, h2, m2, s2, ms2, body = m.groups()
        start = int(h1) * 3600 + int(m1) * 60 + int(s1) + int(ms1) / 1000
        end = int(h2) * 3600 + int(m2) * 60 + int(s2) + int(ms2) / 1000
        words = len(re.findall(r"\S+", body))
        cues.append((start, end, words))
    return cues

def fmt(sec):
    sec = int(sec)
    return f"{sec // 60:02d}:{sec % 60:02d}" if sec < 3600 else f"{sec // 3600}:{(sec % 3600) // 60:02d}:{sec % 60:02d}"

def main():
    srt, duration = sys.argv[1], float(sys.argv[2])
    cues = parse_srt(srt)
    bucket = 300
    n = int(duration // bucket) + (1 if duration % bucket else 0)
    counts = [0] * n
    for start, end, words in cues:
        mid = min((start + end) / 2, duration - 0.001)
        counts[int(mid // bucket)] += words
    for i, c in enumerate(counts):
        lo, hi = i * bucket, min((i + 1) * bucket, duration)
        print(f"{fmt(lo)}–{fmt(hi)} | {c} words")

if __name__ == "__main__":
    main()
