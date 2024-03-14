DROP TABLE IF EXISTS users;

CREATE TABLE users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT UNIQUE NOT NULL,
                      password TEXT NOT NULL
);

INSERT INTO users (username, password) VALUES ('toto', 'tata');
INSERT INTO users (username, password) VALUES ('tata', 'toto');
