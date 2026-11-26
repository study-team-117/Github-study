# 01〜07章の演習準備｜講師向け

[← 教材トップ](../../README.md#目次)

授業前に、その回で使う課題の初期状態を作ります。基本・応用・発展の開始状態は独立しています。授業では準備確認5分、基本・応用25分、発展への挑戦20分、振り返り10分を目安とします。発展が途中でも、確認できたことと次に調べることを説明してもらいます。

## 共通準備

- 教材リポジトリとは別に、課題ごとの練習リポジトリを用意します。GitHubを使う課題では個人またはペアごとに分け、課題文の `main` を既定ブランチにします。練習用の値だけを使います。
- ペア課題では作業担当・確認担当を決め、作業ブランチの共有、レビュー、必要な場合のマージができることを確認します。
- 以下のコマンド例はGit BashなどのBashで実行します。初回のコミットより前にGitのユーザー名とメールアドレスを設定します。作業フォルダを作り直すときは、別の空の場所から準備します。
- コミットIDを比べる課題では、開始時のIDを学習者が確認できるようにします。発展の回答例は、授業中はヒントとは別に扱います。

## 01章の準備

- **基本・応用共通**　空のGitHubリポジトリに、`README.md` の「# 練習用」、`profile.md` の「# 自己紹介」、`notes.md` の「# 個人用メモ」をそれぞれ1行目として記録します。学習者のPCにクローンし、手元から作業を反映できることを確認します。
- **基本**　クローンした時点で配布します。
- **応用**　PCだけで `profile.md` に「興味のある技術はWeb開発です。」、`notes.md` に「あとで用語を調べる。」を追記し、両方とも未記録にします。
- **発展**　クローン後にGitHub側だけで `README.md` に「資料は前日までに読んでください。」を追加してコミットします。PCでは `profile.md` と `notes.md` に応用と同じ文を未記録のまま追記します。案内と紹介文は異なるファイルにし、初回の発展では競合が発生しないようにします。

## 02章の準備

- **基本**　`main` にREADMEだけがある練習環境を用意します。
- **応用**　基本と同じ状態をGitHubにも用意し、PCの `main` で `draft.md` に「# 下書き」と書いて保存します。履歴には追加しません。
- **発展**　READMEだけがあるコミットから `practice/draft` を作り、`guide.md` に「# 学習ガイド」、`notes.md` に「# 未承認メモ」を記録します。次に `main` に戻り、READMEに「集合は15時」と追記して記録します。配布するローカルリポジトリには両ブランチを残します。

## 03章の準備

- **基本**　`main` のREADMEに「# 教材」と「## 目次」を置きます。作業ブランチ `practice/usage` のREADME末尾に「## 使い方」と「教材を読む。」を追加して共有します。PRは作らずに渡します。
- **応用**　基本と同じ状態から、`practice/usage` → `main` のPRを作って開いた状態で渡します。作成者と別のアカウントがレビューできることを確認します。
- **発展**　基点から `practice/review-base` を作り、README末尾に「レビュー用」と追記します。さらにそこから `practice/usage` を作り、README末尾に「## 使い方」と「教材を読む。」を追加し、「## 目次」を「## 読むもの一覧」に変更します。準備するPRの取り込み先は `practice/review-base`、変更元は `practice/usage` です。`main` は基点のままにします。

## 04章の準備

- **基本**　`practice.md` に「# 練習メモ」を記録します。「あとで使う追記。」を追加し、ステージ済み・未コミットの状態で配布します。
- **応用**　READMEの先頭行を「確認方法：まず手順を読む」とします。この時点から `practice/conflict` を作り、先頭行を「確認方法：VSCodeで差分を見る」に変更し、`branch-note.md` に「作業ブランチのメモ」と書いて記録します。`main` では先頭行を「確認方法：ターミナルで状態を見る」に変更して記録します。マージは始めずに渡します。
- **発展**　基点に `deadline.md` の「締切：6月10日」と、READMEの「質問は担当者まで。」を記録します。基点から作った `practice/announcements` ではREADMEの同じ行を「質問は掲示板へ。」に変更し、`main` 向けのPRを開きます。`main` では次の3件を別々のコミットとして記録・共有します。締切の誤変更のコミットにほかのファイルを混ぜないことを確認します。
  1. `deadline.md` の締切を「6月1日」に変更
  2. `contacts.md` に「連絡先：案内担当」を追加
  3. READMEの同じ行を「質問は担当者へ。急ぎの場合は直接連絡してください。」に変更

## 05章の準備

- **基本**　`README.md` と `notes.md` を記録済みにし、それぞれ「案内を更新しました。」と「このメモは編集中です。」を未記録で追記します。
- **応用**　`main` のREADMEに「閲覧リンクを共用」と記録して、`practice/guide` へ切り替えます。そこでREADMEの末尾に「# ガイド（執筆中）」を未記録で追記します。
- **発展**　空のフォルダで以下を実行し、そのローカル作業フォルダを配布します。退避の記録はクローンしても引き継がれません。学習者が使うPC側で準備するか、`.git` を含むフォルダ一式を渡します。

```bash
git init -b main
printf '# ガイド\n\n## 作業\n\n下書き本文\n' > guide.md
git add guide.md
git commit -m "Add guide"
printf '\nレビュー待ちの確認方法：担当者の返信を確認する。\n' >> guide.md
git stash push -m "メモA"
printf '\n発表の練習：資料を声に出して読む。\n' >> guide.md
git stash push -m "メモB"
git switch -c practice/resume
printf '# チームガイド\n\n## 作業\n\n下書き本文\n' > guide.md
git add guide.md
git commit -m "Clarify the guide title"
```

## 06章の準備

- **基本**　Issuesが有効な練習リポジトリを用意します。A教室・受付15時の依頼は問題文を使います。
- **応用**　同じ内容のIssueを1件作り、READMEに案内を入れた作業ブランチを共有します。下記のテストとワークフローを入れ、`display.py` は最初から仕様を満たすようにします。PRは学習者が作ります。
- **発展**　「空文字は未入力、それ以外は入力どおり」と書いたIssueを作ります。まず、`main` に、戻り値が `return value` の実装と、通常入力のテストだけを用意します。下記のワークフローも記録します。次に、作業ブランチで空欄のテストを追加し、実装はそのままでPRを作ります。空欄だけ失敗し、通常入力は成功したログが出ていることを確認してから渡します。

`display.py` の正常な状態です。

```python
def display_label(value):
    return value if value else "未入力"
```

`test_display.py` を同じフォルダに置きます。

```python
import unittest

from display import display_label


class DisplayTests(unittest.TestCase):
    def test_regular_input(self):
        self.assertEqual(display_label("Git"), "Git")

    def test_empty_input(self):
        self.assertEqual(display_label(""), "未入力")
```

次を `.github/workflows/check.yml` として保存します。

```yaml
name: Check display

on:
  pull_request:

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - run: python3 -m unittest -v
```

授業前にActionsが使える状態か確認します。授業中の再実行が待機した場合は、配布した失敗ログとローカルでの修正後の結果を先に確認し、GitHubでの成功は別途確認します。WindowsでPythonランチャーを使う場合は `py -3 -m unittest -v` でも実行できます。

## 07章の準備

- **基本**　READMEを記録したコミットから未共有の `practice/guide` を作り、`guide.md` を追加して記録します。`main` に戻り、READMEへ案内を追記して記録します。両ブランチの変更が別ファイルであることを確認します。
- **応用**　READMEだけがある `main` から `practice/draft` と `practice/release` を作ります。`practice/draft` に `guide.md` を記録したあと、別のコミットで `memo.md` を追加します。`practice/release` は作成時の状態のままにします。
- **発展**　空のフォルダで以下を実行します。正常な開始点に `practice-good` タグを付けます。最新には不具合と、その後の必要な変更が3件あります。GitHubへの接続は不要です。

```bash
git init -b main
printf 'status=ready\n' > display.txt
git add display.txt
git commit -m "Prepare display"
git tag practice-good
printf '# 教材\n' > README.md
git add README.md
git commit -m "Add readme"
printf '開始前に教材を読む。\n' > setup.md
git add setup.md
git commit -m "Add setup"
printf '作業は練習環境で行う。\n' > guide.md
git add guide.md
git commit -m "Add guide"
printf 'status=hidden\n' > display.txt
git add display.txt
git commit -m "Update display settings"
printf '基本操作を練習する。\n' > lesson.md
git add lesson.md
git commit -m "Add lesson"
printf '不明点は講師に確認する。\n' > faq.md
git add faq.md
git commit -m "Add FAQ"
printf 'ブランチ：作業を分けるための目印。\n' > glossary.md
git add glossary.md
git commit -m "Add glossary"
```

最新の `display.txt` が `status=hidden`、タグの状態では `status=ready` であることを確認します。判定にプログラミングは不要です。
