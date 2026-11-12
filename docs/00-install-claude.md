# GitHub 初期設定ガイド

アカウント作成 → Gitインストール → 名前とメールの設定 → GitHubへの認証、までを一通りやる資料。全部終わるまで30分くらい。最終ゴールは「自分のPCからGitHubにpushできる状態」にすること。

## 全体の流れ

1. GitHubアカウントを作る
2. Gitをインストールする
3. Gitに名前とメールアドレスを登録する
4. GitHubへの認証を設定する（SSH or GitHub CLI）
5. 動作確認として、リポジトリを作ってpushしてみる

---

## 1. GitHubアカウントを作る

[https://github.com](https://github.com) にアクセスして「Sign up」を押す。メールアドレス、パスワード、ユーザー名を入力して、パズル認証とメールの確認コードを通せば作成完了。

ユーザー名は**URLにもコミット履歴にも公開される**から、ちょっとだけ慎重に決めたほうがいい。`github.com/ユーザー名` がそのまま自分のポートフォリオURLになるし、XやInstagramのプロフィールにも貼ることになる。本名っぽいものか、普段のSNSと揃えた名前にしておくと後で困らない。

アカウントを作ったら、すぐに**二要素認証（2FA）**を設定する。GitHubはコード公開サービスの都合上2FAがほぼ必須になっていて、Settings → Password and authentication から認証アプリ（Google AuthenticatorやAuthyなど）かパスキーを登録できる。リカバリーコードは必ずどこかに保存しておくこと。スマホをなくしたときに本当に詰む。

### 大学生ならやっておきたいこと

大学のメールアドレスがあるなら、**GitHub Student Developer Pack**に申請しておくといい。学生は無料でGitHub Copilotなどの有料ツールが使えるようになる。[https://education.github.com/students](https://education.github.com/students) から申請して、Settings → Emails に大学のメールを追加しておくとスムーズ。審査に数日かかることもあるから、早めに出しておくのがおすすめ。

---

## 2. Gitをインストールする

Gitはローカルでバージョン管理をするソフトで、GitHubはそれをネット上で預かって共有するサービス。この2つは別物だから、両方セットで必要になる。

### Windows

公式サイト [https://git-scm.com/download/win](https://git-scm.com/download/win) からインストーラーをダウンロードして実行する。基本は全部デフォルトのまま「Next」で進めて大丈夫。迷いやすいのは次の2点。

- デフォルトエディタの選択: Vimが初期値だけど、慣れてないならVisual Studio Codeを選んでおくと楽。
- 初期ブランチ名: 「Override the default branch name」で `main` を指定しておく。

ターミナルが使えるなら、これでも入る。

```powershell
winget install --id Git.Git -e --source winget
```

### Mac

ターミナルで次を実行する。

```bash
xcode-select --install
```

ダイアログが出てくるからインストールすればGitが使えるようになる。Homebrewを使っているなら `brew install git` でもOK。

### Linux（Ubuntu系）

```bash
sudo apt update
sudo apt install git
```

### インストール確認

どの環境でも、ターミナル（Windowsなら Git Bash か PowerShell）を開いて次を打つ。

```bash
git --version
```

`git version 2.xx.x` みたいに表示されれば成功。Windowsでインストール直後に反応しないときは、ターミナルを一度閉じて開き直す。

---

## 3. 名前とメールアドレスを設定する

Gitは**コミットするたびに「誰がやったか」を記録する**から、最初に名前とメールアドレスを登録しておく必要がある。これを設定しないとコミットのときに怒られる。

```bash
git config --global user.name "あなたの名前"
git config --global user.email "your-email@example.com"
```

`--global` は「このPC全体で使う設定」という意味。リポジトリごとに変えたいときは、そのリポジトリ内で `--global` を外して実行する。

### メールアドレスは非公開にするのがおすすめ

コミット履歴にはメールアドレスが残って、公開リポジトリだと誰でも見られる。これを避けたいなら、GitHubが用意している**noreplyアドレス**を使う。

1. GitHubの Settings → Emails を開く
2. 「Keep my email addresses private」にチェックを入れる
3. 同じ画面に表示される `12345678+ユーザー名@users.noreply.github.com` の形式のアドレスをコピーする
4. そのアドレスをGitのメールとして設定する

```bash
git config --global user.email "12345678+ユーザー名@users.noreply.github.com"
```

あわせて「Block command line pushes that expose my email」にもチェックを入れておくと、うっかり本物のメールを公開するのを防げる。

### ついでに入れておきたい設定

```bash
# 新しく作るリポジトリの最初のブランチ名を main にする
git config --global init.defaultBranch main

# Windowsだけ: 改行コードの違いによるトラブルを防ぐ
git config --global core.autocrlf true

# MacとLinux: 同じ目的で
git config --global core.autocrlf input
```

### 設定内容の確認

```bash
git config --global --list
```

さっき入れた `user.name` と `user.email` が出ていればOK。

---

## 4. GitHubへの認証を設定する

ここが一番つまずきやすいところ。まず大事な前提として、**GitHubはもうパスワードでのpushを受け付けていない**。昔のチュートリアルにある「pushするときにパスワードを入力」はそのままでは通らない。認証には主に次の3つの方法がある。

| 方法 | 向いている人 | 難易度 |
| --- | --- | --- |
| SSH鍵 | 長く使う前提で、一度設定したら楽をしたい人 | 中 |
| GitHub CLI（gh） | とにかく早く終わらせたい人 | 低 |
| Personal Access Token（HTTPS） | 一時的に使いたいときや、SSHが使えない環境 | 中 |

最初に1つだけ選ぶなら、**SSH鍵**が長期的には一番楽。早く動かしたいだけなら**GitHub CLI**が最短。以下で両方書くから、好きなほうを選んでほしい。

### 方法A: SSH鍵で認証する（おすすめ）

**① 鍵を作る**

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

保存場所を聞かれるけど、そのままEnterでOK。パスフレーズは設定しておくのが安全（空でも動く）。`~/.ssh/id_ed25519`（秘密鍵）と `~/.ssh/id_ed25519.pub`（公開鍵）の2つができる。**秘密鍵は絶対に誰にも見せない・アップロードしない**こと。GitHubに渡すのは `.pub` のほうだけ。

**② ssh-agentに鍵を登録する**

Mac / Linux:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Windows（Git Bashで）:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

**③ 公開鍵をコピーする**

```bash
# Mac
pbcopy < ~/.ssh/id_ed25519.pub

# Windows（Git Bash）
clip < ~/.ssh/id_ed25519.pub

# Linux など、表示して手でコピーする場合
cat ~/.ssh/id_ed25519.pub
```

**④ GitHubに登録する**

GitHubの Settings → SSH and GPG keys → 「New SSH key」を開く。Titleに「自分のノートPC」など分かる名前を付けて、Keyの欄にさっきコピーした公開鍵を貼り付けて保存する。

**⑤ 接続テスト**

```bash
ssh -T git@github.com
```

初回は「Are you sure you want to continue connecting?」と聞かれるから `yes` と入力する。次のように表示されたら成功。

```
Hi ユーザー名! You've successfully authenticated, but GitHub does not provide shell access.
```

「shell accessは提供しない」と言われているけど、これが成功のメッセージだから安心していい。

### 方法B: GitHub CLI（gh）で認証する

ブラウザ経由でログインするだけで、認証がほぼ自動で終わる最短ルート。

**インストール**

```bash
# Windows
winget install --id GitHub.cli

# Mac
brew install gh

# Ubuntu系は公式手順を参照: https://github.com/cli/cli#installation
```

**ログイン**

```bash
gh auth login
```

対話形式で質問されるから、次のように選ぶ。

1. `GitHub.com` を選ぶ
2. プロトコルは `SSH` か `HTTPS` を選ぶ（迷ったらHTTPSで問題ない）
3. 認証方法は `Login with a web browser` を選ぶ
4. 表示されたワンタイムコードをコピーして、ブラウザで開いたページに貼り付ける

プロトコルでSSHを選ぶと、SSH鍵の作成とGitHubへの登録まで`gh`が代わりにやってくれる。終わったら次で確認する。

```bash
gh auth status
```

`Logged in to github.com` と出ていれば完了。

### 方法C: Personal Access Token（HTTPS）

HTTPSでcloneしたリポジトリにpushするとき、パスワードの代わりに**トークン**を使う方法。Windows版のGitにはGit Credential Managerが同梱されていて、初回pushでブラウザ認証のウィンドウが出てくるから、実は多くの場合はそれで勝手に認証が通る。うまくいかないときだけトークンを手動で作る。

1. GitHubの Settings → Developer settings → Personal access tokens → Fine-grained tokens を開く
2. 「Generate new token」で、有効期限と、アクセスさせたいリポジトリ、権限（`Contents: Read and write` など）を選ぶ
3. 生成されたトークンをコピーする（**一度しか表示されない**）
4. pushのときにパスワードを聞かれたら、そこにトークンを貼り付ける

トークンはパスワードと同じ扱いで、コードや公開リポジトリに絶対に書かないこと。

---

## 5. 動作確認: 実際にpushしてみる

設定が合っているかは、実際に1回pushしてみるのが一番早い。

**① GitHub上でリポジトリを作る**

右上の「+」→「New repository」を選ぶ。名前は `hello-github` など適当でよくて、「Add a README file」にチェックを入れて作成する。

**② ローカルにcloneする**

リポジトリのページの緑の「Code」ボタンから、認証方法に合わせたURLをコピーする。SSHなら `git@github.com:...`、HTTPSなら `https://github.com/...` で始まるほう。

```bash
git clone git@github.com:ユーザー名/hello-github.git
cd hello-github
```

**③ ファイルを編集してpushする**

```bash
echo "初めてのコミット" >> README.md
git add README.md
git commit -m "READMEに一行追加"
git push
```

GitHubのリポジトリページをリロードして、変更が反映されていれば全部成功。ここまでできたらGitHubの初期設定は完了。

---

## よくあるつまずきと対処

**`Permission denied (publickey)` と出る。**
SSH鍵がGitHubに登録されていないか、ssh-agentに鍵が追加されていない。手順③〜⑤をもう一度確認して、`ssh -T git@github.com` で接続テストをやり直す。

**`Author identity unknown` と出てコミットできない。**
名前とメールの設定が入っていない。手順3の `git config --global` を実行する。

**`Authentication failed` や `Support for password authentication was removed` と出る。**
HTTPSでパスワードを入力している。パスワードは使えないから、Personal Access Tokenを使うか、`gh auth login` でログインし直すか、SSHに切り替える。

**cloneしたリポジトリがHTTPSで、SSHに切り替えたい。**
リモートURLを書き換えればいい。

```bash
git remote set-url origin git@github.com:ユーザー名/リポジトリ名.git
```

**`git` コマンドが見つからないと言われる（Windows）。**
インストール後にターミナルを開き直していない可能性が高い。それでもダメなら、Gitのインストール時に「Git from the command line and also from 3rd-party software」を選んでPATHが通っているか確認する。

---

## 次にやること

初期設定が終わったら、次はこの順番で学ぶとスムーズ。

1. 基本コマンド（`add` / `commit` / `push` / `pull` / `status` / `log`）を手に馴染ませる
2. ブランチを切って、マージする流れを体験する
3. Pull Requestを自分のリポジトリ内で1回作ってみる
4. `.gitignore` の書き方を覚える（秘密情報や不要ファイルをpushしないために必須）
5. 他人のリポジトリをForkして、PRを送ってみる

この資料の続きとして、基本コマンド編やブランチ編もまとめられる。
