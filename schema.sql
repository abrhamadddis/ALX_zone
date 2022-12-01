<<<<<<< HEAD
    CREATE SCHEMA IF NOT EXISTS ALX_ZONE;
    USE ALX_ZONE;
    CREATE TABLE IF NOT EXISTS  author(
        user_id BIGINT(20), AUTOINCREAMENT,
        firstName VARCHAR(200) NOT NULL,
        lastName VARCHAR(200) NOT NULL,
        email VARCHAR(200) NOT NULL,
        password VARCHAR(25),
        image VARBYTE(MAX),
        PRIMARY KEY (user_id)

    );
    CREATE TABLE IF NOT EXISTS blogs (
        blog_id BIGINT(20),AUTOINCREAMENT,
        title VARCHAR(200) NOT NULL,
        content TEXT NOT NULL,
        user_id BIGINT(20) NOT NULL,
        _created TIMESTAMP DEFAULT NOW(),
        PRIMARY KEY (blog_id),
        Foreign Key (user_id) REFERENCES author (user_id)
    );

    CREATE TABLE IF NOT EXISTS like (
        blog_id  BIGINT(20),AUTOINCREAMENT,
        user_id BIGINT(20),AUTOINCREAMENT
        Foreign Key (user_id) REFERENCES author (user_id)
        Foreign Key (blog_id) REFERENCES blogs (blog_id)
    );

    CREATE TABLE IF NOT EXISTS comment (
        user_id BIGINT(20),AUTOINCREAMENT,
        blog_id BIGINT(20),AUTOINCREAMENT,
        comment TEXT 
        date_created TIMESTAMP DEFAULT NOW()
        Foreign Key (user_id) REFERENCES author (user_id)
        Foreign Key (blog_id) REFERENCES blogs (blog_id)

    );
=======

CREATE TABLE IF NOT EXISTS user(
        user_id INTEGER PRIMARY KEY  AUTOINCREMENT,
        name VARCHAR(200) NOT NULL,
        email VARCHAR(200) NOT NULL,
        password VARCHAR(25)
    );
CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
>>>>>>> 2b532e12b4eb992576f42a3135bdc977cf465ad1
