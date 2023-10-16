/* Zobrazuje všechny sloupečky a všechny řádky */
SELECT * FROM `IT2020_Ucitel`;
SELECT name FROM `IT2020_Ucitel`;

/* Ze všech výsledků zobrazí pouze část */
SELECT name FROM `IT2020_Ucitel` LIMIT 2; 
SELECT ucitel_id FROM `IT2020_Ucitel` WHERE name="Adam";

SELECT trida_name, name
	FROM `IT2020_Trida` JOIN `IT2020_Ucitel`
	ON IT2020_Trida.tridniUcitel_id = IT2020_Ucitel.ucitel_id;
