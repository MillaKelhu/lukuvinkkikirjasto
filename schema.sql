CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE Links (
    id SERIAL PRIMARY KEY,
    title TEXT,
    link_url TEXT,
    created_at TIMESTAMP,
    created_by INT,
    FOREIGN KEY(created_by) REFERENCES Users(id)
    ON DELETE SET NULL
);
