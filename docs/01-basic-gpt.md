# 01 Git・GitHubの基本操作

> **対象**：Git・GitHubを初めて使う人  
> **目安時間**：45〜60分（操作練習を含む）  
> **ゴール**：GitHubでリポジトリを作り、PCにcloneし、VSCodeで編集した内容をpushできる。ブラウザ上の変更をpullで取り込める。

[← 目次に戻る](../README.md) ｜ [00 インストール・初期設定](00-setup.md) ｜ [02 ブランチの操作](02-branch.md)

---

## 1-1. GitとGitHubの基本

**Git** はファイルの変更履歴を記録する仕組み、**GitHub** はGitで管理するファイルをオンラインで共有できるサービスです。

| 用語 | 意味 |
|---|---|
| リポジトリ | ファイルと変更履歴を管理する場所 |
| ローカル | 自分のPC上の作業場所 |
| リモート | GitHubなどのオンライン上の共有先 |
| clone | GitHubのリポジトリをPCにコピーする |
| commit | 変更を履歴として記録する |
| push | PC上のコミットをGitHubに送る |
| pull | GitHub上の更新をPCに取り込む |

この章では、まずGitHubのブラウザで操作し、次に**ターミナル → VSCode**の順に操作します。WindowsとMacの違いは必要な箇所で分けて説明します。

```text
GitHubでリポジトリ作成
       ↓ clone
PCのフォルダ → code . → VSCodeで編集
       ↓ git add → git commit → git push
GitHubに変更が反映される
       ↓ GitHubのブラウザで編集
PCで git pull → 最新の内容を取得
```

> **事前準備**：00章を参考に、GitとVSCodeのインストール、Gitのユーザー名・メールアドレス設定を済ませてください。

---

## 1-2. GitHubでリポジトリを作成する

