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

CREATE UNIQUE INDEX index_docente
ON Docente (matricola_docente,nome_docente);

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

CREATE UNIQUE INDEX index_esame
ON Esame (codice_corso,matricola_studente);