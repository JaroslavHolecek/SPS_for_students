/* Vyvoření tabulek */
CREATE TABLE `Osoba`(
    `id` INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `BirthDate` DATE NOT NULL,
    `IDnumber` INT NOT NULL,
    `Firstname` CHAR(255) NOT NULL,    
    `id_TrainingGroup` INT UNSIGNED /* POZOR - typ musí být sejný jako id v TrainingGroup */ NOT NULL
);

CREATE TABLE `TrainingGroup`(
    `id` INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `Name` CHAR(255) NOT NULL
);

/* Propojení tabulek */
ALTER TABLE
    `Osoba` ADD CONSTRAINT `Propojeni TrainingGroup a Osoba`
     FOREIGN KEY(`id_TrainingGroup`) REFERENCES `TrainingGroup`(`id`);

/* Vloení dat do tabulek  */
INSERT INTO TrainingGroup(Name) VALUES
("Pondělí"), ("Úterý"), ("Středa"), ("Čtvrtek"), ("Pátek");

INSERT INTO Osoba(BirthDate, IDnumber, Firstname, id_TrainingGroup) VALUES
("2000-01-01", 68, "Jaromír", (SELECT id FROM TrainingGroup WHERE Name="Úterý")),
("1999-05-21", 31, "Tomáš", (SELECT id FROM TrainingGroup WHERE Name="Středa")),
("1998-06-12", 51, "Tonda", (SELECT id FROM TrainingGroup WHERE Name="Úterý"));
INSERT INTO Osoba(BirthDate, IDnumber, Firstname) VALUES
("2002-02-02", 70, "Eliška"),
("1999-08-25", 41, "Franta");

/* Zobrazení dat */
SELECT * FROM Osoba WHERE BirthDate < "1999-12-30";
SELECT Firstname, BirthDate FROM Osoba WHERE
BirthDate < "1999-12-30"
AND id_TrainingGroup=(SELECT id FROM TrainingGroup WHERE Name="Středa") ;

SELECT AVG(IDnumber) FROM Osoba;

SELECT id FROM TrainingGroup WHERE Name="Úterý";
SELECT Firstname, IDnumber FROM Osoba WHERE (SELECT AVG(IDnumber) FROM Osoba) < IDnumber;

SELECT Osoba.id_TrainingGroup, TrainingGroup.id, Osoba.Firstname, Osoba.BirthDate, TrainingGroup.Name
 FROM `Osoba` JOIN TrainingGroup ON Osoba.id_TrainingGroup=TrainingGroup.id
  WHERE Osoba.BirthDate < "2001-01-01"


