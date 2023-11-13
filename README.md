# Documentazione

#### Descrizione del sistema

Questo sistema serve a monitorare la disponibilità di un sito web. La Web API si occupa di ricevere una richiesta, effettuando un controllo su una URL data come parametro di ingresso, memorizzando in un database il tempo di risposta, lo status code e se avviene il match tra un'espressione regolare data opzionalmente in input e il contenuto del response. 

Per l'implementazione del sistema è stato utilizzato:

- Python Django per il backend
- Django REST framework per la web api
- Script in Bash per il test della api



#### Struttura dei dati del modello

La struttura dei dati che vengono memorizzati durante la richiesta HTTP è la seguente:

- **get_time**: data e orario della richiesta
- **url**: url del sito ispezionato
- **regex**: espressione regolare data in input
- **status_code**: status code restituito dal response
- **time_elapsed**: tempo di risposta (in secondi)
- **is_match_regex**: False (Default e se non avviene il match con l'espressione regolare) True (Se avviene il match)

#### Albero del repository

├── db.sqlite3
├── manage.py
├── test.sh
├── sites
│     ├── admin.py
│     ├── api
│   	  ├── responses.py
│   	  ├── serializers.py
│   	  ├── urls.py
│   	  └── views.py

│     ├── migrations
│     ├── models.py
└── webserver
│     ├── settings.py
│     ├── urls.py
├── README.md



Nella cartella **api** sono presenti i seguenti files: 

- nel file **urls.py** della cartella **api** sono stati aggiunti 3 endpoint, in base al tipo di richiesta che si vuole effettuare.

- **views.py** contiene le classi con le funzioni get() relative ad ogni tipologia di richiesta.

- lo script **responses.py**, che viene lanciato dalle funzioni della view.py, si occupa di effettuare le richieste HTTP alla URL del sito, restituendo l'orario di esecuzione della richiesta, lo status_code del sito, il tempo di risposta del sito e se è avvenuto il match con l'eventuale espressione regolare data in input.


Per effettuare delle interrogazioni alle API ci sono 3 modalità:

L'index si trova all'URL http://127.0.0.1:8000/api/sites/, dove è presente tutto lo storico delle richieste.

![](/home/joule/Immagini/Schermate/Schermata del 2023-11-12 21-38-55.png)

Le regole per le altre richieste sono le seguenti:

Per ispezionare una URL, senza il parametro dell'espressione regolare: 

http://127.0.0.1:8000/api/sites/u=<url>/

![](/home/joule/Immagini/Schermate/Schermata del 2023-11-12 21-40-58.png)

Per ispezionare una URL, con il parametro dell'espressione regolare:

http://127.0.0.1:8000/api/sites/u=<url>/r=<regex>

![](/home/joule/Immagini/Schermate/Schermata del 2023-11-13 19-12-35.png)

##### test.sh

Questo script bash esegue una serie di test sulla API.
Altri test possono essere eseguiti direttamente da browser, lanciando le richieste nella barra degli indirizzi.

##### Problemi riscontrabili:

La codifica dei caratteri speciali non è stata implementata, pertanto, per effettuare il controllo dell'URL potrebbe essere necessario codificare manualmente i caratteri speciali.
Non è stata effettuata una gestione di tutti i possibili errori.

#### Guida all'installazione e all'utilizzo

Per installare i requisiti, attivare l'ambiente virtuale e avviare il server, lanciare il comando:

```bash
$ ./run.sh
```

Da browser accedere all'index delle API da http://127.0.0.1:8000/api/sites/

Per effettuare i test lanciare il comando:

```bash
$ ./test.sh
```