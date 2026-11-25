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
