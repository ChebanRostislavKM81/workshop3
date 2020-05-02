DECLARE 
    var_city cities.city%TYPE;
    var_tournament cities.tournament%TYPE;
BEGIN
    var_city := 'city';
    var_tournament := 'tour';
    
    FOR i IN 1..10 LOOP
        INSERT INTO cities (
        city,
        tournament)
        VALUES (
        trim(var_city) || i,
        trim(var_tournament) || i);
        END LOOP;
    END;
    
    