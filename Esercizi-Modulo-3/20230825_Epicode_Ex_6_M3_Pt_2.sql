create database esercizio_6_m3_pt_2;

use esercizio_6_m3_pt_2;

/*

Studente(matricola_studente,nome_studente,anno_laurea,titolo_studio,voto_laurea)
Dipartimento(codice_dipartimento,nome_dipartimento,settore_scientifico,numero_docenti)
Concorso_Master(codice_master,codice_dipartimento,data_pubblicazione,data_scadenza,numero_posti_disponibili)
Partecipa_Concorso_Master(codice_dipartimento,codice_master,matricola_studente,data_invio_domanda)

*/

-- Query 1

select Studente.matricola_studente, Studente.nome_studente, Dipartimento.settore_scientifico
from Studente
inner join Partecipa_Concorso_Master as PCM on Studente.matricola_studente=PCM.matricola_studente
inner join Dipartimento on PCM.codice_dipartimento=Dipartimento.codice_dipartimento
group by Studente.matricola_studente, Studente.nome_studente
having count(PCM.data_invio_domanda)=3
order by Studente.nome_studente;

-- Alternativa

select Studente.matricola_studente, Studente.nome_studente, Dipartimento.settore_scientifico
from Studente,Dipartimento,Partecipa_Corso_Master
WHERE Studente.matricola_studente=Partecipa_Concorso_Master.matricola_studente AND Dipartimento.codice_dipartimento=Partecipa_Concorso_Master.codice_dipartimento
group by Studente.matricola_studente,Studente.nome_studente
having count(Partecipa_Concorso_Master.codice_master)=3
order by Studente.nome_studente;

-- Query 2

select Dipartimento.nome_dipartimento, Dipartimento.settore_scientifico, count(Concorso_Master.codice_master)
from Dipartimento
inner join Concorso_Master on Dipartimento.codice_dipartimento=Concorso_Master.codice_dipartimento
where Dipartimento.codice_dipartimento not in (select Concorso_Master.codice_dipartimento
                                               from Concorso_Master
                                               where Concorso_Master.numero_posti_disponibili<=7)
group by Dipartimento.nome_dipartimento, Dipartimento.settore_scientifico;

-- Query 3 TO BE REVIEWED

select S.matricola_studente, S.nome_studente
from Studente as S
inner join Partecipa_Concorso_Master as PCM1 on S.matricola_studente=PCM1.matricola_studente
inner join Partecipa_Concorso_Master as PCM2 on PCM1.Matricola_studente=PCM2.matricola_studente
inner join Concorso_Master as CM1 on PCM2.cod_master=CM1.cod_master
inner join Concorso_Master as CM2 on CM1.cod_master=CM2.cod_master
 where S.voto_laurea>100
  and CM1.data_pubblicazione=CM2.data_pubblicazione
  and PCM1.cod_master>PCM2.cod_master
group by S.matricola_studente, S.nome_studente
having count(distinct Partecipa_Concorso_Master.data_invio_domanda)>=2;