# 01 基本操作｜ミニ演習

[← 01章の本編](../01-basic.md) ｜ [目次に戻る](../../README.md#目次)

> **難易度：初級＋** ｜ **形式：個人**
>
> この演習では、GitHub上の編集とVSCodeでの編集を組み合わせ、`commit`・`push`・`pull` の流れを確認します。
>
> **演習の目安**　基本 5分 ｜ 応用 3〜5分 ｜ 発展 3〜5分
>
> 各段階の目安は事前準備を終えてからの時間です。基本から応用へ進み、発展は余裕があれば取り組みます。

## 事前準備

講義中に済ませておきます。

01章で使った自分の `git-practice` をそのまま使います。

- GitHubアカウントとGitの初期設定が完了している
- GitHubに自分用の練習リポジトリ `git-practice` を **README付き** で作成済み
- そのリポジトリをPCに `clone` し、VSCodeで開いている
- VSCodeのターミナルで `git status` を実行し、`On branch main` と `nothing to commit, working tree clean` が表示されることを確認する

準備が終わっていない場合は本編を参照してください。

## 基本演習

### 課題1：ローカルの変更をGitHubへ反映

1. VSCodeでリポジトリ内に `profile.md` を新規作成する。
2. 以下の3項目をMarkdown形式で記入する。
   - 自己紹介（ニックネームでも可）
   - 興味のある技術を2つ
   - この勉強会で学びたいことを1つ
3. 変更を確認してから、`profile.md` **だけ** をステージングする。
4. 「Add profile」というコミットメッセージでコミットする。
5. GitHubへpushし、ブラウザで `profile.md` が表示されることを確認する。

**ヒント：** `git status` → `git add .` → `git status` → `git commit` → `git push`

`git add .` を使う場合は、先に `git status` で変更が `profile.md` だけであることを確認します。ほかの変更がある場合は `git add profile.md` で対象を指定できます。

**完了チェック**

- [ ] GitHub上に `profile.md` が存在する。
- [ ] `profile.md` のコミットがGitHubの履歴に残っている。

## 応用演習

### 課題2：GitHub上の変更をPCへ取り込む

1. GitHubのブラウザ画面で `main` の `README.md` を編集し、「学習メモ」という見出しと1行の文章を追加してコミットする。
2. VSCodeに戻り、**ローカルのファイルを追加編集せずに** 最新の変更を取り込む。
3. PC側の `README.md` に「学習メモ」が反映されていることを確認する。

**ヒント：** `git pull`


<details>
<summary>困ったときのコマンド例（クリックして表示）</summary>

```bash
git status
git add .
git status
git commit -m "Add profile"
git push
# GitHubのブラウザ上でREADME.mdを編集・コミットした後
git status
git pull
git status
```

※ ブランチ名が `main` でない場合は、実際のブランチ名に読み替えてください。

</details>

**完了チェック**

- [ ] GitHubで編集した `README.md` がPCにも反映されている。
- [ ] `git status` で未コミットの変更がないことを確認した。

## 発展演習

### 差分と履歴を確認する

1. `profile.md` の「興味のある技術」を1つ増やす。
2. `git diff` で差分を確認し、変更をコミットしてpushする。
3. `git log --oneline -5` で直近のコミット履歴を表示する。
4. **考えてみよう：** `commit` と `push` は何が違う？ `pull` はいつ必要？

**完了チェック**

- [ ] 追記した内容がGitHubに反映され、`git log` でそのコミットを確認できた。

## 注意点

- パスワード・APIキー・住所・電話番号などの個人情報をファイルに書かないでください。
- 演習中は **自分専用のリポジトリ** を使い、他の人の変更と競合しないようにします。
- `git pull` 前にローカルで未コミットの変更があると、取り込みに失敗することがあります。まず `git status` で確認しましょう。
- エラーが出た場合はメッセージを記録し、むやみに `--force` を付けないでください。

## 回答例・解説

[回答例・解説を読む](answer/01.md)

---

[← 01章の本編](../01-basic.md) ｜ [目次に戻る](../../README.md#目次) ｜ [02 ブランチの操作 →](../02-branch.md)
