# PITFALLS — DeepSeek ＋ Maya-DS 速查表

核對日期：2026-11-26

ID 統一 `DS-xxx`。本表只作入口，深度在 `catalogue/records.md`。

| ID | 主題／來源層 | 容易誤判的地方 | 建議處理與驗證 |
|---|---|---|---|
| DS-001 | 版本選擇；本專案 | 追最新版最穩 | DS 程式在 v1.1.78 後凍結，v1.1.79／80 只動 Inkling；pin `v1.1.80`，出事退 `v1.1.78`。驗：`git describe` 與 `--version` 讀回 |
| DS-002 | 安裝下載；本專案 | HF token 會加速 | 公開 repo 不帶 token 也同速；setup 內建 `curl -C -` 續傳。驗：檔案數＋大小對 HF LFS |
| DS-003 | 快取 symlink；本專案 | `/storage` 當執行路徑 | `/storage` 是備份區；壞 symlink 會讓 `huggingface_hub` 寫快取失敗。驗：`ls -ld ~/.cache/huggingface` 不是斷連 |
| DS-004 | JSON 格式；本專案 | 模型推理不行 | 只是多話＋code fence；伺服器端輸出契約可補回 2 題。驗：重跑 EXT-026／028 |
| DS-005 | 工具呼叫；本專案＋harness | 答錯 | 一次回兩個 tool_call，harness 只收單一。驗：放寬 harness 為允許多呼叫 |
| DS-006 | 輸出契約位置；本專案 | 改 `chat_template.jinja` | DeepSeek 走 `serve/ds41_encoding.py`，Jinja 不是渲染器；改 `serve/frontend.py` 接 system。驗：散文無 fence、JSON 無前言 |
| DS-007 | 嚴格 JSON；官方＋本專案 | `response_format` 萬用 | prompt 內要有 `json` 字樣、`max_tokens` 要夠、失敗 content 可能空白要重試。驗：curl 最小案例 |
| DS-008 | Slot 語義；本專案 | 同 prompt 重送測快取 | 那是 rewind，不是命中；正確測法是 A→B→A。驗：250K 取回約 0.21 秒 |
| DS-009 | 思考預算；本專案 | 預設 32768 最好 | 日常設 2048＋low；單一 request 可調 high。驗：啟動日誌 `thinking budget` |
| DS-010 | 去審查代價；本專案 | abliteration 免費 | 每層多一次投影，約慢 5%；單一 request 可 `"ablate": 0`。驗：引擎日誌分段中位 |
| DS-011 | RAM 誤區；本專案 | 加 RAM 加速 decode | 專家已 100% 在 RAM；RAM 只能加大對話保留。驗：啟動日誌 `copied into RAM` |
| DS-012 | THP；官方文件 | 開 THP 會快 | 本機 THP 是 `madvise`，開了複製更慢。驗：不開，decode 無退步 |
| DS-013 | 速度算法；本專案 | client 首 token 法 | 會把思考時間排除，數字虛高；以引擎 `timings` 與 request 行為準。驗：兩邊對齊 `#144 56.7` |
| DS-014 | 更新洗設定；上游 issue #1089 | setup 會保留自訂 | 會掉未知鍵；用 `reapply.sh`＋`restore-config.py` 重套。驗：重跑後 `git diff` 為空 |
| DS-015 | whoami 驗證；本專案 | v1 回 Invalid 即 token 壞 | fine-grained token 要用 whoami-v2 驗。驗：`arthurlin1979／fineGrained` |

## 使用限制

- 來源層幫助選擇驗證方法，不表示每條都是上游缺陷。
- 沒有重跑全部 live 流程，歷史搜尋鏈未完整保留。
- 新問題先歸類再補來源；不要因相似錯誤碼套用過去根因。
