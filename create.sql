create table Neutral(
    dates date NOT NULL,
    home_team varchar(28) NOT NULL,
    away_team varchar(28) NOT NULL,
    neutral boolean NOT NULL)
create table Cities(
    dates data NOT NULL,
    tournament varchar(28) NOT NULL,
    city varchar(28) NOT NULL,
    country varchar(28) NOT NULL)
    
create table Results(
    dates date NOT NULL,
     home_team varchar(28) NOT NULL,
    away_team varchar(28) NOT NULL,
    home_score int NOT NULL,
    away_score int NOT NULL,
    tournament varchar NOT NULL)
    
ALTER TABLE Neutral ADD CONSTRAINT PK_Dates PRIMARY KEY (dates);
ALTER TABLE Neutral ADD CONSTRAINT PK_Home_Team PRIMARY KEY (home_team);
ALTER TABLE Neutral ADD CONSTRAINT PK_Away_Team PRIMARY KEY (away_team);
ALTER TABLE Results ADD CONSTRAINT PK_Dates1 PRIMARY KEY (dates);
ALTER TABLE Results ADD CONSTRAINT PK_Home_Team1 PRIMARY KEY (home_team);    
ALTER TABLE Results ADD CONSTRAINT PK_Away_Team1 PRIMARY KEY (away_team);
ALTER TABLE Cities ADD CONSTRAINT PK_Dates2 PRIMARY KEY (dates);
ALTER TABLE Cities ADD CONSTRAINT PK_City PRIMARY KEY (city);
ALTER TABLE Cities ADD CONSTRAINT PKTournament PRIMARY KEY (tournament);

ALTER TABLE Results
ADD CONSTRAINT FK_Dates FOREIGN KEY (dates) REFERENCES Neutral;
ALTER TABLE Results
ADD CONSTRAINT FK_Dates1 FOREIGN KEY (dates) REFERENCES Cities;
ALTER TABLE Results
ADD CONSTRAINT FK_Home_Team FOREIGN KEY (home_team) REFERENCES Neutral;
ALTER TABLE Results
ADD CONSTRAINT FK_Away_Team FOREIGN KEY (away_team) REFERENCES Neutral;
ALTER TABLE Results
ADD CONSTRAINT FK_Home_Score FOREIGN KEY (tournament) REFERENCES Cities;
