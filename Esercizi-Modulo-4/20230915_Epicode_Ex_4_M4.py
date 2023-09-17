"""
Domanda 1:
Abbiamo la stringa: nome_scuola = "Epicode". Stampare ogni carattere della stringa, uno su ogni riga, utilizzando un costrutto for.
"""

# Soluzione con ciclo for:

nome_scuola = "Epicode"
for x in nome_scuola:
    print(x)

# Soluzione con ciclo while:

nome_scuola = "Epicode"
i = 0
while i < len(nome_scuola):
    print(nome_scuola[i])
    i += 1

"""
Domanda 2: 
Abbiamo una serie di simboli di elementi chimici (tutti da una sola lettera)
all'interno della variabile elementi: elementi = "NPKOHC". Stampare ogni elemento su una riga diversa.
"""

# Soluzione con ciclo for:

elementi = "NPKOHC"
for x in elementi:
    print(x)

# Soluzione con ciclo while:

elementi = "NPKOHC"
i = 0
while i < len(elementi):
    print(elementi[i])
    i += 1

"""
Domanda 3:
Abbiamo una serie di simboli di elementi chimici (tutti da una sola lettera)
all'interno della variabile elementi: elementi = "NPKOHC". Stampare ogni elemento su una riga diversa, preceduto dalla scritta "elemento - ".
"""

# Soluzione con ciclo for:

elementi = "NPKOHC"
for x in elementi:
    print("elemento - ", x)

# Soluzione con ciclo while:

elementi = "NPKOHC"
i = 0
while i < len(elementi):
    print("elemento - ", elementi[i])
    i += 1

"""
Domanda 4:
Abbiamo una serie di simboli di elementi chimici (tutti da una sola lettera) all'interno della variabile elementi: elementi = "NPKOHC". 
Stampare ogni elemento su una riga diversa, preceduto dalla scritta "elemento - numero n" dove al posto di n scriveremo un numero progressivo che parte da 1.
"""

# Soluzione con ciclo for:

elementi = "NPKOHC"
for n, x in enumerate(elementi,start=1):
    print("elemento - numero ",n,": ",x)

# Soluzione con ciclo while:

elementi = "NPKOHC"
i = 0
n = 1
while i < len(elementi):
    print("elemento - numero ",n,": ",elementi[i])
    i += 1
    n += 1

"""
Domanda 5:
Modificare la parola "marmalade" in modo sostituire le "e" con le "a" e viceversa. Salvare il risultato in una variabile e stamparla a video.

Fare diverse versioni:
• una con un ciclo for,
• una con un ciclo while,
• una con il metodo delle stringhe .replace().
"""

# Soluzione con ciclo for:

stringa = "marmalade"
nuova_stringa = ""

for x in stringa:
    if x == "a":
        nuova_stringa += "e"
    elif x == "e":
        nuova_stringa += "a"
    else:
        nuova_stringa += x 

print(nuova_stringa)               

# Soluzione con ciclo while:

stringa = "marmalade"
i = 0
nuova_stringa = ""

while i < len(stringa):
    if stringa[i] == "a":
        nuova_stringa += "e"
    elif stringa[i] == "e":
        nuova_stringa += "a"
    else:
        nuova_stringa += stringa[i] 
    i += 1

print(nuova_stringa) 

# Soluzione con metodo stringhe .replace()

x = "marmalade"
num_a = x.count("a")

x = x.replace("e","a")
x = x.replace("a","e",num_a)

print(str(x))

# Alternativa proposta da Vita:

parola_originale = "marmalade"
parola_modificata = parola_originale.replace("e", "1").replace("a", "e").replace("1", "a")

print(parola_modificata)

"""
Domanda 6: 
Calcolare e stampare tutte le prime 10 potenze di 2 utilizzando un ciclo for. 

Utilizzeremo:
1. la funzione range(), e.g.:
2. for contatore in range(10):
pass # modificare qui
"""

x = 2

for i in range(10):
    print("2 ^", i, "=", x**i)

"""
Domanda 7: 
Calcolare (ma non stampare) le prime N potenze di 2; ognuna di esse andrà memorizzata in coda a una lista.
Alla fine, stampare la lista risultante.

Realizzare due versioni:
• con un ciclo while,
• con un ciclo for.
"""

# Versione con ciclo while:

N = int(input("Scrivi un numero intero N."))
x = 2
i = 0
lista_risultante = list()

while i <= N:
    lista_risultante.append(x**i)
    i += 1

