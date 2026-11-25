# GitHub-study

チーム開発に向けて、Git・GitHubの基本操作から応用までを学ぶための教材です。

## この教材について

Gitのインストールと初期設定から始め、コミットやブランチ操作、Pull Requestを使ったチーム開発を学びます。コンフリクトなどのトラブルへの対処や、GitHub Actions、rebaseなどの応用も扱います。

GitやGitHubを初めて使う人を対象に、実際にコマンドを実行しながら学べるようにまとめています。Windows・Macのどちらでも学習できるよう、OSごとに操作が異なる部分は各章で説明します。

## 目次

| 資料 | 学習内容 |
|---|---|
| [00 インストール・初期設定](docs/00-install.md) | Git・VSCodeの導入、GitHubアカウントと初期設定 |
| [01 Git・GitHubの基本操作](docs/01-basic.md) | リポジトリ作成、clone、VSCode、add・commit・push・pull |
| [02 ブランチの操作](docs/02-branch.md) | ブランチの作成・切り替え・push |
| [03 チーム開発の基本](docs/03-team.md) | Pull Request、レビュー、マージ、共同開発 |
| [04 トラブルシューティング](docs/04-troubleshooting.md) | push拒否、コンフリクト、mainへの誤push、変更の取り消し |
| [05 便利なGitコマンド・小技](docs/05-tips.md) | diff、log、stash、.gitignoreなど |
| [06 GitHubの便利な機能](docs/06-features.md) | Issues、Projects、Actions、Pages、ブランチ保護 |
| [07 Git・GitHub応用編](docs/07-advanced.md) | rebase、cherry-pick、reflog、bisect、worktree、運用戦略 |

## 学習の進め方

1. **00〜01章：環境準備と基本操作** — GitHub上にリポジトリを作成し、PCから変更を反映する。
2. **02〜03章：チーム開発** — ブランチを作成し、Pull Requestを通して変更を取り込む。
3. **04〜05章：トラブル対応と便利な操作** — エラーへの対処方法や日常的に役立つコマンドを学ぶ。
4. **06〜07章：機能紹介と応用** — GitHubの管理機能と、より高度なGit操作を学ぶ。

> **演習について**：各章の演習問題と回答例は、今後順次追加する予定です。

## 補足教材

- [SQL入門](docs/sql/README.md) — SQLiteでデータの絞り込み・集計・結合を練習します。

## 学習時の注意

- 最初は個人の練習用リポジトリで操作してください。
- チーム開発では、原則として作業ブランチからPull Requestを作成します。
- `git push --force` など履歴に影響する操作は、意味を理解せずに実行しないでください。
- パスワードやAPIキーなどの機密情報をコミットしないでください。

---

この資料は学習・チーム開発のために随時更新していきます。
