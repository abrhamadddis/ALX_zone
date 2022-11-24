    CREATE SCHEMA IF NOT EXISTS ALX_ZONE;
    USE ALX_ZONE;
    CREATE TABLE IF NOT EXISTS  autors(
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
    Foreign Key (user_id) REFERENCES autors (user_id)
);
