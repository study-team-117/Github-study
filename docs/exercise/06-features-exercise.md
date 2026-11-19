# 06 GitHubの便利な機能｜ミニ演習

[← 06章の本編](../06-features.md) ｜ [← 教材の目次](../../README.md#目次)

> **目安：15〜20分** ｜ **形式：個人**

## 準備

自分の練習用リポジトリ `git-practice` を使います。GitHubでIssuesが有効で、既定ブランチが `main` であることを確認します。VSCodeで練習用リポジトリを開き、`git status` で未コミットの変更がないことを確認します。

## 課題1：Issueに作業と完了条件を書く

**Issues → New issue** から「GitHub機能の学習メモを追加」というIssueを作ります。本文に作業内容と完了条件を書きます。完了条件には、`github-features-note.md` にIssuesとPull Requestの使い分けが書かれ、`main` から読めることを含めます。作成後にIssue番号を控えます。

## 課題2：Pull RequestをIssueに関連付ける

1. PCで `main` に切り替え、`git pull --ff-only` で更新します。`docs/github-features-note` ブランチを作り、`github-features-note.md` にIssuesとPull Requestの用途を1行ずつ書きます。
2. 対象ファイルを確認してコミットし、作業用ブランチをpushします。
3. GitHubで `main` 向けのPRを作ります。説明欄に変更内容と確認方法を書き、`Closes #12` の `12` を実際のIssue番号に置き換えて記載します。
4. 差分を確認してマージします。Issueが **Closed** になり、GitHubの `main` にメモが表示されることを確認します。

**完了チェック**　Issueの完了条件を満たしたことと、IssueとPRの関連をGitHub上で確認できれば完了です。

## 発展課題：Actionsの失敗ログから原因を見つける（任意・10〜15分）

練習用リポジトリでActionsが利用でき、ワークフローファイルをpushできる場合に取り組みます。

1. 課題2のマージ後、PCの `main` を更新し、新しいブランチ `practice/actions-check` を作ります。
2. [本編のPythonの例](../06-features.md#pythonの最小例)を使って、`test_sample.py` と `.github/workflows/python-test.yml` を用意します。初回だけ、`assert add(2, 3) == 6` として、失敗を確認できるようにします。
3. 2ファイルをコミットしてpushし、`main` 向けのPRを作ります。PRの **Checks** で失敗したジョブを開き、`Run tests` のログから期待値と実際の値を確認します。
4. 期待値を `5` に直し、同じブランチでコミットしてpushします。同じPRのチェックが成功することを確認します。この発展課題は成功を確認した時点で完了です。

[06章の回答例・解説](answer/06.md)

---

[← 06章の本編](../06-features.md) ｜ [← 教材の目次](../../README.md#目次) ｜ [07 応用編へ進む →](../07-advanced.md)
