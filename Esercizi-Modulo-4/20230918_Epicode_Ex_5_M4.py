"""
Domanda 1:
Abbiamo una lista di numeri:

numeri = [4, 10, 50, 100, 128, 71, 46]

creare una nuova lista i cui elementi siano gli stessi di numeri incrementati di 10, mediante comprehension.
"""

numeri = [4, 10, 50, 100, 128, 71, 46]
numeri_aumentati_10 = [num + 10 for num in numeri ]

print(numeri_aumentati_10)

"""
Domanda 2: 
Abbiamo una lista di numeri:

numeri = [4, 10, 50, 100, 128, 71, 46]

creare una nuova lista i cui elementi siano gli stessi di numeri ma raddoppiati, mediante comprehension.
"""

numeri = [4, 10, 50, 100, 128, 71, 46]
numeri_raddoppiati = [num*2 for num in numeri]

print(numeri_raddoppiati)

"""
Domanda 3:
Abbiamo una lista di nomi:

nomi = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]

creare una nuova lista i cui elementi siano le iniziali dei nomi, mediante comprehension.
"""

nomi = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
iniziali_nomi = [nome[0] for nome in nomi]

print(iniziali_nomi)

"""
Domanda 4: 
Abbiamo una lista di nomi:

nomi = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]

creare una nuova lista i cui elementi siano le iniziali dei nomi seguite da punto, mediante comprehension.
"""

nomi = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
iniziali_nomi = [nome[0] + "." for nome in nomi]

print(iniziali_nomi)

"""
Domanda 5:
Abbiamo una lista di codici fiscali:

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]

Creare una lista che contenga (per ogni CF) solo i caratteri relativi al nome, mediante comprehension.
"""

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]
lista_caratteri_nome = [cf[3:6] for cf in lista_cf]

print(lista_caratteri_nome)

"""
Domanda 6:
Abbiamo una lista di codici fiscali:

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]

Creare due liste, una che contenga (per ogni CF) solo i caratteri relativi al nome, e una che contenga (per ogni CF) solo i caratteri relativi al cognome; entrambe mediante comprehension.
"""

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]
lista_caratteri_nome = [cf[3:6] for cf in lista_cf]
lista_caratteri_cognome = [cf[0:3] for cf in lista_cf]

print(lista_caratteri_nome, lista_caratteri_cognome)

"""
Domanda 7:
Abbiamo una lista di codici fiscali:

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]

Creare una lista che contenga solo i codici fiscali dei nati nel '95, tramite comprehension
"""

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]
lista_nati_95 = [cf for cf in lista_cf if cf[6:8] == "95"]

print(lista_nati_95)

"""
Domanda 8:
Abbiamo una lista di codici fiscali:

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]

Creare una lista che contenga gli ultimi cinque caratteri dei soli codici fiscali di persone nate nel '95, tramite comprehension
"""

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]
lista_nati_95 = [cf[-5:] for cf in lista_cf if cf[6:8] == "95"]

print(lista_nati_95)

"""
Domanda 9:
Abbiamo una lista di stringhe di prezzi in dollari, che erroneamente sono stati scritti con il simbolo dell'euro:

prezzi = ["100 €", "200 €", "500 €", "10 €", "50 €", "70 €"]

cambiare il simbolo dell'euro (€) in quello del dollaro ($) per ogni stringa nella lista, usando la comprehension.
"""

prezzi = ["100 €", "200 €", "500 €", "10 €", "50 €", "70 €"]
prezzi_dollaro = [prezzo.replace("€", "$") for prezzo in prezzi]

print(prezzi_dollaro)

"""
Domanda 10:
Abbiamo una lista di studenti:

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"]

vogliamo dividere gli studenti in due squadre per un campionato di Uno nel seguente modo: la prima metà per un squadra, e la seconda metà per l'altra.
Creiamo due liste per ogni squadra, e alla fine visualizziamole.
"""

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"]

studenti_squadra_1 = [studente for studente in studenti[0:int(len(studenti)/2)]]
studenti_squadra_2 = [studente for studente in studenti[int(len(studenti)/2):]]

print(studenti_squadra_1,studenti_squadra_2)

