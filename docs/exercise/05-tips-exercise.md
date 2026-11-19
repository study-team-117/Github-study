# 05 便利なGitコマンド・小技｜ミニ演習

[← 05章の本編](../05-tips.md) ｜ [← 教材の目次](../../README.md#目次)

> **目安：15〜20分** ｜ **形式：個人**

## 準備

既存のリポジトリの外に、空のフォルダ `git-tips-practice` を作ってVSCodeで開きます。そのフォルダのターミナルで `git init -b main` を実行します。GitHubへの接続は不要です。

`README.md` に「# Gitの練習」、`notes.md` に「# 作業メモ」と書いて保存します。

```bash
git add README.md notes.md
git commit -m "Add practice files"
git status
```

未コミットの変更がないことを確認します。

## 課題1：差分を見て、必要な変更だけをコミットする

1. `README.md` に「差分を確認してからコミットする。」、`notes.md` に「このメモは編集中です。」を追記して保存します。
2. `git status -sb` で2ファイルの状態を確認し、`git diff` で追記した行を見つけます。
3. `README.md` だけをステージします。`git diff --staged` にREADMEの変更だけが表示され、`git diff` に作業メモの変更が表示されることを確認します。
4. 「Update practice README」というメッセージでコミットし、`git show --stat HEAD` で変更されたファイルを確認します。

## 課題2：作業メモを一時退避して戻す

1. 課題1で残した `notes.md` の変更を「作業メモの途中」という名前でstashに退避します。
2. `git stash list` と `git status` を実行し、退避の名前が一覧の先頭にあり、作業フォルダに未コミットの変更がないことを確認します。
3. `git stash pop` で今回の退避を戻します。VSCodeで追記が戻ったことと、`git stash list` からその退避が消えたことを確認します。
4. 戻ったメモを「Update practice notes」というメッセージでコミットし、`git log --oneline -3` でここまでの3件を確認します。

## 発展課題：ローカル専用のファイルを除外する（任意・5分）

1. 練習用に `local-notes.txt` を作り、「PCだけで使う練習メモ」と書きます。まだステージせず、`git status --short` の `??` を確認します。
2. リポジトリのルートに `.gitignore` を作り、`local-notes.txt` を1行で指定します。
3. ファイルがVSCodeに残っていることと、`git status --short` に `.gitignore` だけが表示されることを確認します。`.gitignore` をコミットして、`git status --short --ignored` で `!! local-notes.txt` が表示されることを確認します。

**考えてみよう**　すでにコミットしたファイルを `.gitignore` に追記すると、過去のコミットからも消えるでしょうか。

[05章の回答例・解説](answer/05.md)

---

[← 05章の本編](../05-tips.md) ｜ [← 教材の目次](../../README.md#目次) ｜ [06 GitHubの便利な機能へ進む →](../06-features.md)
