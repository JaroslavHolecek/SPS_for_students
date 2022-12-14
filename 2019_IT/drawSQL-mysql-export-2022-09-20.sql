/* Vytvoření tabulek */
CREATE TABLE `Osoba`(
    `id` INT(3) UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `BirthDate` DATE NOT NULL,
    `IDnumber` INT(3) NOT NULL,
    `Firstname` CHAR(20) NOT NULL,
    `id_TrainingGroup` INT(3) UNSIGNED
);

CREATE TABLE `TrainingGroup`(
    `id` INT(3) UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `Name` CHAR(30) NOT NULL
);

ALTER TABLE
    `Osoba` ADD CONSTRAINT `Cizí klíč Osoba-TrainingGroup-id`
    FOREIGN KEY(`id_TrainingGroup`)
    REFERENCES `TrainingGroup`(`id`);

/* Vkládání dat */
INSERT INTO TrainingGroup (Name) VALUES
("Pondělí"), ("Úterý"), ("Středa"), ("Čtvrtek"), ("Pátek");

INSERT INTO
Osoba (BirthDate, IDnumber, Firstname, id_TrainingGroup) VALUES
("2020-10-4", 68, "Jarda", (SELECT id FROM `TrainingGroup` WHERE Name="Pondělí")),
("2000-12-5", 71, "Franta", (SELECT id FROM `TrainingGroup` WHERE Name="Pondělí")),
("2020-10-4", 80, "Bára", (SELECT id FROM `TrainingGroup` WHERE Name="Úterý")),
("2020-10-4", 35, "Klára", (SELECT id FROM `TrainingGroup` WHERE Name="Středa")),
("1999-1-1", 38, "Adéla", (SELECT id FROM `TrainingGroup` WHERE Name="Středa"));
INSERT INTO Osoba(BirthDate, IDnumber, Firstname) VALUES
("1999-12-24", 50, "Eliška");


/* Čtení dat */
SELECT id FROM `TrainingGroup` WHERE Name="Středa";
SELECT Firstname FROM Osoba WHERE IDnumber > (SELECT AVG(IDnumber) FROM Osoba);

/* Průměrné číslo dresu */
SELECT AVG(IDnumber) FROM Osoba;

SELECT * FROM Osoba WHERE id_TrainingGroup = (SELECT id FROM `TrainingGroup` WHERE Name="Pondělí") /* chodí v pondělí */
                            AND BirthDate < "2015-1-1" /* je "starý" */

/* Select s JOIN */
SELECT Firstname, TrainingGroup.Name FROM `Osoba` JOIN TrainingGroup ON id_TrainingGroup = TrainingGroup.id;
SELECT Firstname, TrainingGroup.Name FROM `Osoba` LEFT JOIN TrainingGroup ON id_TrainingGroup = TrainingGroup.id;
/* MariaDB neumí FULL OUTER -> je potřeba ho "nasimulovat" https://stackoverflow.com/questions/4796872/how-can-i-do-a-full-outer-join-in-mysql */

/* ukázka připojení z pythonu viz https://github.com/JaroslavHolecek/Teaching/tree/master/JupyterNotebook/SQL  */

