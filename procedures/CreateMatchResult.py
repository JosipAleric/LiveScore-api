create_match_result_after_match_insert = """
CREATE PROCEDURE CreateMatchResultAfterMatchInsert()
BEGIN
    DECLARE match_id INT;
    DECLARE home_team_id INT;
    DECLARE away_team_id INT;

    -- Get the ID, home_team_id and away_team_id of the last inserted match
    SELECT id, home_team_id, away_team_id INTO match_id, home_team_id, away_team_id FROM matches ORDER BY id DESC LIMIT 1;

    -- Insert a new row into match_results for the new match
    INSERT INTO match_results (match_id, home_team_goals, away_team_goals)
    VALUES (match_id, 0, 0);
END 
"""