1. [GitHub](https://github.com/) にログインします。
2. **New repository** を選択します。
3. **Repository name** に `git-practice` と入力します。
4. **Public** または **Private** を選択します。練習用ならPrivateでも構いません。
5. **Add a README file** にチェックを入れます。
6. **Create repository** を押します。

`README.md` が表示されれば成功です。READMEはリポジトリの説明を書くMarkdownファイルです。

> **注意**：Publicのリポジトリは誰でも閲覧できます。パスワードやAPIキーなどは記載しないでください。

---

## 1-3. ブラウザからファイルを編集する

1. リポジトリ内の `README.md` を開きます。
2. 鉛筆アイコン（**Edit this file**）を押します。
3. 次の文章を追記します。

```markdown
## 自己紹介

GitHubの操作を練習しています。
```

4. **Commit changes...** を押します。
5. コミットメッセージに `READMEに自己紹介を追加` と入力し、コミットします。
6. READMEの表示が更新されたことを確認します。

### ブラウザから新しいファイルを作る

リポジトリ画面で **Add file → Create new file** を選び、`memo.md` という名前でファイルを作ってコミットします。

> 今回は個人用の練習リポジトリなので、`main` に直接コミットして構いません。チーム開発では、02・03章で扱う作業ブランチとPull Requestを使います。

---

## 1-4. リポジトリをPCにcloneする

ここからはPCで操作します。**clone** はGitHubのリポジトリを変更履歴ごとPCにコピーする操作です。

### ① GitHubでURLをコピーする

リポジトリ画面の **Code → HTTPS** からURLをコピーします。

```text
https://github.com/ユーザー名/git-practice.git
```

### ② ターミナルを開く

- **Windows**：スタートメニューで `cmd` と検索し、**コマンドプロンプト**を起動します。
- **Mac**：`Command + Space` でSpotlightを開き、`ターミナル`（Terminal）と入力して起動します。

### ③ 保存先に移動する

今回は、OSに関係なく**自分のホームフォルダ**を保存先にします。

**Windows（コマンドプロンプト）**

```cmd
cd /d %USERPROFILE%
```

**Mac（ターミナル）**

```bash
cd ~
```

> 保存先は任意です。すでに `git-practice` フォルダがある場合は、別の保存先を選んでください。

### ④ cloneしてフォルダに移動する（Windows・Mac共通）

```bash
git clone https://github.com/ユーザー名/git-practice.git
cd git-practice
```

`ユーザー名` は自分のGitHubユーザー名に置き換えます。Privateリポジトリの場合、認証画面が出ることがあります。

### ⑤ `code .` でVSCodeを開く（Windows・Mac共通）

`cd git-practice` でリポジトリの中に移動したら、次を実行します。

```bash
code .
```

- `code`：VSCodeを起動するコマンド
- `.`（ドット）：現在いるフォルダを表す

**`code .` は「今いるフォルダをVSCodeで開く」**という意味です。VSCodeのエクスプローラーに `README.md` と `memo.md` が表示されれば成功です。

### OS別：ここまでのコマンド一覧

**Windows（コマンドプロンプト）**

```cmd
cd /d %USERPROFILE%
git clone https://github.com/ユーザー名/git-practice.git
cd git-practice
code .
```

**Mac（ターミナル）**

```bash
cd ~
git clone https://github.com/ユーザー名/git-practice.git
cd git-practice
code .
```

> **Macで `code: command not found` と表示された場合**：VSCodeを開き、`Command + Shift + P` → `Shell Command: Install 'code' command in PATH` を実行します。その後、ターミナルを開き直してください。
>
> **Windowsで `code` が認識されない場合**：VSCodeのPATH設定を確認し、コマンドプロンプトを開き直してください。
>
> **共通の代替方法**：VSCodeの **File → Open Folder**（Macでは **File → Open Folder...**）から `git-practice` を選んでも構いません。
>
> **WindowsのPowerShellの場合**：ホームフォルダへの移動は `cd $HOME` です。それ以外のコマンドは共通です。

---

## 1-5. VSCodeでファイルを編集し、変更を確認する

1. VSCodeのエクスプローラーで `README.md` を開きます。
2. 末尾に次の一文を追加します。

```markdown
VSCodeからファイルを編集しました。
```

3. **Ctrl + S** で保存します。
4. VSCodeのメニューから **Terminal → New Terminal** を選びます。
5. ターミナルで次のコマンドを実行します。

```bash
git status
git diff
```

- `git status`：どのファイルが変更されたかを確認する
- `git diff`：変更前と変更後の差分を確認する

`modified: README.md` のように表示されれば、変更を認識できています。

> **重要**：VSCodeで保存しただけでは、GitHubには反映されません。

---

## 1-6. add → commit → pushでGitHubに反映する

変更をGitHubに送るには、基本的に次の3段階を行います。

```text
編集・保存
   ↓
git add（コミット対象を選ぶ）
   ↓
git commit（PC上に変更履歴を記録）
   ↓
git push（GitHubに送信）
```

### ① 変更をステージングする

```bash
git add README.md
```

`git add` は、次のコミットに含める変更を選ぶ操作です。`git add .` で複数ファイルをまとめて選べますが、不要なファイルを含めないよう注意してください。

### ② コミットする

```bash
git commit -m "READMEを更新"
```

`-m` の後には、何を変更したか分かる短いメッセージを書きます。

### ③ GitHubにpushする

```bash
git push origin main
```

- `origin`：cloneしたときに登録されるリモートの一般的な名前
- `main`：この教材で使用するブランチ名

GitHubのリポジトリ画面を再読み込みし、追記した文章が表示されれば成功です。

> **注意**：他の人が先にGitHubを更新していると、pushが拒否されることがあります。安易に `git push --force` は使わず、04章の対処方法を確認してください。

### VSCodeの画面から操作する方法

左側の **ソース管理（Source Control）** から、変更の確認、ステージング、コミット、pushなどもできます。最初はコマンドで仕組みを理解すると、画面操作の意味も分かりやすくなります。

---

## 1-7. pullでGitHubの最新変更を取り込む

今度は逆に、**GitHub上で編集した内容をPCに取り込みます**。

1. GitHubのブラウザで `README.md` を開き、`ブラウザから追記しました。` と追加してコミットします。
2. VSCodeに戻り、ターミナルで作業状態を確認します。

```bash
git status
```

3. 未コミットの変更がない状態で、次を実行します。

```bash
git pull origin main
```

4. VSCodeでREADMEを確認し、ブラウザで追加した文章が反映されていれば成功です。

> `git pull` はGitHubの変更を取得して現在のブランチに統合します。ローカルに未コミット変更がある場合や、履歴が分岐した場合は追加の対応が必要になることがあります。

---

## 1-8. よく使うコマンド早見表

| コマンド | 役割 |
|---|---|
| `cd フォルダ名` | 指定したフォルダへ移動する |
| `code .` | 現在のフォルダをVSCodeで開く |
| `git clone URL` | GitHubのリポジトリをPCにコピーする |
| `git status` | 現在の変更状態を確認する |
| `git diff` | ステージング前の変更内容を確認する |
| `git add ファイル名` | コミット対象を選ぶ |
| `git commit -m "説明"` | 変更を履歴に記録する |
| `git push origin main` | コミットをGitHubに送る |
| `git pull origin main` | GitHubの更新を取り込む |
| `git log --oneline` | コミット履歴を簡潔に表示する |
| `git remote -v` | リモートの接続先を確認する |

---

## 1-9. よくあるつまずき

### `code` コマンドが見つからない

WindowsではVSCodeのPATH設定を確認し、コマンドプロンプトを開き直します。MacではVSCodeのコマンドパレット（`Command + Shift + P`）から `Shell Command: Install 'code' command in PATH` を実行し、ターミナルを開き直します。急ぐ場合はVSCodeの **File → Open Folder** を使えます。

### `fatal: not a git repository` と表示される

Git管理されていないフォルダでコマンドを実行している可能性があります。`cd git-practice` でリポジトリに移動し、`git status` を試してください。

### `nothing to commit, working tree clean` と表示される

未コミットの変更がない状態です。保存忘れや、すでにコミット済みでないかを確認してください。エラーとは限りません。

### `Author identity unknown` と表示される

Gitのユーザー名・メールアドレスが未設定の可能性があります。[00 インストール・初期設定](00-setup.md) の `git config` を確認してください。

### `rejected` / `non-fast-forward` と表示される

GitHub側にローカルにない変更がある可能性があります。**`--force` を付けて解決しようとせず**、[04 エラー・コンフリクト対処](04-troubleshooting.md) を確認してください。

### 認証画面が表示される／認証に失敗する

HTTPS接続ではGit Credential Managerなどによるブラウザ認証が必要になる場合があります。GitHubアカウントの通常のパスワードをGit操作の認証欄に直接入力する方式は使えません。

---

## 1-10. まとめ・理解度チェック

ここまでの基本操作を説明できるか確認しましょう。

- `git clone` と `git pull` は何が違う？
- `code .` の `.` は何を意味する？
- ファイルを保存した後、GitHubに反映するには何をする？
- `git commit` と `git push` は何が違う？
- GitHub上のREADMEを編集した後、PCに反映するには何をする？

### 演習問題（後から追加予定）

演習と回答例は別ファイルとして作成する予定です。完成後、以下のリンクから移動できるようにします。

- [演習01：Git・GitHubの基本操作](exercise/01-basic-exercise.md)
- [演習01：回答例・解説](exercise/01-basic-exercise-answer.md)

---

## 参考資料（公式）

- [GitHub Docs：リポジトリの作成](https://docs.github.com/ja/repositories/creating-and-managing-repositories/creating-a-new-repository)
- [GitHub Docs：リポジトリのクローン](https://docs.github.com/ja/repositories/creating-and-managing-repositories/cloning-a-repository)
- [GitHub Docs：ファイルの編集](https://docs.github.com/ja/repositories/working-with-files/managing-files/editing-files)
- [VSCode公式：Command Line Interface](https://code.visualstudio.com/docs/configure/command-line)
- [VSCode公式：Source Control](https://code.visualstudio.com/docs/sourcecontrol/overview)

---

[← 00 インストール・初期設定](00-setup.md) ｜ [目次に戻る](../README.md) ｜ [02 ブランチの操作 →](02-branch.md)
