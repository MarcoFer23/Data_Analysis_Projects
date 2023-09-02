/* 

Ho scelto di realizzare un database (semplificato) per una clinica veterinaria sita in Provincia di Roma,
che riceve e visita animali domestici di clienti residenti tra le Provincie di Roma, Latina e Frosinone.

Motivo della scelta: da amante degli animali, mi piacerebbe in futuro contribuire allo sviluppo digital
di una clinica veterinaria altamente specializzata, e ai fini dell'esercizio ho pensato di sviluppare
un database sufficientemente ricco di informazioni che potesse consentire interrogazioni mediante 
query SQL di diversa natura, operando su un totale di 6 tabelle.

Per facilitare la consultazione dei diagrammi realizzati per progettare il database, di seguito 
inserisco il link ai due grafici inseriti su Canva (con aggiunta del modello relazionale ottenuto
mediante Database > Reverse Engineer su MySQL Workbench nel secondo file).

Privilegi di accesso: Anyone with the link CAN COMMENT.

Link al Diagramma ER: https://www.canva.com/design/DAFtOKMyT0Q/r8T1lMh1EYaUbYYpuB2diQ/edit?utm_content=DAFtOKMyT0Q&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

Link al Modello Relazionale: https://www.canva.com/design/DAFtOGZ_HVk/snS4X5j3VIDuFRng4W0mcQ/edit?utm_content=DAFtOGZ_HVk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

*/

-- Creazione del database da utilizzare

create database esercizio_finale_m3;

use esercizio_finale_m3;

-- Creazione delle Tabelle

CREATE TABLE Città (
    ID_Città INT,
    Nome_Città VARCHAR(255) NOT NULL,
    Regione VARCHAR(255) NOT NULL,
    Provincia VARCHAR(255) NOT NULL,
		PRIMARY KEY (ID_Città)
);

CREATE TABLE Proprietario (
    ID_Proprietario INT,
    ID_Città INT,
    Nome_Completo VARCHAR(255) NOT NULL,
    Età INT NOT NULL,
    Indirizzo_Email VARCHAR(255) NOT NULL,
    Recapito_Telefonico VARCHAR(255) NOT NULL,
    Indirizzo VARCHAR(255) NOT NULL,
		PRIMARY KEY (ID_Proprietario),
			CONSTRAINT FK_ID_Città_Proprietario_Città FOREIGN KEY (ID_Città) REFERENCES Città(ID_Città)
);

CREATE TABLE Veterinario (
    ID_Veterinario INT,
    Nome_Veterinario VARCHAR(255) NOT NULL,
    Età INT NOT NULL,
    Data_Laurea DATE NOT NULL,
    Data_Assunzione DATE NOT NULL,
    Stipendio DECIMAL(10, 2) NOT NULL,
		PRIMARY KEY (ID_Veterinario)
);

CREATE TABLE Specie (
    ID_Specie INT,
    Nome_Specie VARCHAR(255) NOT NULL,
    Nome_Comune VARCHAR(255) NOT NULL,
    Genere VARCHAR(255) NOT NULL,
    Famiglia VARCHAR(255) NOT NULL,
    Phylum VARCHAR(255) NOT NULL,
		PRIMARY KEY (ID_Specie)
);

CREATE TABLE Animale_Domestico (
    ID_Animale INT ,
    ID_Proprietario INT,
    ID_Specie INT,
    Nome_Animale VARCHAR(255) NOT NULL,
    Data_Nascita DATE NOT NULL,
    Sterilizzato ENUM("Sì","No") NOT NULL,
    Peso_kg DECIMAL(5, 2) NOT NULL,
		PRIMARY KEY (ID_Animale),
			CONSTRAINT FK_ID_Proprietario_Animale_Domestico_Proprietario FOREIGN KEY (ID_Proprietario) REFERENCES Proprietario(ID_Proprietario),
			CONSTRAINT FR_ID_Specie_Animale_Domestico_Specie FOREIGN KEY (ID_Specie) REFERENCES Specie(ID_Specie)
);


