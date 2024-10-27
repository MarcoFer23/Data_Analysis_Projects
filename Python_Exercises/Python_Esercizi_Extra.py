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
    starter = starter - 1 # Uguale a: starter -= 1
print("parola invertita :", parola_invertita)

# Soluzione Andrea

nome_stringa= str((input("Inserisci una stringa da invertire: ")))
i = len(nome_stringa) - 1
while i >= 0:
    print(nome_stringa[i], end = '')
    i = i - 1

# Alternative Marco: 1    

stringa = input("Scrivi un messaggio da inviare nel Cyberspazio!")

contrario = list()

for x in stringa:
    contrario.insert(0,x) # Con questa sintassi, il programma inserisce ogni carattere della stringa sempre in posizione 0, e proseguendo nel ciclo scriverà l'input iniziale al contrario

print(" ".join(contrario))

# Alternative Marco: 2

stringa = input("Scrivi un messaggio da inviare nel Cyberspazio!")

for x in range(len(stringa),0,-1): # len(stringa) rappresenta il valore iniziale, 0 rappresenta il valore finale, -1 rappresenta lo step per procedere nel ciclo
    print(stringa[x-1], " ", end="")

"""
Esercizio 2: Filtraggio di Liste
Scrivi un programma Python che chiede all'utente di inserire una lista di numeri e poi utilizza un ciclo while e istruzioni if per filtrare e stampare solo i numeri pari dalla lista.
"""

# Soluzione con ciclo while:

stringa = input("Inserisci una lista di numeri separati da spazi: ")
numeri = stringa.split()  # Divide la stringa in una lista di stringhe
numeri_pari = []
i = 0

while i < len(numeri):
    try:
        num = int(numeri[i])  # Converte la stringa in un numero intero
        if num % 2 == 0:
            numeri_pari.append(num)
    except ValueError:
        # In questo modo vengono ignorate le stringhe che non possono essere convertite in numeri
        pass
    i += 1

print("Numeri pari nella lista:", numeri_pari)    

# Soluzione con ciclo for:

stringa = input("Inserisci una lista di numeri separati da spazi: ")
numeri = stringa.split()  # Divide la stringa in una lista di stringhe
numeri_pari = []

for num in numeri:
    try:
        num = int(num)  # Converte la stringa in un numero intero
        if num % 2 == 0:
            numeri_pari.append(num)
    except ValueError:
        # In questo modo vengono ignorate le stringhe che non possono essere convertite in numeri
        pass

print("Numeri pari nella lista:", numeri_pari)    

"""
Esercizio 3: Validazione delle Password
Crea un programma Python che chiede all'utente di inserire una password. Utilizza un ciclo while e istruzioni if per verificare se la password inserita soddisfa i seguenti criteri:

Lunga almeno 8 caratteri.
Contiene almeno una lettera maiuscola.
Contiene almeno una lettera minuscola.
Contiene almeno una cifra.
Stampa un messaggio che indica se la password è valida o no.
"""

password = input("Inserisci una password: ")

# Inizializzazione delle variabili True / False per tenere traccia dei criteri di validazione

lunghezza_valida = False
ha_maiuscole = False
ha_minuscole = False
ha_cifre = False

# Verifica dei criteri uno ad uno
while not lunghezza_valida or not ha_maiuscole or not ha_minuscole or not ha_cifre:
    # 1. Verifica la lunghezza della password
    if len(password) >= 8:
        lunghezza_valida = True
    else:
        print("La password deve essere lunga almeno 8 caratteri.")
        password = input("Inserisci una nuova password: ")

    # 2. Verifica se la password contiene almeno una lettera maiuscola
    if any(char.isupper() for char in password):
        ha_maiuscole = True
    else:
        print("La password deve contenere almeno una lettera maiuscola.")
        password = input("Inserisci una nuova password: ")

    # 3. Verifica se la password contiene almeno una lettera minuscola
    if any(char.islower() for char in password):
        ha_minuscole = True
    else:
        print("La password deve contenere almeno una lettera minuscola.")
        password = input("Inserisci una nuova password: ")

    # 4. Verifica se la password contiene almeno una cifra
    if any(char.isdigit() for char in password):
        ha_cifre = True
    else:
        print("La password deve contenere almeno una cifra.")
        password = input("Inserisci una nuova password: ")

# Se tutte le verifiche sono passate, la password è valida e stampa il messaggio "La password è valida."
print("La password è valida.")

"""
Esercizio 4: Verifica dei Palindromi
Scrivi un programma Python che chiede all'utente di inserire una stringa e verifica se è un palindromo 
(una parola, frase, numero o altra sequenza di caratteri che si legge allo stesso modo in avanti e all'indietro). 
Utilizza un ciclo while e istruzioni if per effettuare il controllo e fornire un feedback appropriato.
"""

input_string = input("Inserisci una stringa: ")

# La sintassi di seguito rimuove spazi e converte la stringa in lettere minuscole (potremmo anche convertire il tutto il maiuscole)
# La distinzione tra maiuscole e minuscole non è utile ai fini dell'esercizio: quel che ci interessa è che la parola data si "legga" allo stesso modo

input_string = input_string.replace(" ", "").lower()

# Inizializzazione di due indici, uno all'inizio e uno alla fine della stringa
# len restituisce il numero di oggetti in una stringa, ma non parte da 0, quindi dobbiamo escludere il valore finale aggiungendo - 1 per usare l'indice

start = 0
end = len(input_string) - 1 

# Inizializzazione di un ciclo while che continua finché gli indici non si incrociano
while start < end:
    # Verifica se i caratteri agli indici correnti sono diversi
    if input_string[start] != input_string[end]:
        print("La stringa non è un palindromo.")
        break  # Se la stringa non è un palindromo, con "break" usciamo dal ciclo
    # Per spostare gli indici verso il centro della stringa, incrementiamo il valore di start e diminuiamo il valore di end
    start += 1 # Uguale a: start = start + 1
    end -= 1 # Uguale a: end = end - 1
else:
    # Se il ciclo while termina senza interruzioni, la stringa è un palindromo
    print("La stringa è un palindromo.")

"""
Esercizio 5: Gioco dell'impiccato
Crea un gioco in cui il programma seleziona una parola casuale da una lista predefinita e l'utente deve indovinare la parola lettera per lettera. Utilizza un ciclo while e istruzioni if per guidare l'utente e fornire feedback. Includi un limite al numero di tentativi errati consentiti e dai un suggerimento se l'utente si blocca.
"""

import random

err = False

death_man = ["	 _______","	|	|","	|	|","	|      ( )",'	|      /|\ ',"	|	|","	|      / \ ","	| ","  ______|______"," |__GAME_OVER__|\n "]

dm_count = 0
err_count = 0
lett_list = []
hint_count = 0

err_msg = str("La lettera che hai inserito non si trova nella parola, mi dispiace =(\nFino ad ora queste lettere non sono presenti: ")

