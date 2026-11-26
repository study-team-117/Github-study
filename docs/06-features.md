# 06 GitHubの便利な機能

[← 05 便利なGitコマンド・小技](05-tips.md) ｜ [目次に戻る](../README.md#目次) ｜ [07 Git・GitHub応用編 →](07-advanced.md)

> **この章の目標**：Gitのコマンド操作に加え、GitHub上でタスク管理・共同作業・自動テスト・Web公開を行うための主要機能を理解する。
>
> **想定時間**：読むだけなら15〜20分。実際の設定は別途時間が必要です。

## 6-1. GitとGitHubの機能はどう違う？

Gitはファイルの変更履歴を管理するツールです。一方、GitHubはGitリポジトリを共有し、開発チームが協力するための機能を提供します。

| 機能 | 何に使う？ | 例 |
|---|---|---|
| Issues | タスク・バグ・要望を記録 | 「ログイン画面を作る」 |
| Projects | タスクの進捗を一覧管理 | 未着手／作業中／完了 |
| Discussions | 質問やアイデアを議論 | 新機能の提案 |
| Actions | テストや処理を自動実行 | push時にPythonテスト |
| Pages | 静的なWebサイトを公開 | プロジェクト紹介ページ |
| Rulesets・ブランチ保護 | 重要なブランチへの変更を制御 | mainへの直接pushを制限 |

## 6-2. GitHub Issues：タスク・バグを管理する

### どんなときに使う？

共同開発で「誰が何をするか」を明確にしたいときに使います。Issueは、作業内容を記録するための単位です。

**作成手順（ブラウザ）**

1. GitHubで対象リポジトリを開く。
2. **Issues** タブを選ぶ（表示されない場合はリポジトリ設定で有効化を確認）。
3. **New issue** を選び、タイトルと説明を書く。
4. 必要に応じて **Assignees**（担当者）、**Labels**（分類）、**Milestone**（目標）を設定する。
5. **Create** を押す。

**Issueの記述例**

```markdown
## やること
じゃんけんゲームに勝敗の表示を追加する。

## 完了条件
- 勝ち・負け・あいこを表示する
- 3通りの動作を確認する

## 補足
変更対象: janken.py
```

Issue番号が `#12` なら、Pull Requestの説明に `Closes #12` と書くと、同じリポジトリの既定ブランチ（この教材では `main`）にそのPRをマージしたときにIssueが自動で閉じます。別のリポジトリのIssueを指定する場合は `Closes 所有者/リポジトリ#12` と書きます。

**ポイント**：Issueは単なるメモではなく、作業の完了条件を明確にするためにも使えます。

公式：[GitHub Issuesのドキュメント](https://docs.github.com/ja/issues/tracking-your-work-with-issues)

## 6-3. GitHub Projects：進捗を見える化する

複数のIssueをまとめて管理したいときはProjectsが便利です。テーブル表示やボード表示で、タスクの状態を整理できます。

### 基本的な使い方

1. GitHubの **Projects** から新しいプロジェクトを作成する。
2. ボード表示を選ぶ。
3. Issueを追加する。
4. `Todo` → `In Progress` → `Done` のように進捗を更新する。

| Todo | In Progress | Done |
|---|---|---|
| READMEの整理 | 勝敗判定の実装 | リポジトリ作成 |
| テスト追加 |  |  |

**Issuesとの違い**：Issuesは個々の作業内容、Projectsは複数の作業の全体像を管理するものです。

公式：[GitHub Projectsのドキュメント](https://docs.github.com/ja/issues/planning-and-tracking-with-projects)

## 6-4. GitHub Discussions：質問・アイデアの共有

Discussionsは、すぐに作業として登録するほどではない質問や相談をまとめる機能です。

- **Issues**：具体的な作業・不具合を追跡する
- **Discussions**：質問、アイデア、意見交換を行う

例えば「次の勉強会ではどんな機能を実装する？」といった相談に向いています。

使うには、リポジトリの **Settings → General** などからDiscussionsを有効にします。権限や画面構成により設定場所が異なる場合があります。

公式：[GitHub Discussionsのドキュメント](https://docs.github.com/ja/discussions)

## 6-5. GitHub Actions：テストを自動化する

GitHub Actionsでは、pushやPull Requestなどをきっかけに処理を実行できます。例えば、誰かがコードを変更するたびにPythonのテストを自動実行できます。

### 仕組み

```text
コードをpush / Pull Requestを作成
              ↓
GitHub Actionsが起動
              ↓
Pythonを準備してテストを実行
              ↓
成功・失敗をGitHub上で確認
```

### Pythonの最小例

リポジトリに `test_sample.py` を作ります。

```python

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

続いて、**`.github/workflows/python-test.yml`** を作成します。

```yaml
name: Python Test

on:
  push:
    branches: [main]
  pull_request:

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install pytest
        run: python -m pip install pytest
      - name: Run tests
        run: python -m pytest -q
```

> **注意**：実運用ではActionsのバージョンや権限設定を公式ドキュメントで確認してください。

この例は、`main` へのpushや、`main` などへのPRの作成・更新で実行されます。作業ブランチだけをpushした場合は、PRを開いてから確認します。PRの **Checks** またはリポジトリの **Actions** で実行結果を開き、失敗時はジョブの **Run tests** などのログを確認します。

### 何をテストし、結果をどう読むか

- 仕様から入力と期待する結果を決めます。この例では「2と3を足すと5になる」を確かめます。変更する機能に応じて、0や負の数なども確認します。
- 失敗したら、ログで失敗したテスト名と期待値、実際の値を確認します。途中でセットアップが失敗した場合は、テストが始まる前のログを確認します。
- 仕様を読み直し、実装とテストのどちらに修正が必要か判断します。修正後は同じテストを再実行します。

**実際のチーム開発での用途**：Pull Requestをマージする前に、自動テストが通るかを確認できます。

公式：[GitHub Actionsのドキュメント](https://docs.github.com/ja/actions)

## 6-6. GitHub Pages：静的なWebサイトを公開する

GitHub Pagesは、HTML・CSS・JavaScriptなどで作成した静的サイトを公開する機能です。サーバー側で動作するPythonやPHPのアプリを、そのまま実行する用途には向きません。

### 最小構成

リポジトリのルートに `index.html` を作成します。

```html
<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>GitHub Pages 練習</title>
</head>
<body>
  <h1>はじめてのGitHub Pages</h1>
  <p>GitHubから公開したWebページです。</p>
</body>
</html>
```

### 公開までの流れ

1. リポジトリの **Settings → Pages** を開く。
2. **Build and deployment** で **Deploy from a branch** を選ぶ。
3. 公開元のブランチ（例：`main`）とフォルダ（例：`/(root)`）を指定して保存する。
4. デプロイ完了後、表示される公開URLを開く。

通常、プロジェクト用リポジトリの公開URLは `https://ユーザー名.github.io/リポジトリ名/` の形式です。公開まで少し時間がかかることがあります。プランやリポジトリの公開設定によって利用条件が異なる場合があります。

**注意**：プランによっては非公開リポジトリでもサイトが一般公開されます。公開URLのアクセス範囲を確認し、パスワード・APIキー・個人情報は置かないでください。

公式：[GitHub Pagesのドキュメント](https://docs.github.com/ja/pages)

## 6-7. mainブランチを守る：Rulesets・ブランチ保護

複数人で開発すると、誤って `main` に直接pushしてしまうことがあります。重要なブランチへの変更を制限するには、Rulesetsやブランチ保護の設定を使います。

### 設定例

1. リポジトリの **Settings** を開く。
2. **Rules → Rulesets** からブランチ用のルールを作成する（画面や権限によって表示が異なる場合があります）。
3. 対象ブランチに `main` を指定する。対象の条件を確認し、他のブランチまで含まれていないことを確かめる。
4. **Pull Requestを必須にする**、必要に応じて**承認レビュー**や**ステータスチェック**を要求する。
5. ルールを有効化し、想定どおり制限されるか確認する。

> **重要**：利用可能な保護機能は、リポジトリの公開範囲・プラン・権限などによって異なります。また、管理者やバイパス権限を持つユーザーに例外が設定されている場合もあります。

### チーム開発でのおすすめ運用

- 普段の作業は `feature/機能名` などのブランチで行う。
- Pull Requestを作り、変更内容を確認してからmainへマージする。
- 自動テストを設定した場合は、テスト結果も確認する。
- mainを直接変更してしまった場合の対処は [04 エラー・コンフリクト対処](04-troubleshooting.md) を参照する。

公式：[Rulesetsのドキュメント](https://docs.github.com/ja/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)

## 6-8. どの機能をいつ使う？

| 状況 | 使う機能 |
|---|---|
| バグを見つけた | Issues |
| チームの進捗を共有したい | Projects |
| アイデアについて相談したい | Discussions |
| push時にテストしたい | Actions |
| 制作物の紹介サイトを公開したい | Pages |
| mainへの直接pushを防ぎたい | Rulesets・ブランチ保護 |

## 6-9. 理解度チェック

1. IssuesとProjectsは何が違うでしょうか？
2. Pull Requestの作成時にテストを自動実行したい場合、どの機能を使いますか？
3. HTMLで作った静的な紹介ページを公開する機能は何でしょうか？
4. mainへの直接pushを制限するには、どの機能を使いますか？
5. 「新機能について意見を集めたい」という相談はIssuesとDiscussionsのどちらが向いていますか？

<details>
<summary>解答例を表示</summary>

1. Issuesは個々の作業を記録し、Projectsは複数の作業の進捗をまとめて管理する。
2. GitHub Actions。
3. GitHub Pages。
4. Rulesetsまたはブランチ保護。
5. Discussions。具体的な実装タスクになったらIssueを作るとよい。

</details>

---

## 演習問題

- [演習06：GitHubの便利な機能](exercise/06-features-exercise.md)
- [演習06：回答例・解説](exercise/answer/06.md)

---

## 参考資料（公式）

- [GitHub Docs（日本語）](https://docs.github.com/ja)
- [GitHub Issues](https://docs.github.com/ja/issues)
- [GitHub Actions](https://docs.github.com/ja/actions)
- [GitHub Pages](https://docs.github.com/ja/pages)

[← 05 便利なGitコマンド・小技](05-tips.md) ｜ [目次に戻る](../README.md#目次) ｜ [07 Git・GitHub応用編 →](07-advanced.md)
