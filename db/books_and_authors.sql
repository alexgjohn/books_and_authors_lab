DROP TABLE books;
DROP TABLE authors;


CREATE TABLE authors(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE books(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    author_id INT NOT NULL REFERENCES authors(id)
);



-- INSERT INTO authors(name)
-- VALUES ('Charles Dickens');

-- INSERT INTO authors(name)
-- VALUES ('JK Rowling');

-- INSERT INTO books(title,genre)
-- VALUES ('Oliver Twist','fiction');

-- INSERT INTO book(title,genre,author_id)
-- VALUES ('Tales');