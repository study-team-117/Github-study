# 04 エラー・コンフリクト対処｜ミニ演習

[← 04章の本編](../04-troubleshooting.md) ｜ [← 教材の目次](../../README.md#目次)

> **目安：15〜20分** ｜ **形式：個人**
>
> ステージの取り消しと競合解消を練習します。発展課題では、コミット済みの変更を `git revert` で打ち消します。

## 準備：PC内に練習用リポジトリを作る

既存のリポジトリの外に、新しいフォルダ `git-troubleshooting-practice` を作ってVSCodeで開きます。ターミナルを開き、`git init -b main` を実行します。GitHubへの接続は不要です。

VSCodeで `practice.md` を作り、「確認方法：まず手順を読む」と1行書いて保存します。次のコマンドで最初の変更を記録します。

```bash
git add practice.md
git commit -m "Add practice note"
git status
```

`On branch main` と `nothing to commit, working tree clean` を確認します。

## 課題1：ステージだけを取り消す

1. `practice.md` の末尾に「これは一時メモです。」を追記し、保存してステージします。
2. `git status` でステージ済みと確認し、`git restore --staged practice.md` を実行します。
3. `git status` とVSCodeで、ステージから外れても一時メモがファイルに残っていることを確認します。
4. 課題2に進む前に、VSCodeで一時メモの行だけを削除して保存します。`git status` で未コミットの変更がないことを確認します。

## 課題2：同じ行を変更して競合を解消する

1. `main` から `practice/conflict` ブランチを作って切り替えます。最初の行を「確認方法：VSCodeで差分を見る」に置き換えてコミットします。
2. `main` に戻り、同じ行を「確認方法：ターミナルで状態を見る」に置き換えてコミットします。
3. `main` で `git merge practice/conflict` を実行します。`CONFLICT` が表示されたら、`git status` で競合したファイルを確認します。
4. VSCodeで両方の内容を読んで、「確認方法：ターミナルで状態を見て、VSCodeで差分を見る」という1行にまとめます。競合マーカーが残っていないことを確認し、保存します。
5. 修正したファイルをステージし、`git merge --continue` で完了します。`git status` とファイルの内容を確認します。

## 発展課題：コミット済みの変更を打ち消す（任意・5分）

課題2のマージを終えた `main` で、`practice.md` に「取り消し練習の行」を追記し、通常のコミットを1件作ります。`git log --oneline -3` で取り消すコミットを確認し、`git revert` で打ち消します。

**完了チェック**　追記した行だけが消え、履歴に元のコミットと取り消し用のコミットが両方残っていれば完了です。課題2でまとめた「確認方法」の行は残ります。

[04章の回答例・解説](answer/04.md)

---

[← 04章の本編](../04-troubleshooting.md) ｜ [← 教材の目次](../../README.md#目次) ｜ [05 便利なコマンドへ進む →](../05-tips.md)
