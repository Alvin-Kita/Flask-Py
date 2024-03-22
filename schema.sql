DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS pokedex;
CREATE TABLE users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT UNIQUE NOT NULL,
                      password TEXT NOT NULL
);

INSERT INTO users (username, password) VALUES ('toto', 'tata');
INSERT INTO users (username, password) VALUES ('tata', 'toto');

CREATE TABLE pokedex (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    pkmn_name TEXT NOT NULL,
    pkmn_picture_url TEXT,
    pkmn_type1 TEXT NOT NULL,
    pkmn_type2 TEXT
);

INSERT INTO pokedex (username,pkmn_name, pkmn_picture_url, pkmn_type1)
VALUES (
        'toto',
        'Pikachu',
        'https://toppng.com/uploads/preview/anime-pokemon-png-transparent-pokemon-pikachu-115628931001szanhj4sy.png',
        'Electrik');

INSERT INTO pokedex (username, pkmn_name, pkmn_picture_url, pkmn_type1, pkmn_type2)
VALUES (
        'tata',
        'Ectoplasma',
        'https://w7.pngwing.com/pngs/855/531/png-transparent-gengar-funny-monster-thumbnail.png',
        'Spectre',
        'Poison');