# データベースの基礎と実践｜回答例・解説

[← 演習に戻る](exercise.md) ｜ [補足教材の目次](README.md)

## 演習1：商品を取得・追加・更新する

```sql
SELECT name, stock
FROM products
WHERE stock <= 5
ORDER BY stock, id;

INSERT INTO products (id, name, category, price, stock)
VALUES (4, '付箋', '文具', 220, 5);

UPDATE products SET stock = 9 WHERE id = 4;

SELECT id, name, stock FROM products ORDER BY id;
```

最初の検索は「マグカップ 2」「ペン 3」です。更新は主キーで対象を1件に絞ります。最後の結果で、ノート12、ペン3、マグカップ2が変わらず、付箋が9になったことを確認します。

## 演習2：商品とタグを設計する

```mermaid
erDiagram
    products ||--o{ product_tags : "商品IDで参照"
    tags ||--o{ product_tags : "タグIDで参照"
```

```sql
CREATE TABLE tags (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE product_tags (
    product_id INTEGER NOT NULL REFERENCES products(id),
    tag_id INTEGER NOT NULL REFERENCES tags(id),
    PRIMARY KEY (product_id, tag_id)
);

INSERT INTO tags (id, name) VALUES (1, '学習用'), (2, '定番');
INSERT INTO product_tags (product_id, tag_id) VALUES (2, 1), (2, 2), (1, 1);

SELECT p.name
FROM products AS p
JOIN product_tags AS pt ON pt.product_id = p.id
JOIN tags AS t ON t.id = pt.tag_id
WHERE t.name = '学習用'
ORDER BY p.id;
```

結果は「ノート」「ペン」です。中間テーブルの主キーをIDの組にすることで、同じ商品とタグを重複して登録できません。タグ名は `tags` の1箇所で変更できます。

## 演習3：既存データを保って列を追加する

準備で使ったSQLiteを終了し、`docs/database` のターミナルで次を実行します。`-bail` は最初のエラーで停止するSQLite CLIのオプションです。途中で失敗すると `COMMIT` まで進まず、接続が閉じると未確定の変更は取り消されます。

```bash
sqlite3 -bail reorder-practice.db ".read migrations/001-add-reorder-level.sql"
```

成功したら `sqlite3 reorder-practice.db` で開き直し、次を実行します。

```sql
SELECT id, stock, reorder_level FROM products ORDER BY id;
SELECT id, product_id, quantity FROM order_items ORDER BY id;
SELECT version FROM schema_migrations;
PRAGMA foreign_key_check;
```

商品は順に「1・12・5」「2・3・5」「3・2・5」です。明細は「1・2・4」「2・3・1」のままで、適用履歴には `001-add-reorder-level` が1件あります。外部キー検査は違反がなければ0行です。`reorder-before.db` では商品ID・在庫と明細の値を比較できます。

**PRの記入例**　「発注点を管理する列を追加しました。既存3商品は初期値5で、ID・在庫と明細2件は変更なしです。練習DBで適用履歴と外部キーを確認しました。失敗した場合は適用を中断し、確定の有無を確認します。未確定なら取り消し、確定済みなら修正用の変更や保管したコピーからの復元を検討します。」

列を追加した後で適用履歴を記録し、両方を1つのトランザクションで確定します。別のツールで実行する場合も、最初のエラーで後続のSQLを止め、接続が開いていれば未確定の変更をロールバックします。エラーを無視して続行する設定では、変更内容と適用履歴が食い違うおそれがあります。練習用の変更ファイルと確認結果を共有すれば、DB本体をGitに入れずにチームで追跡できます。[SQLite CLI](https://sqlite.org/cli.html)・[SQLiteのトランザクション](https://sqlite.org/lang_transaction.html)

---

[← 演習に戻る](exercise.md) ｜ [補足教材の目次](README.md)