parole_giocabili_3 = ['ABC', 'ABS', 'ACE', 'ADE', 'ADI', 'AFA', 'AFE', 'AGA', 'AGI', 'AGO', 'AHI', 'AHM', 'AHO', 'AIA', 'AIE', 'AIO', 'ALA', 'ALE', 'ALI', 'ALO', 'ALT', 'AMA', 'AMI', 'AMO', 'ANA', 'ANE', 'ANI', 'ANO', 'AOH', 'APE', 'API', 'APO', 'ARA', 'ARE', 'ARF', 'ARI', 'ARM', 'ARO', 'ASA', 'ASL', 'ATA', 'ATI', 'ATO', 'ATP', 'AUF', 'AVA', 'AVE', 'AVI', 'AVO', 'BAH', 'BAI', 'BAO', 'BAR', 'BAU', 'BEA', 'BEE', 'BEH', 'BEI', 'BEL', 'BEN', 'BEO', 'BER', 'BEV', 'BEY', 'BIG', 'BIO', 'BIP', 'BIS', 'BIT', 'BLE', 'BLU', 'BOA', 'BOB', 'BOE', 'BOH', 'BON', 'BOP', 'BOT', 'BOX', 'BOY', 'BRA', 'BRR', 'BUA', 'BUE', 'BUG', 'BUH', 'BUI', 'BUM', 'BUS', 'BUU', 'CAB', 'CAD', 'CAI', 'CAM', 'CAN', 'CAP', 'CAR', 'CCT', 'CEL', 'CEN', 'CHE', 'CHI', 'CIF', 'CIN', 'CIO', 'CIP', 'COC', 'COI', 'COL', 'COM', 'CON', 'COR', 'CQR', 'CRA', 'CRI', 'CRU', 'CSI', 'CUI', 'DAE', 'DAI', 'DAL', 'DAN', 'DAR', 'DEA', 'DEB', 'DEE', 'DEH', 'DEI', 'DEL', 'DEO', 'DIA', 'DIE', 'DII', 'DIN', 'DIO', 'DIR', 'DNA', 'DOC', 'DOH', 'DOI', 'DOM', 'DON', 'DOT', 'DRY', 'DUA', 'DUB', 'DUE', 'DUI', 'DUO', 'DVD', 'EBE', 'ECO', 'ECU', 'EGO', 'EHI', 'EHM', 'EIA', 'ELA', 'EME', 'EMI', 'EMU', 'ENE', 'EOA', 'EOE', 'EOI', 'EOO', 'EPA', 'EPE', 'EPO', 'ERA', 'ERE', 'ERG', 'ERI', 'ERO', 'EST', 'ETA', 'EVA', 'EVE', 'EVI', 'EVO', 'FAE', 'FAI', 'FAN', 'FAO', 'FAQ', 'FAR', 'FAS', 'FAX', 'FEA', 'FEI', 'FEN', 'FEO', 'FER', 'FEZ', 'FIA', 'FIE', 'FII', 'FIL', 'FIN', 'FIO', 'FIX', 'FOB', 'FON', 'FOR', 'FOT', 'FRA', 'FUE', 'FUI', 'GAG', 'GAI', 'GAL', 'GAP', 'GAS', 'GAY', 'GAZ', 'GEL', 'GEV', 
'GIA', 'GIN', 'GIO', 'GIP', 'GIU', 'GLI', 'GNE', 'GNU', 'GOA', 'GOI', 'GOL', 'GPS', 'GRO', 'GRU', 'GUA', 'GUP', 'HAC', 'HAG', 'HAI', 'HAN', 'HEI', 'HEM', 'HIP', 'HIT', 'HIV', 'HMM', 'HOI', 'HOP', 'HUB', 'HUC', 'HUI', 'HUM', 'IBI', 'ICI', 'ICS', 'IDI', 'IDO', 'IFA', 'IFE', 'ILA', 'ILE', 'ILI', 'ILO', 'IMA', 'IME', 'IMI', 'IMO', 'INA', 'INE', 'INI', 'INO', 'IOD', 'IRA', 'IRE', 'IRI', 'IRO', 'ISO', 'ITA', 'ITE', 'ITI', 'ITO', 'IUD', 'IUS', 'IVA', 'IVE', 'IVI', 'IVO', 'JAB', 'JAY', 'JET', 'JOB', 'KAT', 'KEV', 'KIP', 'KIT', 'KIU', 'KYU', 'LAE', 'LAI', 'LAO', 'LEA', 'LED', 'LEE', 'LEI', 'LEK', 'LEL', 'LEM', 'LEO', 'LEU', 'LEV', 'LIE', 'LOB', 'LOG', 'LOR', 'LOW', 'LSD', 'LUE', 'LUI', 'LUX', 'MAE', 'MAH', 'MAI', 'MAL', 'MAN', 'MAO', 'MAR', 'MAS', 'MAT', 'MAX', 'MEA', 'MEE', 'MEI', 'MEL', 'MEN', 'MEO', 'MEV', 'MHO', 'MIA', 'MIE', 'MIO', 'MIX', 'MMH', 'MMS', 'MOA', 'MOB', 'MOD', 'MOL', 'MOU', 'MPS', 'NAA', 'NED', 'NEH', 'NEI', 'NEL', 'NEO', 'NET', 'NIP', 'NIT', 'NIX', 'NOA', 'NOE', 'NOI', 'NOL', 'NON', 'NOO', 'NUI', 'NUT', 'OBI', 'OCA', 'ODA', 'ODE', 'ODI', 'ODO', 'OFF', 'OGM', 'OHE', 'OHI', 'OHM', 'OIL', 'OLA', 'OLE', 'OLI', 'OMO', 'ONG', 'ONI', 'OPA', 'OPS', 'OPV', 'ORA', 'ORE', 'ORI', 'ORO', 'OSA', 'OSE', 'OSI', 'OSO', 'OUT', 'OVA', 'OVE', 'OVI', 'OVO', 'OZI', 'PAF', 'PAM', 'PAR', 'PAT', 'PEI', 'PEL', 'PER', 'PET', 'PHI', 'PIA', 'PIE', 'PIF', 'PII', 'PIL', 'PIM', 'PIN', 'PIO', 'PIU', 'PNL', 'POA', 'POE', 'POH', 'POI', 'POP', 'POR', 'POS', 'PRE', 'PRM', 'PRO', 'PRR', 'PSI', 'PSS', 'PST', 'PUB', 'PUF', 'PUH', 'PUI', 'PUM', 'PUO', 'PUR', 'PUS', 'PUT', 'PVC', 'QAT', 'QUA', 'QUE', 'QUI', 'RAD', 'RAI', 'RAK', 'RAM', 'RAP', 'RAS', 'REA', 'REE', 'REG', 'REI', 'REM', 'REO', 'RHO', 'RIA', 'RIE', 'RII', 'RIO', 'RNA', 'ROE', 'ROI', 'ROM', 'ROS', 'RUA', 'RUE', 'RUI', 'RUM', 'RUO', 'SAI', 'SAN', 'SAO', 'SAX', 'SCI', 'SDA', 'SDO', 'SED', 'SEI', 'SEL', 'SEN', 'SER', 'SET', 'SFA', 'SFO', 'SIA', 'SIC', 'SIE', 'SII', 'SIM', 'SIN', 'SIO', 'SIR', 'SKA', 'SKI', 'SME', 'SMS', 'SOB', 'SOL', 'SON', 'SOR', 'SOS', 'SPA', 'SPI', 'SSH', 'SSS', 'SST', 'STA', 'STE', 'STI', 'STO', 'SUA', 'SUB', 'SUD', 'SUE', 'SUI', 'SUK', 'SUL', 
'SUO', 'SUQ', 'SUR', 'SUV', 'TAC', 'TAF', 'TAG', 'TAI', 'TAL', 'TAN', 'TAO', 'TAR', 'TAU', 'TBC', 'TEA', 'TEE', 'TEK', 'TEL', 'TEN', 'TEP', 'TER', 'TEV', 'THE', 'TIC', 'TIE', 'TIR', 'TOC', 'TOE', 'TOH', 'TOI', 'TON', 'TOP', 'TOR', 'TOT', 'TRA', 'TRE', 'TSH', 'TUA', 'TUE', 'TUI', 'TUO', 'TUS', 'UBI', 'UDI', 'UFF', 'UFO', 'UHI', 'UHM', 'UMI', 'UMO', 'UNA', 'UNE', 'UNI', 'UNO', 'URI', 'URL', 'URO', 'USA', 'USE', 'USI', 'USO', 'UVA', 'UVE', 'VAH', 'VAI', 'VAL', 'VAN', 'VAR', 'VAS', 'VEH', 'VEI', 'VEL', 'VEN', 'VER', 'VES', 'VIA', 'VIE', 'VIP', 'VIS', 'VOI', 'VOV', 'VUI', 'VUO', 'WAD', 'WEB', 'WIT', 'WOK', 'WON', 'WOW', 'YAK', 'YEN', 'YIN', 'ZAC', 'ZAF', 'ZAR', 'ZEN', 'ZIA', 'ZIC', 'ZIE', 'ZIF', 'ZII', 'ZIO', 'ZIP', 'ZOO', 'ZUM', 'ZZZ']

