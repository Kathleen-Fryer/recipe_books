DROP TABLE IF EXISTS books;
DROP SEQUENCE IF EXISTS books_id_seq;
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;


CREATE SEQUENCE IF NOT EXISTS books_id_seq;
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    release_year INTEGER
);

CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    ingredients VARCHAR(255),
    allergens VARCHAR(255),
    prep_time INTEGER,
    cook_time INTEGER,
    meal_type VARCHAR(255),
    appliances VARCHAR(255)
    book_id int,
    constraint fk_book foreign key(book_id)
    references books(id)
    on delete cascade
);


-- seed data

INSERT INTO books (title, author, release_year) VALUES
    ('The Official Halo Cookbook', 'Victoria Rosenthal', 2022),
    ('Mary Berrys Christmas Collection', 'Mary Berry', 2013),
    ('Aisnleys Good Mood Food', 'Ainsley Harriott', 2021);



INSERT INTO recipes (title, ingredients, prep_time, cook_time, meal_type, appliances, book_id) VALUES
    ('Freyas Tea', 'raspberries, blackberries, sugar, water, mint, lemon juice, earl grey tea bags', 15, 30, 'soft drink', 'hob, fridge'),
    ('Fast-Lane Salmon', 'puff pastry, salmon, salt, black pepper, creme fraiche, parmesan, parsley, eggs, cucumbers, spring onions', 10, 20, 'main course', 'oven, hob'),
    ('Lemon and Herb Chicken Flatties with Celariac Remoulade', 'lemon juice, olive oil, garlic, mixed herbs, parsley, chicken, lemons, salt, black pepper, rocket, celeriac, mayonnaise, creme fraiche, mustard', 45, 10, 'main course', 'hob');
