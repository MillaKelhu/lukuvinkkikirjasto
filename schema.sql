CREATE TABLE Links (
    id SERIAL PRIMARY KEY,
    title TEXT,
    link_url TEXT,
    created_at TIMESTAMP
);

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

