# 01 基本操作｜ミニ演習

> **目安：8〜10分** ｜ **難易度：初級＋** ｜ **形式：個人**
>
> この演習では、GitHub上の編集とVSCodeでの編集を組み合わせ、`commit`・`push`・`pull` の流れを確認します。

[← 01 基本操作の解説に戻る](../docs/01-basic.md) ｜ [← 教材の目次に戻る](../README.md)

## 事前準備（講義中に済ませておく）

- GitHubアカウントとGitの初期設定が完了している
- GitHubに自分用の練習リポジトリ `git-practice` を **README付き** で作成済み
- そのリポジトリをPCに `clone` し、VSCodeで開いている
- `main` ブランチで作業している（確認：`git branch --show-current`）

※ **事前準備は演習時間に含めません。** 準備が終わっていない場合は解説資料を参照してください。

## 必須課題（8〜10分）

### 課題1：ローカルの変更をGitHubへ反映（目安5分）

1. VSCodeでリポジトリ内に `profile.md` を新規作成する。
2. 以下の3項目をMarkdown形式で記入する。
   - 自己紹介（ニックネームでも可）
   - 興味のある技術を2つ
   - この勉強会で学びたいことを1つ
3. 変更を確認してから、`profile.md` **だけ** をステージングする。
4. 「Add profile」というコミットメッセージでコミットする。
5. GitHubへpushし、ブラウザで `profile.md` が表示されることを確認する。

**ヒント：** `git status` → `git add` → `git commit` → `git push`

### 課題2：GitHub上の変更をPCへ取り込む（目安3〜5分）

1. GitHubのブラウザ画面で `README.md` を編集し、「学習メモ」という見出しと1行の文章を追加してコミットする。
2. VSCodeに戻り、**ローカルのファイルを追加編集せずに** 最新の変更を取り込む。
3. PC側の `README.md` に「学習メモ」が反映されていることを確認する。

**ヒント：** `git pull`

## 完了チェック

- [ ] GitHub上に `profile.md` が存在する
- [ ] `profile.md` のコミットがGitHubの履歴に残っている
- [ ] GitHubで編集した `README.md` がPCにも反映されている
- [ ] `git status` で未コミットの変更がないことを確認できる

## 余裕がある人向け（追加3〜5分・任意）

1. `profile.md` の「興味のある技術」を1つ増やす。
2. `git diff` で差分を確認し、変更をコミットしてpushする。
3. `git log --oneline -5` で直近のコミット履歴を表示する。
4. **考えてみよう：** `commit` と `push` は何が違う？ `pull` はいつ必要？

<details>
<summary>困ったときのコマンド例（クリックして表示）</summary>

```bash
git status
git add profile.md
git commit -m "Add profile"
git push origin main
# GitHubのブラウザ上でREADME.mdを編集・コミットした後
git pull origin main
git status
```

※ ブランチ名が `main` でない場合は、実際のブランチ名に読み替えてください。

</details>

## 注意点

- パスワード・APIキー・住所・電話番号などの個人情報をファイルに書かないでください。
- 演習中は **自分専用のリポジトリ** を使い、他の人の変更と競合しないようにします。
- `git pull` 前にローカルで未コミットの変更があると、取り込みに失敗することがあります。まず `git status` で確認しましょう。
- エラーが出た場合はメッセージを記録し、むやみに `--force` を付けないでください。

---

**次の章：** [02 ブランチの操作](../docs/02-branch.md)（公開後にリンクが有効になります）
