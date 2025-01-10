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
            del dizionario_utenti[username]
            print("Utente " + nome + " rimosso")
    # Se sono presenti più utenti con quel nome
    elif len(utenti_da_rimuovere) > 1:
        print("Sono presenti più utenti con il nome " + nome + ".")
        print("Selezionare l'utente da rimuovere:")
        # Stampa la lista degli utenti con quel nome
        for username in utenti_da_rimuovere:
            print(username + ": " + dizionario_utenti[username]
                  ['nome'] + " " + dizionario_utenti[username]['cognome'])
        # Chiede all'utente di selezionare l'utente da rimuovere
        username_selezionato = input(
            "Inserisci l'username dell'utente da rimuovere: ")
        # Se l'utente selezionato è presente nella lista
        if username_selezionato in utenti_da_rimuovere:
            # Elimina l'utente e i suoi dati
            del dizionario_utenti[username_selezionato]
            print("Utente " + username_selezionato + " rimosso")
        else:
            # Se l'utente selezionato non è presente nella lista, si limita a segnalarlo
            print("Utente " + username_selezionato + " non trovato")


'''
Esempio di utilizzo
gestione_utenti.rimuovi_utente("Giovanni", dizionario_utenti)
'''