CREATE TABLE Visita (
    ID_Visita INT UNIQUE NOT NULL,
    ID_Animale INT,
    ID_Veterinario INT NOT NULL,
    Data_Visita DATETIME,
		PRIMARY KEY (ID_Animale, Data_Visita),
			CONSTRAINT FK_ID_Animale_Visita_Animale_Domestico FOREIGN KEY (ID_Animale) REFERENCES Animale_Domestico(ID_Animale),
			CONSTRAINT FK_ID_Veterinario_Visita_Veterinario FOREIGN KEY (ID_Veterinario) REFERENCES Veterinario(ID_Veterinario)
);

-- Inserimento dei valori nelle tabelle

INSERT INTO Città (ID_Città, Nome_Città, Regione, Provincia)
VALUES
	(1, 'Albano Laziale', 'Lazio', 'RM'),
	(2, 'Artena', 'Lazio', 'RM'),
	(3, 'Bassiano', 'Lazio', 'LT'),
	(4, 'Carpineto Romano', 'Lazio', 'RM'),
	(5, 'Cori', 'Lazio', 'LT'),
	(6, 'Ferentino', 'Lazio', 'FR'),
	(7, 'Frosinone', 'Lazio', 'FR'),
	(8, 'Isola dei Liri', 'Lazio', 'FR'),
	(9, 'Latina', 'Lazio', 'LT'),
	(10, 'Nemi', 'Lazio', 'RM'),
	(11, 'Norma', 'Lazio', 'LT'),
	(12, 'Rocca Massima', 'Lazio', 'LT'),
	(13, 'Roccasecca', 'Lazio', 'FR'),
	(14, 'Roma', 'Lazio', 'RM'),
	(15, 'Sermoneta', 'Lazio', 'LT');


INSERT INTO Proprietario (ID_Proprietario, ID_Città, Nome_Completo, Età, Indirizzo_Email, Recapito_Telefonico, Indirizzo)
VALUES
	(1,11,'Marco Rossi',31, 'marco.rossi@gmail.com', '3514620460', 'Via del Boschetto, 14'),
	(2,6,'Laura Bianchi',24,'laura.bianchi@outlook.it','3469876543','Vicolo dei Pini, 56'),
	(3,7,'Simone Ricci',42,'simone.ricci@yahoo.com','3345678901','Piazza del Sole, 89'),
	(4,8,'Anna Martini',19,'anna.martini@gmail.com','3502345678','Corso delle Rose, 34'),
	(5,13,'Luca Ferrari',38,'luca.ferrari@libero.it','3478765432','Largo dei Ciliegi, 72'),
	(6,3,'Giulia Russo',22,'giulia.russo@yahoo.com','3514567890','Viale delle Palme, 45'),
	(7,5,'Paolo Conti',33,'paolo.conti@gmail.com','3463456789','Via delle Viole, 17'),
	(8,9,'Sara Santoro',41,'sara.santoro@outlook.it','3347890123','Piazza della Luna, 98'),
	(9,11,'Davide Romano',27,'davide.romano@gmail.com','3505678901','Vicolo delle Orchidee, 21'),
	(10,12,'Valentina Gatti',20,'valentina.gatti@yahoo.com','3476789012','Corso dei Gigli, 63'),
	(11,15,'Antonio Moretti',36,'antonio.moretti@libero.it','3512345678','Largo delle Azalee, 37'),
	(12,1,'Francesca De Luca',29,'francesca.deluca@gmail.com','3468901234','Viale dei Papaveri, 81'),
	(13,2,'Lorenzo Barbieri',43,'lorenzo.barbieri@outlook.it','3346789012','Via delle Mimose, 29'),
	(14,4,'Marta Ferri',25,'marta.ferri@yahoo.com','3501234567','Piazza delle Stelle, 52'),
	(15,10,'Giovanni Marchetti',31,'giovanni.marchetti@gmail.com','3472345678','Corso delle Tulipani, 76'),
	(16,14,'Elena Rizzo',40,'elena.rizzo@libero.it','3515678901','Largo dei Girasoli, 42'),
	(17,1,'Andrea Lombardi',21,'andrea.lombardi@gmail.com','3464567890','Vicolo dei Narcisi, 15'),
	(18,2,'Roberta Colombo',37,'roberta.colombo@outlook.it','3342345678','Viale delle Ortensie, 69'),
	(19,4,'Michele Monti',28,'michele.monti@yahoo.com','3507890123','Via dei Rododendri, 23'),
	(20,10,'Claudia Villa',44,'claudia.villa@gmail.com','3477890123','Piazza dei Fiori, 58'),
	(21,14,'Fabio Ferrara',23,'fabio.ferrara@libero.it','3516789012','Corso delle Camelie, 31'),
	(22,3,'Giorgia Pellegrini',34,'giorgia.pellegrini@gmail.com','3465678901','Largo delle Peonie, 74'),
	(23,5,'Alessandro Rossetti',18,'alessandro.rossetti@yahoo.com','3341234567','Vicolo dei Lillà, 67'),
	(24,9,'Eleonora Galli',35,'eleonora.galli@outlook.it','3508901234','Via delle Azalee, 38'),
	(25,11,'Nicolas Russo',26,'nicolas.russo@gmail.com','3473456789','Piazza delle Margherite, 91');

