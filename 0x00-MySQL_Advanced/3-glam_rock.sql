-- list all bands with `Glam rock` as their style.
SELECT band_name, (IFNULL(split, '2022') - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
