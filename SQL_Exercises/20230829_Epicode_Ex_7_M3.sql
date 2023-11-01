create database esercizio_7_m3;

use esercizio_7_m3;


CREATE TABLE Dipendente (
    id INT PRIMARY KEY,
    nome VARCHAR(255),
    cognome VARCHAR(255),
    email VARCHAR(255),
    numerotelefono VARCHAR(20),
    data_assunzione DATE,
    id_lavoro INT,
    salario DECIMAL(10, 2),
    id_manager INT,
    id_dipartimento INT
);

INSERT INTO Dipendente (id, nome, cognome, email, numerotelefono, data_assunzione, id_lavoro, salario, id_manager, id_dipartimento)
VALUES
    (1, 'Mario', 'Rossi', 'mario.rossi@email.com', '1234567890', '2023-01-15', 1, 50000.00, 4, 1),
    (2, 'Luca', 'Bianchi', 'luca.bianchi@email.com', '9876543210', '2023-02-20', 2, 55000.00, 4, 2),
    (3, 'Anna', 'Verdi', 'anna.verdi@email.com', '5678901234', '2023-06-10', 1, 48000.00, 5, 1),
    (4, 'Giovanna', 'Marrone', 'giovanna.marrone@email.com', '6789012345', '2015-12-01', 3, 60000.00, 4, 2),
    (5, 'Paolo', 'Giallo', 'paolo.giallo@email.com', '3456789012', '2022-09-05', 2, 52000.00, 5, 3),
    (6, 'Roberto', 'Neri', 'roberto.neri@email.com', '1231231234', '2022-05-15', 2, 49000.00, 5, 2),
    (7, 'Giulia', 'Bianchi', 'giulia.bianchi@email.com', '4564564567', '2022-08-12', 1, 55000.00, 3, 3),
    (8, 'Elena', 'Verdi', 'elena.verdi@email.com', '7897897890', '2022-07-10', 3, 60000.00, 4, 1),
    (9, 'Massimo', 'Giallo', 'massimo.giallo@email.com', '2342342345', '2022-09-20', 1, 48000.00, 5, 2),
    (10, 'Laura', 'Rosa', 'laura.rosa@email.com', '3453453456', '2022-03-05', 2, 52000.00, 6, 3),
    (11, 'Simone', 'Marrone', 'simone.marrone@email.com', '5675675678', '2022-11-18', 1, 49000.00, 5, 1),
    (12, 'Francesca', 'Rossi', 'francesca.rossi@email.com', '7897897890', '2022-10-02', 3, 57000.00, 4, 2),
    (13, 'Marco', 'Neri', 'marco.neri@email.com', '1231231234', '2022-06-25', 2, 52000.00, 6, 3),
    (14, 'Sara', 'Verdi', 'sara.verdi@email.com', '2342342345', '2022-04-15', 1, 46000.00, 3, 1),
    (15, 'Davide', 'Giallo', 'davide.giallo@email.com', '4564564567', '2022-12-28', 2, 49000.00, 4, 2);

CREATE TABLE Dipartimento (
    id_dipartimento INT PRIMARY KEY,
    nome_dip VARCHAR(255),
    id_manager INT,
    id_location INT
);

INSERT INTO Dipartimento (id_dipartimento, nome_dip, id_manager, id_location)
VALUES
    (1, 'Amministrazione', 4, 101),
    (2, 'Vendite', 5, 102),
    (3, 'Produzione', 6, 103);


-- Query 1

/* Visualizzare la data di assunzione dei manager e i loro id appartenenti al dipartimento ‘Amministrazione’ nel formato Nome mese, giorno, anno
(Diverse soluzioni possibili) */

select date_format(Dipendente.data_assunzione, '%M %d %y') as data_assunzione, Dipendente.id
from Dipendente
inner join Dipartimento on Dipendente.id=Dipartimento.id_manager
where Dipartimento.nome_dip='Amministrazione';

select date_format(Dipendente.data_assunzione, '%M %d %y') as data_assunzione, Dipendente.id
from Dipendente
where Dipendente.id in (select Dipartimento.id_manager
from Dipartimento
where Dipartimento.nome_dip='Amministrazione');

-- Query 2

/* Visualizzare il nome e il cognome dei dipendenti assunti nel mese di Giugno
(Diverse soluzioni possibili) */

select Dipendente.nome, Dipendente.cognome, Dipendente.data_assunzione
from Dipendente
where month(data_assunzione)=6;

select Dipendente.nome, Dipendente.cognome, Dipendente.data_assunzione
from Dipendente
where monthname(data_assunzione)='June';

-- Query 3

-- Visualizzare gli anni in cui più di 10 dipendenti sono stati assunti

select year(Dipendente.data_assunzione) as Data_Assunzione
from Dipendente
group by year(Dipendente.data_assunzione)
having count(*)>10;

-- Query 4

/* Visualizzare il nome del dipartimento, il nome del manager, il salario del manager di tutti i manager la cui esperienza è maggiore di 5 anni
(Diverse soluzioni possibili) */

select Dipartimento.nome_dip, concat(Dipendente.nome,' ',Dipendente.cognome), Dipendente.salario
from Dipartimento, Dipendente
where Dipartimento.id_manager=Dipendente.id
and datediff(now(),Dipendente.data_assunzione)>1825;

select Dipartimento.nome_dip, concat(Dipendente.nome,' ',Dipendente.cognome), Dipendente.salario
from Dipartimento, Dipendente
where Dipartimento.id_manager=Dipendente.id
and year(now())-year(Dipendente.data_assunzione)>5;

select Dipartimento.nome_dip, concat(Dipendente.nome,' ',Dipendente.cognome), Dipendente.salario
from Dipartimento
inner join Dipendente on Dipartimento.id_manager=Dipendente.id
where datediff(now(),Dipendente.data_assunzione)>1825;

select Dipartimento.nome_dip, concat(Dipendente.nome,' ',Dipendente.cognome), Dipendente.salario
from Dipartimento
inner join Dipendente on Dipartimento.id_manager=Dipendente.id
where year(now())-year(Dipendente.data_assunzione)>5;