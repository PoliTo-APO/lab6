# Laboratorio 6
In questo laboratorio viene esplorata l'ereditarietà.

Pertanto gli obiettivi principali di questo laboratorio sono:
- creare classi figlio da una classe padre
- utilizzo di super() nei costruttori e nei metodi
- prendere confidenza con l'overriding dei metodi
- comprendere e sfruttare il polimorfismo

Gli ultimi due esercizi, invece, trattano le strutture dati e la ricorsione.


## Esercizio 1
Creare la classe ```Room``` rappresentate una generica stanza di un'abitazione.
I costruttore accetta come parametri il numero di metri quadri,
il numero di finestre e il numero di prese per la corrente.
Fornire un getter per ciascuna di queste proprietà.

Creare la classe ```BathRoom``` che eredita da ```Room```.
Il costruttore, oltre ai parametri del padre,
accetta il numero di lavandini e tre valori booleani
indicanti la presenza della doccia, della vasca e del bidet.
Scrivere dei getter per questi parametri aggiuntivi.

Scrivere un main che crei delle istanze di queste classi.
Verificare che la classe figlio possieda i getter del padre
senza averli dovuti riscrivere.

## Esercizio 2
Creare la classe *Vehicle* che rappresentante un generico veicolo.
Il costruttore accetta come parametri il modello del veicolo, il suo consumo espresso in km/L,
e la sua classe euro (0-6).
Tutti questi valori devono essere ottenibili tramite opportuni getters.

Il metodo ```get_travel_cost(self, kms: float, fuel_cost: float) -> float```,
deve restituire il costo in carburante di un viaggio, dati i km percorsi e il costo del carburante in €/L.

Il metodo ```enter_ztl(self) -> bool``` deve autorizzare il veicolo all'accesso in ZTL (restituendo ```True```).
Un veicolo di classe euro minore di quattro può entrare in ZTL al massimo tre volte,
dopodiché gli verrà bloccato l'accesso, e il metodo restituirà ```False```.

La classe ```Car``` eredita da ```Vehicle```.
Fornire un setter e un getter per settare e ottenere il passeggeri presenti in auto.
Di default l'auto ha un solo passeggero (il guidatore).

Fare l'override del metodo ```get_travel_cost```,
di modo che la spesa totale sia divisa per il numero di passeggeri
(**USARE** il metodo padre per ottenere il prezzo da dividere)

La classe ```Truck``` eredita da ```Vehicle```, e aggiunge come parametro del costruttore il peso del camion.
Scrivere un getter che permetta di ottenerlo.
Fornire un setter e un getter per settare e ottenere il peso del carico.
Il valore di default del carico è zero (camion vuoto).

Fare l'override del metodo ```get_travel_cost```,
di modo che la spesa totale moltiplicata per il peso totale del veicolo (peso camion vuoto e carico)
e divisa per il peso del camion vuoto (**USARE** il metodo padre per ottenere il prezzo da correggere).

Essendo un veicolo commerciale, indipendentemente dalla sua classe euro, l'accesso in ZTL deve essere sempre consentito.

Scrivere un main che crei oggetti delle tre classi e testi il funzionamento degli oggetti in tutti i casi descritti.

## Esercizio 3
Creare la classe *Ticket* rappresentate un biglietto per una coda.

Il costruttore accetta come parametri il nome del possessore e il numero.
Il metodo ```get_queue_pos(self)``` restituisce la posizione in coda, pari al numero del biglietto.
Il metodo ```__repr__(self)``` restituisce una stringa contenente il nome e il numero del biglietto.

Implementare il metodo ```__lt__(self, other)``` per confrontare i biglietti per posizione in coda.
**RICHIAMARE** il metodo ```get_queue_pos(self)``` per ottenere la posizione.

Creare la classe *PriorityTicket* che eredita da *Ticket*, per rappresentare i biglietti prioritari.
Il costruttore accetta gli stessi parametri della classe padre,
più un numero intero che indica la priorità

Il metodo ```__repr__(self)``` restituisce una stringa 
contente le stesse informazioni del metodo di cui fa l'override
(usare il metodo padre per evitare la duplicazione di codice), più il valore della priorità.

Fare l'override di ```get_queue_pos(self)```, restituendo come posizione in coda il numero del biglietto
meno la priorità moltiplicata per 10.

Nel main creare una lista contenete diversi biglietti, prioritari e non, e ordinarla tramite il metodo ```sort()```.
Notare come avendo fornito un'implementazione di ```__lt__(self)``` sia possibile riordinare i biglietti per posizione.
Notare anche come l'override di ```get_queue_pos(self)```, usato da ``` __lt__(self, other)```,
abbia permesso di confrontare biglietti delle due diverse tipologie, tenendo conto della priorità.