print(lista_risultante)

# Versione con ciclo for:

N = int(input("Scrivi un numero intero N."))
x = 2

lista_risultante = list()

for y in range(0,N+1): # Nel range il valore N non sarebbe incluso, quindi scriviamo N + 1 per assicurarci che venga preso proprio N come valore massimo del range
    lista_risultante.append(x**y)    

print(lista_risultante)

"""
Domanda 8:
Calcolare (ma non stampare) le prime N potenze di 3; ognuna di esse andrà memorizzata in coda a una lista.
Alla fine, stampare la lista risultante.

Realizzare due versioni:
• con un ciclo while,
• con un ciclo for.
"""

# Versione con ciclo while:

N = int(input("Scrivi un numero intero N."))
x = 3
i = 0
lista_risultante = list()

while i <= N:
    lista_risultante.append(x**i)
    i += 1

print(lista_risultante)

# Versione con ciclo for:

N = int(input("Scrivi un numero intero N."))
x = 3
lista_risultante = list()

for y in range(0,N+1):
    lista_risultante.append(x**y)    

print(lista_risultante)

"""
Domanda 9:
Calcolare (ma non stampare) le prime N potenze di K; ognuna di esse andrà memorizzata in coda a una lista.
Alla fine, stampare la lista risultante. Proviamo con diversi valori di K, oppure facciamola inserire all'utente.

Realizzare due versioni:
• con un ciclo while,
• con un ciclo for.
"""

# Versione con ciclo while:

N = int(input("Scrivi un numero intero N per definire il numero di potenze da calcolare."))
K = int(input("Scrivi un numero intero K per definire la base da elevare a potenza."))
x = K
i = 0
lista_risultante = list()

while i <= N:
    lista_risultante.append(x**i)
    i += 1

print(lista_risultante)

# Versione con ciclo for:

N = int(input("Scrivi un numero intero N per definire il numero di potenze da calcolare."))
K = int(input("Scrivi un numero intero K per definire la base da elevare a potenza."))
x = K

lista_risultante = list()

for y in range(0,N+1):
    lista_risultante.append(x**y)    

print(lista_risultante)

"""
Domanda 10:
Calcolare e stampare tutte le potenze di 2 minori di 25000.
"""

x = 2
i = 0 

while x**i <= 25000:
    print("2 ^", i, "=" , x**i)
    i += 1

"""
Domanda 11:
Calcolare e stampare tutte le potenze di 2 minori di un certo numero N.
"""

N = int(input("Scrivi un numero intero N."))
x = 2
i = 0 

while x**i <= N:
    print("2 ^", i, "=" , x**i)
    i += 1

"""
Domanda 12:
Calcolare e stampare tutte le prime 100 potenze di 2, ogni 3 (e.g. 20, 23, 26, 29, ...).
Oltre a stamparle, memorizzarle in coda a una lista e stamparla alla fine.

Usate due metodi diversi:
1. usare un costrutto for e range(100), e poi un costrutto if per visualizzare e memorizzare solo ogni 3
2. usare un costrutto for e range(0, 100, 3)
"""

# Versione 1:

x = 2
lista_risultante = list()

for y in range(0,100):
    if y % 3 == 0:
        lista_risultante.append(x**y)

print(lista_risultante, " ", end="")    

# Versione 2:

x = 2
lista_risultante = list()

for y in range(0,100,3):
    lista_risultante.append(x**y)

print(lista_risultante, " ", end="")

"""
Domanda 13:
Abbiamo una lista con dei numeri:

numeri = [4, 9, 5, 1, 7, 10, 2, 3]

utilizzando un costrutto for, trovare il massimo di questa lista e stamparlo a video.
"""

# Versione principale:

numeri = [4, 9, 5, 1, 7, 10, 2, 3]
max = 0

for x in numeri:
    if x > max:
        max = x
    
print(max)

# Alternativa più easy senza ciclo for:

numeri = [4, 9, 5, 1, 7, 10, 2, 3]

max = max(numeri)

print(max)

"""
Domanda  14:
Abbiamo raccolto tutte le età degli studenti in una lista: eta_studenti = [20, 30, 40, 50, 60].
Utilizzando un ciclo for, calcolare la media delle età. Alla fine, stampa (a video) il risultato.
"""

eta_studenti = [20, 30, 40, 50, 60]
sum = 0

for x in eta_studenti:
    sum += x 

print(float(sum / len(eta_studenti)))   

