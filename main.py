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
print("\nBenvenuto nella biblioteca!")
while True:
    print("\nCosa vuoi fare?\n")
    print("1. Aggiungi un utente")
    print("2. Rimuovi un utente")
    print("3. Cerca un utente")
    print("4. Presta un libro")
    print("5. Restituisci un libro")
    print("6. Esci")
    scelta = input(
        "\nInserisci il numero corrispondente all'azione che vuoi eseguire: ")

    if scelta == "1":
        nome = input("Inserisci il nome dell'utente: ")
        cognome = input("\nInserisci il cognome dell'utente: ")
        gestione_utenti.aggiungi_utente(nome, cognome, dizionario_utenti)
    elif scelta == "2":
        nome = input("\nInserisci il nome dell'utente che vuoi rimuovere: ")
        gestione_utenti.rimuovi_utente(nome, dizionario_utenti)
    elif scelta == "3":
        nome = input("\nInserisci il nome dell'utente che vuoi cercare: ")
        cognome = input(
            "\nInserisci il cognome dell'utente che vuoi cercare: ")
        gestione_utenti.cerca_utente(nome, cognome, dizionario_utenti)
    elif scelta == "4":
        print()
        # Da implementare, in attesa della funzione
    elif scelta == "5":
        print()
        # Da implementare, in attesa della funzione
    elif scelta == "6":
        print("Grazie per aver scelto la nostra biblioteca!")
        break
    else:
        print("Scelta non valida. Riprova.")
