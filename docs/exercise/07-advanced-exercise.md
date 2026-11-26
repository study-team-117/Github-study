# 07 Git・GitHub応用編｜ミニ演習

[← 07章の本編](../07-advanced.md) ｜ [目次に戻る](../../README.md#目次)

> **演習の目安**　基本 8〜10分・個人｜応用 10〜15分・個人｜発展 25〜35分・ペア
>
> 所要時間は問題に取り組む時間の目安です。授業ではまず各課題の「準備」を一緒に行います。本編は演習中も参照できます。発展は時間内の完答を前提としません。

## 事前準備

[GitとVSCodeの初期設定](../00-install.md)を済ませ、下の手順を使ってその場で練習環境を作ります。前の演習の状態を使う場合は、各課題の準備欄に記載しています。

各課題はGitHubに接続しない練習用リポジトリで行います。課題ごとにVSCodeで空のフォルダを開きます。基本・応用では `git init -b main` を実行し、READMEを最初のコミットに記録します。

実際のプロジェクトや教材本体で作業したり、共有済みの履歴を書き換えたりしないでください。

## 基本演習

### 共有前の作業ブランチの土台を更新する

#### 準備

1. READMEだけがある `main` から `practice/guide` を作り、`guide.md` に「# 学習ガイド」を書いてコミットします。
2. `main` に戻り、READMEに「先に事前資料を読んでください。」と追記してコミットします。ここでの `main` のコミットIDを控え、統合せずに止めます。

#### ここから演習

**初期状態**　共有していない `practice/guide` と `main` が共通の起点から分かれており、双方に新しいコミットがあります。

**課題**　最新の `main` を土台にしたうえで、ガイドの変更をその上で確認できる履歴に整えてください。

**達成条件**　ガイドの変更が最新の `main` の直後に記録され、ガイドの内容が残る。`main` は演習前と同じコミットを指す。

## 応用演習

### 別ブランチから公開対象の変更だけを取り込む

#### 準備

1. READMEだけがある `main` で `git branch practice/release` を実行し、公開用の作業先を用意します。
2. `main` から `practice/draft` へ分かれ、`guide.md` に「# 公開用ガイド」を書いてコミットします。
3. 同じブランチで `memo.md` に「# チーム内メモ」を書き、別のコミットにします。公開用ブランチにはまだ変更を入れません。

#### ここから演習

**初期状態**　`practice/draft` には公開できる `guide.md` の追加と、後から記録した `memo.md` の追加があります。作業先 `practice/release` は `main` と同じ状態です。

**課題**　公開できる変更の記録だけを `practice/release` に取り込んでください。

**達成条件**　取り込み先でガイドを読めて、メモは含まれない。取り込み元のブランチにはガイドとメモが残っている。

## 発展演習

### 不具合が入った記録を特定し、後続の変更を保つ

#### 準備

ペアで取り組む場合は、検証担当が空のフォルダで以下の準備を実行し、調査担当に作業を交代します。個人の場合も同じ手順で準備できます。準備時の表示だけで判断せず、課題では履歴からコミットIDと根拠を確かめます。

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

作業フォルダに `display.txt` があり、8件の履歴と `practice-good` タグがあれば準備完了です。

#### ここから演習

**初期状態**　練習用の履歴は8件です。タグ `practice-good` の付いた最初のコミットは正常です。最新では `display.txt` の案内表示が失敗します。正常の判定は `display.txt` の先頭行が `status=ready` であることです。履歴には、その後も必要な変更が入っています。

**課題**　ペアで調査と検証を分担し、最初に失敗したコミットを特定して直してください。元の履歴は書き換えず、必要な後続変更も残してください。

**達成条件**　対象コミットと、その直前では正常だったことを示せる。修正後に同じ基準で正常と判定でき、後続の教材ファイルも残っている。

<details>
<summary>ヒント1：着目点</summary>

最初と最新に同じ判定を適用し、正常から失敗に変わる範囲を考えます。

</details>

<details>
<summary>ヒント2：本編の参照先</summary>

本編の「バグが入り込んだコミットを特定する」と、04章の共有済み変更の取り消しを読み返します。

</details>

<details>
<summary>ヒント3：判断の基準</summary>

原因を特定したことと、後続の変更を保ったまま直したことは、何を見れば別々に確認できますか。

</details>

## 回答例・解説

[回答例・解説を読む](answer/07.md)

---

[← 07章の本編](../07-advanced.md) ｜ [目次に戻る](../../README.md#目次)
