# simple_room_meeting
Report della risoluzione:

1) Identificazione del problema e stesura della struttura.
Prendendo spunto dall'esercizio assegnato precedentemente ho definito gli "assert" per i controlli e ho definito input e output della funzione "findrooms" assumendo la struttura del dato "prenotation_vector" come indicata.

2) Logica per la risoluzione del problema.
Ho stabilito una logica iniziale per la risoluzione del problema. In sostanza ho visto il numero di "sovrapposizioni" nello stesso range. 

3) Ho provato prima a risolverlo controllando su internet solo i comandi essenziali come "len","range". Ho cercato di usare il meno possibile delle funzioni "automatiche/elaborate" di python utilizzando solo gli elementi basilari.

Il codice ottenuto così è nel file test_meeting_room_simple.py


3) Analisi delle problematiche del codice:
Il codice assume che le prenotazioni siano fatte su base di "slot" (es. la prima prenotazione occupa gli slot temporali da 0 a 30). Il fatto che si debba creare una lista con tutti gli elementi implica che aumentando il numero di slot o di prenotazioni la quantità di dati da tenere in memoria nella lista aumenti.

4) Un'alternativa proposta, che comunque necessita di salvare alcuni elementi è presentata nel file test_meeting_room_simple_secondversion.py


5) L'alternativa è molto più contorta e ha molti cicli (sicuramente ottimizzabili) al suo interno. Non so se ci sono dei modi per fare più cose contemporaneamente senza cercare nello specifico su internet. Il vantaggio di questo metodo è il fatto che al massimo il numero di cose da salvare è il numero di slot disponibili e non dipende dal punto di vista della "memoria" dal numero di prenotazioni. Inoltre contiene le informazioni sulle "fasce orarie" più occupate e ha già una struttura per eventuali lavori successivi.

6) Commento finale. In entrambi i metodi non ho usato strutture complesse / librerie esterne perchè non ho particolare dimestichezza e avrei dovuto cercare moolto su internet (volevo evitare visto lo scopo). Sono consapevole che magari esiste un modo per risolvere il problema in molto spazio ma non so se python ha dei metodi per "sovrapporre dei range". 
