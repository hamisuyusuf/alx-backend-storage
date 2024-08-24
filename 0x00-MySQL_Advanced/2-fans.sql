-- Task: Rank country origins of bands by the number of fans
-- The result will have two columns: origin (country) and nb_fans (total number of fans)
-- The result will be ordered by the number of fans in descending order

SELECT
    origin,                               -- The country of origin of the band
    SUM(nb_fans) AS nb_fans               -- The total number of fans from all bands in that country
FROM
    metal_bands                           -- The table that stores the metal bands data
GROUP BY
    origin                                -- Group the result by the country of origin
ORDER BY
    nb_fans DESC;                         -- Order the result by the number of fans in descending order

-- End of script

