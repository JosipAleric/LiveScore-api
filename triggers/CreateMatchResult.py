create_match_result = """
CREATE TRIGGER after_match_insert
AFTER INSERT ON matches
FOR EACH ROW
CALL CreateMatchResultAfterMatchInsert() 
"""