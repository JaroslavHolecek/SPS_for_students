INSERT INTO 2023EP_Mesto (nazev) VALUES
('Praha'),
('Brno'),
('Ostrava');

INSERT INTO 2023EP_Clovek (jmeno, mestoNarozeni_id) VALUES
('Alice', 1 ), -- Zde bych musel znát id města - což obvykle neznám a ani mě nezajímá, jaké konkrétní id má konkrétní město
('Bob', (SELECT id FROM 2023EP_Mesto WHERE nazev = 'Brno') ),
('Charlie', (SELECT id FROM 2023EP_Mesto WHERE nazev = 'Ostrava') );

INSERT INTO 2023EP_Pozice (nazev, ma_smlouvu) VALUES
('Učitel', TRUE),
('Vedoucí kroužku', FALSE),
('Správce', TRUE);

INSERT INTO 2023EP_Pozice_ve_skole (clovek_id, pozice_id, od, do) VALUES
(   (SELECT id FROM 2023EP_Clovek WHERE jmeno = 'Alice'),
    (SELECT id FROM 2023EP_Pozice WHERE nazev = 'Učitel'), '2023-01-01', NULL
),
(   (SELECT id FROM 2023EP_Clovek WHERE jmeno = 'Bob'),
    (SELECT id FROM 2023EP_Pozice WHERE nazev = 'Vedoucí kroužku'), '2023-02-01', '2023-06-30'
),
(   (SELECT id FROM 2023EP_Clovek WHERE jmeno = 'Charlie'),
    (SELECT id FROM 2023EP_Pozice WHERE nazev = 'Správce'), '2023-03-01', NULL
);