CREATE SCHEMA IF NOT EXISTS clinic;

CREATE TABLE IF NOT EXISTS clinic.patients(
    id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    birthday DATE NOT NULL,
    gender CHAR(1) NOT NULL CHECK (gender IN ('M','F'))
);

CREATE TABLE IF NOT EXISTS clinic.doctors(
    id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    specialization TEXT NOT NULL,
    phone_number TEXT UNIQUE
);