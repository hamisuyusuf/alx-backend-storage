-- Task: List all bands with "Glam rock" as their main style, ranked by longevity
-- The result will have two columns: band_name and lifespan (in years until 2022)
-- Lifespan is calculated using the difference between the year formed and the year split, or 2022 if still active

SELECT
    name AS band_name,                                       -- The name of the band
    CASE 
        WHEN split IS NULL THEN 2022 - formed                -- If the band is still active, subtract formed year from 2022
        ELSE split - formed                                  -- If the band has split, subtract formed year from split year
    END AS lifespan                                          -- Calculate the lifespan in years
FROM
    metal_bands                                              -- The table that stores the metal bands data
WHERE
    main_style = 'Glam rock'                                 -- Filter bands that have "Glam rock" as their main style
ORDER BY
    lifespan DESC,                                           -- Order the result by lifespan in descending order
    band_name;                                               -- Secondary ordering by band name

-- End of script