INSERT INTO Veterinario (ID_Veterinario, Nome_Veterinario, Età, Data_Laurea, Data_Assunzione, Stipendio)
VALUES
	(1,'Mario Bianchi',35,'2015-06-15','2016-03-20',50000),
	(2,'Laura Bonicalzi',28,'2022-09-10','2023-07-12',45000),
	(3,'Luca Marini',42,'2009-03-25','2010-11-08',55000),
	(4,'Giulia De Benedettis',31,'2014-11-30','2016-02-14',48000),
	(5,'Andrea Morosini',37,'2013-07-18','2015-05-01',52000),
	(6,'Sofia Cangemi',29,'2018-05-22','2019-09-03',47000),
	(7,'Marco Tamberi',45,'2008-09-05','2011-04-19',58000),
	(8,'Elena Sorrentini',33,'2014-12-10','2016-08-26',49000),
	(9,'Alessio Trentini',39,'2009-04-03','2011-10-15',53000),
	(10,'Serena Prati',27,'2018-08-14','2022-06-07',46000);
   
INSERT INTO Specie (ID_Specie, Nome_Specie, Nome_Comune, Genere, Famiglia, Phylum)
VALUES
	(1, 'Canis lupus familiaris', 'Cane', 'Canis', 'Canidae', 'Chordata'),
	(2, 'Felis catus', 'Gatto', 'Felis', 'Felidae', 'Chordata'),
	(3, 'Oryctolagus cuniculus', 'Coniglio', 'Oryctolagus', 'Leporidae', 'Chordata'),
	(4, 'Cricetus cricetus', 'Criceto europeo', 'Cricetus', 'Cricetidae', 'Chordata'),
	(5, 'Melopsittacus undulatus', 'Pappagallo ondulato', 'Melopsittacus', 'Psittacidae', 'Chordata'),
	(6, 'Testudo graeca', 'Tartaruga greca', 'Testudo', 'Testudinidae', 'Chordata'),
	(7, 'Canis familiaris', 'Cane', 'Canis', 'Canidae', 'Chordata'),
	(8, 'Felis domesticus', 'Gatto', 'Felis', 'Felidae', 'Chordata'),
	(9, 'Lepus europaeus', 'Lepre europea', 'Lepus', 'Leporidae', 'Chordata'),
	(10, 'Phodopus sungorus', 'Criceto nano russo', 'Phodopus', 'Cricetidae', 'Chordata');

