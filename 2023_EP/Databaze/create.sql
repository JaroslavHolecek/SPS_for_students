CREATE TABLE 2023EP_Mesto (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nazev CHAR(10) NOT NULL UNIQUE    
);

CREATE TABLE 2023EP_Clovek (
	id INT PRIMARY KEY AUTO_INCREMENT,
    jmeno CHAR(10) NOT NULL,
    mestoNarozeni_id INT,
    FOREIGN KEY (mestoNarozeni_id) REFERENCES 2023EP_Mesto(id)
);

CREATE TABLE 2023EP_Pozice (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nazev CHAR(20) NOT NULL UNIQUE,
    ma_smlouvu BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE 2023EP_Pozice_ve_skole (
    id INT PRIMARY KEY AUTO_INCREMENT,
    clovek_id INT,
    pozice_id INT,
    od DATE NOT NULL,
    do DATE,
    CONSTRAINT uc_clovek_pozice UNIQUE (clovek_id, pozice_id, od),
    FOREIGN KEY (clovek_id) REFERENCES 2023EP_Clovek(id),
    FOREIGN KEY (pozice_id) REFERENCES 2023EP_Pozice(id)
);