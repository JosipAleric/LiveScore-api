
update_match_result = """
CREATE TRIGGER update_match_result
AFTER INSERT ON match_events
FOR EACH ROW
BEGIN
   IF NEW.event_description = 'Goal' THEN
      IF (SELECT home_team_id FROM matches WHERE id = NEW.match_id) = (SELECT team_id FROM players WHERE id = NEW.player_id) THEN
         UPDATE match_results
         SET home_team_goals = home_team_goals + 1
         WHERE match_id = NEW.match_id;
      ELSE
         UPDATE match_results
         SET away_team_goals = away_team_goals + 1
         WHERE match_id = NEW.match_id;
      END IF;
   END IF;
END;
"""