# Componenti fortemente connesse

Una componente fortemente connessa di un grafo diretto G è un sottografo massimale di G in cui esiste un cammino orientato tra ogni coppia di nodi ad esso appartenenti.

Le componenti fortemente connesse formano una partizione di G poiché un nodo non può trovarsi contemporaneamente in due componenti fortemente connesse, di conseguenza un grafo diretto è fortemente connesso se e solo se ha una sola componente connessa.

Due vertici di G sono fortemente connessi se e solo se fanno parte dello stesso ciclo orientato. 

(Definizione tratta da [wikipedia](https://it.wikipedia.org/wiki/Componente_fortemente_connessa)

### Funzioni
<description for="scc">
Dovrai implementare la procedura `scc` che prevede i seguenti parametri:
- <param>N</param> numero di nodi del grafo
- <param>Dout</param> grado uscente di un nodo
- <param>Aout</param> lista di adiacenza uscente di un nodo
- <param>Din</param> grado entrante di un nodo
- <param>Ain</param> lista di adiacenza entrante di un nodo

Dovrai comunicare il risultato invocando le seguenti callback:
- <param>start_component()</param> avvia una nuova componente connessa
- <param>add_node(n)</param> aggiunge il nodo n alla attuale componente connessa
</description>

### Goals
Il programma prevede i seguenti goal:
- cubica: implementa una soluzione cubica O(M^2 * N)
- quadratica: implementa una soluzione quadratica O(MN)
- lineare: implementa una soluzione lineare O(M + N)

