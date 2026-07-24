# PIPELINE_REPORT.md

Run date: 2026-07-24 (Phase A complete; Phase B pending approval)

## Tooling
- yt-dlp 2026.07.04 (fresh install)
- ffmpeg 6.1.1 with drawtext ✓
- openai-whisper: install in progress at Phase A checkpoint (torch download is large); model choice (`medium` vs `small`) will be recorded per-video in manifests.

## Channel verification
| Church | URL given | Resolved channel | Status |
|---|---|---|---|
| The Gathering (Prosper) | @wethegathering | "The Gathering \| Prosper, Tx" (UCR1YH2P4elYO0FGeFxBN7nQ, ~1.4k subs) | ✅ correct channel |
| Movement Church (Celina) | UC8Eu_wVWEtgk2bYv4higUZQ | "Movement Church" (584 subs; content confirms Celina TX) | ✅ correct channel |
| Consumed Church (NRH) | @TheConsumedChurch | "Consumed Church" (UCYPyxygLho4glKZfFUY2kYQ, 513 subs) | ✅ correct channel |

## Issues / reliability flags
1. **The Gathering (Prosper): NO full-service video exists on YouTube.**
   - Channel has no /streams tab (yt-dlp: "This channel does not have a streams tab").
   - /videos tab is 100% sermon-only cuts (22–66 min) plus a separate "Sunday School" teaching series (~1h classroom-style).
   - Playlists checked (incl. "September Gathering", "Supernatural Matters") — all sermon cuts.
   - `ytsearch10:"The Gathering Prosper Texas church live service"` returns only their own sermon cuts; longest hit is a 2:44 funeral (Celebration of Life).
   - Consequence: worship sets, ministry time, and crowd footage are NOT verifiable from YouTube for this church. They may livestream on another platform (Facebook/website) — outside this pipeline's scope unless a URL is provided.
   - Fallback available: sermon cuts still yield transcript-based signals (prophetic/healing language frequency, ministry-time tail ends if not clipped). Flagged for user decision at checkpoint.
2. Upload dates in channel_dump files come from `youtubetab:approximate_date` — month-level precision for older items; exact dates confirmed at Phase B via `--dump-json` per video.
3. Movement Church has one upcoming/live entry ("Covenant Living -", id 0zHVT8Bi3yw, no duration) — not downloadable yet; excluded.
4. Consumed Church: no midweek/worship-night uploads found in the 40 most recent streams (window reaches back to ~Sep 2025). Sunday streams only.
5. Movement Church "Healing Night" is a monthly midweek stream Jan–May 2026; none visible for June or July 2026.
