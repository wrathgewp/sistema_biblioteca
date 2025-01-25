'''
Implementare una funzione aggiungi utente che prende come argomenti
il nome e il cognome dell'utente e
aggiunge un nuovo utente alla lista;
'''

def aggiungi_utente(nome, cognome, dizionario_utenti):
    username = nome.lower() + cognome.lower()
    if username in dizionario_utenti:
        print(f"L'utente {nome} {cognome} esiste già.")
    else:
        dizionario_utenti[username] = {
            'nome': nome,
            'cognome': cognome,
            'libri_prestati': []
        }
        print(f"Utente {nome} {cognome} aggiunto.")

def rimuovi_utente(nome, cognome, dizionario_utenti):
    username = nome.lower() + cognome.lower()
    if username not in dizionario_utenti:
        print(f"Utente {nome} {cognome} non trovato.")
    else:
        del dizionario_utenti[username]
        print(f"Utente {nome} {cognome} rimosso.")

def cerca_utente(nome, cognome, dizionario_utenti):
    username = nome.lower() + cognome.lower()
    if username not in dizionario_utenti:
        print(f"Utente {nome} {cognome} non trovato.")
    else:
        if len(dizionario_utenti[username]['libri_prestati']) == 0:
            print(f"L'utente {nome} {cognome} non ha libri prestati.")
        else:
            print(f"Libri prestati all'utente {nome} {cognome}:")
            for libro in dizionario_utenti[username]['libri_prestati']:
                print(libro)

def presta_libro(nome, cognome, libro, dizionario_utenti):
    username = nome.lower() + cognome.lower()
    if username not in dizionario_utenti:
        print(f"Utente {nome} {cognome} non trovato.")
    else:
        dizionario_utenti[username]['libri_prestati'].append(libro)
        print(f"Il libro '{libro}' è stato prestato a {nome} {cognome}.")

def restituisci_libro(nome, cognome, libro, dizionario_utenti):
    username = nome.lower() + cognome.lower()
    if username not in dizionario_utenti:
        print(f"Utente {nome} {cognome} non trovato.")
    else:
        if libro in dizionario_utenti[username]['libri_prestati']:
            dizionario_utenti[username]['libri_prestati'].remove(libro)
            print(f"Il libro '{libro}' è stato restituito da {nome} {cognome}.")
        else:
            print(f"Il libro '{libro}' non è stato trovato tra i libri prestati a {nome} {cognome}.")

