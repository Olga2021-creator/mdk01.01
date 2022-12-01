CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    login VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS positions(
    id INTEGER PRIMARY KEY,
    post VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS artists(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    nickname VARCHAR(100) NOT NULL UNIQUE,
    salary INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS team_titles(
    id INTEGER PRIMARY KEY,
    title VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS concert_venues(
    id INTEGER PRIMARY KEY,
    title VARCHAR(100) NOT NULL UNIQUE,
    city VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS staff(
    id INTEGER PRIMARY KEY,
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL ,
    surname VARCHAR(100) NOT NULL,
    date_birth VARCHAR(100) NOT NULL,
    FOREIGN KEY(user_id)
        REFERENCES users(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY(post_id)
        REFERENCES positions(id)
        ON DELETE SET NULL ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS teams(
    id INTEGER PRIMARY KEY,
    staff_id INTEGER NOT NULL,
    team_id INTEGER NOT NULL,
    FOREIGN KEY(staff_id)
        REFERENCES staff(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY(team_id)
        REFERENCES team_titles(id)
        ON DELETE SET NULL ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS concerts(
    id INTEGER PRIMARY KEY,
    artist_id INTEGER NOT NULL,
    venue_id INTEGER NOT NULL,
    team_id INTEGER NOT NULL,
    count_ticket INTEGER NOT NULL,
    title VARCHAR(100) NOT NULL,
    FOREIGN KEY(artist_id)
        REFERENCES artists(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY(venue_id)
        REFERENCES concert_venues(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY(team_id)
        REFERENCES team_titles(id)
        ON DELETE SET NULL ON UPDATE NO ACTION
);