INSERT INTO Animale_Domestico (ID_Animale, ID_Proprietario, ID_Specie, Nome_Animale, Data_Nascita, Sterilizzato, Peso_kg)
VALUES
	(1,23,7,'Fido','2019-05-15','Sì',12.5),
	(2,4,3,'Whiskers','2020-02-10','No',4.2),
	(3,10,9,'Buddy','2018-08-20','Sì',9.0),
	(4,17,2,'Mittens','2021-04-03','No',3.8),
	(5,6,8,'Luna','2019-11-25','No',5.6),
	(6,21,4,'Rocky','2020-07-12','Sì',15.2),
	(7,2,6,'Charlie','2017-09-08','No',7.9),
	(8,14,1,'Daisy','2018-01-19','No',6.4),
	(9,25,5,'Max','2020-06-30','Sì',8.7),
	(10,9,10,'Lucy','2019-03-04','No',11.3),
	(11,19,3,'Oliver','2020-11-14','Sì',4.5),
	(12,12,7,'Bella','2018-12-27','No',5.9),
	(13,1,2,'Leo','2019-08-05','Sì',10.1),
	(14,15,9,'Lola','2017-07-01','No',8.0),
	(15,7,8,'Oscar','2020-09-22','Sì',6.7),
	(16,22,1,'Molly','2019-02-17','No',3.3),
	(17,24,4,'Rosie','2021-01-08','No',9.8),
	(18,11,5,'Charlie','2018-04-12','Sì',12.6),
	(19,18,10,'Sophie','2020-03-27','Sì',7.1),
	(20,5,6,'Lucky','2019-06-09','No',14.0),
	(21,16,7,'Milo','2018-10-31','Sì',9.4),
	(22,8,3,'Zoe','2017-12-15','No',5.2),
	(23,3,2,'Chloe','2020-08-02','No',6.8),
	(24,13,8,'Coco','2019-04-19','Sì',7.7),
	(25,20,9,'Simba','2018-03-08','Sì',10.9),
	(26,20,1,'Ruby','2020-10-27','No',8.5),
	(27,13,4,'Harley','2019-07-13','Sì',11.7),
	(28,3,10,'Mia','2018-05-28','No',4.0),
	(29,8,6,'Zeus','2017-06-04','Sì',13.2),
	(30,16,5,'Lily','2019-09-16','No',7.3);

INSERT INTO Visita (ID_Visita, ID_Animale, ID_Veterinario, Data_Visita)
VALUES
	(1,13,7,'2023-01-15 08:30:00'),
	(2,7,3,'2023-02-20 10:45:00'),
	(3,23,9,'2023-03-25 14:15:00'),
	(4,28,5,'2023-04-10 09:00:00'),
	(5,2,1,'2023-05-05 11:30:00'),
	(6,20,8,'2023-06-12 16:20:00'),
	(7,5,4,'2023-07-19 13:00:00'),
	(8,15,6,'2023-08-08 17:45:00'),
	(9,29,2,'2023-09-14 10:00:00'),
	(10,22,10,'2023-10-21 12:30:00'),
	(11,2,2,'2023-11-26 15:15:00'),
	(12,19,6,'2023-12-02 08:00:00'),
	(13,9,4,'2023-04-05 09:30:00'),
	(14,6,8,'2023-05-10 11:10:00'),
	(15,23,1,'2023-06-15 14:50:00'),
	(16,15,5,'2023-07-20 16:25:00'),
	(17,26,9,'2023-08-25 18:40:00'),
	(18,11,3,'2023-09-30 07:15:00'),
	(19,17,7,'2023-10-06 10:20:00'),
	(20,4,7,'2023-11-11 13:55:00'),
	(21,16,8,'2023-12-16 15:05:00'),
	(22,6,4,'2023-02-22 09:25:00'),
	(23,25,2,'2023-03-30 11:40:00'),
	(24,26,7,'2023-04-14 14:00:00'),
	(25,11,10,'2023-05-19 16:10:00');
    
-- Query per interrogare il database creato { non in ordine di difficoltà crescente }

-- Query 1: Visualizzare l'ID, il nome e l'età dell'animale, insieme al nome del proprietario; ordinare per età dell'animale in ordine decrescente.

select Animale_Domestico.ID_Animale, Animale_Domestico.Nome_Animale, year(now())-year(Animale_Domestico.Data_Nascita) as Età_Animale, Proprietario.Nome_Completo as Nome_Proprietario
from Animale_Domestico
inner join Proprietario on Animale_Domestico.ID_Proprietario=Proprietario.ID_Proprietario
order by Età_Animale DESC;

-- Query 2: Visualizzare mediante una vista il nome e lo stipendio del veterinario dallo stipendio più alto. 

create view Veterinario_Massimo_Stipendio (Nome_Veterinario, Stipendio) as
select Nome_Veterinario, Stipendio
from Veterinario
where Stipendio = (select MAX(Stipendio) from Veterinario);

-- Query 3: Visualizzare l'ID e il nome dell'animale insieme al nome, al genere e al nome comune della specie di tutti quelli animali il cui genere non corrisponde a Canis e Felis.

select Animale_Domestico.ID_Animale, Animale_Domestico.Nome_Animale, Specie.Nome_Specie, Specie.Genere, Specie.Nome_Comune
from Animale_Domestico
inner join Specie on Animale_Domestico.ID_Specie=Specie.ID_Specie
where Specie.Genere not in ('Canis','Felis')
order by Animale_Domestico.ID_Animale;

