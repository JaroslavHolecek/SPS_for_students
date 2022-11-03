/* Vytvoření tabulek */
CREATE TABLE `Osoba`(
    `id` INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `BirthDate` DATE NOT NULL,
    `IDnumber` INT NOT NULL,
    `Firstname` CHAR(255) NOT NULL,
    `id_TrainingGroup` INT UNSIGNED NOT NULL
);

CREATE TABLE `TrainingGroup`(
    `id` INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `Name` CHAR(255) NOT NULL
);

/* Propojení tabulek */
ALTER TABLE
    `Osoba` ADD CONSTRAINT `Cizí klíč`
     FOREIGN KEY(`id_TrainingGroup`) REFERENCES `TrainingGroup`(`id`);

/* Vložení dat */
INSERT INTO TrainingGroup(Name) VALUES
("Pondělí"), ("Úterý"), ("Středa");

INSERT INTO Osoba(BirthDate, IDnumber, Firstname, id_TrainingGroup) VALUES
("1985-10-02", 68, "Jaromír", (SELECT id FROM TrainingGroup WHERE Name="Pondělí")),
 ("2000-12-24", 31, "Tonda", (SELECT id FROM TrainingGroup WHERE Name="Středa")),
("1999-06-14", 54, "Franta", (SELECT id FROM TrainingGroup WHERE Name="Středa"));

/* Čtení dat */
SELECT id FROM TrainingGroup WHERE Name="Středa";

SELECT Firstname, IDnumber FROM Osoba WHERE
 IDnumber > (SELECT AVG(IDnumber) FROM Osoba) AND BirthDate < "1990-12-15";
SELECT AVG(IDnumber) FROM Osoba;

SELECT FirstName, Name FROM Osoba JOIN TrainingGroup WHERE id_TrainingGroup = TrainingGroup.id;

