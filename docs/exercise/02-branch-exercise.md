# 02 ブランチの操作｜ミニ演習

[← 02章の本編](../02-branch.md) ｜ [目次に戻る](../../README.md#目次)

> **形式：個人**
>
> 作業用ブランチで変更をコミットしてGitHubに送り、`main` と作業用ブランチでファイルの表示がどう変わるかを確かめます。
>
> **演習の目安**　基本 5分 ｜ 応用 5〜10分 ｜ 発展 5〜10分
>
> 各段階の目安は事前準備を終えてからの時間です。基本から応用へ進み、発展は余裕があれば取り組みます。

## 事前準備

- 01章で使った自分の練習用リポジトリ `git-practice` をVSCodeで開く。
- VSCodeのターミナルで `git status` を実行し、`nothing to commit, working tree clean` が表示されることを確認する。
- この演習では、02章本編の `feature/profile` とは別に `feature/branch-practice` を作る。

## 基本演習

### 課題1：作業用ブランチでコミットする

1. `main` に切り替え、`feature/branch-practice` を作成して切り替える。
2. `git branch` を実行し、`*` が `feature/branch-practice` に付いていることを確認する。
3. VSCodeで `branch-practice.md` を新規作成する。見出しに「ブランチ演習」と書き、その下にブランチを使う利点を1行書いて保存する。
4. `git status` で今回のファイルだけが変更として表示されることを確認し、ステージする。
5. もう一度 `git status` を実行し、`Changes to be committed` に `branch-practice.md` だけがあることを確認してから、`Add branch practice` というメッセージでコミットする。

**完了チェック**

- [ ] 作業用ブランチに `Add branch practice` のコミットがある。

## 応用演習

### 課題2：ブランチを切り替えてファイルを確認する

1. `main` に切り替え、VSCodeのファイル一覧に `branch-practice.md` が表示されないことを確認する。
2. `feature/branch-practice` に戻り、ファイルが再び表示されることを確認する。

### 課題3：作業用ブランチをGitHubに送る

1. `feature/branch-practice` をGitHubにpushする。
2. GitHubの練習用リポジトリでブランチ選択メニューを開き、`feature/branch-practice` を選ぶ。
3. `branch-practice.md` が表示されることを確認する。続けてGitHub上で `main` を選び、そこには演習で追加したファイルが表示されないことを確認する。

ここではpushまで行います。この応用演習でpushしたブランチを03章で使います。

<details>
<summary>困ったときのコマンド例</summary>

**課題1**：`git status` で作業中の変更がないことを確認したら、ブランチを作ります。

```bash
git switch main
git switch -c feature/branch-practice
git branch
```

VSCodeで `branch-practice.md` を作成・保存した後、`git status` で変更を確認しながら1行ずつ進めます。

```bash
git status
git add .
git status
git commit -m "Add branch practice"
```

**課題2**：1行ずつ実行し、切り替えるたびにVSCodeのファイル一覧を確認します。

```bash
git switch main
git switch feature/branch-practice
```

**課題3**：作業用ブランチを初めてpushするときは `-u` を付けます。次回から同じブランチで `git push` を使えます。

```bash
git push -u origin feature/branch-practice
```

</details>

**完了チェック**

- [ ] PCとGitHubの両方で、`branch-practice.md` が作業用ブランチにだけ表示されることを確認した。
- [ ] `git status` で未コミットの変更がないことを確認した。

**考えてみよう**　作業用ブランチをpushしても、GitHubの `main` にファイルが表示されないのはなぜでしょうか。

## 発展演習

### 2回目の変更を送り、ブランチを比較する

1. `git status` で `feature/branch-practice` にいることと、未コミットの変更がないことを確認する。
2. `branch-practice.md` に「ブランチを切り替えて確認したこと」を1行追記し、保存する。`git diff` で追記した行を確認する。
3. `git status` で変更が `branch-practice.md` だけであることを確認し、`git add .` でステージする。もう一度 `git status` で対象を確かめてから、`Update branch practice` というメッセージでコミットする。
4. `git push` を実行する。応用演習の課題3で `-u` を付けて送信先を設定したため、今回は `git push` だけで送れる。

#### 差分と履歴を確認する

```bash
git diff --stat main..feature/branch-practice
git log --oneline main..feature/branch-practice
```

- `git diff --stat` で、2つのブランチの間で内容が異なるファイルを確認する。この演習で追加した `branch-practice.md` が表示される。
- `git log --oneline` で、作業用ブランチにあり `main` には入っていないコミットを確認する。この演習の `Update branch practice` と `Add branch practice` が新しい順に表示される。
- GitHubでも作業用ブランチを選び、追記した1行が反映されていることを確認する。

**考えてみよう**　この演習では、差分に表示されるファイルは1つですが、履歴にはコミットが2つあります。それぞれのコマンドは何を比べていますか。

**完了チェック**

- [ ] GitHubの作業用ブランチに追記が表示され、`main` に入っていないコミットを2件確認できた。

## 回答例・解説

[回答例・解説を読む](answer/02.md)

---

[← 02章の本編](../02-branch.md) ｜ [目次に戻る](../../README.md#目次) ｜ [03 チーム開発の基本 →](../03-team.md)
