# Write your MySQL query statement below

SELECT Cinema.id, Cinema.movie, Cinema.description, Cinema.rating
FROM cinema
WHERE description != 'boring' AND id % 2 != 0
ORDER BY rating DESC;
