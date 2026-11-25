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
