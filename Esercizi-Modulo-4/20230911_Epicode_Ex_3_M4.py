"""
Domanda 1: 

Abbiamo la stringa: nome_scuola = "Epicode". Stampare ogni carattere della stringa, uno su ogni riga, utilizzando un costrutto while.
"""

nome_scuola = "Epicode"
i = 0

while i < len(nome_scuola):
    print(nome_scuola[i])
    i += 1

"""
Domanda 2: 

Stampare a video tutti i numeri da 0 a 20 utilizzando il costrutto while.
"""

# Prima versione

i = 0
while i <= 20:
    print(i)
    i += 1

# Seconda versione    

i = 0
while i <= 20:
    print(i," ", end="")
    i += 1

# Terza versione ( in due varianti )

# Variante 1
    
i = 0
risultato = ""

while i <= 20:
    risultato += str(i) + "-"
    i += 1

print(risultato.strip("-"))

# Variante 2

i = 0
risultato = ""

while i <= 20:
    risultato += str(i) + " "
    i += 1

print(risultato.strip())

"""
Domanda 3: 

Calcolare e stampare tutte le prime 10 potenze di 2, utilizzando un ciclo while.
"""

# Prima versione

i = 2
x = 0 

risultato = ""

while x < 10:
    risultato  += str(i**x) + "-"
    x += 1

print(risultato.strip("-"))

# Seconda versione

i = 2
x = 0 

risultato = ""

while x <10:
    risultato  += str(i) + "^" + str(x) + " = " + str(i**x) + " - "
    x += 1

print(risultato.strip(" - "))

"""
Domanda 4: 

Calcolare e stampare tutte le prime N potenze di 2 con un ciclo while, domandando all'utente di inserire N.
"""

# Prima versione

i = 2
x = 0 
N = int(input("Specificare un valore N per avviare il calcolo."))
risultato = ""

while x < N:
    risultato += str(i**x) + "-"
    x += 1

print(risultato.strip("-"))

# Seconda versione

i = 2
x = 0 
N = int(input("Specificare un valore N per avviare il calcolo."))

risultato = ""

while x < N:
    risultato  += str(i) + "^" + str(x) + " = " + str(i**x) + " - "
    x += 1

print(risultato.strip(" - "))

"""
Domanda 5: 

Abbiamo due liste, una di studenti e una di corsi:

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith",
"Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend",
"Frontend", "Data Analyst", "Backend", "Frontend"]

Verificare che entrambe le liste abbiano la stessa lunghezza, e stampare a video
una frase che ci dica se è così o meno. 
"""

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend"]

if len(studenti) == len(corsi):
    print("Le due liste hanno la stessa lunghezza.")
else:
    print("Le due liste non hanno la stessa lunghezza")

"""
Domanda 6:

Parte 1:

Abbiamo due liste, una di studenti e una di corsi:

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith",
"Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend",
"Frontend", "Data Analyst", "Backend"]

Parte 2:

Aggiungere i dati mancanti alla lista corsi, sapendo che:

Emma segue Data Analyst
Faith segue Backend
Grace segue Frontend
Henry segue Cybersecurity

Aggiungeremo i dati mancanti uno alla volta con il metodo per appendere in
coda alle liste, poi verificheremo che sono della stessa lunghezza e se lo sono
stamperemo la lista corsi.
"""   

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend"]

corsi.append("Frontend")
corsi.append("Cybersecurity")

if len(studenti) == len(corsi):
    print(str(corsi))
else:
    print("Le due liste non hanno la stessa lunghezza")

"""
Domanda 7: 

Scriviamo un programma che chiede in input all'utente una stringa e visualizza i
primi 3 caratteri, seguiti da 3 punti di sospensione e quindi gli ultimi 3 caratteri.
Attenzione a tutti i casi particolari, ovvero implementare soluzioni ad hoc per
stringhe di lunghezza inferiore a 6 caratteri.
"""

stringa_input = str(input("Quale sistema operativo utilizzi?"))

if len(stringa_input) >= 6:
    print(stringa_input[0:3] + "..." + stringa_input[-3:])

else:
    print("Il testo che hai inserito contiene meno di 6 caratteri.")

"""
Domanda 8: 

Memorizza e stampa tutti i fattori di un numero dato in input.
"""

num = int(input("Scrivi un qualsiasi numero intero N."))

lista = []

divisore = 2

while num != 1:
    if num % divisore == 0:
        lista.append(divisore)
        num /= divisore
    else:
        divisore += 1  

print(lista)

# Anar kaluva tielyanna!