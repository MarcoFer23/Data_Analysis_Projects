# Generazione automatizzata di metadati mediante .format() [ in alternativa usare f-strings ]

list = ["Calzini", "Scarpe", "Pantaloni"]
title = "Acquista {} calzini in offerta | DuhShop"
meta_description = "Scopri le migliori offerte su {} e migliaia di altri prodotti in catalogo. Fai l'affare del secolo su DuhShop!"

for x in list:

    if len(title.format(x)) < 67 and len(meta_description.format(x)) < 155:
        print(title.format(x), ";", meta_description.format(x), ";", x, "\n") 

    elif len(title.format(x)) >= 67 and len(meta_description.format(x)) < 155:
        print("Lunghezza title superiore a 67 caratteri.", ";", meta_description.format(x), ";", x, "\n")

    elif len(title.format(x)) < 67 and len(meta_description.format(x)) >= 155:
        print(title.format(x), ";", "Lunghezza Meta Description superiore a 155 caratteri", ";", x, "\n")

    elif len(title.format(x)) >= 67 and len(meta_description.format(x)) >= 155:
        print("Lunghezza title superiore a 67 caratteri.", ";", "Lunghezza Meta Description superiore a 155 caratteri", ";", x, "\n")
