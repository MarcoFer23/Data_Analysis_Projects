"""
Esercizio 1: Manipolazione Semplice delle Stringhe
Scrivi un programma Python che chiede all'utente di inserire una stringa e la stampa in ordine inverso usando un ciclo while.
"""

# Soluzione Stefano

stringa = input("Inserire una stringa da invertire:")
starter = len(stringa) -1
parola_invertita = str() # Uguale a: parola_investita = ""
while starter >= 0 : # Condizione di uscita dal ciclo
    parola_invertita = parola_invertita + stringa[starter] # Uguale a: parola_invertita += stringa[starter]
    starter = starter - 1 # Uguale a: starter += -1
print("parola invertita :", parola_invertita)

# Soluzione Andrea

nome_stringa= str((input("Inserisci una stringa da invertire: ")))
i = len(nome_stringa) - 1
while i >= 0:
    print(nome_stringa[i], end = '')
    i = i - 1

# Alternative Marco: 1    

stringa = input("Scrivi un messaggio da inviare al Cyberspazio, affinché possa essere invertito!")

contrario = list()

for x in stringa:
    contrario.insert(0,x)

print(" ".join(contrario))

# Alternative Marco: 2

stringa = input("Scrivi un messaggio da inviare al Cyberspazio, affinché possa essere invertito!")

for x in range(len(stringa),0,-1):
    print(stringa[x-1], " ", end="")

"""
Esercizio 2: Filtraggio di Liste
Scrivi un programma Python che chiede all'utente di inserire una lista di numeri e poi utilizza un ciclo while e istruzioni if per filtrare e stampare solo i numeri pari dalla lista.
"""

"""
Esercizio 3: Validazione delle Password
Crea un programma Python che chiede all'utente di inserire una password. Utilizza un ciclo while e istruzioni if per verificare se la password inserita soddisfa i seguenti criteri:

Lunga almeno 8 caratteri.
Contiene almeno una lettera maiuscola.
Contiene almeno una lettera minuscola.
Contiene almeno una cifra.
Stampa un messaggio che indica se la password è valida o no.
"""

"""
Esercizio 4: Verifica dei Palindromi
Scrivi un programma Python che chiede all'utente di inserire una stringa e verifica se è un palindromo (una parola, frase, numero o altra sequenza di caratteri che si legge allo stesso modo in avanti e all'indietro). Utilizza un ciclo while e istruzioni if per effettuare il controllo e fornire un feedback appropriato.
"""

"""
Esercizio 5: Gioco dell'impiccato
Crea un gioco in cui il programma seleziona una parola casuale da una lista predefinita e l'utente deve indovinare la parola lettera per lettera. Utilizza un ciclo while e istruzioni if per guidare l'utente e fornire feedback. Includi un limite al numero di tentativi errati consentiti e dai un suggerimento se l'utente si blocca.
"""