"""
Domanda 15:
Abbiamo una lista con i guadagni degli ultimi 12 mesi: guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50].
Usando un costrutto for, calcolare la media dei guadagni e stamparla a video.
"""

guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]
sum = 0

for x in guadagni:
    sum += x

print(float(sum / len(guadagni)))    

"""
Domanda 16: 
Abbiamo una lista con i guadagni degli ultimi N mesi: guadagni = [100, 90, 70, 40, 50, 80, 90, 120].
Usando un costrutto for, calcolare la media dei guadagni e stamparla a video; stampare anche il numero di mesi considerati.
"""

guadagni = [100, 90, 70, 40, 50, 80, 90, 120]
sum = 0
N = len(guadagni)

for x in guadagni:
    sum += x 

print(float(sum / N))

print("La media dei guadagni degli ultimi ", N, "mesi è pari a: ", float(sum / N))

"""
Domanda 17:
Abbiamo una lista di studenti: studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"].
Utilizzare un ciclo for per stampare i nomi di tutti gli studenti con questa formattazione:

Studenti:
- Alex
- Bob
- Cindy
...
"""

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]

for x in studenti:
    print("- ", x)

"""
Domanda  18:
Abbiamo tre liste (sono tutte della stessa lunghezza):
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

Stampare a video, usando print(), ogni studente che corso segue e di che edizione, e.g.:

Alex segue Cybersecurity, edizione 1
Bob segue Data Analyst, edizione 2
...

Fare in modo che non ci sia uno spazio tra il corso e la virgola subito dopo.
"""

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

for x, y, z in zip(studenti, corsi, edizioni):
    print(str(x) + " segue " + str(y) + ", edizione " + str(z))

# Alternativa proposta da Andrea:

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

for i in range(len(studenti)):
    print(f"{studenti[i]} segue {corsi[i]}, edizione {edizioni[i]}")    

"""
Domanda 19:
Abbiamo una lista di parole: 

parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Belvedere", "Semestre", "Sosta", "Orpello", "Abete"]

Stampiamo, per ogni parola, quante volte appare la lettera "e".
"""

parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Belvedere", "Semestre", "Sosta", "Orpello", "Abete"]
numero_istanze_e = list()

for x in parole:
    numero_istanze_e.append(x.count("e"))

print(numero_istanze_e, " ", end="") 

# Alternativa proposta da Andrea:

parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Belvedere", "Semestre", "Sosta", "Orpello", "Abete"]
list_nr_e = []

for p in parole:
    nr_e = 0
    for c in p:
        if c == "e":
            nr_e += 1
    list_nr_e.append(nr_e)
print(list_nr_e) 

"""
Domanda 20:
Abbiamo una lista di parole:

parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Eremo", "Belvedere", "Semestre", "Esteta", "Sosta", "Orpello", "Abete", "Orologio", "Cesta", "Ermellino"]

Stampiamo, per ogni parola, quante volte appare la lettera "e"; facciamo attenzione al fatto che appare sia maiuscola che minuscola.
"""

parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Eremo", "Belvedere", "Semestre", "Esteta", "Sosta", "Orpello", "Abete", "Orologio", "Cesta", "Ermellino"]
numero_istanze_e = []
numero_istanze_E = []

for n, x in enumerate(parole, start=1):
    numero_istanze_e = x.count("e")
    numero_istanze_E = x.count("E")
    print(str(n) + ". Parola: " + x + "; numero istanze \"e\": " + str(numero_istanze_e) + "; numero istanze \"E\": " + str(numero_istanze_E) + ".") 

# Alternativa proposta da Andrea:

parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Eremo", "Belvedere", "Semestre", "Esteta", "Sosta", "Orpello", "Abete", "Orologio", "Cesta", "Ermellino"]

for p in parole: 
    nr_e = 0
    nr_E = 0

    for c in p:
        if c == "e":
            nr_e += 1            
        if c == "E":
            nr_E += 1
    
    print(p, nr_e, nr_E)

"""
Domanda 21: 
Abbiamo una lista di codici fiscali:

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]

Trovare i codici fiscali che contengono "95", metterli in una lista, e alla fine stamparla.
"""

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]
lista_cf_95 = []

for x in lista_cf:
  indice = x.find("95",6,8)
  if indice >= 0:
    lista_cf_95.append(x)

print(lista_cf_95)   

