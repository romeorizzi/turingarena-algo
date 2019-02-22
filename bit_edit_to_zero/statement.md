# Da n a zero in meno mosse possibile

Ricevi in input un numero n e devi trasformarlo nel numero 0 impiegando il minor numero possibile di mosse.
Hai a disposizione due tipi di mosse, entrambe operano sulla rappresentazione in binario del numero n:

1. cambiare il bit più a destra, ossia il bit di parità (quello meno rappresentativo);
2. cambiare il bit alla immediata sinistra del bit posto più a destra tra quelli settati ad uno. (Subito a destra del bit che si modifica deve esserci un bit settato ad 1, e non vi è alcun bit settato ad uno a destra di questo).

Devi implementare le seguenti due funzioni:
   * la function num_mosse(n) deve ritornare il minimo numero di mosse per passare da n a zero;
   * la function mossa(n) ritorna 1 oppure 2: la risposta i (=1,2) è corretta se la mossa i ci porta un passo più vicini allo zero.

# Goals:
 + goal 1: Dato un numero n <= 2^10, la tua funzione num_mosse(n) restituisce il minimo numero di mosse per trasformarlo in 0.
 + goal 2: Dato un numero n <= 100000, num_mosse(n) restituisce il minimo numero di mosse per trasformarlo in 0.
 + goal 3: Per n <= 2^10, la tua funzione mossa(n) restituisce una mossa ottimale: applicando iterativamente la mossa suggerita della tua funzione mossa giungo a zero nel minimo numero di mosse. Il tempo e la dimensione stessa del programma sono limitati. 
 + goal 4: Per n <= 10^6, la tua funzione mossa(n) restituisce una mossa ottimale nei limiti di tempo assegnati. 

