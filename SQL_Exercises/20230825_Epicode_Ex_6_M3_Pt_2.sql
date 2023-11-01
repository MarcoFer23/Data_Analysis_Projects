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

-- Query 3 ( Reviewed )

SELECT S.matricola_studente, S.nome_studente
FROM Studente as S
JOIN Partecipa_Concorso_Master as PCM on PCM.matricola_studente=S.matricola_studente
JOIN Concorso_Master as CM on CM.codice_master=PCM.codice_master
WHERE S.voto_laurea>100
GROUP BY S.matricola_studente, S.nome_studente
HAVING COUNT(CM.codice_master)>=2 AND COUNT(DISTINCT CM.data_pubblicazione)<COUNT(CM.codice_master);