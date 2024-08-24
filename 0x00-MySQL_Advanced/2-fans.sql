-- Task: Rank country origins of bands ordered by the number of (non-unique) fans

-- Create a view to rank country origins based on the number of fans
CREATE VIEW ranked_origins AS
SELECT 
    origin,
    SUM(nb_fans) AS total_fans
FROM 
    metal_bands
GROUP BY 
    origin
ORDER BY 
    total_fans DESC;

-- Select from the view to show the ranking of origins
SELECT * FROM ranked_origins;

