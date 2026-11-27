# 06 GitHubの便利な機能｜ミニ演習

[← 06章の本編](../06-features.md) ｜ [目次に戻る](../../README.md#目次)

> **演習の目安**　基本 5〜7分・個人｜応用 10〜15分・ペア｜発展 20〜30分・ペア
>
> 所要時間は問題に取り組む時間の目安です。授業ではまず各課題の「準備」を一緒に行います。本編は演習中も参照できます。発展は時間内の完答を前提としません。

## 事前準備

[事前準備資料](../00-install.md)に沿ってGitの初期設定を済ませ、下の手順で練習環境を作ります。前の演習の状態を使う場合は、各課題の準備欄に記載しています。

ファイル編集はPC上のエディターで行います。VSCodeを推奨しますが、使い慣れたエディターでも構いません。Gitコマンドを練習する課題ではターミナルを使い、PR・レビュー・Issues・ActionsなどのGitHubの機能はブラウザで操作します。

GitHubでIssuesを有効にした、README付きの練習リポジトリを用意します。応用・発展はペアの相手を共同作業者に招待し、既定ブランチが `main` で、Actionsを実行できることを確認します。テストをローカルで実行する場合は、Python 3を使います。

実際のプロジェクトや教材本体で作業したり、共有済みの履歴を書き換えたりしないでください。

### 自動チェックの共通準備

<details>
<summary>応用・発展で使うファイルと配置</summary>

応用・発展では練習リポジトリをPCにクローンし、エディターで開きます。クローンしたフォルダのルートに次の2ファイルを置きます。

`display.py`

```python
def display_label(value):
    return value
```

`test_display.py`

```python
import unittest

from display import display_label


class DisplayTests(unittest.TestCase):
    def test_regular_input(self):
        self.assertEqual(display_label("Git"), "Git")
```

`.github/workflows/check.yml` を次の内容で作ります。

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

PCのターミナルで、3ファイルを `main` に記録してGitHubに反映します。

</details>

## 基本演習

### 完了を判断できるIssueを書く

**使用環境**　GitHubのIssuesをブラウザで操作します。PCへのクローンやターミナル操作は不要です。

#### 準備

練習リポジトリの **Issues** が開けることを確認します。依頼文は下の「ここから演習」で読むので、Issueはまだ作りません。

#### ここから演習

**初期状態**　練習リポジトリで「READMEに開催場所と受付時間を掲載してほしい」という依頼を受けました。場所はA教室、受付は15時です。

**課題**　ほかの人が作業を引き継げるように依頼をIssueにまとめてください。

**達成条件**　Issueに対象ファイル、掲載する内容、完了を判断する条件が書かれている。

## 応用演習

### IssueとPRを関連付け、取り込みを確認する

**使用環境**　準備のファイル編集とGit操作はPCのエディターとターミナルを使います。Issue・PR・Actionsの確認、レビューとマージはGitHubのブラウザで行います。

#### 準備

1. [自動チェックの共通準備](#自動チェックの共通準備)に従い、応用の初期状態を `main` に記録します。
2. 基本で作った「READMEに開催案内を追加」のIssueを使います。基本を飛ばす場合は、A教室と受付15時の掲載を依頼するIssueをあらかじめ1件作ります。
3. `main` から作業ブランチを分け、READMEに開催案内を追記して記録し、GitHubに共有します。PRはまだ作りません。

#### ここから演習

**初期状態**　開催案内のIssueと、READMEに対応済みの共有ブランチがあります。練習リポジトリには自動チェックが設定されています。

**課題**　ペアで変更をレビューし、依頼を完了できる状態にしてから `main` に取り込んでください。

**達成条件**　マージ後の `main` で案内を読める。Issueが閉じ、どのPRで対応したかと自動チェックの結果を確認できる。

## 発展演習

### 仕様・差分・ログからチェック失敗を調べる

**使用環境**　Issue・PR・ActionsのログはGitHubのブラウザで確認し、ファイルの修正と記録はPCで行います。原因調査にはエディターの差分表示や、ターミナルでのローカルテストも使えます。

#### 準備

1. [自動チェックの共通準備](#自動チェックの共通準備)に従い、発展の初期状態を `main` に記録します。「空文字は『未入力』、それ以外は入力どおり」と仕様を書いたIssueも作ります。
2. `main` から作業ブランチを分け、`test_display.py` の `DisplayTests` クラス内に、下の空欄テストを既存のメソッドと同じインデントで追加してコミットします。`display.py` は変更しません。作業ブランチをGitHubに共有し、`main` 向けのPRを作ります。PR本文に仕様のIssue番号を記載します。

```python
    def test_empty_input(self):
        self.assertEqual(display_label(""), "未入力")
```

3. PRのチェックが実行され、空欄だけ失敗したことを確認したら準備完了です。開始時のチェックが待機中なら、PCで `python -m unittest -v` を実行して失敗を確認できます。WindowsでPythonランチャーを使う場合は `py -3 -m unittest -v` でも実行できます。

#### ここから演習

**初期状態**　Issueの仕様は「空欄なら『未入力』と表示し、それ以外は入力どおり」です。開いているPRのチェックでは通常入力が成功し、空欄だけが失敗しています。

**課題**　ペアで調査と検証を分担し、仕様を満たす変更にしてください。テストの削除や無効化はせず、マージの判断に必要な情報をPRに残します。

**達成条件**　通常入力と空欄のチェックが両方成功する。失敗した箇所、仕様から判断した原因、必要な修正と確認結果がPRに残る。

<details>
<summary>ヒント1：着目点</summary>

チェック全体の表示と、失敗したテストの期待値・実際の値を区別します。

</details>

<details>
<summary>ヒント2：本編の参照先</summary>

本編のGitHub Actionsの節と、PRに関連するIssueの仕様を参照します。

</details>

<details>
<summary>ヒント3：判断の基準</summary>

問題が実装かテストかを判断するとき、どの資料が期待する結果を定めていますか。

</details>

## 回答例・解説

[回答例・解説を読む](answer/06.md)

---

[← 06章の本編](../06-features.md) ｜ [目次に戻る](../../README.md#目次) ｜ [07 Git・GitHub応用編 →](../07-advanced.md)
