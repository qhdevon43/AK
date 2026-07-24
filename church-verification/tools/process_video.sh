#!/usr/bin/env bash
# Per-video extraction: download -> audio -> transcript -> density -> baseline grid.
# segments.json + dense grids are done afterwards (they need transcript review).
# Usage: process_video.sh <church-slug> <video-id> <whisper-model>
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SLUG="$1"; VID="$2"; MODEL="${3:-small}"
DIR="$ROOT/$SLUG/$VID"
cd "$DIR"

YTFLAGS=(--extractor-args "youtube:player_client=web_embedded" --remote-components ejs:github --remote-components ejs:npm)
if [ -f "$ROOT/tools/po_token.env" ]; then
  # po_token.env defines VISITOR_DATA and PO_TOKEN
  . "$ROOT/tools/po_token.env"
  YTFLAGS=(--extractor-args "youtube:player_client=web,web_embedded;visitor_data=${VISITOR_DATA};po_token=web.gvs+${PO_TOKEN},web_embedded.gvs+${PO_TOKEN},web.player+${PO_TOKEN},web_embedded.player+${PO_TOKEN}" --remote-components ejs:github --remote-components ejs:npm)
fi

echo "=== [$VID] download"
if [ ! -f video.mp4 ]; then
  yt-dlp "${YTFLAGS[@]}" -f "bv*[height<=480]+ba/b[height<=480]" \
    --merge-output-format mp4 -o video.mp4 "https://www.youtube.com/watch?v=$VID" \
    2>&1 | grep -vE '^\[download\]' | tail -3 || { echo "DOWNLOAD FAILED $VID"; exit 1; }
fi

echo "=== [$VID] audio extract"
[ -f audio.wav ] || ffmpeg -hide_banner -loglevel error -i video.mp4 -vn -ac 1 -ar 16000 audio.wav

echo "=== [$VID] transcript ($MODEL)"
if [ ! -f transcript.srt ]; then
  whisper audio.wav --model "$MODEL" --language en --output_format srt --output_dir . --fp16 False --verbose False
  mv -f audio.srt transcript.srt
fi

DUR=$(python3 -c "import json; print(json.load(open('manifest.json'))['duration_seconds'])")

echo "=== [$VID] speech density"
python3 "$ROOT/tools/speech_density.py" transcript.srt "$DUR" > speech_density.txt

echo "=== [$VID] baseline contact sheets"
if ! ls grid_baseline_*.jpg >/dev/null 2>&1; then
  ffmpeg -hide_banner -loglevel error -i video.mp4 \
    -vf "fps=1/60,scale=480:-1,drawtext=text='%{pts\:hms}':fontsize=28:fontcolor=yellow:box=1:boxcolor=black@0.5:x=10:y=10,tile=4x4" \
    -q:v 3 grid_baseline_%02d.jpg
fi

echo "=== [$VID] done (segments/dense grids pending transcript review)"