"""
Domanda 11:
Abbiamo una lista di studenti:

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"]

vogliamo dividere gli studenti in due squadre per un campionato di Uno nel seguente modo: 
selezioneremo i nomi in posizione pari per un squadra, e i nomi in posizione dispari per l'altra.

Creiamo due liste per ogni squadra, e alla fine visualizziamole.
"""

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"]

studenti_squadra_1 = [studente for studente in studenti if studenti.index(studente) % 2 == 0]
studenti_squadra_2 = [studente for studente in studenti if studenti.index(studente) % 2 == 1]

studenti_squadra_1 = [studente for studente in studenti[::2]]
studenti_squadra_2 = [studente for studente in studenti[1::2]]

print(studenti_squadra_1, studenti_squadra_2)

"""
Domanda 12:
Abbiamo una lista con i guadagni degli ultimi 12 mesi (supponiamo da Gennaio a Dicembre):

guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]

dobbiamo confrontare, stampando tutto a video, il guadagno di ogni mese con la media dei guadagni precedenti

Esempio di un possibile output:
Mese 1: 100 €
Mese 2: 90 € (media prec: 100 €)
Mese 3: 70 € (media prec: 95 €)
"""

guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]

print("Mese 1:", str(guadagni[0]))
print("".join(["Mese " + str(pos+1) +": " + str(guadagni[pos]) + " (media prec: " + str(sum(guadagni[:pos])//(pos)) + ")\n" for pos in range(1,len(guadagni))])) 

"""
Domanda 13:
Abbiamo una lista con i guadagni degli ultimi 12 mesi (supponiamo da Gennaio a Dicembre):

guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]

dobbiamo confrontare, stampando tutto a video, il guadagno di ogni mese con la media dei guadagni precedenti, 
e specificare nell'output se è maggiore o minore
"""

guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]

print("Mese 1:", str(guadagni[0]))
print("".join(["Mese " + str(pos+1) +": " + str(guadagni[pos]) + ", media prec: " + str(sum(guadagni[:pos])//(pos)) + " - siamo sopra la media\n"
                if (sum(guadagni[:pos])//(pos))>guadagni[pos] 
                else "Mese " + str(pos+1) +": " + str(guadagni[pos]) + ", media prec: " + str(sum(guadagni[:pos])//(pos)) + " - siamo sotto la media\n" 
                for pos in range(1,len(guadagni))]))

"""
Domanda 14:
Scrivere una funzione che, data una lista di numeri, fornisca in output il maggiore di tutti, senza utilizzare la funzione max()
"""

list = input("Inserire una lista di numeri interi separati da uno spazio:")
list = list.split(" ")

def max(list):
    max = 0
    for x in list:
        if int(x) > int(max): max = x
    return int(max)

print("Il valore massimo è: " + str(max(list)))

"""
Domanda 15:
Scrivere una funzione che, data una lista di numeri, fornisca in output il minimo e il massimo (possiamo usare o meno le funzioni min() e max())
"""

list = input("Inserire una lista di numeri interi separati da uno spazio:")
list = list.split(" ")

def max(list):
    max = 0
    for x in list:
        if int(x) > int(max): max = x
    return int(max)

def min(list):
    min = max(list)
    for x in list:
        if int(x) < int(min) : min = x
    return int(min)

print("Il valore minimo è: " + str(min(list)),"\nIl valore massimo è: " + str(max(list)))

"""
Domanda 16:
Scrivere una funzione che, data una lista di numeri, fornisca in output i due numeri più grandi
"""

numeri = input("Inserire una lista di numeri interi separati da uno spazio:")
numeri = numeri.split(" ") # .split() usa lo spazio come separatore per generare una lista di [sub]stringhe, sulla quale andrà ad operare la funzione

def due_n_maggiori(numeri):
   
    primo_maggiore = 0
    secondo_maggiore = 0
    
    for x in numeri:
        x = int(x)
        if x > primo_maggiore:
            secondo_maggiore = primo_maggiore
            primo_maggiore = x
        elif x > secondo_maggiore and x != primo_maggiore:
            secondo_maggiore = x
    
    return primo_maggiore, secondo_maggiore

risultato = due_n_maggiori(numeri)

if len(numeri) < 2:
    print("Hey, la lista deve contenere almeno due numeri!") 
else:
    print("I due numeri più grandi tra quelli digitati sono:", risultato)

"""
Domanda 17:
Scrivere una funzione che in input acquisisce una lista di numeri e un numero K; 
in output, dovrà restituire la media di tutti i numeri nella lista maggiori o uguali a K; 
se non ce ne dovesse essere nessuno, dovrà stampare a schermo un messaggio adeguato
"""

num = input("Inserire una lista di numeri interi separati da uno spazio:")
num = num.split(" ")
K = input("Inserire un numero intero K come parametro per avviare il calcolo:")

def controllo_K(num,K):
    numeri_magg_ug_K = [int(x) for x in num if x >= K]
    if len(numeri_magg_ug_K) > 0: # Se non ci dovessero essere numeri >= a K, la lista definita con comprehension non avrà elementi, e quindi .len() darà come risultato 0
        numeri_magg_ug_K = "La media dei numeri maggiori o uguali a K è: ", float(sum(numeri_magg_ug_K)/len(numeri_magg_ug_K))
    else:
        numeri_magg_ug_K = "La lista inserita non contiene numeri maggiori o uguali a K."
    return numeri_magg_ug_K
print(controllo_K(num,K))

"""
Domanda 18:
Scrivere una funzione che, data una lista di numeri, come output stamperà lo
stesso numero di asterischi su righe diverse, ottenendo una semplice visualizzazione grafica

Esempio, supponendo di chiamare la funzione aster():

numeri = [5, 2, 3, 4]

aster(numeri)

Output:
*****
**
***
****
"""

num = input("Inserire una lista di numeri interi separati da uno spazio:")
num = num.split(" ")

def aster(num):
    for x in num:
        print ("*" * int(x))
    return aster
print(aster(num))

"""
Domanda 19:
Abbiamo un testo, ad esempio:

racconto = '''
Lisetta va a passeggio in campagna; è felice di
raccogliere i fiori che crescono sulle rive, ai bordi della strada.
Ha già un bel mazzetto di ranuncoli e margherite.'''

Creiamo una funzione che prenda il testo in input, e in output ci dia un dizionario che
contiene ogni tipo di carattere e quante volte appare.

Esempio: 

Se il testo è
testo = '''Ciao a tutti!'''

l'output sarà:
{"C": 1, "i": 2, "a": 2, "o": 1, " ": 2, "t": 3, "u": 1, "!": 1}
"""

racconto = """Lisetta va a passeggio in campagna; è felice di raccogliere i fiori che crescono sulle rive, ai bordi della strada. Ha già un bel mazzetto di ranuncoli e margherite."""

def count_char(racconto):
    dizionario = {}
    for x in racconto:
        if x not in dizionario.keys():
            dizionario.update({x:1})
        elif x in dizionario.keys():
            dizionario[x] += 1 
    return dizionario
print("Nel testo ogni carattere X si ripete N volte, secondo lo schema:" + str(count_char(racconto)))

"""
Domanda 20:
Abbiamo un testo, 

ad esempio:

racconto = '''Lisetta va a passeggio in campagna; è felice di
raccogliere i fiori che crescono sulle rive, ai bordi della strada.
Ha già un bel mazzetto di ranuncoli e margherite.'''

Creiamo una funzione che prenda il testo in input, e in output ci dia un dizionario che
contiene ogni tipo di carattere e quante volte appare, esclusi punteggiatura e spazi.

Esempio: 

Se il testo è
testo = '''Ciao a tutti!'''

l'output sarà:
{"C": 1, "i": 2, "a": 2, "o": 1, "t": 3, "u": 1}
"""

racconto = """Lisetta va a passeggio in campagna; è felice di raccogliere i fiori che crescono sulle rive, ai bordi della strada. Ha già un bel mazzetto di ranuncoli e margherite."""

def count_char_alpha_only(racconto):
    dizionario = {}
    for x in racconto:
        if str(x).isalpha():
            if x not in dizionario.keys():
                dizionario.update({x:1})
            elif x in dizionario.keys():
                dizionario[x] += 1 
    return dizionario
print("Nel testo ogni carattere alfabetico X si ripete N volte, secondo lo schema:" + str(count_char_alpha_only(racconto)))

"""
Domanda 21:
Abbiamo un testo, 

ad esempio:
racconto = '''Lisetta va a passeggio in campagna; è felice di
raccogliere i fiori che crescono sulle rive, ai bordi della strada.
Ha già un bel mazzetto di ranuncoli e margherite.'''

Creiamo una funzione che prenda il testo in input, e in output ci dia un dizionario che
contiene ogni tipo di carattere e quante volte appare, senza fare differenza tra maiuscole e minuscole.
"""

racconto = """Lisetta va a passeggio in campagna; è felice di raccogliere i fiori che crescono sulle rive, ai bordi della strada. Ha già un bel mazzetto di ranuncoli e margherite."""

def count_char_all(racconto):
    dizionario = {}
    for x in racconto:
        x = str(x.lower())
        if x not in dizionario.keys():
            dizionario.update({x:1})
        elif x in dizionario.keys():
            dizionario[x] += 1 
    return dizionario
print("Nel testo ogni carattere alfabetico X si ripete N volte, secondo lo schema:" + str(count_char_all(racconto)))

"""
Domanda 22:

Parte 1:

Andiamo su http://www.datiopen.it/it/opendata/Mappa_dei_pub_circoli_locali_in_Italia e scarichiamo la mappa dei pub, circoli e locali in Italia

Nota: per leggerlo nella funzione open() dovremo aggiungere il parametro encoding="latin1", ad esempio:

f = open(file_path, "r", encoding="latin1")

Parte 2:

Esaminiamo il dataset:

1. Quanti dati ci sono in totale?
2. Quali sono i metadati?
3. Stampiamo il primo elemento
4. Stampiamo l'ultimo elemento
5. Riusciamo a stampare un elemento a caso?
6. Quali sono gli anni di inserimento presenti?
7. Quante attività ci sono nel quadrato di longitudine 9-10 e latitudine 45-46?
8. Quante attività ci sono nella provincia di Vicenza?
9. Quante enoteche ci sono, e come si chiamano?
10. Quante attività ci sono in Lazio e Abruzzo assieme?
"""

import pandas as pd

mappa = pd.read_csv('Mappa-dei-pub-circoli-locali-in-Italia.csv',sep=";")

print("Nel file sono ci sono " + str(mappa.__len__()) + " righe.")

# Quali sono i metadati?
print("\nI metadati sono:")
for x in mappa.columns.values:
    print("- " + x)

# Stampiamo il primo elemento
print(mappa[:1])

# Stampiamo l'ultimo elemento
print(mappa[-1:])

# Riusciamo a stampare un elemento a caso?
from random import *
x = randint(0,mappa.__len__()-1)
mappa[x:x+1]

# Quali sono gli anni di inserimento presenti?
anni = []
for x in mappa["Anno inserimento"]:
    if x not in anni: 
        anni.append(x)
anni.sort()
print((str(anni))) 

# Quante attività ci sono nel quadrato di longitudine 9-10 e latitudine 45-46?
Long = mappa["Longitudine"].between(9,10)
Lat = mappa["Latitudine"].between(45,46) 
mappa[Long & Lat]

# Quante attività ci sono nella provincia di Vicenza?
Vicenza = mappa["Provincia"] == "VICENZA"
print("Nella provincia di Vicenza sono presenti " + str(mappa[Vicenza].__len__()) + " attività.")

# Quante enoteche ci sono, e come si chiamano?
enoteche = []
for x in mappa["Nome"]:
    if "ENOTECA" in str(x).upper():
        enoteche.append(x)
print("Le enoteche presenti sono:\n")
print("\n".join(enoteche),"\n")              
print("Per un totale di " + str(len(enoteche)) + " enoteche.")

# Alternativa
x=0
print("Le enoteche presenti sono:\n")
for el in mappa["Nome"]:
    if "ENOTECA" in str(el).upper():
        print(el)
        x += 1
print("\nPer un totale di " + str(x) + " enoteche.")

# Quante attività ci sono in Lazio e Abruzzo assieme?
Lazio = mappa["Regione"] == "Lazio"
Abruzzo = mappa["Regione"] == "Abruzzo"
print("Nella regioni Lazio e Abruzzo sono presenti " + str(mappa[Lazio + Abruzzo].__len__()) + " attività.")