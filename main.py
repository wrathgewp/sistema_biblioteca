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
