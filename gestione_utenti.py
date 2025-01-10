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


def rimuovi_utente(nome, cognome, dizionario_utenti):
    # Trova il nome
    username = nome.lower() + cognome.lower()
    # Controlla se l'utente è presente nella lista
    if username in dizionario_utenti:
        # Elimina l'utente e i suoi dati
        del dizionario_utenti[username]
        print("Utente " + nome + " " + cognome + " rimosso")
    else:
        # Se l'utente non è presente nella lista, si limita a segnalarlo
        print("Utente " + nome + " " + cognome + " non trovato")
