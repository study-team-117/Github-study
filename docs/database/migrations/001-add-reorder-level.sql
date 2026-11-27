-- Apply once to the practice database initialized by docs/sql/sample.sql.
-- Use sqlite3 -bail, or stop and roll back on the first error in the caller.
BEGIN;

CREATE TABLE IF NOT EXISTS schema_migrations (
    version TEXT PRIMARY KEY NOT NULL
);

ALTER TABLE products
ADD COLUMN reorder_level INTEGER NOT NULL DEFAULT 5 CHECK (typeof(reorder_level) = 'integer' AND reorder_level >= 0);

INSERT INTO schema_migrations (version) VALUES ('001-add-reorder-level');

COMMIT;
