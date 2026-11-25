# SQL入門｜補足教材

[← 教材トップ](../../README.md)

商品と注文明細のサンプルを使って、SQLiteでデータの検索・追加・更新・削除を練習し、最後に集計と結合を試します。

## 1. SQLとは

SQLは、データベースに「どのデータを読みたいか」「どのデータを追加・変更したいか」を伝える言語です。たとえば、在庫の少ない商品を探したり、カテゴリごとの在庫を集計したりできます。この教材では、SQLを実行するデータベースとして **SQLite** を使います。

データは**テーブル（表）**に入っています。下は `products`（商品テーブル）の一部です。

| id | name | stock |
|---:|---|---:|
| 1 | ノート | 12 |
| 2 | ペン | 3 |

1行が商品1件、1列が商品名や在庫数などの項目です。`id` は商品を一意に識別する**主キー**です。別の表 `order_items`（注文明細）では、`product_id` に対応する商品の `id` を記録します。

## 2. 基本のSQL文

| SQL文・句 | 何を指定するか |
|---|---|
| `CREATE TABLE` | テーブル名、列名、列の型などを定義する。 |
| `SELECT … FROM …` | どのテーブルから、どの列を表示するかを指定する。 |
| `WHERE` | どの行を対象にするかを絞る。たとえば `stock <= 5` は在庫が5個以下の行。 |
| `ORDER BY` | 並べ替えに使う列を指定する。`ASC` は昇順、`DESC` は降順。 |
| `INSERT INTO … VALUES …` | 指定した列に値を入れて、新しい行を追加する。 |
| `UPDATE … SET …` | 既存の行の値を変更する。 |
| `DELETE FROM …` | 指定したテーブルから行を削除する。 |
| `GROUP BY` | 同じ値を持つ行をまとめ、`COUNT`（件数）や `SUM`（合計）で集計する。 |
| `JOIN … ON …` | `ON` の条件に従って、別々のテーブルの行を結び付ける。 |

`WHERE` を省いた `UPDATE` や `DELETE` は全行が対象です。先に同じ条件の `SELECT` で対象を確認します。

## 3. 実際に動かしてみよう

### 準備：SQLiteに練習データを読み込む

SQLiteのコマンドラインツールを使います。ターミナルで `sqlite3 --version` を実行し、バージョンが表示されることを確認します。

`docs/sql` フォルダのターミナルで `sqlite3 :memory:` を実行します。`sqlite>` が表示されたら、次を入力します。

```text
.read sample.sql
.headers on
.mode column
```

データはメモリ上に作られ、`.quit` で終了すると消えます。最初からやり直すには、起動と読み込みを繰り返します。

SQL文の末尾には `;` を付けます。`.read` など、ドットで始まる行はSQLiteのコマンドライン専用の操作なので、末尾の `;` は不要です。

準備ができたら、`.tables` を実行し、`products` と `order_items` があることを確かめます。`.schema products` では、サンプルの `CREATE TABLE` 文を確認できます。

### ステップ1：データを読む（SELECT）

まず、商品名と価格を表示します。

```sql
SELECT name, price
FROM products
ORDER BY id;
```

`SELECT` の後に表示する列、`FROM` の後に表の名前を書きます。この例ではノート、ペン、マグカップの順に表示されます。全列を見たい場合は、列名の代わりに `*` を指定します。

次に、在庫が5個以下の商品を、在庫の少ない順に表示します。

```sql
SELECT name, stock
FROM products
WHERE stock <= 5
ORDER BY stock ASC;
```

`WHERE` は行を絞り込む条件、`ORDER BY` は並び順です。`ASC` は昇順、`DESC` は降順です。この例ではマグカップ（2個）、ペン（3個）の順に表示されます。

### ステップ2：データを追加・更新・削除する

以下は同じSQLiteセッションで、ブロックを上から順に実行します。`BEGIN` から `ROLLBACK` までを1組として実行すると、最後に練習前の状態に戻ります。

#### 追加（INSERT）

```sql
BEGIN;

INSERT INTO products (id, name, category, price, stock)
VALUES (4, '消しゴム', '文具', 100, 8);

SELECT id, name, stock FROM products WHERE id = 4;
```

`INSERT INTO` で表と列を指定し、`VALUES` に同じ順序で値を書きます。最後の検索で、消しゴムの在庫が8個と表示されます。

#### 更新（UPDATE）

```sql
SELECT id, name, stock FROM products WHERE id = 4;

UPDATE products
SET stock = 10
WHERE id = 4;

SELECT id, name, stock FROM products WHERE id = 4;
```

`SET` で変更する列と値を書きます。更新前は8個、更新後は10個と表示されます。

#### 削除（DELETE）

```sql
SELECT id, name FROM products WHERE id = 4;

DELETE FROM products
WHERE id = 4;

SELECT id, name FROM products WHERE id = 4;

ROLLBACK;
```

削除後の検索では該当する行が表示されません。`ROLLBACK` で `BEGIN` 以降の操作を取り消します。変更を確定する場合に使う文は `COMMIT` です。

### ステップ3：グループごとに集計する（GROUP BY）

```sql
SELECT category, COUNT(*) AS product_count, SUM(stock) AS total_stock
FROM products
GROUP BY category
ORDER BY total_stock DESC;
```

`GROUP BY` で同じカテゴリをまとめ、`COUNT(*)` で商品数、`SUM(stock)` で在庫の合計を求めます。`AS` は結果に付ける列名です。文具は2件・15個、雑貨は1件・2個です。

### ステップ4：別のテーブルと結び付ける（JOIN）

```sql
SELECT products.name, order_items.quantity
FROM order_items
JOIN products ON order_items.product_id = products.id
ORDER BY order_items.id;
```

注文明細には商品名の代わりに `product_id` が入っています。`JOIN` の `ON` で商品テーブルの `id` と結び付けると、ペン4個とマグカップ1個の注文を表示できます。

[練習用データ](sample.sql) ｜ [演習に進む](exercise.md) ｜ [回答例を見る](answer.md)
