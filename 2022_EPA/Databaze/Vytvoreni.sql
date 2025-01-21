CREATE TABLE 2022_EPA_Mesto (
    id int PRIMARY KEY AUTO_INCREMENT,
    nazev char(30) NOT NULL
);

CREATE TABLE 2022_EPA_Clovek (
	id int PRIMARY KEY AUTO_INCREMENT,
    jmeno char(20) NOT NULL,
    rodne_cislo int NOT NULL UNIQUE,
    mesto_id int UNIQUE,
    FOREIGN KEY (mesto_id) REFERENCES Mesto(id)
);

