-- Assuming you have tables named 'users' and 'scores'

-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score DECIMAL(10, 2);
    DECLARE total_weight INT;

    -- Calculate total_score and total_weight for the user
    SELECT SUM(score * weight), SUM(weight)
    INTO total_score, total_weight
    FROM scores
    WHERE user_id = user_id;

    -- Ensure total_weight is not zero to avoid division by zero
    IF total_weight > 0 THEN
        -- Calculate the average weighted score and store it
        UPDATE users
        SET average_weighted_score = total_score / total_weight
        WHERE id = user_id;
    END IF;
END //

DELIMITER ;

