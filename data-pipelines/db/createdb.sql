CREATE TABLE catalog (
    ID serial PRIMARY KEY,
    url varchar(255) UNIQUE NOT NULL,
    date_added timestamp NOT NULL,
    date_updated timestamp,
    status varchar(20) NOT NULL,
    page_type varchar(20) NOT NULL
);


INSERT INTO catalog (url, date_added, status, page_type)
VALUES ('https://www.transfermarkt.co.uk/wettbewerbe/afrika?page=1',
        CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/amerika?page=1',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/amerika?page=2',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/asien?page=1',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/asien?page=2',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/asien?page=3',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=1',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=2',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=3',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=4',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=5',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=6',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=7',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=8',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=9',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=10',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=11',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=12',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=13',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=14',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=15',
 CURRENT_TIMESTAMP(0), 'new', 'area'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=16',
 CURRENT_TIMESTAMP(0), 'new', 'area');

CREATE TABLE leagues (
    league_id serial PRIMARY KEY,
    league varchar(100) NOT NULL,
    country varchar(100) NOT NULL,
    clubs smallint NOT NULL,
    players smallint NOT NULL,
    avg_age real NOT NULL,
    foreing_players real NOT NULL,
    total_market_value real NOT NULL
);

CREATE TABLE teams (
    team_id serial PRIMARY KEY,
    league_id serial NOT NULL,
    team varchar(100) NOT NULL,
    players smallint NOT NULL,
    foreing_players real NOT NULL,
    avg_age real NOT NULL,
    total_market_value real NOT NULL,
    avg_market_value real NOT NULL
);

CREATE TABLE players (
    player_id serial PRIMARY KEY,
    team_id serial NOT NULL,
    name varchar(100) NOT NULL,
    number smallint NOT NULL,
    position varchar(100) NOT NULL,
    date_of_birth_and_date varchar(100) NOT NULL,
    nationality varchar(100) NOT NULL,
    market_value real NOT NULL
);
