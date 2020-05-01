CREATE OR REPLACE VIEW match AS
    SELECT
    RESULTS.home_team,
    RESULTS.away_team,
    RESULTS.tournament,
    RESULTS.neutral,    
    CITIES.city AS city
    FROM RESULTS
    INNER JOIN CITIES ON CITIES.city = RESULTS.city;
    
    