CREATE TABLE IF NOT EXISTS products(
    id SERIAL PRIMARY KEY,
    name_product TEXT NOT NULL UNIQUE,
    price INT NOT NULL CHECK(price > 0),
    store INT NOT NULL CHECK(store >= 0)
);

INSERT INTO products 
    (name_product, price, store)
VALUES
    ('Помидоры', 100, 1000),
    -- ('Огурцы', -1, 2000),
    -- ('Картофель', 10, -1),
    ('Баклажан', 120, 3);