parole_giocabili_4 = ['ABBI', 'ENFI', 'EOLI', 'ENTI', 'ENTE', 'ENNO', 'ENNE', 'ENNA', 'ENEO', 'EONI', 'ENEI', 'ENEE', 'ENEA', 'ENDE', 'EMPI', 'EMMI', 'EONE', 'EPOS', 'EMBE', 'EREI', 'ERMA', 'ERGO', 'ERGI', 'ERGE', 'ERGA', 'EREO', 'EREE', 'EQUA', 'EREA', 'ERBI', 'ERBE', 'ERBA', 'EQUO', 'EQUI', 'EQUE', 'EMME', 'ELUI', 'ERMI', 'EGUI', 'ELCI', 'ELCE', 'EIRA', 'EIME', 'EIBO', 'EGUO', 'EGUA', 'ELEE', 'EGRO', 'EGRI', 'EGRE', 'EGRA', 'EGLI', 'EGEO', 'EGEI', 'ELEA', 'ELEI', 'ELSO', 'ELLI', 'ELSI', 'ELSE', 'ELSA', 'ELMO', 'ELMI', 'ELLO', 'ELLE', 'ELEO', 'ELLA', 'ELIO', 'ELII', 'ELIE', 'ELIA', 'ELFO', 'ELFI', 'ERME', 'ERMO', 'EGEA', 'FALA', 'FAMO', 'FAMI', 'FAME', 'FAMA', 'FALO', 'FALE', 'FAGO', 'FANI', 'FAGI', 'FADO', 'FADI', 'FADE', 'FADA', 'FACI', 'FANE', 'FANO', 'EXPO', 'FATI', 'FAXA', 'FAVO', 'FAVI', 'FAVE', 'FAVA', 'FATO', 'FATE', 'FARA', 'FATA', 'FASI', 'FASE', 'FARO', 'FARI', 'FARE', 'FARD', 'FACE', 'EXIT', 'EROE', 'ERTA', 'ESCI', 'ESCE', 'ESCA', 'ERTO', 'ERTI', 'ERTE', 'ERSI', 'ESSA', 'ERSE', 'ERRO', 'ERRI', 'ERRE', 'ERRA', 'EROS', 'EROI', 'ESCO', 'ESSE', 'EVVI', 'ETTI', 'EVOE', 'EVIE', 'EVIA', 'EURO', 'EURI', 'ETTO', 'ETTE', 'ESSI', 'ETRA', 'ETCI', 'ESTO', 'ESTI', 'ESTE', 'ESTA', 'ESSO', 'EGEE', 'EFOD', 'FAXO', 'DEVA', 'DICI', 'DICE', 'DICA', 'DEVO', 'DEVI', 'DEVE', 'DEST', 'DIDI', 'DESK', 'DEMO', 'DEMI', 'DELO', 'DELI', 'DELE', 'DICO', 'DIDO', 'DEGU', 'DIRO', 'DIVE', 'DIVA', 'DITO', 'DITI', 'DITE', 'DITA', 'DIRI', 'DIEL', 'DIRE', 'DIRA', 'DINE', 'DINA', 'DIME', 'DIMA', 'DIGA', 'DELA', 'DECO', 'DIVO', 'DADI', 'DAME', 'DAMA', 'DAIO', 'DAIE', 'DAGA', 'DADO', 'DADA', 'DAMO', 'DACO', 'DACI', 'DACE', 'DACA', 'CZAR', 'CUTI', 'CUTE', 'DAMI', 'DAPE', 'DECK', 'DATO', 'DECE', 'DECA', 'DAZI', 'DAVO', 'DAVI', 'DAVA', 'DATI', 'DAPI', 'DATE', 'DATA', 'DARO', 'DARK', 'DARI', 'DARE', 'DARA', 'DIVI', 'DOCE', 'EFFE', 'DUMO', 'DURE', 'DURA', 'DUOI', 'DUNE', 'DUNA', 'DUMY', 'DUMI', 'DURO', 'DUMA', 'DUCO', 'DUCI', 'DUCE', 'DUCA', 'DUBI', 'DURI', 'EASY', 'DRIN', 'ECRU', 'EDUO', 'EDUI', 'EDUE', 'EDUA', 'EDEN', 'EDAM', 
'ECHI', 'EBBE', 'ECCO', 'ECCI', 'EBRO', 'EBRI', 'EBRE', 'EBRA', 'EBBI', 'DROP', 'DRAP', 'DOCK', 'DOLO', 'DONG', 'DONA', 'DOMO', 'DOMI', 'DOME', 'DOMA', 'DOLI', 'DONO', 'DOLA', 'DOGO', 'DOGI', 'DOGE', 'DOGA', 'DODO', 'DODI', 'DONI', 'DONT', 'DOWN', 'DOSI', 'DOVE', 'DOTO', 'DOTI', 'DOTE', 'DOTA', 'DOSO', 'DOSE', 'DOPA', 'DOSA', 'DORO', 'DORI', 'DORA', 'DOPO', 'DOPI', 'DOPE', 'FAXI', 'FECE', 'CURI', 'GRRR', 'GUFA', 'GUAR', 'GUAI', 'GRUP', 'GRUE', 'GRUA', 'GROS', 'GUFO', 'GROG', 'GRIP', 'GRES', 'GRAY', 'GRAN', 'GOTO', 'GUFI', 'GULI', 'GOTE', 'HIGH', 'HOST', 'HOPI', 'HOOK', 'HOMO', 'HOME', 'HOBO', 'HELP', 'GULO', 'HARD', 'HALO', 'HALL', 'HALI', 'HAIK', 'GURU', 'GULP', 'GOTI', 'GOTA', 'HULA', 'GIRO', 'GIVA', 'GIUE', 'GITO', 'GITI', 'GITE', 'GITA', 'GIRL', 'GIVO', 'GIRI', 'GIRE', 'GIRA', 'GIOI', 'GILL', 'GILE', 'GILA', 'GIVI', 'GLIA', 'GORE', 'GOGO', 'GORA', 'GONG', 'GOMI', 'GOLF', 'GOLE', 'GOLA', 'GODO', 'GLIE', 'GODI', 'GODE', 'GODA', 'GOAL', 'GNAU', 'GNAO', 'GNAM', 'HUCO', 'HUTU', 'GHIE', 'IOGA', 'IOTA', 'IOSA', 'IONI', 'IONE', 'IOLI', 'IOLE', 'IODI', 'IPOD', 'IOCO', 'INSU', 'INNO', 'INNI', 'INKA', 'INIE', 'IOTE', 'IRAI', 'INGA', 'IRMI', 'IRTO', 'IRTI', 'IRTE', 'IRTA', 'IRSI', 'IRNE', 'IRLO', 'IRAP', 'IRLI', 'IRLE', 'IRLA', 'IRIS', 'IREI', 'IRCO', 'IRCI', 'INIA', 'INFO', 'IACE', 'IDEI', 'IENE', 'IENA', 'IDRE', 'IDRA', 'IDEO', 'IDEM', 'IDEE', 'IGLO', 'IDEA', 'IBIS', 'IATO', 'IATI', 'IANO', 'IANI', 'IACI', 'IERI', 'IGLU', 'INFI', 'IMPI', 'INDU', 'INDO', 'INDI', 'INDE', 'INDA', 'INCA', 'IMAN', 'IGNE', 'IMAM', 'ILOR', 'ILIO', 'ILII', 'ILEO', 'ILEI', 'IGNI', 'GIGA', 'GHIA', 'FECI', 'FIRN', 'FLAN', 'FLAG', 'FISO', 'FISI', 'FISE', 'FISA', 'FIOR', 'FLAT', 'FINO', 'FINN', 'FINI', 'FINE', 'FINA', 'FIMO', 'FLAP', 'FLIP', 'FILO', 'FODI', 'FOLE', 'FOLA', 'FOIE', 'FOIA', 'FOHN', 'FOGA', 'FOCO', 'FLIT', 'FOCI', 'FOCE', 'FOCA', 'FLUO', 'FLUI', 'FLOU', 'FLOP', 'FIMI', 'FILM', 'FONA', 'FERA', 'FETA', 'FESE', 'FESA', 'FERO', 'FERI', 'FERE', 'FENE', 'FETI', 'FELI', 'FELE', 'FEED', 'FEDO', 'FEDI', 'FEDE', 'FEDA', 'FETE', 'FETO', 'FILI', 'FIFO', 'FILE', 'FILA', 'FIGO', 'FIGI', 'FIGE', 'FIGA', 'FIFE', 'FIAT', 'FIFA', 'FIDO', 'FIDI', 'FIDE', 'FIDA', 'FICO', 'FICA', 'FOLK', 'FONI', 'GETO', 'GANG', 'GASP', 'GASO', 'GASI', 'GASA', 'GARE', 'GARA', 'GAME', 'GATO', 'GALE', 'GALA', 'GAIO', 
'GAIE', 'GAIA', 'GAGI', 'GATE', 'GAZA', 'GAGA', 'GEMO', 'GETI', 'GESU', 'GENO', 'GENI', 'GENE', 'GENA', 'GEMI', 'GAZI', 'GEME', 'GEMA', 'GELO', 'GELI', 'GELA', 'GECO', 'GAZO', 'GAGE', 'FUTE', 'FONO', 'FRAC', 'FUIA', 'FUGO', 'FUGA', 'FUCO', 'FRUO', 'FRUI', 'FOTO', 'FUIO', 'FORO', 'FORM', 'FORI', 'FORE', 'FORA', 'FOOD', 'FONT', 'FUIE', 'FULL', 'FUTA', 'FURE', 'FUSO', 'FUSI', 'FUSE', 'FUSA', 'FURO', 'FURI', 'FURA', 'FUMA', 'FUOR', 'FUNK', 'FUNI', 'FUNE', 'FUMO', 'FUMI', 'FUME', 'CURO', 'CURE', 'ABBO', 'ATEA', 'ATRI', 'ATRE', 'ATRA', 'ATEO', 'ATEI', 'ATEE', 'ATAI', 'ATTA', 'ASTI', 'ASTE', 'ASTA', 'ASSO', 'ASSI', 'ASSE', 'ATRO', 'ATTE', 'ASPI', 'AUNA', 'AURI', 'AURE', 'AURA', 'AUNO', 'AUNI', 'AUNE', 'AULE', 'ATTI', 'AULA', 'AUGE', 'AUFF', 'AUDO', 'AUDI', 'AUDE', 'ATTO', 'ASPO', 'ASPE', 'AUSA', 'ARII', 'ARPA', 'ARMO', 'ARMI', 'ARME', 'ARMA', 'ARIO', 'ARIE', 'ARRA', 'ARIA', 'ARGO', 'AREO', 'AREM', 'AREI', 'AREE', 'AREA', 'ARPE', 'ARRE', 'ASPA', 'ARVA', 'ASMI', 'ASME', 'ASMA', 'ASCO', 'ASCI', 'ASCE', 'ARTO', 'ARRI', 'ARTI', 'ARTE', 'ARTA', 'ARSO', 'ARSI', 'ARSE', 'ARSA', 'AURO', 'AUSE', 'ARDI', 'BEAR', 'BEEP', 'BEEN', 'BECO', 'BECA', 'BEBE', 'BEAT', 'BEAI', 'BELA', 'BAVE', 'BAVA', 'BAUD', 'BASO', 'BASI', 'BASE', 'BEGA', 'BELI', 'BARO', 'BEVA', 'BIDE', 'BICI', 'BICA', 'BEVO', 'BEVI', 'BEVE', 'BETA', 'BELO', 'BERK', 'BERI', 'BERE', 'BENI', 'BENG', 'BENE', 'BEMA', 'BASA', 'BARN', 'AUSI', 'AVRO', 'BABY', 'BABE', 'BABA', 'AZZE', 'AZZA', 'AXEL', 'AVRA', 'BACI', 'AVIO', 'AVEA', 'AUTO', 'AUTI', 'AUTE', 'AUTA', 'AUSO', 'BACA', 'BACO', 'BARI', 'BALI', 'BARE', 'BARA', 'BANO', 'BANI', 'BANG', 'BAND', 'BAIO', 'BADA', 'BAIE', 'BAIA', 'BAHT', 'BAGA', 'BADO', 'BADI', 'BADE', 'ARDO', 'ARDE', 'BIGE', 'AGNA', 'AGRI', 'AGRE', 'AGRA', 'AGNO', 'AGNI', 'AGNE', 'AGLI', 'AHIA', 'AGIO', 'AGII', 'AGIA', 'AGHI', 'AGHA', 'AGGI', 'AGRO', 'AIDS', 'AFTE', 'ALBA', 'ALCI', 'ALCE', 'ALCA', 'ALBO', 'ALBI', 'ALBE', 'ALAI', 'AIME', 'AITO', 'AITI', 'AITE', 'AITA', 'AIRI', 'AIRE', 'AIRA', 'AGAR', 'AFTA', 'ALEA', 'ACMI', 'ACRO', 'ACRI', 'ACRE', 'ACRA', 'ACNI', 'ACNE', 'ACME', 'ACUI', 'ACIE', 'ACID', 'ACCI', 'ACCE', 'ACCA', 'ABRO', 'ABRI', 'ACTA', 'ADDA', 'AFRO', 'AERO', 'AFRI', 'AFRE', 'AFRA', 'AFNI', 'AFFE', 'AFFA', 'AERI', 'ADDI', 'AERE', 'AERA', 'AEDO', 'AEDI', 'ADSL', 'ADII', 'ADDO', 'ALDI', 'ALEE', 
'ARDA', 'ANNO', 'ANTE', 'ANTA', 'ANSO', 'ANSI', 'ANSE', 'ANSA', 'ANNI', 'AONI', 'ANGE', 'ANDO', 'ANDE', 'ANDA', 'ANCO', 'ANCE', 'ANZI', 'APII', 'AMPI', 'ARAC', 'ARCO', 'ARCI', 'ARCE', 'ARCA', 'ARAK', 'ARAI', 'AQUE', 'APIO', 'AQUA', 'APRO', 'APRI', 'APRE', 'APRA', 'APPO', 'APPI', 'ANCA', 'AMOK', 'ALEF', 'ALMA', 'ALOE', 'ALNO', 'ALNI', 'ALMO', 'ALMI', 'ALME', 'ALLO', 'ALPI', 'ALLE', 'ALLA', 'ALIO', 'ALIA', 'ALGA', 'ALFE', 'ALFA', 'ALPE', 'ALSE', 'AMNI', 'ALZO', 'AMEN', 'AMBO', 'AMBI', 'AMBE', 'AMBA', 'AMAI', 'ALZI', 'ALSI', 'ALZA', 'ALVO', 'ALVI', 'ALTO', 'ALTI', 'ALTE', 'ALTA', 'BIGA', 'BIGI', 'CURA', 'CIRE', 'CITY', 'CITO', 'CITI', 'CITA', 'CISI', 'CIRO', 'CIOE', 'CIVE', 'CINZ', 'CINE', 'CIMO', 'CIMI', 'CIME', 'CIMA', 'CIUF', 'CIVI', 'CICA', 'COBO', 'CODE', 'CODA', 'COCO', 'COCI', 'COCE', 'COCA', 'COBI', 'CLAN', 'CLUB', 'CLOU', 'CLOP', 'CLOF', 'CLIP', 'CLIC', 'CLAP', 'CIDI', 'CIBO', 'COII', 'CELO', 'CERA', 'CENT', 'CENO', 'CENI', 'CENE', 'CENA', 'CELI', 'CERI', 'CELA', 'CEKO', 'CEKI', 'CEKE', 'CEKA', 'CEFO', 'CEFI', 'CERE', 'CERO', 'CIBI', 'CHOC', 'CIBA', 'CIAO', 'CIAK', 'CIAF', 'CIAC', 'CHOU', 'CHIU', 'CESI', 'CHIP', 'CHIC', 'CHEF', 'CHED', 'CHAT', 'CETO', 'CETI', 'CODI', 'COIL', 'CEDI', 'CRII', 'CUAS', 'CSAR', 'CRUX', 'CRUP', 'CROI', 'CRIO', 'CRIE', 'CUBE', 'CRIC', 'CRIA', 'CREW', 'CREO', 'CREN', 'CREI', 'CUBA', 'CUBI', 'CRAI', 'CUNA', 'CUPO', 'CUPI', 'CUPE', 'CUPA', 'CUOI', 'CUNE', 'CULT', 'CUBO', 'CULO', 'CULI', 'CUIO', 'CUDU', 'CUCU', 'CUCI', 'CUCE', 'CREA', 'CRAC', 'COIO', 'COME', 'COOP', 'COOL', 'CONO', 'CONI', 'COMO', 'COMI', 'COMA', 'COPY', 'COLT', 'COLO', 'COLI', 'COLF', 'COLE', 'COLA', 'COKE', 'COPI', 'CORA', 'COVO', 'COTE', 'COVI', 'COVE', 'COVA', 'COUP', 'COTO', 'COTI', 'COTA', 'CORE', 'COSY', 'COSO', 'COSI', 'COSE', 'COSA', 'CORO', 'CORI', 'CEDO', 'CEDE', 'BIGO', 'BOTI', 'BOXE', 'BOXA', 'BOVO', 'BOVI', 'BOVE', 'BOTO', 'BOTE', 'BOXO', 'BOTA', 'BOSS', 'BOSE', 'BOSA', 'BORT', 'BORO', 'BOXI', 'BRAI', 'BORE', 'BUCA', 'BUGE', 'BUFO', 'BUFI', 'BUFA', 'BUCO', 'BUCI', 'BUBU', 'BRIC', 'BRUT', 'BRUM', 'BRUI', 'BRIO', 'BRIK', 'BRII', 'BRIE', 'BORI', 'BORA', 'BUIA', 'BIRO', 'BLOG', 'BLOB', 'BLEU', 'BLAH', 'BIVI', 'BITE', 'BIOT', 'BOBE', 'BIOS', 'BINO', 'BINI', 'BINE', 'BINA', 'BILI', 'BILE', 'BOBA', 'BOCE', 'BOOM', 'BOMI', 'BOOK', 'BONO', 'BONI', 'BONE', 
'BOND', 'BONA', 'BOME', 'BOCI', 'BOMA', 'BOLO', 'BOLI', 'BOLD', 'BOIA', 'BOGA', 'BODY', 'BUGI', 'BUIE', 'CEDA', 'CAOS', 'CARD', 'CARA', 'CAPO', 'CAPI', 'CAPE', 'CAPA', 'CANO', 'CARI', 'CANI', 'CANE', 'CANA', 'CAMP', 'CAMO', 'CAMI', 'CALO', 'CARE', 'CARO', 'CALI', 'CAVO', 'CECO', 'CECI', 'CECE', 'CECA', 'CEBO', 'CEBI', 'CAVI', 'CASA', 'CAVE', 'CAVA', 'CAST', 'CASO', 'CASI', 'CASH', 'CASE', 'CALL', 'CALE', 'BUIO', 'BUON', 'BUSE', 'BUSA', 'BURO', 'BURI', 'BURE', 'BURA', 'BUOI', 'BUSO', 'BUNE', 'BUNA', 'BULO', 'BULL', 'BULI', 'BULE', 'BULA', 'BUSI', 'BUUU', 'CALA', 'CAGA', 'CAKE', 'CAIO', 'CAIE', 'CAID', 'CAIA', 'CAGO', 'CADY', 'BYTE', 'CADO', 'CADI', 'CADE', 'CADA', 'CACO', 'CACI', 'CACA', 'IRVI']

