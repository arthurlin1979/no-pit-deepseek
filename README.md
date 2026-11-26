# 不踩坑：DeepSeek V4.1 Flash ＋ Maya-DS

[English version](README.en.md)

核對日期：2026-11-26

給 AI agents 與開發者用的 Maya-DS 實戰紀錄：在 RTX PRO 6000 上把 DeepSeek V4.1 Flash 跑穩的參數、補丁與量測，不含其他引擎的切換操作。

本專案整理版本選擇、安裝、驗收、輸出契約、快取與速度量測。數字來自 OB 報告與引擎日誌，部分由 AI 協助整理，不宣稱所有方法皆為原創。

## 為什麼有這個專案

說句實話，Qwen3.8 是真的快又好用，日常任務丟給它又省又穩。但一碰到比較複雜的內容、要從零開創新東西的時候，它就很容易卡關，繞來繞去出不來。這種時候，還是得請更大的模型出來，也就是 DeepSeek。

原則上 2.5 這個等級就已經非常厲害了，跑測試基本上都會過。剩下一些簡單的小錯，在實際 agent 流程裡多半會被過濾掉，不過為了安全起見，還是稍微修一下，讓輸出穩定一點。

跟 Qwen3.8 比起來，DeepSeek 多出來的不是分數，而是創造跟推理的能力，這是做評測做不出來的。RTX 6000 跑起來其實有點慢，5090 跑起來也有點痛苦，但為了解決問題，有時候不得不使用。尤其最近 DeepSeek 線上版常常有點問題，能在本地還原 99% 線上版的 AI，就變得很重要。

技術面補一句：DeepSeek V4.1 Flash 用 Maya-DS 跑得動，但預設值是給通用環境的：JSON 常包 code fence、長文重讀很慢、思考預算預設太大、更新會洗掉自訂參數。我把驗收 88/89 過程中踩到的坑全部留下來，做成可重套的補丁與設定。這包只保證 v1.1.80 的行為，其他版本僅供參考。

![鎮站之貓](assets/cat.jpg)

## 先從這裡讀

- [給 AI agents 的入口](AGENTS.md)：先讀本檔，再查 PITFALLS 與 catalogue。
- [30 秒 Quick Start](QUICKSTART.md)：起服務、驗收、重套補丁三步。
- [避坑速查表](PITFALLS.md)：DS-001 起的速查入口，只作索引。
- [完整紀錄索引](catalogue/INDEX.md)：逐條保留原編號與處理結果。
- [實測速度](catalogue/speed.md)：decode／prefill／併發實測。
- [變更區塊說明](BLOCKS.md)：本專案對上游的所有修改，含實證狀態。
- [來源與版本](SOURCES.md)：來源、版本、證據邊界。
- [第三方聲明](THIRD_PARTY_NOTICES.md)：第三方內容授權範圍。
- [v1.1.80 版自述](v1.1.80/RELEASE.md)：現行預設版本的故事。
- [範例設定](v1.1.80/maya-ds4.example.json)：去識別化的設定範本。
- [補丁](v1.1.80/patches/)：輸出契約與 run script 補丁。
- [重套工具](v1.1.80/reapply.sh)：更新後一鍵重套。

## 最小操作方式

1. 取 `v1.1.80/maya-ds4.example.json`，改模型路徑與 port，存成 `maya-ds4.json`。
2. 套補丁：`git apply v1.1.80/patches/*.patch`，或跑 `v1.1.80/reapply.sh`。
3. 起服務，打 `/v1/models` 與一次 `chat/completions` 驗收。

## 核心表格

| 項目 | 值（核對日期 2026-11-26） |
|---|---|
| 引擎 | Maya v1.1.80，`maya-ds4`，`--parallel 4` |
| 模型 | DeepSeek-V4.1-Flash Maya-S，context 262144 |
| 89 題 | 88/89（契約版；公平 harness 89/89） |
| decode | 中位約 70 tok/s（無外來負載；有併發會掉） |
| 32K prefill | 冷讀約 9 秒，重用約 0.04 秒 |
| 250K 重取 | 換對話後再回約 0.21 秒（同 prompt 立即重送不命中） |
| 思考預算 | 2048，`reasoning_effort low` |
| 去審查 | abliteration 預設 on，約慢 5% |

## 已知限制

- 250K 同 prompt 立即重送不會命中 slot，這是引擎語義，不是故障。
- abliteration 會讓 decode 慢約 5%，要速度可在單一 request 關掉。
- 閒置 RAM 幫不了 decode（專家已全在 RAM），只能拿去加大對話保留。
- `chat_template.jinja` 不是 DeepSeek 渲染路徑，改它沒用。

## 授權

MIT，見 [LICENSE](LICENSE)。第三方內容見 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

## 範圍與維護

- 歷史記載，未重跑全部流程驗證；僅保證 v1.1.80 在當時環境的行為。
- 不屬於本包的東西：其他引擎的安裝與切換操作、私人對話紀錄、家目錄絕對路徑。
- 同系列互連：[no-pit-qwen38](https://github.com/arthurlin1979/no-pit-qwen38) ／ [no-pit-glm](https://github.com/arthurlin1979/no-pit-glm) ／ [no-pit-google-workspace](https://github.com/arthurlin1979/no-pit-google-workspace)。

## 使用限制

- 來源層幫助選擇驗證方法，不表示每條都是上游缺陷。
- 沒有重跑全部 live 流程，歷史搜尋鏈未完整保留。
- 新問題先歸類再補來源；不要因相似錯誤碼套用過去根因。
