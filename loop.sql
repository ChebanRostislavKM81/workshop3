DECLARE 
    var_city cities.city%TYPE;
    var_tournament cities.tournament%TYPE;
BEGIN
    var_city := 'city';
    var_tournament := 'tour';
    
    FOR i IN 1..10 LOOP
        INSERT INTO cities (
        dates,
        city,
        country,
        tournament)
        VALUES (
        01.01.70,
        trim(var_city) || i,
        England,
        trim(var_tournament) || i);
        END LOOP;
    END;
    
    
