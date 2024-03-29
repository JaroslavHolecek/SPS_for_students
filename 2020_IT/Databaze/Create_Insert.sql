CREATE TABLE IT2020_Ucitel (
    ucitel_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name char(50) NOT NULL,
    datum_narozeni date NOT NULL
);

INSERT INTO IT2020_Ucitel (name, datum_narozeni)
VALUES ("Adam", "1980-01-01"),
	   ("Bert", "1991-08-03"),
	   ("Cecílie", "1994-11-05");

CREATE TABLE IT2020_Trida (
    trida_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    trida_name char(50) NOT NULL,
    obor_name char(50) NOT NULL,
    rok_nastupu date NOT NULL,
    tridniUcitel_id int NOT NULL UNIQUE,
    FOREIGN KEY (tridniUcitel_id) REFERENCES IT2020_Ucitel(ucitel_id)
);

INSERT INTO IT2020_Trida (trida_name, obor_name, rok_nastupu, tridniUcitel_id)
VALUES ("IT4", "Informační technologie", "2020-01-01", (SELECT ucitel_id FROM `IT2020_Ucitel` WHERE name="Adam")),
	   ("IT3", "Informační technologie", "2021-01-01", (SELECT ucitel_id FROM `IT2020_Ucitel` WHERE name="Bert")),
	   ("EP4", "Elektronické počítačové systémy", "2020-01-01", (SELECT ucitel_id FROM `IT2020_Ucitel` WHERE name="Cecílie"));

CREATE TABLE IT2020_Student (
    student_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    student_name char(50) NOT NULL,
    datum_narozeni date NOT NULL,
    trida_id int NOT NULL,
    FOREIGN KEY (trida_id) REFERENCES IT2020_Trida(trida_id)
);

INSERT INTO IT2020_Student (student_name, datum_narozeni, trida_id)
VALUES ("Dan", "2004-03-12", 1),
	   ("Eliška", "2004-12-20", 1),
	   ("Franta", "2003-02-04", 3);

CREATE TABLE IT2020_Predmet (
    predmet_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name char(50) NOT NULL
);

INSERT INTO IT2020_Predmet (name)
VALUES ("CJL"),
	   ("MAT"),
	   ("SAP");

CREATE TABLE IT2020_Zapis (
    zapis_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    predmet_id int NOT NULL,
    student_id int NOT NULL,
    FOREIGN KEY (predmet_id) REFERENCES IT2020_Predmet(predmet_id),
    FOREIGN KEY (student_id) REFERENCES IT2020_Student(student_id)
);

INSERT INTO IT2020_Zapis (predmet_id, student_id)
VALUES (1, 1),
		(2, 2),
		(3, 3),
		(1, 3),
		(2, 1),
		(3, 2);
