CREATE TABLE EP2020_Predmet (
    predmet_id int PRIMARY KEY AUTO_INCREMENT,
    nazev varchar(50) NOT NULL,
    kod int NOT NULL
);

INSERT INTO EP2020_Predmet (nazev, kod)
VALUES ("Matematika",52), ("Fyzika",53), ("Český jazyk",54);

CREATE TABLE EP2020_Obor (
    obor_id int PRIMARY KEY AUTO_INCREMENT,
    nazev varchar(50) NOT NULL,
    kod int NOT NULL
);

INSERT INTO EP2020_Obor (nazev, kod)
VALUES ("Automatizace",40), ("Počítačové systémy",41);


CREATE TABLE EP2020_Ucitel (
    ucitel_id int PRIMARY KEY AUTO_INCREMENT,
    jmeno char(50) NOT NULL,
    datum_narozeni date NOT NULL,
    cislo_skrinky int 
); 

INSERT INTO EP2020_Ucitel (jmeno, datum_narozeni, cislo_skrinky)
VALUES ("Josef", "1984-07-25", 58);   
INSERT INTO EP2020_Ucitel (jmeno, datum_narozeni)
VALUES ("Adam", "1984-09-25");


CREATE TABLE EP2020_Trida (
    trida_id int PRIMARY KEY AUTO_INCREMENT,
    nazev varchar(50) NOT NULL,
    kod int NOT NULL,
    tridni_ucitel int NOT NULL UNIQUE,
    FOREIGN KEY (tridni_ucitel) REFERENCES EP2020_Ucitel(ucitel_id)

);
INSERT INTO EP2020_Trida (nazev, kod, tridni_ucitel)
VALUES ("EP4", 101, (SELECT ucitel_id FROM `EP2020_Ucitel`WHERE jmeno= "Josef")),
("IT2", 201, (SELECT ucitel_id FROM `EP2020_Ucitel`WHERE jmeno= "Adam"));

CREATE TABLE EP2020_Zak (
    zak_id int PRIMARY KEY AUTO_INCREMENT,
    jmeno char(50) NOT NULL,
    datum_narozeni date NOT NULL,
    cislo_skrinky int,
    obor_id int NOT NULL,
    trida_id int NOT NULL,
    FOREIGN KEY (obor_id) REFERENCES EP2020_Obor(obor_id),
    FOREIGN KEY (trida_id) REFERENCES EP2020_Trida(trida_id)
);
INSERT INTO EP2020_Zak (jmeno, datum_narozeni, cislo_skrinky, obor_id, trida_id)
VALUES ("Anezka", "2005-07-25" ,5 , (SELECT obor_id FROM `EP2020_Obor`WHERE nazev="Automatizace"), (SELECT trida_id FROM `EP2020_Trida`WHERE nazev="IT2")),
("Petr", "2005-08-28" ,6 , (SELECT obor_id FROM `EP2020_Obor`WHERE nazev="Automatizace"), (SELECT trida_id FROM `EP2020_Trida`WHERE nazev="EP4"));

CREATE TABLE EP2020_Dochazka (
    dochazka_id int PRIMARY KEY AUTO_INCREMENT,
    datum_zapisu date,
    zak_id int  NOT NULL,
    predmet_id int  NOT NULL,
    FOREIGN KEY (zak_id) REFERENCES EP2020_Zak(zak_id),
    FOREIGN KEY (predmet_id) REFERENCES EP2020_Predmet(predmet_id)

);

