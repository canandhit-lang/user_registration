create table users(
user_id SERIAL PRIMARY KEY,
name VARCHAR(50),
sure_name VARCHAR(50),
dob DATE,
mobile VARCHAR(10),
email VARCHAR(50) UNIQUE,
address TEXT
);
