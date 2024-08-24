-- Task: Create the 'users' table if it doesn't already exist
-- The table will have the following columns:
-- id (integer, not null, auto increment, primary key)
-- email (string, 255 characters, not null, unique)
-- name (string, 255 characters)
-- This script is designed for execution on Ubuntu 18.04 LTS using MySQL 5.7

CREATE TABLE IF NOT EXISTS users (
	    id INT NOT NULL AUTO_INCREMENT,        -- Primary key, auto incrementing integer
	    email VARCHAR(255) NOT NULL UNIQUE,    -- Email column, cannot be null, must be unique
	    name VARCHAR(255),                     -- Name column, can be null
	    PRIMARY KEY (id)                       -- Define 'id' as the primary key
	);

	-- End of script

