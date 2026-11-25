PRAGMA foreign_keys = ON;

BEGIN;

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price INTEGER NOT NULL,
    stock INTEGER NOT NULL
);

CREATE TABLE order_items (
    id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products (id),
    quantity INTEGER NOT NULL
);

INSERT INTO products (id, name, category, price, stock) VALUES
    (1, 'ノート', '文具', 300, 12),
    (2, 'ペン', '文具', 150, 3),
    (3, 'マグカップ', '雑貨', 800, 2);

INSERT INTO order_items (id, product_id, quantity) VALUES
    (1, 2, 4),
    (2, 3, 1);

COMMIT;
