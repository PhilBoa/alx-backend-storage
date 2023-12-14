-- Script to list Glam rock bands ranked by longevity until 2022

SELECT band_name, (IFNULL(split, YEAR(CURDATE()) - 1) - formed) AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', style) > 0
ORDER BY lifespan DESC;
