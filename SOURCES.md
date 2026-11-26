# SOURCES — 來源、版本、證據邊界

核對日期：2026-11-26

## 來源種類

- 整合案例：本機 8 篇 OB 報告（去識別化後整理）。
- 本次官方佐證：[mw00/project-maya](https://github.com/mw00/project-maya) releases（v1.1.80）、docs（MEMORY／SETTINGS／SETUP）、issue #299、#763、#1089、#1206／#1207。
- 新增上游補充：Hugging Face [peasantsmith/DeepSeek-V4.1-Flash-1017-Maya-GGUF](https://huggingface.co/peasantsmith/DeepSeek-V4.1-Flash-1017-Maya-GGUF)（rev `c33d87b8`）、Unsloth Dynamic 3.1、DeepSeek 官方 JSON 提醒。
- 背景回報：zephel01 實測、Strata issue #4163、#5589（僅連結，不宣稱採用修法）。

## 本機報告（Maya-DS 範圍內）

- `2026-11-23-5092-deepseek-maya-vs-strata-research.md`
- `2026-11-25-5092-maya-version-pick.md`
- `2026-11-25-5092-maya-s-install-and-hf-token.md`
- `2026-11-25-5092-maya-s-acceptance.md`
- `2026-11-26-5092-maya-s-params-and-contract.md`
- `2026-11-26-5092-maya-speed-and-5090-strata-crash.md`（只取 Maya 實速段）
- `2026-11-26-mac-maya-5092-client-onboarding.md`（只取 provider 命名段）

未收錄：切換至其他引擎的操作報告（依要求排除）。

## 版本

- Maya `v1.1.80`（commit `1d0f8c5`），設定範本見 `v1.1.80/`。
- 模型 `DeepSeek-V4.1-Flash-1017-GGUF` Maya-S。

## 證據邊界

- 歷史記載，未重跑全部流程驗證。
- 數字皆為原記載時點，不當現行保證。
- 新問題先歸類再補來源。

## 尚未核實與未收錄

- `--parallel 1` 留 250K KV（理論，未實測）。
- 其他引擎的安裝與切換（超出範圍）。
