'''
Implementare una funzione aggiungi utente che prende come argomenti
il nome e il cognome dell'utente e
aggiunge un nuovo utente alla lista;
'''


def aggiungi_utente(nome, cognome, dizionario_utenti):
    # Crea un unsername dell'utente unendo il nome e il cognome
    dizionario_utenti[nome.lower() + cognome.lower()] = {
        # Aggiungi il nome e il cognome all'utente
        'nome': nome,
        'cognome': cognome,
        # Aggiungi una lista vuota di libri prestati all'utente
        'libri_prestati': []
    }
    print("Utente " + nome + " " + cognome + " aggiunto")


'''
Esempio di utilizzo
gestione_utenti.aggiungi_utente("Giovanni", "Bianchi", dizionario_utenti)
'''


'''
Implementare una funzione rimuovi utente che prende come argomento
il nome dell'utente e lo rimuove dalla lista se esiste.
'''


def rimuovi_utente(nome, dizionario_utenti):
    # Crea una lista di utenti da rimuovere
    utenti_da_rimuovere = []
    for username in dizionario_utenti:
        if dizionario_utenti[username]['nome'] == nome:
            utenti_da_rimuovere.append(username)
    # Se non è presente nessun utente con quel nome
    if len(utenti_da_rimuovere) == 0:
        # Se l'utente non è presente nella lista, si limita a segnalarlo
        print("Utente " + nome + " non trovato")
    # Se è presente un solo utente con quel nome
    elif len(utenti_da_rimuovere) == 1:
        for username in utenti_da_rimuovere:
            # Elimina l'utente e i suoi dati
            print("\nUtente " + dizionario_utenti[username]['nome'] + " " +
                  dizionario_utenti[username]['cognome'] + " rimosso")
            del dizionario_utenti[username]
    # Se sono presenti più utenti con quel nome
    elif len(utenti_da_rimuovere) > 1:
        print("\nSono presenti più utenti con il nome " + nome + ".")
        print("\nSelezionare l'utente da rimuovere:\n")
        # Stampa la lista degli utenti con quel nome
        for username in utenti_da_rimuovere:
            print(username + ": " + dizionario_utenti[username]
                  ['nome'] + " " + dizionario_utenti[username]['cognome'])
        # Chiede all'utente di selezionare l'utente da rimuovere
        username_selezionato = input(
            "\nInserisci l'username dell'utente da rimuovere: ")
        # Se l'utente selezionato è presente nella lista
        if username_selezionato in utenti_da_rimuovere:
            # Elimina l'utente e i suoi dati
            print("\nUtente " + dizionario_utenti[username]['nome'] + " " +
                  dizionario_utenti[username]['cognome'] + " rimosso")
            del dizionario_utenti[username_selezionato]
        else:
            # Se l'utente selezionato non è presente nella lista, si limita a segnalarlo
            print("\nUtente " + username_selezionato + " non trovato")


'''
Esempio di utilizzo
gestione_utenti.rimuovi_utente("Giovanni", dizionario_utenti)
'''

'''
Implementare una funzione cerca utente
che prende come argomento il nome e cognome di un utente
e stampa a video la lista dei libri prestati all’utente.
'''


def cerca_utente(nome, cognome, dizionario_utenti):
    # Crea un username dell'utente unendo il nome e il cognome
    username = nome.lower() + cognome.lower()
    # Effettua un controllo se l'utente esista o meno usando l'username.
    # Nel caso in cui non esista, si limita a segnalarlo
    if username not in dizionario_utenti:
        print("\nUtente " + nome + " " + cognome + " non trovato")
    # Se l'username esiste
    else:
        # Se l'utente non ha libri prestati, si limita a segnalarlo
        if len(dizionario_utenti[username]['libri_prestati']) == 0:
            print("\nL'utente " + nome + " " +
                  cognome + " non ha libri prestati")
        # Se l'utente ha libri prestati, li stampa a schermo
        else:
            print("\nLibri prestati all'utente " + nome + " " + cognome + ":")
            for libro in dizionario_utenti[username]['libri_prestati']:
                print(libro)


'''
Esempio di utilizzo:
gestione_utenti.cerca_utente("Mario", "Rossi", dizionario_utenti)
'''
