# 01 Git・GitHubの基本操作

> **対象**：GitHubを初めて使う人  
> **目安時間**：45〜60分（実習込み）  
> **ゴール**：ブラウザでファイルを編集できる／VSCodeで編集した内容をGitHubに反映できる／最新の変更を取得できる

[← 目次に戻る](../README.md) ｜ [00 インストール・初期設定](00-setup.md) ｜ [02 ブランチの操作](02-branch.md)

---

## 1-1. この章で学ぶこと

GitHubには、大きく分けて次の2つの操作方法があります。

| 方法 | 作業する場所 | 向いている作業 |
|---|---|---|
| **ブラウザ操作** | GitHubのWebサイト | READMEの修正、簡単なファイル追加、変更履歴の確認 |
| **ローカル操作** | PCのVSCode・ターミナル | プログラムの作成、複数ファイルの編集、動作確認 |

どちらも最終的にはGitHub上のリポジトリに変更を記録できます。この章では**ブラウザ操作 → VSCodeでの操作**の順に試します。

### 用語を先に確認

- **リポジトリ（repository）**：ファイルとその変更履歴を管理する場所。
- **ローカル**：自分のPC上にある作業環境。
- **リモート**：GitHubなど、ネットワーク上にある共有先。
- **コミット（commit）**：変更内容を履歴として記録すること。
- **プッシュ（push）**：ローカルのコミットをリモートに送ること。
- **プル（pull）**：リモートの更新をローカルに取り込むこと。

> **注意**：GitHub上の編集とローカルの編集は、常に自動同期されるわけではありません。変更を反映するには適切な操作が必要です。

---

## 1-2. ブラウザでリポジトリを作成する

