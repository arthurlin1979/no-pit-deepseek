# No-Pit: DeepSeek V4.1 Flash + Maya-DS

[中文版](README.md)

![House cat](assets/cat.jpg)

Check date: 2026-11-26

Field notes for running DeepSeek V4.1 Flash on Maya-DS: parameters, patches, and measurements on an RTX PRO 6000. No engine-switching operations included.

This repo covers version pinning, install, acceptance, output contract, cache, and speed. Numbers come from local reports and engine logs, partly organized with AI help.

## Why this repo exists

Honestly, Qwen3.8 is fast and solid for everyday work. But when the task gets complex or needs something genuinely new, it tends to get stuck going in circles. That is when a bigger model has to step in: DeepSeek.

The 2.5 class is already strong enough that benchmarks mostly pass. Small leftover errors usually get filtered out in a real agent loop, but a light repair pass keeps output stable.

What DeepSeek adds over Qwen3.8 is not scoreboard points — it is creativity and reasoning you cannot measure with benchmarks. An RTX 6000 runs it a bit slowly, and even a 5090 feels the pain, but some problems leave no alternative. With the hosted DeepSeek acting up lately, a local setup that reproduces 99% of it matters a lot.

On the technical side: DeepSeek V4.1 Flash runs on Maya-DS, but the defaults target generic setups — JSON wrapped in fences, slow long-context refetch, oversized thinking budget, updates wiping custom keys. This repo keeps the patches and settings behind an 88/89 acceptance run. Only v1.1.80 behavior is guaranteed.

## Upstream

* Engine: [mw00/project-maya](https://github.com/mw00/project-maya) (v1.1.80, commit `1d0f8c5`)
* Model: [peasantsmith/DeepSeek-V4.1-Flash-1017-Maya-GGUF](https://huggingface.co/peasantsmith/DeepSeek-V4.1-Flash-1017-Maya-GGUF) (rev `c33d87b8`)
* This repo is an independent collection, not a GitHub fork; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for the license chain.

## Start here

- [Entry for AI agents](AGENTS.md)
- [Quick Start](QUICKSTART.md)
- [Pitfall checklist](PITFALLS.md): DS-001 and up, index only
- [Records index](catalogue/INDEX.md)
- [Measured speed](catalogue/speed.md)
- [Change blocks](BLOCKS.md)
- [Sources](SOURCES.md)
- [Third-party notices](THIRD_PARTY_NOTICES.md)
- [v1.1.80 notes](v1.1.80/RELEASE.en.md)

## Core table

| Item | Value (2026-11-26) |
|---|---|
| Engine | Maya v1.1.80, `maya-ds4`, `--parallel 4` |
| Model | DeepSeek-V4.1-Flash Maya-S, context 262144 |
| 89-task | 88/89 (89/89 with fair harness) |
| Decode | Median about 70 tok/s clean; lower with contention |
| 250K refetch | About 0.21s after switching conversations |

## Known limits

- Immediate resend of the same prompt does not hit slots; this is engine semantics.
- Abliteration costs about 5% decode; disable per request if needed.
- Idle RAM does not speed decode; use it for conversation slots.

## License

MIT, see [LICENSE](LICENSE).

## Scope

- Historical record; not a live guarantee.
- Out of scope: other engines, private logs, absolute home paths.
- Siblings: [no-pit-qwen38](https://github.com/arthurlin1979/no-pit-qwen38) / [no-pit-glm](https://github.com/arthurlin1979/no-pit-glm) / [no-pit-google-workspace](https://github.com/arthurlin1979/no-pit-google-workspace).

## Limits

- Sources guide verification; not every entry is an upstream bug.
- Full live flow not re-run.
