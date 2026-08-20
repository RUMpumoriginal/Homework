CREATE TABLE [IF NOT EXISTS] Books (
--     NAME        AUTHOR      YEAR        PRICE
    id      INTEGER     PRIMARY KEY     AUTOINCREMENT,
    name    TEXT,
    author  TEXT,
    year    INTEGER,
    price   REAL
);


INSERT INTO Books (id, name, author, year, price)
VALUES
    (0, 'soul', 'bro', 2000, 49.50),
    (1, 'my life', 'me', 1998, 67.52),
    (2, 'my favorite pet', 'someone', 2015, 29.00);


UPDATE Books
SET year = 1997
WHERE id = 1;


DELETE FROM Books
WHERE price = 29.00;

