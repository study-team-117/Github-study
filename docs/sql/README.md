# SQL入門｜補足教材

[← 教材トップ](../../README.md)

商品と注文明細のサンプルを使って、SQLiteでデータの絞り込み・集計・結合を練習します。

## 準備

SQLiteのコマンドラインツールを使います。ターミナルで `sqlite3 --version` を実行し、バージョンが表示されることを確認します。

`docs/sql` フォルダのターミナルで `sqlite3 :memory:` を実行します。`sqlite>` が表示されたら、次を入力します。

```text
.read sample.sql
.headers on
.mode column
```

データはメモリ上に作られ、`.quit` で終了すると消えます。最初からやり直すには、起動と読み込みを繰り返します。

## 例：在庫が少ない商品を探す

```sql
SELECT name, stock
FROM products
WHERE stock <= 5
ORDER BY stock ASC;
```

`SELECT` で表示する列、`FROM` でテーブル、`WHERE` で行の条件、`ORDER BY` で並び順を指定します。この例では「マグカップ 2」「ペン 3」の順に表示されます。

[練習用データ](sample.sql) ｜ [演習に進む](exercise.md) ｜ [回答例を見る](answer.md)
