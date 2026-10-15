-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name TEXT,
    cooking_time INT,
    rating INT
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (name, cooking_time, rating) VALUES 
    ('Classic Caprese Salad', 10, 3), 
    ('Garlic Butter Shrimp Pasta', 20, 4), 
    ('Beef and Broccoli Stir-Fry', 25, 5), 
    ('Chicken Tikka Masala', 45, 5), 
    ('Classic chocolate chip cookies', 30, 5);
    