
"""
Domanda 1: Creare una variabile che contiene la stringa "Epicode", quindi stamparla a
video.
"""

variabile = "Epicode"
print(variabile)

"""
Domanda 2: Abbiamo la stringa: nome_scuola = "Epicode"; Stampare l'iniziale.
"""

nome_scuola = "Epicode"

"""
Domanda 3: Abbiamo la stringa: nome_scuola = "Epicode"; Stampare le prime tre lettere.
"""



"""
Domanda 4: Abbiamo la stringa: nome_scuola = "Epicode"; Stampare la stringa trasformando tutte le lettere in maiuscole.
"""



"""
Domanda 5: Abbiamo la variabile: x = 10; incrementarla di 2 e poi moltiplicarla per 3. Usare due metodi diversi!
"""



""" 
Domanda 6: Scriviamo un programma che chiede all'utente in input:
• i litri di benzina nel serbatoio
• l'efficienza espressa in km per litro
• il prezzo della benzina per litro
e quindi visualizza il costo per 100 km 
"""



"""
Domanda 7: Scriviamo un programma che chiede in input all'utente una stringa e visualizza i
primi 3 caratteri, seguiti da 3 punti di sospensione e quindi gli ultimi 3 caratteri.
"""



"""
Domanda 8: Verificare, per ognuna delle seguenti stringhe, se il numero di caratteri è
compreso tra 5 e 8:
• Epicode
• Windows
• Excel
• Powerpoint
• Word.
"""



"""
Domanda 9: Abbiamo la seguente lista di codici prodotto:
codici = ["knt-S1", "cba-G9", "qtr-Z8"]
Per ognuno dei codici, estrarre la parte finale (gli ultimi tre caratteri, quindi
trattino incluso) e memorizzarlo in tre variabili.
"""



"""
Domanda 10: Abbiamo la seguente lista di codici prodotto:
codici = ["knt-S1", "cba-G9", "qtr-Z8"]
Per ognuno dei codici, estrarre la parte finale (gli ultimi tre caratteri, quindi
trattino incluso) e memorizzarli in una nuova lista.
"""



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

tech = {"Apple", "Microsoft", "Alphabet", "Amazon", "NVIDIA", "Meta
Platforms", "Tesla", "Alibaba", "Salesforce", "Advanced Micro
Devices", "Intel", "PayPal", "Activision Blizzard", "Electronic
Arts", "The Trade Desk", "Zillow Group", "Match Group", "Yelp"}

Abbiamo un insieme di titoli di aziende nell'healthcare:

healthcare = {"UnitedHealth Group", "Johnson & Johnson", "Eli Lilly
& Co.", "Novo Nordisk", "Merck & Co.", "Roche Holding", "Pfizer",
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

print( "Per diversificare l'investimento, investendo in aziende growth e value, investire nelle seguenti aziende:", growth | value)
print( "Per diversificare l'investimento, investendo in aziende growth e value, investire nelle seguenti aziende:", growth.union(value))

print("Le aziende tecnologiche growth sono le seguenti:", growth & tech)
print("Le aziende tecnologiche growth sono le seguenti:", growth.intersection(tech))

print("Le aziende tecnologiche growth sono le seguenti:", value & tech)
print("Le aziende tecnologiche growth sono le seguenti:", value.intersection(tech))

print("Le aziende tecnologiche growth sono le seguenti:", healthcare - value)
print("Le aziende tecnologiche growth sono le seguenti:", healthcare.difference(value))

print("Le aziende tecnologiche growth sono le seguenti:", tech & healthcare)
print("Le aziende tecnologiche growth sono le seguenti:", tech.intersection(healthcare))

print("Le aziende tecnologiche growth sono le seguenti:", (growth | value) & tech)
print("Le aziende tecnologiche growth sono le seguenti:", (growth.intersection(value)).union(tech))