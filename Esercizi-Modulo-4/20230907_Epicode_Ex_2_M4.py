"""
Domanda 1: 
Creare una variabile che contiene la stringa "Epicode", quindi stamparla a video.
"""

variabile = "Epicode"
print(variabile)

"""
Domanda 2: 
Abbiamo la stringa: nome_scuola = "Epicode"; stampare l'iniziale.
"""

nome_scuola = "Epicode"
print(nome_scuola[0])

"""
Domanda 3: 
Abbiamo la stringa: nome_scuola = "Epicode"; stampare le prime tre lettere.
"""

nome_scuola = "Epicode"
print(nome_scuola[0:3])

"""
Domanda 4: 
Abbiamo la stringa: nome_scuola = "Epicode"; stampare la stringa trasformando tutte le lettere in maiuscole.
"""

nome_scuola = "Epicode"
print(nome_scuola.upper())

"""
Domanda 5: 
Abbiamo la variabile: x = 10. Incrementarla di 2 e poi moltiplicarla per 3.
"""

# Di seguito metodi differenti per la soluzione

x = 10
x = x + 2
x = x * 3
print(int(x))

x = 10
x += 2
x *= 3
print(int(x))

x = 10
x = x.__add__(2)
x = x.__mul__(3)
print(int(x))

""" 
Domanda 6: 
Scriviamo un programma che chiede all'utente in input:

                • i litri di benzina nel serbatoio
                • l'efficienza espressa in km per litro
                • il prezzo della benzina per litro

                    quindi, visualizza il costo per 100 km.
"""

# Input dati per l'utente

nome_utente = str(input("Come ti chiami?"))
litri_carburante_disponibili = float(input("Ciao " + nome_utente + "! Quanti litri di benzina ci sono nel serbatoio?"))
efficienza_km_per_litro = float(input("Quanti chilometri percorri con 1 litro?"))
prezzo_carburante = float(input("Qual è il prezzo della benzina per litro?"))

# Calcolo della distanza in kilometri percorribile dall'auto con i litri di carburante a disposizione ( extra che ritengo sia utile all'utente )

distanza_percorsa = litri_carburante_disponibili * efficienza_km_per_litro

# Calcolo del costo del carburante per una percorrenza di 100 kilometri 

costo_100_km = (100 / efficienza_km_per_litro) * prezzo_carburante

# Mostra il risultato all'utente (con uso di operatori e metodo .format() simultaneamente)

risposta1 = str("Grazie per i dati forniti, " + nome_utente + "! L'auto può percorrere {} km con i litri di carburante disponibili.")
risposta2 = str("Il costo del carburante per 100 km è di €{}.")

print(risposta1.format(distanza_percorsa))
print(risposta2.format(costo_100_km))

# In alternativa, possiamo snellire il codice come riportato di seguito

risposta = str("Grazie per i dati forniti, " + nome_utente + "! L'auto può percorrere {0} km con i litri di carburante disponibili.\nIl costo del carburante per 100 km è di €{1}.")

print(risposta.format(distanza_percorsa,costo_100_km))

"""
Domanda 7: 
Scriviamo un programma che chiede in input all'utente una stringa e 
visualizza i primi 3 caratteri, seguiti da 3 punti di sospensione e quindi gli ultimi 3 caratteri.
"""

stringa_input = str(input("Quale sistema operativo utilizzi?"))
print(stringa_input[0:3] + "..." + stringa_input[-3:])

"""
Domanda 8: 
Verificare, per ognuna delle seguenti stringhe, se il numero di caratteri è
compreso tra 5 e 8:
• Epicode
• Windows
• Excel
• Powerpoint
• Word.
"""

stringhe = ["Epicode", "Windows", "Excel", "Powerpoint", "Word"]

for x in stringhe:
    if 5 <= len(x) <= 8:
        risposta_1 ="{} ha un numero di caratteri compreso tra 5 e 8."
        print(risposta_1.format(x))
    else:
        risposta_2 = "{} non ha un numero di caratteri compreso tra 5 e 8."
        print(risposta_2.format(x))

"""
Domanda 9: 
Abbiamo la seguente lista di codici prodotto:

codici = ["knt-S1", "cba-G9", "qtr-Z8"]

Per ognuno dei codici, estrarre la parte finale (gli ultimi tre caratteri, quindi
trattino incluso) e memorizzarlo in tre variabili.
"""

codici = ["knt-S1", "cba-G9", "qtr-Z8"]
codice_1 = codici[0]
codice_2 = codici[1]
codice_3 = codici[2]
print(str(codice_1[-3:]), codice_2[-3:], codice_3[-3:])

"""
Domanda 10: 
Abbiamo la seguente lista di codici prodotto:

codici = ["knt-S1", "cba-G9", "qtr-Z8"]

Per ognuno dei codici, estrarre la parte finale (gli ultimi tre caratteri, quindi
trattino incluso) e memorizzarli in una nuova lista.
"""

