'''
Creare una lista di dizionari per rappresentare gli utenti della biblioteca.
Ogni dizionario deve contenere le seguenti chiavi: 
nome, cognome, libri_prestati (una lista di titoli di libri prestati).
'''
import gestione_utenti

# Questo è un esempio di come potrebbe essere strutturato il dizionario degli utenti
dizionario_utenti = {
    'mariorossi': {
        'nome': 'Mario',
        'cognome': 'Rossi',
        'libri_prestati': ['Eragon']
    },
    'lucaverdi': {
        'nome': 'Luca',
        'cognome': 'Verdi',
        'libri_prestati': ['Guerra e pace']
    },
    'giuliabianchi': {
        'nome': 'Giulia',
        'cognome': 'Bianchi',
        'libri_prestati': ['Se questo è un uomo']
    }
}

# Creare una lista di dizionari per rappresentare i libri nella biblioteca. Ogni dizionario deve contenere
# le seguenti chiavi: titolo, autore, anno_pubblicazione, disponibile (un booleano che indica se il libro è disponibile o meno).
dizionario_libro = {

    "Eragon": {
        "autore": "Jhon",
        "anno_pubblicazione": 2015,
        "disponibile": True
    },

    "Se questo è un uomo": {
        "autore": "Primo Levi",
        "anno_pubblicazione": 1947,
        "disponibile": True
    },

    "Guerra e pace": {
        "autore": "Lev Tolstoj",
        "anno_pubblicazione": 1867,
        "disponibile": False
    }
}
'''
Creare un menu interattivo
che permetta all'utente di scegliere tra le diverse funzionalità
(aggiungere, rimuovere, cercare, prestare, restituire un libro, aggiungere, rimuovere un utente)
e chiamare le funzioni appropriate.
'''
# biblioteca.py
import gestione_utenti

# Dizionario degli utenti (inizializzato vuoto)
dizionario_utenti = {}

print("\nBenvenuto nella biblioteca!")

while True:
    # Stampa il menu
    print("\nCosa vuoi fare?\n")
    print("1. Aggiungi un utente")
    print("2. Rimuovi un utente")
    print("3. Cerca un utente")
    print("4. Presta un libro")
    print("5. Restituisci un libro")
    print("6. Esci")

    # Chiede all'utente di selezionare un'opzione
    scelta = input("\nInserisci il numero corrispondente all'azione che vuoi eseguire: ")

    if scelta == "1":
        # Aggiungi un utente
        nome = input("Inserisci il nome dell'utente: ")
        cognome = input("Inserisci il cognome dell'utente: ")
        gestione_utenti.aggiungi_utente(nome, cognome, dizionario_utenti)

    elif scelta == "2":
        # Rimuovi un utente
        nome = input("Inserisci il nome dell'utente da rimuovere: ")
        cognome = input("Inserisci il cognome dell'utente da rimuovere: ")
        gestione_utenti.rimuovi_utente(nome, cognome, dizionario_utenti)

    elif scelta == "3":
        # Cerca un utente
        nome = input("Inserisci il nome dell'utente che vuoi cercare: ")
        cognome = input("Inserisci il cognome dell'utente che vuoi cercare: ")
        gestione_utenti.cerca_utente(nome, cognome, dizionario_utenti)

    elif scelta == "4":
        # Presta un libro
        nome = input("Inserisci il nome dell'utente: ")
        cognome = input("Inserisci il cognome dell'utente: ")
        libro = input("Inserisci il titolo del libro da prestare: ")
        gestione_utenti.presta_libro(nome, cognome, libro, dizionario_utenti)

    elif scelta == "5":
        # Restituisci un libro
        nome = input("Inserisci il nome dell'utente: ")
        cognome = input("Inserisci il cognome dell'utente: ")
        libro = input("Inserisci il titolo del libro da restituire: ")
        gestione_utenti.restituisci_libro(nome, cognome, libro, dizionario_utenti)

    elif scelta == "6":
        # Esci
        print("Grazie per aver scelto la nostra biblioteca!")
        break

    else:
        print("Scelta non valida. Riprova.")
