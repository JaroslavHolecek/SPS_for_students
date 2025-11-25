-- SELECT sloupce AS prejmenovani FROM tabulka
--      WHERE podmínka na řádky; -- podmínka umí =, <, >, OR, AND, NOT, IN, BETWEEN, LIKE, IS NULL

SELECT nazev AS `Název pozice` FROM 2023EP_Pozice WHERE ma_smlouvu = TRUE;

-- Agregační funkce: COUNT(), SUM(), AVG(), MAX(), MIN() spočítají hodnotu z jednoho sloupce
SELECT MIN(Price) AS "Nejnižší cena" 
FROM Products; 

SELECT COUNT(*)
FROM Products
WHERE price > 20;

-- DISTINCT - vybere jen různé hodnoty (odstraní duplicitní řádky)
SELECT COUNT(DISTINCT Price)
FROM Products;