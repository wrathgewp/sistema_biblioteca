# 1.	Definizione delle variabili e strutture dati:
# a.	Creare una lista di dizionari per rappresentare i libri nella biblioteca. Ogni dizionario deve contenere le seguenti chiavi: titolo, autore, anno_pubblicazione, disponibile (un booleano che indica se il libro è disponibile o meno).
# b.	Creare una lista di dizionari per rappresentare gli utenti della biblioteca. Ogni dizionario deve contenere le seguenti chiavi: nome, cognome, libri_prestati (una lista di titoli di libri prestati).
# Lista di dizionari per rappresentare i libri nella biblioteca

biblioteca = [
    {
        "titolo": "Eragon",
        "autore": "Jhon",
        "anno_pubblicazione": 2015,
        "disponibile": True
    },
    {
        "titolo": "Se questo è un uomo",
        "autore": "Primo Levi",
        "anno_pubblicazione": 1947,
        "disponibile": True
    },
    {
        "titolo": "Guerra e pace",
        "autore": "Lev Tolstoj",
        "anno_pubblicazione": 1867,
        "disponibile": False
    }
]

# Visualizzazione della lista
for libro in biblioteca:
    print(libro)
    
# Lista di dizionari per rappresentare i libri nella biblioteca
biblioteca = [
    {"titolo": "Eragon", "autore": "Jhon", "anno_pubblicazione": 2015, "disponibile": True},
    {"titolo": "Se questo è un uomo", "autore": "Primo Levi", "anno_pubblicazione": 1947, "disponibile": True},
    {"titolo": "Guerra e pace", "autore": "Lev Tolstoj", "anno_pubblicazione": 1867, "disponibile": False}
      ]

# Lista di dizionari per rappresentare gli utenti della biblioteca
utenti = [
    {"nome": "Luca", "cognome": "Rossi", "libri_prestati": ["1984"]},
    {"nome": "Anna", "cognome": "Bianchi", "libri_prestati": []},
    {"nome": "Marco", "cognome": "Verdi", "libri_prestati": ["Il nome della rosa"]}
      ]

import gestione_utenti

def aggiungi_libro(titolo, autore, anno_pubblicazione):
    nuovo_libro = {"titolo": titolo, "autore": autore, "anno_pubblicazione": anno_pubblicazione, "disponibile": True}
    biblioteca.append(nuovo_libro)
    print(f"Libro '{titolo}' aggiunto con successo.")

# Funzione per rimuovere un libro
def rimuovi_libro(titolo):
    for libro in biblioteca:
        if libro["titolo"] == titolo:
            biblioteca.remove(libro)
            print(f"Libro '{titolo}' rimosso con successo.")
            return
    print(f"Libro '{titolo}' non trovato.")

# Funzione per cercare un libro
def cerca_libro(titolo):
    for libro in biblioteca:
        if libro["titolo"] == titolo:
            return libro
    return f"Libro '{titolo}' non trovato."

# Funzione per prestare un libro
def prestito_libro(titolo, nome_utente):
    libro = cerca_libro(titolo)
    if isinstance(libro, dict) and libro["disponibile"]:
        for utente in utenti:
            if utente["nome"] == nome_utente:
                libro["disponibile"] = False
                utente["libri_prestati"].append(titolo)
                print(f"Il libro '{titolo}' è stato prestato a {nome_utente}.")
                return
        print(f"Utente '{nome_utente}' non trovato.")
    else:
        print(f"Il libro '{titolo}' non è disponibile per il prestito.")

# Funzione per restituire un libro
def restituisci_libro(titolo, nome_utente):
    libro = cerca_libro(titolo)
    if isinstance(libro, dict) and not libro["disponibile"]:
        for utente in utenti:
            if utente["nome"] == nome_utente and titolo in utente["libri_prestati"]:
                libro["disponibile"] = True
                utente["libri_prestati"].remove(titolo)
                print(f"Il libro '{titolo}' è stato restituito da {nome_utente}.")
                return
        print(f"Utente '{nome_utente}' non ha prestato il libro '{titolo}'.")
    else:
        print(f"Il libro '{titolo}' non è stato prestato o non esiste.")

# Menu interattivo
def menu():
    while True:
        print("\nBenvenuto nella biblioteca!")
        print("Cosa vuoi fare?")
        print("1. Aggiungi un libro")
        print("2. Rimuovi un libro")
        print("3. Cerca un libro")
        print("4. Presta un libro")
        print("5. Restituisci un libro")
        print("6. Esci")

        scelta = input("\nInserisci il numero corrispondente all'azione che vuoi eseguire: ")

        if scelta == "1":
            titolo = input("Inserisci il titolo del libro: ")
            autore = input("Inserisci l'autore del libro: ")
            anno_pubblicazione = int(input("Inserisci l'anno di pubblicazione: "))
            aggiungi_libro(titolo, autore, anno_pubblicazione)
        
        elif scelta == "2":
            titolo = input("Inserisci il titolo del libro da rimuovere: ")
            rimuovi_libro(titolo)
        
        elif scelta == "3":
            titolo = input("Inserisci il titolo del libro da cercare: ")
            libro = cerca_libro(titolo)
            if isinstance(libro, dict):
                print(libro)
            else:
                print(libro)
        
        elif scelta == "4":
            titolo = input("Inserisci il titolo del libro da prestare: ")
            nome_utente = input("Inserisci il nome dell'utente che prende in prestito il libro: ")
            prestito_libro(titolo, nome_utente)
        
        elif scelta == "5":
            titolo = input("Inserisci il titolo del libro da restituire: ")
            nome_utente = input("Inserisci il nome dell'utente che restituisce il libro: ")
            restituisci_libro(titolo, nome_utente)
        
        elif scelta == "6":
            print("Grazie per aver scelto la nostra biblioteca!")
            break
        
        else:
            print("Scelta non valida. Riprova.")

# Esegui il menu
menu()
