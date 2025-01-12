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

    # Stampa il menu
    print("\nCosa vuoi fare?\n")
    print("1. Aggiungi un utente")
    print("2. Rimuovi un utente")
    print("3. Cerca un utente")
    print("4. Presta un libro")
    print("5. Restituisci un libro")
    print("6. Esci")

    # Chiede all'utente di selezionare un'opzione
    scelta = input(
        "\nInserisci il numero corrispondente all'azione che vuoi eseguire: ")

    # Esegue l'azione corrispondente al numero inserito dall'utente
    if scelta == "1":

        # Chiede all'utente di inserire il nome e il cognome dell'utente
        nome = input("Inserisci il nome dell'utente: ")
        cognome = input("\nInserisci il cognome dell'utente: ")
        # Esegue la funzione aggiungi_utente all'interno di gestione_utenti.py
        gestione_utenti.aggiungi_utente(nome, cognome, dizionario_utenti)

    elif scelta == "2":

        # Chiede all'utente di inserire il nome dell'utente da rimuovere
        nome = input("\nInserisci il nome dell'utente che vuoi rimuovere: ")
        # Esegue la funzione rimuovi_utente all'interno di gestione_utenti.py
        gestione_utenti.rimuovi_utente(nome, dizionario_utenti)

    elif scelta == "3":

        # Chiede all'utente di inserire il nome e il cognome dell'utente da cercare
        nome = input("\nInserisci il nome dell'utente che vuoi cercare: ")
        cognome = input(
            "\nInserisci il cognome dell'utente che vuoi cercare: ")
        # Esegue la funzione cerca_utente all'interno di gestione_utenti.py
        gestione_utenti.cerca_utente(nome, cognome, dizionario_utenti)

    elif scelta == "4":

        print()
        # Da implementare, in attesa della funzione

    elif scelta == "5":

        print()
        # Da implementare, in attesa della funzione

    elif scelta == "6":

        # Se l'utente ha scelto di uscire, esce dal ciclo while
        print("Grazie per aver scelto la nostra biblioteca!")
        break

    # Se l'utente ha inserito un numero diverso da 1, 2, 3, 4, 5 o 6
    # O se ha inserito un valore non numerico
    else:

        print("Scelta non valida. Riprova.")