codici = ["knt-S1", "cba-G9", "qtr-Z8"]
nuova_lista = [codici[0][-3:], codici[1][-3:], codici[2][-3:]]
print(str(nuova_lista))

# In alternativa, possiamo utilizzare le variabili definite nel quesito precedente

nuova_lista = [codice_1[-3:], codice_2[-3:], codice_3[-3:]]
print(str(nuova_lista))

"""
Domanda 11: 

1 - Abbiamo un insieme (set) di titoli di azioni "growth" (cioè che hanno una crescita dei
ricavi maggiore della media):

growth = {"Tesla", "Shopify", "Block", "Etsy", "MercadoLibre",
"Netflix", "Amazon", "Meta Platforms", "Salesforce", "Alphabet"}

Abbiamo un insieme di titoli "value" (cioè titoli che offrono agli investitori un elevato
ritorno, garantendo al contempo stabilità e sicurezza):

value = {"Pfizer", "Johnson & Johnson", "JPMorgan Chase & Co.",
"Wells Fargo & Co.", "Verizon Communications", "BP PLC",
"LyondellBasell Industries", "MetLife", "Interactive Brokers Group",
"Intel"}

2- Abbiamo un insieme di titoli di aziende ad alta tecnologia:

tech = {"Apple", "Microsoft", "Alphabet", "Amazon", "NVIDIA", "Meta Platforms",
"Tesla", "Alibaba", "Salesforce", "Advanced Micro
Devices", "Intel", "PayPal", "Activision Blizzard", "Electronic
Arts", "The Trade Desk", "Zillow Group", "Match Group", "Yelp"}

Abbiamo un insieme di titoli di aziende nell'healthcare:

healthcare = {"UnitedHealth Group", "Johnson & Johnson", "Eli Lilly & Co.", "Novo Nordisk", "Merck & Co.", "Roche Holding", "Pfizer",
"Thermo Fisher Scientific", "Abbott Laboratories"}

3- Un investitore vuole sapere:

• se vuole diversificare l'investimento, investendo in aziende growth e value,
quali sono le aziende?
• quali sono le aziende tecnologiche growth?
• se vuole investire sia in aziende tecnologiche che value, quali deve
considerare?
• quali sono i titoli healthcare che non sono value?
• ci sono aziende sia tech che healthcare?
• in quali deve investire se vuole azioni tech ma solo se siano growth o value?

"""

# Di seguito due alternative di risposta per ognuno dei punti richiesti, utilizzando caratteri dedicati o funzioni ad-hoc in Python.

growth = {"Tesla", "Shopify", "Block", "Etsy", "MercadoLibre", "Netflix", "Amazon", "Meta Platforms", "Salesforce", "Alphabet"}
value = {"Pfizer", "Johnson & Johnson", "JPMorgan Chase & Co.", "Wells Fargo & Co.", "Verizon Communications", "BP PLC", "LyondellBasell Industries", "MetLife", "Interactive Brokers Group", "Intel"}
tech = {"Apple", "Microsoft", "Alphabet", "Amazon", "NVIDIA", "Meta Platforms", "Tesla", "Alibaba", "Salesforce", "Advanced Micro Devices", "Intel", "PayPal", "Activision Blizzard", "Electronic Arts", "The Trade Desk", "Zillow Group", "Match Group", "Yelp"}
healthcare = {"UnitedHealth Group", "Johnson & Johnson", "Eli Lilly & Co.", "Novo Nordisk", "Merck & Co.", "Roche Holding", "Pfizer", "Thermo Fisher Scientific", "Abbott Laboratories"}

print( "Per diversificare l'investimento, investendo in aziende growth e value, investire in:", growth | value)
print( "Per diversificare l'investimento, investendo in aziende growth e value, investire in:", growth.union(value))

print("Le aziende tecnologiche growth sono:", growth & tech)
print("Le aziende tecnologiche growth sono:", growth.intersection(tech))

print("Le aziende sia tecnologiche che value sono:", value & tech)
print("Le aziende sia tecnologiche che value sono:", value.intersection(tech))

print("I titoli healthcare che non sono value sono:", healthcare - value)
print("I titoli healthcare che non sono value sono:", healthcare.difference(value))

print("Le aziende sia tech che healthcare sono:", tech & healthcare) # Con i dati a disposizione, il risultato è un insieme vuoto ---> set()
print("Le aziende sia tech che healthcare sono:", tech.intersection(healthcare)) # Con i dati a disposizione, il risultato è un insieme vuoto ---> set()

print("Per investire in azioni tech, ma solo se growth o value, investire in:", (growth | value) & tech)
print("Per investire in azioni tech, ma solo se growth o value, investire in:", (growth.intersection(value)).union(tech))