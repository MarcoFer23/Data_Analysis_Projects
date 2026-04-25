create database esercizio_5_m3_pt_2;

use esercizio_5_m3_pt_2;

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

select Studente.nome_studente, Studente.matricola_studente, Corso.nome_corso, Esame.data_esame, Esame.voto_esame, Docente.nome_docente
from Studente
inner join Esame on Studente.matricola_studente=Esame.matricola_studente
inner join Corso on Esame.codice_corso=Corso.codice_corso
inner join Docente on Corso.matricola_docente=Docente.matricola_docente
where Esame.voto_esame>28;

select Docente.nome_docente, Corso.nome_corso, Esame.settore_scientifico
from Docente
inner join Corso on Docente.matricola_docente=Corso.matricola_docente
inner join Esame on Corso.codice_corso=Esame.codice_corso;