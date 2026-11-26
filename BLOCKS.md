# BLOCKS — 本專案對上游的修改

核對日期：2026-11-26

只列本專案修改部分，上游原有內容不列。

## 有效

1. 伺服器端輸出契約（`serve/frontend.py`）：DeepSeek 分支渲染前把 `MAYA_DS4_OUTPUT_CONTRACT` 接到 system；無 system 則新建。實證：89 題 84/89 → 88/89，散文無 fence。狀態：有效。
2. Run script 契約文字（`run-maya-ds4.sh`）：export 契約英文原文，條件式而非一律 JSON。實證：同上。狀態：有效。
3. 對話保留加大（`maya-ds4.json` env）：`SLOT_KEEP=1`、`SLOT_RAM_GB=32`、`SLOT_CAP=8`、`PREFIX_KEEP=4`、`PREFIX_GB=8`、`KEEP_THINKING=1`。實證：8 段 60K 輪流後取回 0.06–0.07 秒，250K 取回 0.21 秒。狀態：有效。
4. 思考預算（頂層）：`thinking_budget 2048`、`reasoning_effort low`。實證：88/89 無退步。狀態：有效。
5. 去審查預設開（args）：`--ablate-default on`。實證：88/89 無退步，decode 約慢 5%。狀態：有效（刪減亦記錄）。
6. 重套工具（`reapply.sh`＋`restore-config.py`）：idempotent，先備份再寫回，加語法檢查。實證：重複執行不壞。狀態：有效。

## 不予收錄

- 改 `tools/ds4/chat_template.jinja`：DeepSeek 不走它，改了沒用，僅於報告留存。
- `MAYA_DS4_ARENA_THP=1`：本機 THP 為 `madvise`，無加速紀錄，僅於報告留存。
- `--parallel 1` 留 250K KV：理論可行，未實測，不收。

## 使用限制

- 僅保證 v1.1.80；新版需重驗。
- 來源層幫助選擇驗證方法，不表示每條都是上游缺陷。
