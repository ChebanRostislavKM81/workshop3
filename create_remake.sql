create table Neutral(
    dates date NOT NULL,
    home_team varchar(28) NOT NULL,
    away_team varchar(28) NOT NULL,
    neutral varchar(28) NOT NULL);
create table Cities(
    dates date NOT NULL,
    tournament varchar(28) NOT NULL,
    city varchar(28) NOT NULL,
    country varchar(28) NOT NULL);
    
create table Results(
    dates date NOT NULL,
     home_team varchar(28) NOT NULL,
    away_team varchar(28) NOT NULL,
    home_score int NOT NULL,
    away_score int NOT NULL,
    tournament varchar(28) NOT NULL,
    city VARCHAR(28) NOT NULL,
    neutral varchar(28) NOT NULL);
    