"""
Domanda 22:
Abbiamo una lista di codici fiscali:

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]

Per ognuno di essi, stampare a video i caratteri relativi al nome e quelli relativi al cognome.
"""

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]

for x in lista_cf:
    print(x, x[0:3], x[3:6])

"""
Domanda 23:
Abbiamo tre liste della stessa lunghezza:

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

Dove ogni elemento nella medesima posizione si riferisce ai dati dello stesso studente.
Stampare a video tutti e soli gli studenti che frequentano una prima edizione; utilizzare solo i dati necessari.
"""

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

for x, y, z in zip(studenti,corsi,edizioni):
    if z == 1:
        print(x)

"""
Domanda 24:
Abbiamo tre liste della stessa lunghezza:

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

Dove ogni elemento nella medesima posizione si riferisce ai dati dello stesso studente.
Riuscite a vedere una similarità di qualche tipo con la logica che si usa in SQL e le tabelle relazionali?
"""

# Dopo aver definito una matrice / tabella con la funzione zip(), il costrutto IF mi ricorda la clausola WHERE utilizzata in SQL.

"""
Domanda 25:
Creiamo un dizionario che assegni ad ogni proprietario la sua auto, sapendo che:
• Ada guida una Punto
• Ben guida una Multipla
• Charlie guida una Golf
• Debbie guida una 107 
Poi stampiamo il dizionario per intero, e poi l'auto associata a Debbie.
"""

proprietari_auto = {
    "Ada": "Fiat Punto",
    "Ben": "Fiat Multipla",
    "Charlie": "Volkswagen Golf",
    "Debbie": "Peugeot 107"
}

print("Il dizionario \"proprietari_auto\" è composto dalle seguenti coppie di valori:", proprietari_auto)

print("Debbie guida quest'auto:", proprietari_auto["Debbie"])

"""
Domanda 26:
Abbiamo un dizionario che assegni ad ogni proprietario la sua auto:

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107"}

Aggiungere i proprietari Emily e Fred che posseggono rispettivamente una A1 e una Octavia; eliminare i dati relativi a Ben.
Stampare il dizionario per controllare che sia tutto corretto.
"""

dizionario_auto = {
    "Ada": "Fiat Punto",
    "Ben": "Fiat Multipla",
    "Charlie": "Volkswagen Golf",
    "Debbie": "Peugeot 107"
}

dizionario_auto["Emily"] = "Audi A1"
dizionario_auto["Fred"] = "Skoda Octavia"

del dizionario_auto["Ben"]

print("Il dizionario \"dizionario_auto\" è composto dalle seguenti coppie di valori:", dizionario_auto)

"""
Domande 27:
Abbiamo due dizionari che assegnano ad ogni proprietario la propria auto:

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", "Emily": "A1"}
nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"}

Aggiornare il dizionario dizionario_auto con i dati contenuti in nuovi_proprietari e stamparlo. Cosa è successo a Ben?
"""

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", "Emily": "A1"}
nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"}

dizionario_auto.update(nuovi_proprietari)

print("Il dizionario \"dizionario_auto\", aggiornato con i valori del dizionario \"nuovi_proprietari\", contiene le seguenti coppie di valori:\n",dizionario_auto)
print("Il valore relativo all'auto guidata da Ben è stato aggiornato, sovrascrivendo \"Polo\" a \"Multipla\".")

"""
Domande 28:
Abbiamo un dataset che assegna ad ogni proprietario la propria auto, in forma di dizionario:

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", "Emily": "A1", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"}

Viene richiesto di ricercare in questo dataset i dati di Hugh, Ada, Emily e Debbie, e visualizzare le auto relative.
"""

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", "Emily": "A1", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"}

print("L'auto guidata da Hugh è:", dizionario_auto["Hugh"])
print("L'auto duidata da Ada è:", dizionario_auto["Ada"])
print("L'auto guidata da Emily è:", dizionario_auto["Emily"])
print("L'auto guidata da Debbie è:", dizionario_auto["Debbie"])

# Alternativa con funzioni per dizionari:

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", "Emily": "A1", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"}

print("L'auto guidata da Hugh è:", dizionario_auto.get("Hugh"))
print("L'auto duidata da Ada è:", dizionario_auto.get("Ada"))
print("L'auto guidata da Emily è:", dizionario_auto.get("Emily"))
print("L'auto guidata da Debbie è:", dizionario_auto.get("Debbie"))

