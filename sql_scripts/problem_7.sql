CREATE TABLE IF NOT EXISTS temperatures(
    id SERIAL PRIMARY KEY,
    town_name TEXT NOT NULL UNIQUE,
    date_measurement DATE NOT NULL,
    temperature INT NOT NULL CHECK(temperature BETWEEN -60 AND 60)
);

INSERT INTO temperatures 
    (town_name, date_measurment, temperature)
VALUES
    ('Москва', '2024-01-15', -15),
    ('Сочи', '2024-01-15', 8),
    ('Якутск', '2024-01-15', -42),
    ('Санкт-Петербург', '2024-01-15', -10),
    ('Краснодар', '2024-01-15', 5);