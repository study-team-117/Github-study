# 07 Git・GitHub応用編｜ミニ演習

[← 07章の本編](../07-advanced.md) ｜ [目次に戻る](../../README.md#目次)

> **形式：個人**
>
> **演習の目安**　基本 10〜15分 ｜ 応用 10分 ｜ 発展 5〜10分
>
> 各段階の目安は事前準備を終えてからの時間です。基本から応用へ進み、発展は余裕があれば取り組みます。

## 事前準備

既存のリポジトリの外に空のフォルダ `git-advanced-practice` を作り、VSCodeで開きます。そのフォルダのターミナルで `git init -b main` を実行します。GitHubへの接続は不要です。

`README.md` に「# Git応用演習」と書いて保存し、最初のコミットを作ります。

```bash
git add README.md
git commit -m "Add practice README"
```

## 基本演習

### 課題1：rebaseで作業ブランチの起点を更新する

1. `main` から `practice/guide` を作り、`guide.md` に「# 作業ガイド」と書いてコミットします。メッセージは `Add practice guide` にします。
2. `main` に切り替え、`README.md` に「応用コマンドを練習する。」と追記してコミットします。
3. `git log --oneline --graph --all` で2つのブランチが分かれていることを確認します。作業ブランチに切り替え、`git status` で変更がないことを確認してから `git rebase main` を実行します。
4. 履歴を再確認し、作業ブランチのコミットが `main` の最新コミットの上にあることと、作業ブランチのコミットIDが変わったことを確かめます。

**完了チェック**

- [ ] rebase後、作業ブランチのコミットが最新の `main` の上にあり、コミットIDが変わった。

## 応用演習

### 課題2：cherry-pickで1件だけ取り込む

1. `practice/guide` に `memo.md` を追加し、「# 個人メモ」と書いて別のコミットにします。
2. `git log --oneline -2` で `Add practice guide` のコミットIDを控えます。
3. `main` から `practice/pick-guide` を作り、控えたIDを指定して `git cherry-pick` を実行します。
4. ファイル一覧に `guide.md` があり、`memo.md` がないことを確認します。

**完了チェック**

- [ ] cherry-pick後、取り込み先に `guide.md` があり、`memo.md` は含まれていない。

## 発展演習

### worktreeで2つのブランチを別フォルダに開く

今の作業フォルダは `practice/pick-guide` のまま、`git worktree add` で別フォルダに `practice/guide` を開きます。以下のパスに既存のフォルダがある場合は、空いている名前に読み替えます。

```bash
git worktree add ../git-advanced-guide practice/guide
git worktree list
```

VSCodeで追加したフォルダを開き、両方のフォルダの `memo.md` の有無を比べます。確認後はVSCodeの追加フォルダを閉じ、元のフォルダのターミナルで `git worktree remove ../git-advanced-guide` を実行します。変更がある場合は内容を確認してから進めます。

**考えてみよう**　作業ブランチの履歴を新しい起点に移す場合と、別ブランチのコミット1件を取り込む場合では、どのコマンドを使いますか。

**完了チェック**

- [ ] 2つのフォルダで `memo.md` の有無を比較し、練習後に追加したworktreeを削除できた。

## 回答例・解説

[回答例・解説を読む](answer/07.md)

---

[← 07章の本編](../07-advanced.md) ｜ [目次に戻る](../../README.md#目次) ｜ [08 セキュリティと安全な開発 →](../08-security.md)