"""
Domande 29:
Abbiamo un dataset che assegna ad ogni proprietario la propria auto, in forma di dizionario:

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", "Emily": "A1", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"}

Viene richiesto di ricercare in questo dataset i dati di Ada, Emily, Jade, Ben, Hugh, Kelly e Charlie, e visualizzare le auto relative.

Non tutti i dati potrebbero essere presenti nel dataset, quindi quando un nome non è presente visualizzeremo un messaggio adeguato.
"""

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", "Emily": "A1", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"}

for nome in ["Ada", "Emily", "Jade", "Ben", "Hugh", "Kelly", "Charlie"]:
    if nome in dizionario_auto.keys():
        print(f"{nome} guida una {dizionario_auto[nome]}")
    else:
        print(f"Il nome {nome} non è presente nel dizionario \"dizionario_auto\".")

"""
Domanda 30:
Abbiamo un dizionario:

diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k": 12, "clap": 9}

Utilizzando il metodo .keys(), stampiamone tutte le chiavi.
"""

diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k": 12, "clap": 9}

print(diz.keys())

"""
Domanda 31:
Abbiamo un dizionario:

diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k": 12, "clap": 9}

Utilizzando il metodo .values(), stampiamone tutte i valori.
"""

diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k": 12, "clap": 9}

print(diz.values())

"""
Domanda 32:
Abbiamo un dizionario:

diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k": 12, "clap": 9}

Utilizzando il metodo dei dizionari .items() stampate le coppie chiave-valore presenti nel dizionario su righe diverse.
"""

diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k": 12, "clap": 9}

for key, value in diz.items():
  print(key, value)

"""
Domanda 33:
Abbiamo un dizionario:

diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k": 12, "clap": 9}

Utilizzando il metodo dei dizionari .values(), calcolare il valore massimo, il valore minimo, la somma, e stampiamo i risultati.
"""

diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k": 12, "clap": 9}

print("I valori contenuti nel dizionario \"diz\" sono i seguenti:", list(diz.values()))
print("Il valore massimo contenuto nel dizionario \"diz\" è:", int(max(diz.values())))
print("Il valore minimo contenuto nel dizionario \"diz\" è:", int(min(diz.values())))
print("La somma dei valori contenuti nel dizionario \"diz\" è:", int(sum(diz.values())))

"""
Domanda 34:
Abbiamo un dizionario che assegna ad ogni proprietario la sua auto:

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107"}

Con un ciclo for, e usando il metodo .items(), stampiamo ogni proprietario e la sua auto, formattandolo come:

Ada guida una Punto
Ben guida una Multipla
...

"""

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107"}

for nome, auto in dizionario_auto.items():
    print(f"{nome} guida una {auto}")

"""
Domanda 35:
Abbiamo un dizionario che assegna ad ogni proprietario la sua auto:

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107"}

Con un ciclo, e usando il metodo .values(), stampiamo a video tutte le auto che non sono una Multipla.
"""

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107"}

for auto in dizionario_auto.values():
    if auto != "Multipla":
        print(auto, " ", end="")

"""
Domanda 36:
Abbiamo i seguenti dati riguardo dei collezionisti e le loro collezioni:

• Ada ha 10 Funko Pop, 5 action figures e 35 manga
• Ben ha 2 Funko Pop, 6 action figures, 40 manga e 2 graphic novels
• Charlie ha 31 action figures e 18 graphic novels
• Debbie ha 1 Funko Pop, 9 graphic novels, 25 manga e 2 action figures

Creare dei dizionari innestati che contengano questi dati, e quindi visualizzarli.
"""

dizionario = {}

dizionario["Ada"] = {"Funko Pop": 10, "Action Figure": 5, "Manga": 35}
dizionario["Ben"] = {"Funko Pop": 2, "Action Figure": 6, "Manga": 40, "Graphic Novel": 2}
dizionario["Charlie"] = {"Action Figure": 31, "Graphic Novel": 18}
dizionario["Debbie"] = {"Funko Pop": 1, "Graphic Novel": 9, "Manga": 25, "Action Figure": 2}

print(dizionario)

"""
Domanda 37:
Abbiamo i seguenti dati riguardo dei collezionisti e le loro collezioni:

• Ada ha 10 Funko Pop, 5 action figures e 35 manga
• Ben ha 2 Funko Pop, 6 action figures, 40 manga e 2 graphic novels (entrambe della DC)
• Charlie ha 31 action figures e 18 graphic novels (di cui 10 della Marvel e 8 della DC)
• Debbie ha 1 Funko Pop, 9 graphic novels (di cui 4 della DC e 5 della Marvel), 25 manga e 2 action figures

Creare dei dizionari innestati che contengano questi dati, e quindi visualizzarli.
"""

