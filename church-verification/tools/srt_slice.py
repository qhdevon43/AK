#!/usr/bin/env python3
"""Extract SRT cues in a time window, or cues matching keyword regex.

Usage:
  srt_slice.py transcript.srt window START_SEC END_SEC
  srt_slice.py transcript.srt keywords
Output: plain text lines "HH:MM:SS  text" (compact, for HANDOFF excerpts).
"""
import re, sys

KEYWORDS = re.compile(
    r"\b(prophes\w*|prophet\w*|word from the lord|heal\w*|lay(?:ing)? hands?|"
    r"tongues|fire|presence|altar|come forward|receive|impartation|deliver\w*)\b", re.I)

def parse(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    pat = re.compile(
        r"(\d{2}):(\d{2}):(\d{2})[,.](\d{3})\s*-->\s*\d{2}:\d{2}:\d{2}[,.]\d{3}\s*\n(.*?)(?=\n\s*\n|\Z)", re.S)
    for m in pat.finditer(text):
        h, mi, s, _ms, body = m.groups()
        start = int(h) * 3600 + int(mi) * 60 + int(s)
        yield start, " ".join(body.split())

def hms(t):
    return f"{t // 3600:02d}:{(t % 3600) // 60:02d}:{t % 60:02d}"

def main():
    path, mode = sys.argv[1], sys.argv[2]
    if mode == "window":
        lo, hi = float(sys.argv[3]), float(sys.argv[4])
        for start, body in parse(path):
            if lo <= start <= hi:
                print(f"{hms(start)}  {body}")
    elif mode == "keywords":
        for start, body in parse(path):
            if KEYWORDS.search(body):
                print(f"{hms(start)}  {body}")

if __name__ == "__main__":
    main()
