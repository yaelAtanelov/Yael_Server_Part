create table users
(
    id         int auto_increment
        primary key,
    first_name varchar(200) not null,
    last_name  varchar(200) not null,
    Email      varchar(200) not null,
    password   varchar(200) not null,
    fav_song   varchar(200) not null,
    constraint users_Email_uindex
        unique (Email),
    constraint users_id_uindex
        unique (id)
);

INSERT INTO my_flask_db.users (id, first_name, last_name, Email, password, fav_song) VALUES (3, 'avi', 'atanelov', 'atanelov@post.bgu.com', '1402', 'ZikI Ziki');
INSERT INTO my_flask_db.users (id, first_name, last_name, Email, password, fav_song) VALUES (4, 'shoham', 'harif', 'shoham@gimal.com', '2608', 'Mi Zot');
INSERT INTO my_flask_db.users (id, first_name, last_name, Email, password, fav_song) VALUES (5, 'mister', 'salsa', 'salsa@co.il', '5555', 'Salsa song');
INSERT INTO my_flask_db.users (id, first_name, last_name, Email, password, fav_song) VALUES (6, 'shaham', 'tal', 'maximilan@co.il', '1998', 'shalosh Banot');
INSERT INTO my_flask_db.users (id, first_name, last_name, Email, password, fav_song) VALUES (16, 'yael', 'itzhaky', 'itzhakyy@co.il', '1999', 'Lalalala');
INSERT INTO my_flask_db.users (id, first_name, last_name, Email, password, fav_song) VALUES (20, 'shlomo', 'itzhaky', 'momo@gmail', '123456', 'lalalala');
INSERT INTO my_flask_db.users (id, first_name, last_name, Email, password, fav_song) VALUES (22, 'AAA', 'BBB', 'aaa@bbb', '1234', 'lalalalal');
