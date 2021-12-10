CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE Links (
    id INTEGER PRIMARY KEY,
    title TEXT,
    link_url TEXT,
    created_at TIMESTAMP,
    created_by INT,
    FOREIGN KEY(created_by) REFERENCES Users(id)
    ON DELETE SET NULL
);

INSERT INTO Users (username, password)
VALUES ('user_one', 'good_password');

INSERT INTO Links (title, link_url, created_at, created_by)
VALUES ('BWT', 'https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform', datetime('now'), 1),
('Spark', 'https://spark.apache.org/', datetime('now'), 1),
('DBG', 'https://en.wikipedia.org/wiki/De_Bruijn_graph', datetime('now'), 1);
