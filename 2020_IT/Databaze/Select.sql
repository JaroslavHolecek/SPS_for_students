/* Zobrazuje všechny sloupečky a všechny řádky */
SELECT * FROM `IT2020_Ucitel`;
SELECT name FROM `IT2020_Ucitel`;

/* Ze všech výsledků zobrazí pouze část */
SELECT name FROM `IT2020_Ucitel` LIMIT 2; 
SELECT ucitel_id FROM `IT2020_Ucitel` WHERE name="Adam";

SELECT trida_name, name
	FROM `IT2020_Trida` JOIN `IT2020_Ucitel`
	ON IT2020_Trida.tridniUcitel_id = IT2020_Ucitel.ucitel_id;


/* Zobrazí nejnovější třídu */
SELECT MAX(rok_nastupu),trida_name FROM IT2020_Trida;

/* Zobrazí všechny studenty v jejichž jméně je písmenko "A" */
SELECT * FROM IT2020_Student
WHERE student_name LIKE '%a%';

/* Zobrazí název třídy a jméno studenta vedle sebe */
SELECT trida_name , student_name
FROM IT2020_Trida INNER JOIN IT2020_Student
 ON IT2020_Trida.trida_id=IT2020_Student.trida_id;
/* Smaže/pokusí se smazat třídu s id 1 */
DELETE FROM IT2020_Trida WHERE trida_id = 1;