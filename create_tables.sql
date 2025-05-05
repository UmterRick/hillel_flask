CREATE TABLE students(

    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    birth_date DATE NOT NULL
);

INSERT INTO students (name, birth_date) VALUES ('John Doe', '2000-01-01');

ALTER TABLE students ADD COLUMN course_name Varchar(500), photo_url Varchar(100)

