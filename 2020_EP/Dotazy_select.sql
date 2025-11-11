SELECT * FROM Dochazka;

SELECT kod, nazev FROM Predmet;

SELECT jmeno FROM Zak
	WHERE datum_narozeni>"01.01.2001";

SELECT kod, nazev FROM Predmet
	ORDER BY kod ASC;

SELECT jmeno FROM Zak
	WHERE NOT (datum_narozeni >"01.01.2001" AND cislo_skrinky >100);

SELECT COUNT(zak_id), predmet_id
	FROM Dochazka
	GROUP BY predmet_id;

SELECT * FROM Trida
	WHERE kod like 'EP%';

SELECT MIN(cislo_skrinky) FROM EP2020_Ucitel;

SELECT * FROM EP2020_Ucitel
	WHERE jmeno LIKE 'A%';

SELECT jmeno, nazev
	FROM EP2020_Ucitel INNER JOIN EP2020_Trida
	ON EP2020_Ucitel.ucitel_id = EP2020_Trida.tridni_ucitel;