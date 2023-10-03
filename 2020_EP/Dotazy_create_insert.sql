CREATE TABLE Predmet (
    predmet_id int PRIMARY KEY AUTO_INCREMENT,
    nazev varchar(50) NOT NULL,
    kod int NOT NULL
);

INSERT INTO Predmet (nazev, kod)
VALUES ("Matematika",52), ("Fyzika",53), ("Český jazyk",54);

CREATE TABLE Obor (
    obor_id int PRIMARY KEY AUTO_INCREMENT,
    nazev varchar(50) NOT NULL,
    kod int NOT NULL
);

INSERT INTO Obor (nazev, kod)
VALUES ("Automatizace",40), ("Počítačové systémy",41);


CREATE TABLE Ucitel (
    ucitel_id int PRIMARY KEY AUTO_INCREMENT,
    jmeno char(50) NOT NULL,
    datum_narozeni date NOT NULL,
    cislo_skrinky int 
); 

INSERT INTO Ucitel (jmeno, datum_narozeni, cislo_skrinky)
VALUES ("Josef", "1984-07-25", 58);   
INSERT INTO Ucitel (jmeno, datum_narozeni)
VALUES ("Adam", "1984-09-25");


CREATE TABLE Trida (
    trida_id int PRIMARY KEY AUTO_INCREMENT,
    nazev varchar(50) NOT NULL,
    kod int NOT NULL,
    tridni_ucitel int NOT NULL UNIQUE,
    FOREIGN KEY (tridni_ucitel) REFERENCES Ucitel(ucitel_id)
);

CREATE TABLE Zak (
    zak_id int PRIMARY KEY AUTO_INCREMENT,
    jmeno char(50) NOT NULL,
    datum_narozeni date NOT NULL,
    cislo_skrinky int,
    obor_id int NOT NULL,
    trida_id int NOT NULL,
    FOREIGN KEY (obor_id) REFERENCES Obor(obor_id),
    FOREIGN KEY (trida_id) REFERENCES Trida(trida_id)
);

CREATE TABLE Dochazka (
    dochazka_id int PRIMARY KEY AUTO_INCREMENT,
    datum_zapisu date,
    zak_id int  NOT NULL,
    predmet_id int  NOT NULL,
    FOREIGN KEY (zak_id) REFERENCES Zak(zak_id),
    FOREIGN KEY (predmet_id) REFERENCES Predmet(predmet_id)
);

