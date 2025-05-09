CREATE TABLE students(
    id INTEGER PROMARY KEY,
    name TEXT NOT NULL,
    birth_date DATE NOT NULL
);
INSERT INTO students (name, birth_date) VALUES ('John Doe', '2000-01-01');