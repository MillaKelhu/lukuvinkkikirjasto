CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE Links (
    id SERIAL PRIMARY KEY,
    title TEXT,
    link_url TEXT,
    created_at TIMESTAMP,
    created_by INT,
    FOREIGN KEY(created_by) REFERENCES Users(user_id)
    ON DELETE SET NULL
);