-- Query 4: Visualizzare l'ID, il nome, la data di nascita e il nome del proprietario degli animali domestici che appartengono a persone il cui nome inizia per M.

select Animale_Domestico.ID_Animale, Animale_Domestico.Nome_Animale, Animale_Domestico.Data_Nascita, Proprietario.Nome_Completo
from Animale_Domestico
inner join Proprietario on Animale_Domestico.ID_Proprietario=Proprietario.ID_Proprietario
where Proprietario.Nome_Completo like 'M%'
order by Animale_Domestico.ID_Animale;

-- Query 5: Query 5: Visualizzare il nome del proprietario, l'ID del proprietario e la provincia di appartenenza di tutti i proprietari di animali non residenti in provincia di Latina.

select Proprietario.Nome_Completo, Proprietario.ID_Proprietario, Città.Provincia
from Proprietario
inner join Città on Città.ID_Città=Proprietario.ID_Città
where not Città.Provincia = 'LT'
order by Proprietario.Nome_Completo;

-- Query 6: Visualizzare per ogni città il numero totale di animali domestici presenti; ordinare per il totale di animali domestici presenti in ordine decrescente, e per nome città in ordine alfabetico dalla A alla Z.

select Città.Nome_Città, count(Animale_Domestico.ID_Animale) as Totale_Animali_Presenti
from Città
inner join Proprietario on Città.ID_Città=Proprietario.ID_Città
inner join Animale_Domestico on Proprietario.ID_Proprietario=Animale_Domestico.ID_Proprietario
group by Città.Nome_Città
order by Totale_Animali_Presenti desc, Città.Nome_Città;

-- Query 7: Visualizzare l'ID, il nome, l'indirizzo email e il recapito telefonico di tutti i clienti che vivono a Bassiano.

select ID_Proprietario, Nome_Completo, Indirizzo_Email, Recapito_Telefonico
from Proprietario
where ID_Città = (select ID_Città from Città where Nome_Città = 'Bassiano');

-- Query 8: Visualizzare l'ID, il nome, l'indirizzo email e il recapito telefonico, più la città di residenza, di tutti i clienti che risiedono nella Provincia di Latina: Ordinare dalla A alla Z per il nome del proprietario.

select Proprietario.ID_Proprietario, Proprietario.Nome_Completo, Proprietario.Indirizzo_Email, Proprietario.Recapito_Telefonico, Città.Nome_Città
from Proprietario
inner join Città ON Proprietario.ID_Città=Città.ID_Città
where Provincia = 'LT'
order by Proprietario.Nome_Completo;

-- Query 9: Visualizzare per ogni veterinario l'ID, il nome, gli anni di esperienza (dalla data della laurea), lo stipendio e il numero di visite effettuate nell'anno corrente. Ordinare dalla A alla Z per nome veterinario.

select Veterinario.ID_Veterinario, Veterinario.Nome_Veterinario, year(now())-year(Veterinario.Data_Laurea) as Anni_di_Esperienza ,Veterinario.Stipendio, count(Visita.Data_Visita) as Totale_Visite_2023
from Veterinario
inner join Visita ON Veterinario.ID_Veterinario = Visita.ID_Veterinario
group by Veterinario.ID_Veterinario
order by Veterinario.Nome_Veterinario;

-- Query 10: Per ogni veterinario visualizzare il nome completo e il numero di visite effettuate nell'anno corrente; ordinare in ordine alfabetico.

select Veterinario.Nome_Veterinario, count(Visita.Data_Visita) as Totale_Visite_2023
from Veterinario
join Visita ON Veterinario.ID_Veterinario = Visita.ID_Veterinario
group by Veterinario.Nome_Veterinario
order by Veterinario.Nome_Veterinario;

/* 
Dato che per praticità vi sono solo riferimenti a visite del 2023, non c'è necessità di utilizzare delle condizionali tramite WHERE o HAVING (a seconda dei casi).
Grazie mille per essere arrivato fin qui Simone e per l'aiuto che ci dai praticamente tutti i giorni :-) 
Per ringraziarti ti lascio un piccolo "Easter Egg", dato che hai apprezzato i The Algorithm. A presto e buon fine settimana! 
https://www.youtube.com/watch?v=i74eZ2N_lB4 
*/