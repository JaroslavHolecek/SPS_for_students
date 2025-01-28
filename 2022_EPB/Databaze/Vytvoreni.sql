CREATE TABLE 2022_EPB_Uzivatel (
	id int AUTO_INCREMENT PRIMARY KEY,
    email char(50),
    heslo char(50)
);
INSERT INTO 2022_EPB_Uzivatel (email, heslo) VALUES ("ahoj@mail.cz", "ahoj123"), ("cau@mail.cz", "cau123"); 

CREATE TABLE 2022_EPB_Postava (
	id int AUTO_INCREMENT PRIMARY KEY,
    jmeno char(20) NOT NULL UNIQUE,
    hp int NOT NULL,
    uzivatel_id int NOT NULL,
    FOREIGN KEY (uzivatel_id) REFERENCES 2022_EPB_Uzivatel(id)
);
INSERT INTO 2022_EPB_Postava(jmeno, hp, uzivatel_id) VALUES ("Adam", 1000, 1);

SELECT id FROM `2022_EPB_Uzivatel` WHERE email="ahoj@mail.cz"; 
INSERT INTO 2022_EPB_Postava(jmeno, hp, uzivatel_id) VALUES ("Bára", 1500, (SELECT id FROM `2022_EPB_Uzivatel` WHERE email="cau@mail.cz") ); 