parole_giocabili_5 = ['ABACA', 'ABACO', 'ABATE', 'ABATI', 'ABATO', 'ABAVI', 'ABAVO', 'ABBAI', 'ABBIA', 'ABBUI', 'ABENA', 'ABENE', 'ABETE', 'ABETI', 'ABETO', 'ABICI', 'ABILE', 'ABILI', 'ABITA', 'ABITI', 'ABITO', 'ABOLI', 'ABUNA', 'ABUSA', 'ABUSI', 'ABUSO', 'ACARI', 'ACARO', 'ACATI', 'ACATO', 'ACAZI', 'ACCHE', 'ACCIA', 'ACCIO', 'ACERI', 'ACERO', 'ACESE', 'ACESI', 'ACETI', 'ACETO', 'ACHEA', 'ACHEE', 'ACHEI', 'ACHEO', 'ACIDA', 'ACIDE', 'ACIDI', 'ACIDO', 'ACINI', 'ACINO', 'ACORI', 'ACORO', 'ACQUA', 'ACQUE', 'ACQUI', 'ACQUO', 'ACTEA', 'ACTEE', 'ACUII', 'ACUME', 'ACUMI', 'ACUTA', 'ACUTE', 'ACUTI', 'ACUTO', 'ADAGI', 'ADAMI', 'ADAMO', 'ADDAI', 'ADDAX', 'ADDIA', 'ADDIO', 'ADERI', 'ADESA', 'ADESE', 'ADESI', 'ADESO', 'ADIBI', 'ADIMA', 'ADIMI', 'ADIMO', 'ADIPE', 'ADIPI', 'ADIRA', 'ADIRE', 'ADIRI', 'ADIRO', 'ADITA', 'ADITE', 'ADITI', 'ADITO', 'ADIVA', 'ADIVI', 'ADIVO', 'ADOBE', 'ADONA', 'ADONE', 'ADONI', 'ADONO', 'ADORA', 'ADORI', 'ADORO', 'ADOXA', 'ADOXE', 'ADULA', 'ADULI', 'ADULO', 'ADUNA', 'ADUNI', 'ADUNO', 'ADUSA', 'ADUSE', 'ADUSI', 'ADUSO', 'AERAI', 'AEREA', 'AEREE', 'AEREI', 'AEREO', 'AFACA', 'AFELI', 'AFFLA', 'AFFLI', 'AFIDE', 'AFIDI', 'AFNII', 'AFNIO', 'AFONA', 'AFONE', 'AFONI', 'AFONO', 'AFOSA', 'AFOSE', 'AFOSI', 'AFOSO','AFOXE', 'AGAMA', 'AGAME', 'AGAMI', 'AGAMO', 'AGAPE', 'AGAPI', 'AGATA', 'AGATE', 'AGAVE', 'AGAVI', 'AGERA', 'AGERO', 'AGGIA', 'AGGIO', 'AGIAI', 'AGILE', 'AGILI', 'AGIRA', 'AGIRE', 'AGIRO', 'AGITA', 'AGITE', 'AGITI', 'AGITO', 'AGIVA', 'AGIVI', 'AGIVO', 'AGLIO', 'AGONE', 'AGONI', 'AGORA', 'AGUNA', 'AGUNI', 'AGUNO', 'AGURA', 'AGURI', 'AGURO', 'AGUTI', 'AGUTO', 'AHIME', 'AIOLA', 'AIOLE', 'AIOLI', 'AIOLO', 'AITAI', 'AIUGA', 'AIUTA', 'AIUTI', 'AIUTO', 'AIZZA', 'AIZZI', 'AIZZO', 'AJOUR', 'ALALA', 'ALANA', 'ALANE', 'ALANI', 'ALANO', 'ALARE', 'ALARI', 'ALATA', 'ALATE', 'ALATI', 'ALATO', 'ALAVA', 'ALAVI', 'ALAVO', 'ALBUM', 'ALCEA', 'ALCEE', 'ALCHE', 'ALCOL', 'ALCUN', 'ALDIA', 'ALDIE', 'ALDIO', 'ALENA', 'ALENI', 'ALERA', 'ALERE', 'ALERO', 'ALESA', 'ALESI', 'ALESO', 'ALGHE', 'ALGIA', 'ALGIE', 'ALIAI', 'ALIAS', 'ALIBI', 'ALICE', 'ALICI', 'ALIDA', 'ALIDE', 'ALIDI', 'ALIDO', 'ALIGA', 'ALIMI', 'ALIMO', 'ALINO', 'ALITA', 'ALITE', 'ALITI', 'ALITO', 'ALLEA', 'ALLEI', 'ALLEO', 'ALMEA', 'ALMEE', 'ALOBI', 'ALONA', 'ALONE', 'ALONI', 'ALONO', 'ALOSA', 'ALOSE', 'ALPAX', 'ALTEA', 'ALTEE', 'ALTRA', 'ALTRE', 'ALTRI', 'ALTRO', 'ALULA', 'ALULE', 'ALVEI', 'ALVEO', 'ALZAI', 'AMACA', 'AMANO', 'AMARA', 'AMARE', 'AMARI', 'AMARO', 'AMASI', 'AMATA', 'AMATE', 'AMATI', 'AMATO', 'AMAVA', 'AMAVI', 'AMAVO', 'AMBIA', 'AMBII', 'AMBIO', 'AMBRA', 'AMBRE', 'AMEBA', 'AMEBE', 'AMENA', 'AMENE', 'AMENI', 'AMENO', 'AMERA', 'AMERO', 'AMICA', 'AMICI', 'AMICO', 'AMIDA', 'AMIDE', 'AMIDI', 'AMIDO', 'AMINA', 'AMINE', 'AMINO', 'AMMAI', 'AMMEN', 'AMNII', 'AMNIO', 'AMOMI', 'AMOMO', 'AMORA', 'AMORE', 'AMORI', 'AMPEX', 'AMPIA', 'AMPIE', 'AMPIO', 'AMPLI', 'AMPLO', 'AMULI', 'AMULO', 'ANACE', 'ANALE', 'ANALI', 'ANCHE', 'ANCIA', 'ANCOI', 'ANDAI', 'ANDRA', 'ANDRO', 'ANELA', 'ANELE', 'ANELI', 'ANELO', 'ANETI', 'ANETO', 'ANGLA', 'ANGLE', 'ANGLI', 'ANGLO', 'ANGUE', 'ANGUI', 'ANICE', 'ANICI', 'ANILE', 'ANILI', 'ANIMA', 'ANIME', 'ANIMI', 'ANIMO', 'ANNOI', 'ANNUA', 'ANNUE', 'ANNUI', 'ANNUO', 'ANOBI', 'ANODI', 'ANODO', 'ANONA', 'ANONE', 'ANSAI', 'ANSIA', 'ANSIE', 'ANSIO', 'ANTRI', 'ANTRO', 'ANURA', 'ANURE', 'ANURI', 'ANURO', 'AONIA', 'AONIE', 'AONIO', 'AOPPI', 'AORTA', 'AORTE', 'APALE', 'APALI', 'APIAI', 'APICE', 'APICI', 'APIDE', 'APIDI', 'APINA', 'APINE', 'APNEA', 'APNEE', 'APODA', 'APODE', 'APODI', 'APODO', 'APPAI', 'APPIA', 'APPIE', 'APPIO', 'APRII', 'APULA', 'APULE', 'APULI', 'APULO', 'AQUEA', 'AQUEE', 'AQUEI', 'AQUEO', 'ARABA', 'ARABE', 'ARABI', 'ARABO', 'ARANO', 'ARARE', 'ARATA', 'ARATE', 'ARATI', 'ARATO', 'ARAVA', 'ARAVI', 'ARAVO', 'ARCAI', 'ARCHE', 'ARCHI', 'ARCUA', 'ARCUI', 'ARCUO', 'ARDEA', 'ARDEE', 'ARDII', 'ARDUA', 'ARDUE', 'ARDUI', 'ARDUO', 'AREAI', 'ARECA', 'ARENA', 'ARENE', 'ARENI', 'ARENO', 'ARERA', 'ARERO', 'ARGHI', 'ARGON', 'ARGOT', 'ARGUI', 
'ARIDA', 'ARIDE', 'ARIDI', 'ARIDO', 'ARILE', 'ARILI', 'ARINO', 'ARMAI', 'ARNIA', 'ARNIE', 'AROMA', 'AROMI', 'ARPIA', 'ARPIE', 'ARRAK', 'ARRAY', 'ARTAI', 'ASARI', 'ASARO', 'ASCHI', 'ASCIA', 'ASCIO', 'ASDIC', 'ASILI', 'ASILO', 'ASINA', 'ASINE', 'ASINI', 'ASINO', 'ASOLA', 'ASOLE', 'ASOLI', 'ASOLO', 'ASPIC', 'ASPRA', 'ASPRE', 'ASPRI', 'ASPRO', 'ASSAI', 'ASSET', 'ASTER', 'ASTIO', 'ASTRI', 'ASTRO', 'ATANO', 'ATARE', 'ATATA', 'ATATE', 'ATATI', 'ATATO', 'ATAVA', 'ATAVE', 'ATAVI', 'ATAVO', 'ATCIU', 'ATELE', 'ATELI', 'ATERA', 'ATERO', 'ATINO', 'ATOMI', 'ATOMO', 'ATONA', 'ATONE', 'ATONI', 'ATONO', 'ATOUT', 'ATRII', 'ATRIO', 'ATTAI', 'ATTUA', 'ATTUI', 'ATTUO', 'AUDIO', 'AUDIT', 'AUFFA', 'AUGGI', 'AUGNA', 'AUGNI', 'AUGNO', 'AULOS', 'AUNAI', 'AUREA', 'AUREE', 'AUREI', 'AUREO', 'AURIO', 'AUSAI', 'AUTOS', 'AVANA', 'AVARA', 'AVARE', 'AVARI', 'AVARO', 'AVEMO', 'AVENA', 'AVENE', 'AVERE', 'AVERI', 'AVERO', 'AVETE', 'AVEVA', 'AVEVI', 'AVEVO', 'AVIDA', 'AVIDE', 'AVIDI', 'AVIDO', 'AVITA', 'AVITE', 'AVITI', 'AVITO', 'AVOCA', 'AVOCO', 'AVOLA', 'AVOLE', 'AVOLI', 'AVOLO', 'AVORI', 'AVRAI', 'AVREI', 'AVRIA', 'AVUTA', 'AVUTE', 'AVUTI', 'AVUTO', 'AVVIA', 'AVVII', 'AVVIO', 'AXONE', 'AXONI', 'AZERA', 'AZERE', 'AZERI', 'AZERO', 'AZIMA', 'AZIME', 'AZIMO', 'AZONI', 'AZOTI', 'AZOTO', 'AZUKI', 'BABAO', 'BABAU', 'BABBI', 'BABBO', 'BACAI', 'BACCA', 'BACCO', 'BACHI', 'BACIA', 'BACIE', 'BACII', 'BACIO', 'BACON', 'BADAI', 'BADGE', 'BADIA', 'BADIE', 'BAFFI', 'BAFFO', 'BAGEL', 'BAGLI', 'BAGNA', 'BAGNE', 'BAGNI', 'BAGNO', 'BAIAI', 'BAILA', 'BAILE', 'BAILI', 'BAILO', 'BAINO', 'BAITA', 'BAITE', 'BALBO', 'BALCO', 'BALDA', 'BALDE', 'BALDI', 'BALDO', 'BALIA', 'BALIE', 'BALII', 'BALIO', 'BALLA', 'BALLE', 'BALLI', 'BALLO', 'BALMA', 'BALME', 'BALSA', 'BALSE', 'BALTA', 'BALTE', 'BALZA', 'BALZE', 'BALZI', 'BALZO', 'BAMBA', 'BAMBE', 'BAMBI', 'BAMBO', 'BAMBU', 'BANCA', 'BANCO', 'BANDA', 'BANDE', 'BANDI', 'BANDO', 'BANGI', 'BANJO', 'BANNA', 'BANNI', 'BANNO', 'BANTU', 'BARAI', 'BARBA', 'BARBE', 'BARBI', 'BARBO', 'BARCA', 'BARCO', 'BARDA', 'BARDE', 'BARDI', 'BARDO', 'BARGE', 'BARIA', 'BARIE', 'BARII', 'BARIO', 'BARRA', 'BARRE', 'BARRI', 'BARRO', 'BASAI', 'BASCA', 'BASCO', 'BASIC', 'BASII', 'BASSA', 'BASSE', 'BASSI', 'BASSO', 'BASTA', 'BASTE', 'BASTI', 'BASTO', 'BATCH', 'BATIK', 'BATTA', 'BATTE', 'BATTI', 'BATTO', 'BAULA', 'BAULE', 'BAULI', 'BAULO', 'BAUTA', 'BAZAR', 'BAZZA', 'BAZZE', 'BEANO', 'BEARE', 'BEATA', 'BEATE', 'BEATI', 'BEATO', 'BEAVA', 'BEAVI', 'BEAVO', 'BECCA', 'BECCO', 'BECHE', 'BECHI', 'BEERA', 'BEERO', 'BEFFA', 'BEFFE', 'BEFFI', 'BEFFO', 'BEGHE', 'BEGHI', 'BEGLI', 'BEGUM', 'BEIGE', 'BEINO', 'BEISA', 'BEISE', 'BELAI', 'BELGA', 'BELGI', 'BELII', 'BELIO', 'BELLA', 'BELLE', 'BELLI', 'BELLO', 'BELTA', 'BELVA', 'BELVE', 'BEMBE', 'BENDA', 
'BENDE', 'BENDI', 'BENDO', 'BENNA', 'BENNE', 'BENSI', 'BEOLA', 'BEOLE', 'BEONA', 'BEONE', 'BEONI', 'BEOTA', 'BEOTE', 'BEOTI', 'BERCI', 'BERGA', 'BERMA', 'BERME', 'BERRA', 'BERRO', 'BERSI', 'BERSO', 'BERTA', 'BERTE', 'BERUF', 'BERZA', 'BERZE', 'BESCI', 'BESSA', 'BESSE', 'BESSI', 'BESSO', 'BETEL', 'BETON', 'BETTA', 'BETTE', 'BEUTA', 'BEUTE', 'BEVEI', 'BEVVE', 'BEVVI', 'BEZZI', 'BEZZO', 'BIADA', 'BIADE', 'BIADI', 'BIADO', 'BIAVA', 'BIAVE', 'BIAVI', 'BIAVO', 'BIBBI', 'BICCI', 'BICHE', 'BIDET', 'BIECA', 'BIECO', 'BIETA', 'BIETE', 'BIFFA', 'BIFFE', 'BIFFI', 'BIFFO', 'BIGHE', 'BIGHI', 'BIGIA', 'BIGIE', 'BIGIO', 'BIGIU', 'BIGNE', 'BIJOU', 'BIKER', 'BILIA', 'BILIE', 'BILLE', 'BILLI', 'BILTA', 'BIMBA', 'BIMBE', 'BIMBI', 'BIMBO', 'BINAI', 'BINDA', 'BINDE', 'BINGO', 'BIODI', 'BIODO', 'BIOMA', 'BIOMI', 'BIOVA', 'BIOVE', 'BIRBA', 'BIRBE', 'BIRBI', 'BIRBO', 'BIRCE', 'BIRCI', 'BIRRA', 'BIRRE', 'BIRRI', 'BIRRO', 'BISCA', 'BISCE', 'BISCI', 'BISEX', 'BISSA', 'BISSI', 'BISSO', 'BITTA', 'BITTE', 'BITTI', 'BITTO', 'BIUTA', 'BIUTE', 'BIVIO', 'BIZZA', 'BIZZE', 'BLASE', 'BLEAH', 'BLESA', 'BLESE', 'BLESI', 'BLESO', 'BLIMP', 'BLINI', 'BLINY', 'BLITZ', 'BLOCK', 'BLOOM', 'BLUES', 'BLUFF', 'BLUMI', 'BLUMO', 'BLUSA', 'BLUSE', 'BOARA', 'BOARD', 'BOARE', 'BOARI', 'BOARO', 'BOATI', 'BOATO', 'BOBBA', 'BOBBE', 'BOCCA', 'BOCCE', 'BOCCI', 'BOCHE', 'BOCIA', 'BOCIO', 'BODDA', 'BODDE', 'BOEMA', 'BOEME', 'BOEMI', 'BOEMO', 'BOERA', 'BOERE', 'BOERI', 'BOERO', 'BOGHE', 'BOGLI', 'BOHRI', 'BOIDE', 'BOIDI', 'BOINA', 'BOITE', 'BOLDI', 'BOLDO', 'BOLGE', 'BOLLA', 'BOLLE', 'BOLLI', 'BOLLO', 'BOLSA', 'BOLSE', 'BOLSI', 'BOLSO', 'BOMBA', 'BOMBE', 'BOMBI', 'BOMBO', 'BOMII', 'BONCI', 'BONET', 'BONGO', 'BONNE', 'BONTA', 'BONUS', 'BONZA', 'BONZE', 'BONZI', 'BONZO', 'BORDA', 'BORDE', 'BORDI', 'BORDO', 'BOREA', 'BOREI', 'BORGO', 'BORIA', 'BORIE', 'BORII', 'BORIO', 'BORNI', 'BORRA', 'BORRE', 'BORRI', 'BORRO', 'BORSA', 'BORSC', 'BORSE', 'BOSCO', 'BOSSI', 'BOSSO', 'BOTAI', 'BOTRI', 'BOTRO', 'BOTTA', 'BOTTE', 'BOTTI', 'BOTTO', 'BOULE', 'BOXAI', 'BOXER', 'BOZZA', 'BOZZE', 'BOZZI', 'BOZZO', 'BRACA', 'BRACE', 'BRACI', 'BRACO', 'BRADA', 'BRADE', 'BRADI', 'BRADO', 'BRAGA', 'BRAGE', 'BRAGO', 'BRAII', 'BRAMA', 'BRAME', 'BRAMI', 'BRAMO', 'BRAND', 'BRANI', 'BRANO', 'BRASA', 'BRASI', 'BRASO', 'BRAVA', 'BRAVE', 'BRAVI', 'BRAVO', 'BREAK', 'BRENT', 'BREVA', 'BREVE', 'BREVI', 'BRICA', 'BRICE', 'BRIDA', 'BRIDE', 'BRIEF', 'BRIGA', 'BRIGO', 'BRINA', 'BRINE', 'BRINI', 'BRINO', 'BRODA', 'BRODE', 'BRODI', 'BRODO', 'BROLI', 'BROLO', 'BROMI', 'BROMO', 'BRUCA', 'BRUCE', 'BRUCI', 'BRUCO', 'BRUGO', 'BRUII', 'BRULE', 'BRUMA', 'BRUME', 'BRUNA', 'BRUNE', 'BRUNI', 'BRUNO', 'BRUSI', 'BRUTA', 'BRUTE', 'BRUTI', 'BRUTO', 'BUANA', 'BUCAI', 'BUCCE', 'BUCCI', 'BUCHE', 'BUCHI', 'BUCIO', 
'BUDDA', 'BUDDI', 'BUFAI', 'BUFFA', 'BUFFE', 'BUFFI', 'BUFFO', 'BUGIA', 'BUGIE', 'BUGIO', 'BUGLI', 'BUGNA', 'BUGNE', 'BUGNI', 'BUGNO', 'BUINA', 'BUINE', 'BULBI', 'BULBO', 'BULGE', 'BULLA', 'BULLE', 'BULLI', 'BULLO', 'BUNET', 'BUONA', 'BUONE', 'BUONI', 'BUONO', 'BURBA', 'BURBE', 'BURGA', 'BURKA', 'BURLA', 'BURLE', 'BURLI', 'BURLO', 'BURQA', 'BURRI', 'BURRO', 'BURST', 'BUSCA', 'BUSCO', 'BUSSA', 'BUSSE', 'BUSSI', 'BUSSO', 'BUSTA', 'BUSTE', 'BUSTI', 'BUSTO', 'BUTTA', 'BUTTE', 'BUTTI', 'BUTTO', 'BUYER', 'BUZZA', 'BUZZE', 'BUZZI', 'BUZZO', 'BWANA', 'CABAN', 'CABLA', 'CABLE', 'CABLI', 'CABLO', 'CABRA', 'CABRI', 'CABRO', 'CACAI', 'CACAO', 'CACCA', 'CACCE', 'CACCI', 'CACHE', 'CACHI', 'CACIO', 'CACTI', 'CACTO', 'CADDE', 'CADDI', 'CADMI', 'CADRA', 'CADRO', 'CAFFA', 'CAFFE', 'CAFFI', 'CAFFO', 'CAFRA', 'CAFRE', 'CAFRI', 'CAFRO', 'CAGAI', 'CAGHI', 'CAGIU', 'CAGLI', 'CAGNA', 'CAGNE', 'CAIAC', 'CAIBA', 'CAIBE', 'CAINI', 'CAINO', 'CAIRN', 'CAJUN', 'CALAI', 'CALAO', 'CALCA', 'CALCE', 'CALCI', 'CALCO', 'CALDA', 'CALDE', 'CALDI', 'CALDO', 'CALEN', 'CALIA', 'CALIE', 'CALLA', 'CALLE', 'CALLI', 'CALLO', 'CALMA', 'CALME', 'CALMI', 'CALMO', 'CALSE', 'CALTA', 'CALTE', 'CALVA', 'CALVE', 'CALVI', 'CALVO', 'CALZA', 'CALZE', 'CALZI', 'CALZO', 'CAMBI', 'CAMEO', 'CAMMA', 'CAMME', 'CAMPA', 'CAMPI', 'CAMPO', 'CANAI', 'CANDI', 'CANEA', 'CANEE', 'CANGA', 'CANGE', 'CANGI', 'CANNA', 'CANNE']

