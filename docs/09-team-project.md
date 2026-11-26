# 09 チーム開発総合演習

[← 08 セキュリティと安全な開発](08-security.md) ｜ [目次に戻る](../README.md#目次)

2人で練習用リポジトリのREADMEを改善します。誰が何を担当するか決め、変更をレビューしてから取り込むまでを通して経験します。

## 9-1. 今回作るもの

READMEに「使い方」と「困ったとき」を追加します。1人が1つのIssueを担当し、もう1人がPRを確認します。最終的に `main` のREADMEを開けば、使い方と困ったときの手順が両方読める状態にします。

| 段階 | やること | 終わったと判断できる状態 |
|---|---|---|
| 基本演習 | Issueで分担し、1件目の変更をPRから取り込む | 「使い方」のPRがマージされ、担当Issueが閉じている |
| 応用演習 | 役割を交代してレビューし、指摘に対応する | 2件目のPRにレビューと修正の記録があり、「困ったとき」も入っている |
| 発展演習 | 競合を解消し、両者の意図を1行にまとめる | 競合を解消した理由をPRで説明でき、`main` に反映されている |

## 9-2. 作業開始前に合意すること

- Issueで担当範囲と完了条件を決めます。1つのPRには1つの作業をまとめます。
- PRを確認する人と、マージする権限を持つ人を決めます。
- レビューでは、完了条件を満たしているか、動作や表示をどう確認したか、秘密情報や対象外の変更が含まれていないかを見ます。
- 指摘を受けたら、同じ作業ブランチに修正をpushし、PRで再確認を依頼します。

---

## 演習問題

- [演習09：2人でREADMEを改善する](exercise/09-team-project-exercise.md)
- [演習09：回答例・解説](exercise/answer/09.md)

---

## 参考資料（公式）

- [GitHub Docs：GitHub Flow](https://docs.github.com/ja/get-started/using-github/github-flow)
- [GitHub Docs：Pull Requestの変更をレビューする](https://docs.github.com/ja/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request)

---

[← 08 セキュリティと安全な開発](08-security.md) ｜ [目次に戻る](../README.md#目次)
