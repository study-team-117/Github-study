# SQL入門｜ミニ演習

[← SQL入門](README.md)

[練習用データ](sample.sql)を読み込んだSQLiteで、次のSQLを書いてみましょう。

1. 在庫が5個以下の商品名と在庫数を、在庫の少ない順に表示する。
2. カテゴリごとの在庫数の合計を表示する。ヒントは `SUM` と `GROUP BY`。
3. 注文明細のID、商品名、注文数量を明細IDの順に表示する。ヒントは `order_items.product_id` と `products.id` を `JOIN` で結び付けること。

[回答例と期待する結果](answer.md)