#Scelta della lunghezza della parola

while True: 
    print("Scegli di quanti caratteri è la parola con cui giocare.\nRicorda che puoi scegliere tra parole di massimo 3, 4 o 5 caratteri.")
    try:    
        scelta_len=int(input())
    except:print("Hai inserito un valore non valido: riprova.")
    else:
        if scelta_len in (3,4,5):
             break
        else:("Hai inserito un valore non valido: riprova.")
if scelta_len == 3:parole_giocabili = parole_giocabili_3
elif scelta_len == 4:parole_giocabili = parole_giocabili_4
elif scelta_len == 5:parole_giocabili = parole_giocabili_5
word_ind = random.randint(0,int(len(parole_giocabili))-1)
word = parole_giocabili[word_ind]
player = list("_" * len(word))
while True:
    try:
        tent = int(input("Inserisci il numero di errori da poter fare. (MAX 10)\n "))
    except: print("Per indicare i tentativi serve un numero =\ ")
    else: 
        if tent > 0 and tent <=10: break 
        else : print("Il numero di tentativi dev'essere fra 1 e 10. Riprova")

#Scelta della lettera

while True:                                                                                                                 
    err = False
    x=0
    while True:
        lett = str(input("Inserire la lettera oppure scrivi 'hint' per avere un suggerimento (MAX 2):\n"))
        if len(lett) == 1:
            if lett.isalpha():
                if lett not in lett_list:
                    lett_list.append(lett)
                    break
                else: print("Hai già scelto questa lettera, riprova =\ ")
            else:print("Il carattere non è una lettera, riprova =\ ")
        elif lett.upper() == "HINT":
            hint_count += 1
            for el in word:
                if el not in (player) and hint_count < 3:
                    print ("Prova con la lettera " + el,end="\n")
                    break 
                else: 
                    print("Hai esaurito entrambi i tentativi: sei da solo adesso, s'è capi? ALONE IN THE DARK!")
                    break
        else: print("Hai inserito troppi caratteri, riprova! ")
    for el in word:
        if lett.upper() == el.upper(): 
            player[x] = lett.upper()
            err = True
        x+=1
    print(" ".join(player))
    if err == False: 
        err_msg += (" " + str(lett.upper()))
        print(err_msg,end="\n")
        dm_count += (10//tent)
        err_count += 1
        if err_count == tent:
            print("\n".join(death_man), end="\n")
            print("Mi dispiace: hai perso ='> CHE PIPPA!")
            break
        print("\n".join(death_man[0:dm_count]), end="\n")
        print("")
    elif err == True:
        print("La lettera che hai inserito compone la parola. Grande!") 
    if ("".join(player)) == word:
        print("Complimenti, hai trovato la parola e salvato il nostro impiccato. Sei un Drago!")
        break