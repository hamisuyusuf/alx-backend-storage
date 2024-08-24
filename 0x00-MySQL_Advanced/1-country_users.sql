-- Task: Create the 'users' table with specified attributes
-- The table will include the following columns:
-- id (integer, not null, auto increment, primary key)
-- email (string, 255 characters, not null, unique)
-- name (string, 255 characters)
-- country (ENUM of countries: US, CO, TN; default is US)
-- The script should not fail if the table already exists.

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,           -- Primary key, auto incrementing integer
    email VARCHAR(255) NOT NULL UNIQUE,       -- Email column, cannot be null, must be unique
    name VARCHAR(255),                        -- Name column, can be null
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US', -- Country column with ENUM, default is 'US'
    PRIMARY KEY (id)                          -- Define 'id' as the primary key
);

-- End of script