1. [GitHub](https://github.com/) にログインします。
2. 右上の **＋** メニューなどから **New repository** を選びます（画面表示は変更される場合があります）。
3. **Repository name** に `git-practice` などの名前を入力します。
4. **Public**（公開）または **Private**（非公開）を選びます。練習用ならPrivateでも構いません。
5. **Add a README file** をオンにします。
6. **Create repository** を押します。

**確認ポイント**：`README.md` が表示されていれば成功です。

> **Publicの注意**：公開リポジトリの内容は誰でも閲覧できます。パスワード、APIキー、個人情報などは載せないでください。

### README.mdとは？

リポジトリの説明書として使われることが多いMarkdownファイルです。`# 見出し`、`- 箇条書き`、`[文字](URL)` などの記法で整理できます。

---

## 1-3. ブラウザでREADMEを編集してコミットする

1. 作成したリポジトリで `README.md` を開きます。
2. 右上付近の鉛筆アイコン（**Edit this file**）を押します。
3. 例えば次の内容を追記します。

```markdown
## 自己紹介

GitHubの操作を練習しています。
```

4. **Commit changes...** を押します。
5. コミットメッセージに `READMEに自己紹介を追加` などと入力します。
6. 変更をコミットします（練習用リポジトリでは、まず直接 `main` にコミットして構いません）。

**確認ポイント**：READMEの表示が変わり、**Commits** などから変更履歴を確認できます。

### ブラウザで新しいファイルを作る

リポジトリ画面で **Add file → Create new file** を選び、ファイル名に `memo.md` と入力します。内容を記入してコミットすれば、新しいファイルが追加されます。

> ブラウザ上のコミットはGitHub上で直接行われます。ローカルで `git add` や `git push` を実行する必要はありません。

---

## 1-4. リポジトリをPCにcloneする

**clone（クローン）** は、GitHub上のリポジトリを変更履歴ごとPCにコピーする操作です。

1. リポジトリの **Code** ボタンを押します。
2. **HTTPS** のURL（例：`https://github.com/ユーザー名/git-practice.git`）をコピーします。
3. VSCodeを開き、**Terminal → New Terminal** でターミナルを開きます。WindowsならPowerShellでもコマンドプロンプトでも構いません。
4. 保存先のフォルダに移動してからcloneします。

```bash
# 例：保存先のフォルダに移動（Windows）
cd %USERPROFILE%\Documents

# コマンドプロンプトで実行する例。URLは自分のものに置き換える
 git clone https://github.com/ユーザー名/git-practice.git
cd git-practice
```

**PowerShellの場合**、最初の移動コマンドは `cd "$HOME\Documents"` のように書きます。`Documents` が別の場所にあるPCでは、実際の保存先を指定してください。

> **重要**：上の `git clone` の行頭の空白は入力不要です。`ユーザー名` は自分のGitHubユーザー名に置き換えてください。

VSCodeで **File → Open Folder** から `git-practice` フォルダを開きます。

**確認ポイント**：`README.md` と `memo.md` がPC側でも確認できます。

### clone時に認証を求められたら

Git for WindowsのGit Credential Managerが使える環境では、GitHubへのブラウザログインが表示されることがあります。画面に従って認証してください。HTTPSでのGit操作に、GitHubアカウントの通常のパスワードを直接入力して認証する方式は使えません。

---

## 1-5. VSCodeでファイルを編集する

1. VSCodeのエクスプローラーで `README.md` を開きます。
2. 次のような一文を追記します。

```markdown
VSCodeからファイルを編集しました。
```

3. **Ctrl + S** で保存します。
4. VSCodeのターミナルで以下を実行します。

```bash
git status
```

`modified: README.md` のように表示されれば、Gitが変更を認識しています。

> **ポイント**：ファイルを保存しただけでは、まだGitHubには反映されません。

---

## 1-6. add → commit → pushでGitHubに反映する

ローカルの変更をGitHubに反映する基本的な流れです。

```text
VSCodeで編集・保存
      ↓
git add（コミット対象を選ぶ）
      ↓
git commit（変更を履歴に記録）
      ↓
git push（GitHubに送信）
```

### ① 変更を確認する

```bash
git status
git diff
```

- `git status`：変更されたファイルやGitの状態を表示します。
- `git diff`：まだステージングしていない変更の差分を表示します。

### ② 変更をステージングする

```bash
git add README.md
```

`git add` は、次のコミットに含める変更を選ぶ操作です。`git add .` なら現在のディレクトリ以下の変更をまとめて追加できますが、**意図しないファイルが含まれないか確認してから使いましょう**。

### ③ コミットする

```bash
git commit -m "READMEを更新"
```

`-m` はコミットメッセージを指定するオプションです。何を変更したか分かる短い文章を付けます。

### ④ GitHubにpushする

```bash
git push origin main
```

- `origin`：clone時に設定されるリモートリポジトリの一般的な名前。
- `main`：送信先のブランチ名。この教材では `main` を使います。

**確認ポイント**：GitHubのリポジトリページを再読み込みし、READMEの追記が反映されていれば成功です。

> **注意**：共有リポジトリでは、他の人が先に更新しているとpushが拒否されることがあります。慌てて `--force` を付けないでください。対応は04章で説明します。

### VSCodeの画面からも操作できる

VSCode左側の **ソース管理（Source Control）** から、変更の確認、ステージング、コミット、同期などを行えます。まずはコマンドで操作の意味を理解し、その後に画面操作も試してみてください。

---

## 1-7. pullでGitHubの最新変更を取得する

ブラウザでREADMEを編集すると、GitHub側の内容がローカルより新しくなります。ローカルに取り込むには `git pull` を使います。

### 実習

1. GitHubのブラウザ画面で `README.md` に `ブラウザから追記しました。` と書いてコミットします。
2. VSCodeのターミナルに戻ります。
3. ローカルに未コミットの変更がないことを確認します。

```bash
git status
```

4. 次を実行します。

```bash
git pull origin main
```

5. VSCodeでREADMEを開き、ブラウザで追加した一文が反映されているか確認します。

**確認ポイント**：ローカルにもGitHub上の変更が取り込まれれば成功です。

> `git pull` はリモートの変更を取得して現在のブランチに統合する操作です。ローカルに未コミット変更がある場合や履歴が分岐した場合、追加の対応が必要になることがあります。

---

## 1-8. よく使うコマンド早見表

| コマンド | 役割 |
|---|---|
| `git clone URL` | GitHubのリポジトリをPCにコピーする |
| `git status` | 現在の状態を確認する |
| `git diff` | 変更内容を確認する |
| `git add ファイル名` | 変更をステージングする |
| `git commit -m "説明"` | 変更を履歴に記録する |
| `git push origin main` | ローカルのコミットをGitHubに送る |
| `git pull origin main` | GitHubの更新をローカルに取り込む |
| `git log --oneline` | コミット履歴を簡潔に表示する |
| `git remote -v` | 接続先のリモートURLを確認する |

---

## 1-9. よくあるつまずき

### `fatal: not a git repository` と表示される

Git管理されていないフォルダでコマンドを実行している可能性があります。`cd git-practice` などで、cloneしたリポジトリの中に移動してください。

### `nothing to commit, working tree clean` と表示される

Gitが認識する未コミットの変更がない状態です。ファイルを保存したか、すでにコミット済みでないか確認しましょう。エラーとは限りません。

### `Author identity unknown` と表示される

Gitの名前とメールアドレスが未設定の可能性があります。[00 インストール・初期設定](00-setup.md) の `git config` の手順を確認してください。

### `rejected` / `non-fast-forward` と表示される

GitHub側にローカルにないコミットがある可能性があります。`git status` を確認し、他の人の変更を取り込んでからpushします。**安易に `git push --force` は使わないでください**。

### 認証画面が表示される／認証に失敗する

HTTPS認証ではブラウザでのログインが必要になる場合があります。Git Credential Managerの設定やGitHubへのログイン状態を確認してください。

---

## 1-10. 理解度チェック・実習課題

### チェックリスト

- [ ] GitHub上でリポジトリを作成できた
- [ ] ブラウザでREADMEを編集・コミットできた
- [ ] リポジトリをPCにcloneできた
- [ ] VSCodeで編集し、`git status` で変更を確認できた
- [ ] `add → commit → push` でGitHubに反映できた
- [ ] ブラウザの変更を `pull` でPCに取り込めた

### 確認問題

1. `git add` と `git commit` は何が違うでしょうか？
2. VSCodeでファイルを保存しただけで、GitHubの内容も変わるでしょうか？
3. GitHub上で編集した内容をPCに取り込むコマンドは何でしょうか？

<details>
<summary>解答を見る</summary>

1. `git add` は次のコミットに含める変更を選び、`git commit` はその変更を履歴に記録します。
2. 変わりません。通常はコミットした後にpushする必要があります。
3. `git pull` です。

</details>

---

## 参考資料（公式）

- [GitHub Docs：リポジトリの作成](https://docs.github.com/ja/repositories/creating-and-managing-repositories/creating-a-new-repository)
- [GitHub Docs：ファイルの編集](https://docs.github.com/ja/repositories/working-with-files/managing-files/editing-files)
- [GitHub Docs：リポジトリのクローン](https://docs.github.com/ja/repositories/creating-and-managing-repositories/cloning-a-repository)
- [GitHub Docs：Gitについて](https://docs.github.com/ja/get-started/using-git/about-git)
- [VSCode公式：Source Control](https://code.visualstudio.com/docs/sourcecontrol/overview)

---

[← 00 インストール・初期設定](00-setup.md) ｜ [目次に戻る](../README.md) ｜ [02 ブランチの操作 →](02-branch.md)
