CREATE TABLE catalog (
    ID serial PRIMARY KEY,
    url varchar(255) UNIQUE NOT NULL,
    date_added timestamp NOT NULL,
    date_updated timestamp,
    status varchar(20) NOT NULL
);


INSERT INTO catalog (url, date_added, status)
VALUES ('https://www.transfermarkt.co.uk/wettbewerbe/afrika?page=1', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/amerika?page=1', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/amerika?page=2', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/asien?page=1', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/asien?page=2', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/asien?page=3', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=1', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=2', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=3', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=4', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=5', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=6', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=7', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=8', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=9', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=10', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=11', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=12', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=13', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=14', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=15', LOCALTIMESTAMP(0), 'new'),
('https://www.transfermarkt.co.uk/wettbewerbe/europa?page=16', LOCALTIMESTAMP(0), 'new');
