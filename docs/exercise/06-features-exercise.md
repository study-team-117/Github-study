# 06 GitHubの便利な機能｜ミニ演習

[← 06章の本編](../06-features.md) ｜ [目次に戻る](../../README.md#目次)

> **形式：個人**
>
> **演習の目安**　基本 5分 ｜ 応用 10〜15分 ｜ 発展 10〜15分
>
> 各段階の目安は事前準備を終えてからの時間です。基本から応用へ進み、発展は余裕があれば取り組みます。
> 発展演習の所要時間は、Actionsの実行待ちで延びることがあります。

## 事前準備

自分の練習用リポジトリ `git-practice` を使います。GitHubでIssuesが有効で、既定ブランチが `main` であることを確認します。VSCodeで練習用リポジトリを開き、`git status` で未コミットの変更がないことを確認します。

## 基本演習

### 課題1：Issueに作業と完了条件を書く

**Issues → New issue** から「GitHub機能の学習メモを追加」というIssueを作ります。本文に作業内容と完了条件を書きます。完了条件には、`github-features-note.md` にIssuesとPull Requestの使い分けが書かれ、`main` から読めることを含めます。作成後にIssue番号を控えます。

**完了チェック**

- [ ] 作業内容と完了条件を書いたIssueを作成し、Issue番号を控えた。

## 応用演習

### 課題2：Pull RequestをIssueに関連付ける

1. PCで `main` に切り替え、`git pull --ff-only` で更新します。`docs/github-features-note` ブランチを作り、`github-features-note.md` にIssuesとPull Requestの用途を1行ずつ書きます。
2. 対象ファイルを確認してコミットし、作業用ブランチをpushします。
3. GitHubで `main` 向けのPRを作ります。説明欄に変更内容と確認方法を書き、`Closes #12` の `12` を実際のIssue番号に置き換えて記載します。
4. 差分を確認してマージします。Issueが **Closed** になり、GitHubの `main` にメモが表示されることを確認します。

**完了チェック**

- [ ] PRをマージし、GitHubの `main` に学習メモがある。
- [ ] Issueが **Closed** になり、PRとの関連を確認できた。

## 発展演習

### Actionsの失敗ログから原因を見つける

練習用リポジトリでActionsが利用でき、ワークフローファイルをpushできる場合に取り組みます。

1. 課題2のマージ後、PCの `main` を更新し、新しいブランチ `practice/actions-check` を作ります。
2. [本編のPythonの例](../06-features.md#pythonの最小例)を使って、`test_sample.py` と `.github/workflows/python-test.yml` を用意します。初回だけ、`assert add(2, 3) == 6` として、失敗を確認できるようにします。
3. 2ファイルをコミットしてpushし、`main` 向けのPRを作ります。PRの **Checks** で失敗したジョブを開き、`Run tests` のログから期待値と実際の値を確認します。
4. 期待値を `5` に直し、同じブランチでコミットしてpushします。同じPRのチェックが成功することを確認します。

**完了チェック**

- [ ] 失敗ログから期待値と実際の値を確認し、修正後に同じPRのチェックが成功した。

## 回答例・解説

[回答例・解説を読む](answer/06.md)

---

[← 06章の本編](../06-features.md) ｜ [目次に戻る](../../README.md#目次) ｜ [07 Git・GitHub応用編 →](../07-advanced.md)
