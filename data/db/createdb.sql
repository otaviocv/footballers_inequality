CREATE TABLE catalog (
    ID serial PRIMARY KEY,
    url varchar(255) UNIQUE NOT NULL,
    date_added timestamp NOT NULL,
    date_updated timestamp NOT NULL
);
