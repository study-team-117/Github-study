# SQL入門｜回答例

[← 演習に戻る](exercise.md) ｜ [← SQL入門](README.md)

## 1. 在庫が5個以下の商品

```sql
SELECT name, stock
FROM products
WHERE stock <= 5
ORDER BY stock ASC;
```

| name | stock |
|---|---:|
| マグカップ | 2 |
| ペン | 3 |

## 2. カテゴリごとの在庫合計

```sql
SELECT category, SUM(stock) AS total_stock
FROM products
GROUP BY category
ORDER BY total_stock DESC;
```

| category | total_stock |
|---|---:|
| 文具 | 15 |
| 雑貨 | 2 |

## 3. 注文明細の商品名と数量

```sql
SELECT order_items.id, products.name, order_items.quantity
FROM order_items
JOIN products ON order_items.product_id = products.id
ORDER BY order_items.id;
```

| id | name | quantity |
|---:|---|---:|
| 1 | ペン | 4 |
| 2 | マグカップ | 1 |

## 4. 在庫状況を表示する（CASE）

```sql
SELECT name, stock,
       CASE WHEN stock <= 5 THEN '少ない' ELSE '十分' END AS stock_status
FROM products
ORDER BY id;
```

| name | stock | stock_status |
| --- | ---: | --- |
| ノート | 12 | 十分 |
| ペン | 3 | 少ない |
| マグカップ | 2 | 少ない |

## 5. 注文一覧をビューにする（VIEW）

```sql
CREATE TEMP VIEW IF NOT EXISTS order_item_summary AS
SELECT order_items.id, products.name, order_items.quantity
FROM order_items
JOIN products ON order_items.product_id = products.id;

SELECT id, name, quantity
FROM order_item_summary
ORDER BY id;
```

| id | name | quantity |
| ---: | --- | ---: |
| 1 | ペン | 4 |
| 2 | マグカップ | 1 |

ビューに名前を付けておくと、結合を書く代わりにその名前で問い合わせられます。この一時ビューはSQLiteの現在の接続で使えます。

## 6. カテゴリと価格の範囲で絞り込む

```sql
SELECT name, price
FROM products
WHERE category = '文具' AND price BETWEEN 150 AND 300
ORDER BY price, id;
```

| name | price |
| --- | ---: |
| ペン | 150 |
| ノート | 300 |

`BETWEEN` は150と300の両方を含みます。

## 7. 価格が2番目に高い商品を表示する

```sql
SELECT name, price
FROM products
ORDER BY price DESC, id
LIMIT 1 OFFSET 1;
```

| name | price |
| --- | ---: |
| ノート | 300 |

価格の高い順に並べたあと、先頭の1件を飛ばして1件を取得します。同じ価格の商品があればID順に並べます。

## 8. 在庫合計が10個以上のカテゴリを表示する

```sql
SELECT category, SUM(stock) AS total_stock
FROM products
GROUP BY category
HAVING SUM(stock) >= 10;
```

| category | total_stock |
| --- | ---: |
| 文具 | 15 |

`HAVING` で、集計した結果が条件を満たすグループを選びます。

## 9. 注文明細がない商品も一覧に表示する

```sql
SELECT p.name, oi.quantity
FROM products AS p
LEFT JOIN order_items AS oi ON oi.product_id = p.id
ORDER BY p.id, oi.id;
```

| name | quantity |
| --- | ---: |
| ノート | NULL |
| ペン | 4 |
| マグカップ | 1 |

`LEFT JOIN` で商品をすべて残します。ノートには対応する明細がないため、数量は `NULL` です。SQLiteのコマンドラインでは、既定で `NULL` が空欄に見えることがあります。

## 10. 平均価格より高い商品を表示する

```sql
SELECT name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products)
ORDER BY price, id;
```

| name | price |
| --- | ---: |
| マグカップ | 800 |

かっこの中で商品全体の平均価格を求め、その値より高い商品を選びます。

## 11. 商品を追加・更新・削除して元に戻す

練習データを読み込んだ接続で、上から順に実行します。

```sql
BEGIN;

INSERT INTO products (id, name, category, price, stock)
VALUES (4, '付箋', '文具', 220, 5);

SELECT id, name, stock FROM products WHERE id = 4;
```

| id | name | stock |
| ---: | --- | ---: |
| 4 | 付箋 | 5 |

```sql
UPDATE products SET stock = 9 WHERE id = 4;

SELECT id, name, stock FROM products WHERE id = 4;
```

| id | name | stock |
| ---: | --- | ---: |
| 4 | 付箋 | 9 |

```sql
DELETE FROM products WHERE id = 4;

SELECT id, name, stock FROM products WHERE id = 4;

ROLLBACK;

SELECT COUNT(*) AS product_count FROM products;
```

削除直後の検索結果は0行です。ロールバック後の件数は次のとおりです。

| product_count |
| ---: |
| 3 |

`UPDATE` と `DELETE` の前に、直前の `SELECT` の結果で対象を確認します。`ROLLBACK` は練習中の変更を取り消します。

## 12. 商品ごとの注文数量と在庫の不足数を集計する

```sql
WITH order_totals AS (
    SELECT product_id, SUM(quantity) AS ordered_qty
    FROM order_items
    GROUP BY product_id
)
SELECT p.name, p.stock, COALESCE(o.ordered_qty, 0) AS ordered_qty,
       CASE
           WHEN COALESCE(o.ordered_qty, 0) > p.stock THEN o.ordered_qty - p.stock
           ELSE 0
       END AS shortage
FROM products AS p
LEFT JOIN order_totals AS o ON o.product_id = p.id
ORDER BY shortage DESC, p.id;
```

| name | stock | ordered_qty | shortage |
| --- | ---: | ---: | ---: |
| ペン | 3 | 4 | 1 |
| ノート | 12 | 0 | 0 |
| マグカップ | 2 | 1 | 0 |

`WITH` で商品ごとの集計に名前を付けます。`LEFT JOIN` で注文がないノートも残し、`COALESCE` で集計結果の `NULL` を0に置き換えます。

## 13. カテゴリ内の平均価格以上の商品を探す

```sql
WITH category_prices AS (
    SELECT category, AVG(price) AS avg_price
    FROM products
    GROUP BY category
)
SELECT p.category, p.name, p.price, c.avg_price
FROM products AS p
JOIN category_prices AS c ON c.category = p.category
WHERE p.price >= c.avg_price
ORDER BY p.category, p.price DESC, p.id;
```

| category | name | price | avg_price |
| --- | --- | ---: | ---: |
| 文具 | ノート | 300 | 225.0 |
| 雑貨 | マグカップ | 800 | 800.0 |

カテゴリ別に平均を求めてから、各商品を自分のカテゴリの平均と比較します。雑貨は1件だけなので、マグカップの価格は平均と等しく、`>=` の条件を満たします。