## Esercizio 4
Creare un classe che implementi una **Linked List**.
La lista deve essere **SEMPLICEMENTE** concatenata (solo in una direzione).
Dovendo sviluppare una struttura dati con certe proprietà,
**NON** usare altre strutture dati Python (list, dict, set, ecc...).
Come spiegato a lezione, creare nodi e riferimenti tra di essi.
In *es4.py* viene già fornito lo scheletro della classe
e un main per testarne le funzionalità principali.

I metodi da implementare sono:
- ```insert_front(self, value: Any) -> None```: inserisce elementi in posizione zero

- ```insert(self, idx: int, value: Any) -> None```: inserisce elementi in posizione specificata.
Se viene fornito zero, l'aggiunta è equivalente a ```insert_front```.
Se l'indice è pari alla lunghezza della stringa l'aggiunta avviene in coda.

- ```remove(self, idx: int) -> None```: rimuove l'elemento in posizione specificata.

Eseguire l'override dei seguenti operatori:

- ```__len__(self) -> int```: restituisce il numero di elementi nella lista

- ```__getitem__(self, idx) -> Any```:
permette di accedere all'elemento in posizione *idx*
tramite l'operatore parentesi quadre (ad. es. ```mylista[5]```).

- ```__setitem__(self, idx, value) -> None```
permette di cambiare il valore dell'elemento in posizione *idx*,
tramite l'operatore parentesi quadre (ad. es. ```mylista[5]= "ciao"```).
**NON** aggiunte o toglie nodi.

- ```__repr__(self) -> str```: restituisce la stringa rappresentante la lista, 
nel formato ```[str1, str2,... strN]``` dove str1...N sono le rappresentazioni in stringa
degli oggetti contenuti nella lista.

Qual è la complessità delle operazioni d'inserimento, rimozione, ottenimento e cambio valore,
secondo la vostra implementazione?

## Esercizio 5
Scrivere un programma in grado di trovare il percorso per attraversare un labirinto.
I labirinti sono rappresentati su file come una matrice di caratteri.
Il carattere ```W``` rappresenta un muro, il carattere ```E``` rappresenta una cella vuota e quindi percorribile,
mentre il carattere ```P``` rappresenta celle del percorso per attraversarlo.
Gli unici caratteri ```P``` forniti indicano l'entrata e l'uscita del labirinto.


```
# labirinto
WWWWWWWWWWWWWWWWWWWWWW      
WEWEWEEEEWWEWEEEEWEEWW
PEEEEEWWEEEEEEWWEEWEEW
WEWEWEEWEWWEWEWEWWWEWW
WWEEEWWEEEEWEEEEEEEEEW
WEEWEWEWWEWWWEWEWEWWEW
WEWWEWEEWWEWWWEEWEEEWW
WWEEWEWEEEEEWWEWWEWEEW
WEEWWEEEWEWEEEWEEWWEWW
WEWWEWEWEWWEWWEWEEEEEW
WEEEEEEEEWEEEEEEEWWEWW
WWPWWWWWWWWWWWWWWWWWWW
```
Trovare il percorso che collega l'entrata e l'uscita e cambiare il contenuto delle celle a ```P```:

```
# soluzione
WWWWWWWWWWWWWWWWWWWWWW
WEWEWPPPPWWEWEEEEWEEWW
PPPPPPWWPPPPPPWWEEWEEW
WEWEWEEWEWWEWPWEWWWEWW
WWEEEWWEEEEWEPPPPPEEEW
WEEWEWEWWEWWWEWEWPWWEW
WEWWEWEEWWEWWWEEWPPPWW
WWEEWEWPPPPPWWEWWEWPEW
WEEWWEPPWEWPEEWEEWWPWW
WEWWEWPWEWWPWWEWPPPPEW
WEPPPPPEEWEPPPPPPWWEWW
WWPWWWWWWWWWWWWWWWWWWW
```

Rappresentati graficamente:

<img src="img/lab1.png" width="300" />

<img src="img/lab1_sol.png" width="300" />


La cartella ```data``` contiene tre labirinti di diverse dimensioni.
```es5.ipynb```, da aprire in *jupyter notebook*, contiene del codice utile per importare e disegnare il labirinti.

**IMPORTANTE**: presa un strada nel labirinto,
essa può condurre a un vicolo cieco, ma non tornare a un punto già percorso.
Il labirinto pertanto può essere visto come un albero
in cui i nodi sono le celle del labirinto e i rami le deviazioni che è possibile prendere (su, giù, destra, sinistra).
L'esplorazione di un labirinto per trovare l'uscita è pertanto equivalente alla ricerca in profondità di un albero
per trovare le foglie (vicoli cechi o uscita).
