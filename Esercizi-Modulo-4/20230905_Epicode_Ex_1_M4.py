'''
1. Abbiamo 25 studenti; memorizzare questo dato in una variabile.
'''
studenti = 25

'''
2. Abbiamo 25 studenti; memorizzare questo dato in una variabile e stamparla a video.
'''
studenti = 25 # Variabile già dichiarata in precedenza, ma aggiunta solo ai fini dell'esercizio.
print("Studenti: ",str(studenti))

'''
3. Abbiamo 25 studenti; memorizzare questo dato in una variabile. 
    Arrivano altri 3 studenti; memorizzare questo dato in un'altra variabile.
'''
studenti = 25 # Variabile già dichiarata in precedenza, ma aggiunta solo ai fini dell'esercizio.
altri_studenti = 3

'''
4. Abbiamo 25 studenti; memorizzare questo dato in una variabile. 
    Arrivano altri 3 studenti; memorizzare questo dato in un'altra variabile. 
        Creare un'altra variabile ancora che contenga la somma delle prime due, poi stamparla a video.
'''
studenti = 25 # Variabile già dichiarata in precedenza, ma aggiunta solo ai fini dell'esercizio.
altri_studenti = 3 # Variabile già dichiarata in precedenza, ma aggiunta solo ai fini dell'esercizio.
somma_studenti = studenti + altri_studenti
print(str(somma_studenti))

'''
5. Creare, a mano, una lista che contenga i numeri da 0 a 5, memorizzarla in una variable e infine stamparla a video.
'''
lista_numeri = [0,1,2,3,4,5]
print("La lista è questa: ",str(lista_numeri))

# alternativa con "range"

lista_range = range(0,6)
print("La lista range è questa: ",list(lista_range))

'''
6. Crea, a mano, una lista che contenga tre dei tuoi film preferiti, memorizzala in una variabile e infine stampala a video.
'''
lista_film = [
    "The Lord of the Rings",
    "The Nightmare Before Christmas",
    "Blade Runner"
]
print(lista_film)

