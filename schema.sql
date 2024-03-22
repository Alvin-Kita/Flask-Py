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
    username TEXT,
    pkmn_name TEXT NOT NULL,
    pkmn_picture_url TEXT,
    pkmn_type1 TEXT NOT NULL,
    pkmn_type2 TEXT
);

INSERT INTO pokedex (username,pkmn_name, pkmn_picture_url, pkmn_type1)
VALUES (
           'toto',
           'Pixel',
           'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTe01Ygr_fYFmma5zlF1TCKpBTyy52MOlTINNOcGmwUA9CgVM0j9V8LiQ679lK-70eN8qE&usqp=CAU',
           'Mascotte');


INSERT INTO pokedex (username,pkmn_name, pkmn_picture_url, pkmn_type1)
VALUES (
        'toto',
        'Pikachu',
        'https://www.coupcritique.fr/images/pokemons/pikachu-partner.png',
        'Electrik');

INSERT INTO pokedex (username,pkmn_name, pkmn_picture_url, pkmn_type1, pkmn_type2)
VALUES (
           'tata',
           'Pixel',
           'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTe01Ygr_fYFmma5zlF1TCKpBTyy52MOlTINNOcGmwUA9CgVM0j9V8LiQ679lK-70eN8qE&usqp=CAU',
           'Mascotte',
           'ultime');