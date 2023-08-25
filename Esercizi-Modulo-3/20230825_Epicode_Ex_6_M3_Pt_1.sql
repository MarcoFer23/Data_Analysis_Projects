create database esercizio_6_m3_pt_1;


use esercizio_6_m3_pt_1;


create table Studente (
    matricola_studente varchar(255),
    nome_studente varchar(255),
    città_studente varchar(255),
        primary key (matricola_studente)
);

create table Docente (
    matricola_docente varchar(255),
    nome_docente varchar(255),
        primary key (matricola_docente,nome_docente)
);

create table Corso (
    codice_corso varchar(255),
    nome_corso varchar(255),
    matricola_docente varchar(255),
primary key (codice_corso),
constraint fk_matricola_docente_Corso_Docente foreign key (matricola_docente) references Docente(matricola_docente) on update cascade on delete no action
);

create table Esame (
    codice_corso varchar(255),
    matricola_studente varchar(255),
    data_esame date,
    voto_esame tinyint unsigned,
    settore_scientifico varchar(255),
    primary key (codice_corso,matricola_studente),
    constraint fk_codice_corso_Esame_Corso foreign key (codice_corso) references Corso(codice_corso) on update cascade on delete no action,
    constraint fk_matricola_studente_Esame_Studente foreign key (matricola_studente) references Studente(matricola_studente) on update cascade on delete no action
);

-- Query 1

select Studente.matricola_studente, Studente.nome_studente, max(Esame.voto_esame), min(Esame.voto_esame), avg(Esame.voto_esame) 
from Studente
inner join Esame on Studente.matricola_studente=Esame.matricola_studente
group by Studente.matricola_studente, Studente.nome_studente;

-- Query 2 

select Studente.matricola_studente, Studente.nome_studente, max(Esame.voto_esame), min(Esame.voto_esame), avg(Esame.voto_esame) as avg_voto_esame
from Studente
inner join Esame on Studente.matricola_studente=Esame.matricola_studente
group by Studente.matricola_studente, Studente.nome_studente
having avg(Esame.voto_esame)>25 and count(distinct Esame.data_esame)>=10
order by avg_voto desc;

-- Buon weekend Simone, e grazie come sempre! :-) 