"""Run two stock updates against the shared, in-memory practice database."""

import sqlite3
from contextlib import closing
from pathlib import Path

SAMPLE_SQL = Path(__file__).resolve().parents[2] / "sql" / "sample.sql"


def record_order(connection, product_id, quantity):
    if type(quantity) is not int or quantity <= 0:
        raise ValueError("数量は正の整数を指定してください。")

    connection.execute("BEGIN")
    try:
        update = connection.execute(
            """UPDATE products SET stock = stock - ?
               WHERE id = ? AND stock >= ?""",
            (quantity, product_id, quantity),
        )
        if update.rowcount != 1:
            connection.rollback()
            return False

        connection.execute(
            "INSERT INTO order_items (product_id, quantity) VALUES (?, ?)",
            (product_id, quantity),
        )
        connection.commit()
        return True
    except sqlite3.Error:
        connection.rollback()
        raise


def show_state(connection, label):
    (stock,) = connection.execute(
        "SELECT stock FROM products WHERE id = ?", (2,)
    ).fetchone()
    (count,) = connection.execute("SELECT COUNT(*) FROM order_items").fetchone()
    print(f"{label}: ペンの在庫={stock}、明細数={count}")


def main():
    with closing(sqlite3.connect(":memory:", isolation_level=None)) as connection:
        connection.executescript(SAMPLE_SQL.read_text(encoding="utf-8"))
        show_state(connection, "開始時")
        for quantity in (1, 9):
            recorded = record_order(connection, 2, quantity)
            show_state(connection, "成功" if recorded else "取り消し")


if __name__ == "__main__":
    main()
