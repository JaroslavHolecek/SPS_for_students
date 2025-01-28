CREATE TABLE 2022_EPB_Uzivatel (
	id int AUTO_INCREMENT PRIMARY KEY,
    email char(50),
    heslo char(50)
);

CREATE TABLE 2022_EPB_Postava (
	id int AUTO_INCREMENT PRIMARY KEY,
    jmeno char(20) NOT NULL UNIQUE,
    hp int NOT NULL,
    uzivatel_id int NOT NULL,
    FOREIGN KEY (uzivatel_id) REFERENCES 2022_EPB_Uzivatel(id)
);