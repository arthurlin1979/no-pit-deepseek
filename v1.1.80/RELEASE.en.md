# v1.1.80 Release Notes: pin first, then speed

Check date: 2026-11-26

This version pins Maya v1.1.80. DS code has been unchanged since v1.1.78; later versions only touch Inkling.

What changed on our side: server-side output contract in `frontend.py`, larger conversation slots, thinking budget 2048 with low effort, abliteration on by default, and a reapply script.

Measured: 89-task suite 88/89 (89/89 with a fair harness); decode median about 70 tok/s on a clean machine; 250K re-fetch about 0.21s after switching conversations.

Scope: Maya-DS with DeepSeek V4.1 Flash only. Switching to other engines is out of scope.

## Limits

- Historical record; full live flow not re-run.
- Only v1.1.80 is guaranteed; new versions need re-check.
