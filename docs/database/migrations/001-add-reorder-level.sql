-- Apply once to the practice database initialized by docs/sql/sample.sql.
BEGIN;

CREATE TABLE IF NOT EXISTS schema_migrations (
    version TEXT PRIMARY KEY NOT NULL
);

INSERT INTO schema_migrations (version) VALUES ('001-add-reorder-level');

ALTER TABLE products
ADD COLUMN reorder_level INTEGER NOT NULL DEFAULT 5 CHECK (typeof(reorder_level) = 'integer' AND reorder_level >= 0);

COMMIT;
