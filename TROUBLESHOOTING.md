# TROUBLESHOOTING — 症狀入口

核對日期：2026-11-26

- JSON 包 code fence、有前言 → 查 DS-004、DS-006 → 解法見 `catalogue/records.md DR-04、DR-06`。
- 一次回兩個 tool_call，被判 turn-limit → 查 DS-005 → `DR-05`。
- `response_format` 回空白 → 查 DS-007 → `DR-07`（prompt 加 json 字、調大 max_tokens、可重試）。
- 同 prompt 重送還是慢 → 查 DS-008 → `DR-08`（改 A→B→A 測法）。
- 更新後參數消失 → 查 DS-014 → 跑 `v1.1.80/reapply.sh`。
- 速度數字對不上 → 查 DS-013 → 以引擎 timings 為準。

## 使用限制

- 每個連結都進入有處理與界線的內容，不只是索引。
- 歷史記載，未重跑全部 live 流程。
