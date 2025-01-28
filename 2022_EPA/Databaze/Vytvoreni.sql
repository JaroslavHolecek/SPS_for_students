CREATE TABLE 2022_EPA_Mesto (
    id int PRIMARY KEY AUTO_INCREMENT,
    nazev char(30) NOT NULL
);

INSERT INTO 2022_EPA_Mesto (nazev) VALUES ("Kladno"), ("Praha"), ("Buštěhrad");

CREATE TABLE 2022_EPA_Clovek (
	id int PRIMARY KEY AUTO_INCREMENT,
    jmeno char(20) NOT NULL,
    rodne_cislo char(10) NOT NULL UNIQUE,
    mesto_id int UNIQUE,
    FOREIGN KEY (mesto_id) REFERENCES 2022_EPA_Mesto(id)
);

INSERT INTO 2022_EPA_Clovek (jmeno, rodne_cislo, mesto_id) VALUES ("Adam", "0161120233", 1); 

SELECT id FROM `2022_EPA_Mesto` WHERE nazev = "Praha"; 
INSERT INTO 2022_EPA_Clovek (jmeno, rodne_cislo, mesto_id) VALUES ("Bára", "0161120233", (SELECT id FROM `2022_EPA_Mesto` WHERE nazev = "Praha")); 