dizionario = {}

dizionario["Ada"] = {"Funko Pop": 10, "Action Figure": 5, "Manga": 35}
dizionario["Ben"] = {"Funko Pop": 2, "Action Figure": 6, "Manga": 40, "Graphic Novel": {"Dc Comics": 2}}
dizionario["Charlie"] = {"Action Figure": 31, "Graphic Novel" : {"Marvel Comics": 10, "Dc Comics": 8}}
dizionario["Debbie"] = {"Funko Pop": 1, "Action Figure": 2, "Manga": 25, "Graphic Novel" : {"Marvel Comics": 5, "Dc Comics": 4}}

print(dizionario)

"""
Domanda 38:
Riguardo l'esercizio precedente, stampiamo le risposte a:

1. Quanti funko pop ha Ada?
2. Quanti manga ha Ben?
3. Quanti graphic novel della Marvel ha Debbie?
4. Quanti funko pop hanno Ada e Ben in tutto?
5. Quanti manga hanno in tutto i collezionisti?
6. Quanti graphic novel della DC hanno in tutto i collezionisti?
7. Quanti graphic novel hanno in tutto i collezionisti?
"""

dizionario = {}

dizionario["Ada"] = {"Funko Pop": 10, "Action Figure": 5, "Manga": 35}
dizionario["Ben"] = {"Funko Pop": 2, "Action Figure": 6, "Manga": 40, "Graphic Novel": {"Dc Comics": 2}}
dizionario["Charlie"] = {"Action Figure": 31, "Graphic Novel" : {"Marvel Comics": 10, "Dc Comics": 8}}
dizionario["Debbie"] = {"Funko Pop": 1, "Action Figure": 2, "Manga": 25, "Graphic Novel" : {"Marvel Comics": 5, "Dc Comics": 4}}

# Metodo alternativo per costruire il dizionario:

collezionisti = {
    "Ada":
        {"Funko Pop": 10, "Action Figure": 5, "Manga": 35},
    "Ben":
        {"Funko Pop": 2, "Action Figure": 6, "Manga": 40, "Graphic Novel":
            {"Dc Comics": 2}
        },
    "Charlie":
        {"Action Figure": 31, "Graphic Novel" :
            {"Marvel Comics": 10, "Dc Comics": 8}
        },
    "Debbie":
        {"Funko Pop": 1, "Action Figure": 2, "Manga": 25, "Graphic Novel" :
            {"Marvel Comics": 5, "Dc Comics": 4}
        }
}

# Per verificare che i due dizionari siano identici, utilizzo: "print(dizionario == collezionisti)"

print("1. Quanti funko pop ha Ada?", collezionisti["Ada"]["Funko Pop"])

print("2. Quanti manga ha Ben?", collezionisti["Ben"]["Manga"])

print("3. Quanti graphic novel della Marvel ha Debbie?", collezionisti["Debbie"]["Graphic Novel"]["Marvel Comics"])

print("4. Quanti funko pop hanno Ada e Ben in tutto?", collezionisti["Ada"]["Funko Pop"] + collezionisti["Ben"]["Funko Pop"])

totale_manga = 0
for collezionista in collezionisti.values():
    totale_manga += collezionista.get("Manga",0)
print("5. Quanti manga hanno in tutto i collezionisti?", totale_manga)

conteggio_dccomics = 0
for collezionista in collezionisti.values():    
    if "Graphic Novel" in collezionista:
        graphic_novel = collezionista["Graphic Novel"]        
        if "Dc Comics" in graphic_novel:
            conteggio_dccomics += graphic_novel["Dc Comics"]
print(f"6. Quanti graphic novel della DC hanno in tutto i collezionisti? {conteggio_dccomics}")

conteggio_graphic_novel = 0
for collezionista in collezionisti.values():    
    if "Graphic Novel" in collezionista:
        graphic_novel = collezionista["Graphic Novel"]        
        if "Dc Comics" in graphic_novel:
            conteggio_graphic_novel += graphic_novel["Dc Comics"]
        if "Marvel Comics" in graphic_novel:
            conteggio_graphic_novel += graphic_novel["Marvel Comics"]
print(f"7. Quanti graphic novel hanno in tutto i collezionisti? {conteggio_graphic_novel}")