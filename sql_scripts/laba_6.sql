CREATE SCHEMA IF NOT EXISTS restaurant;

CREATE TABLE IF NOT EXISTS restaurant.menu_items(
    id SERIAL PRIMARY KEY,
    dish TEXT NOT NULL UNIQUE,
    category TEXT NOT NULL,
    price NUMERIC(6, 2) NOT NULL,
    status TEXT DEFAULT 'available'
);

CREATE TABLE IF NOT EXISTS restaurant.employees(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    post TEXT NOT NULL,
    salary NUMERIC(8, 2)
);
