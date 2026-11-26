# QUICKSTART — 30 秒

核對日期：2026-11-26

人用三步：

1. 複製 `v1.1.80/maya-ds4.example.json` 為 `maya-ds4.json`，改模型路徑、port、host。
2. 套補丁：`git apply v1.1.80/patches/*.patch`。
3. 起服務後打 `/v1/models`，再送一次最小 `chat/completions`。

AI 用三頁：先讀 `AGENTS.md`，再查 `PITFALLS.md`，再追 `catalogue/records.md`。

更新上游後：跑 `v1.1.80/reapply.sh`，重啟服務，`git diff` 應為空。

## 使用限制

- 僅保證 v1.1.80；路徑請用 `$HOME` 相對寫法。
