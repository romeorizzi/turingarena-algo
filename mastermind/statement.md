Immaginati nelle vesti di un ``decodificatore''. 
Il tuo avversario, un ``codificatore'', ha scritto un codice segreto di quattro cifre, ognuna delle quali può assumere un valore tra $0$ e $5$.

Per sconfiggere il tuo avversario, devi scrivere una procedura che individui il suo codice segreto, effettuando il minor numero di tentativi.
Ad ogni tentativo riceverai un feedback che ti consentirà di ricevere informazioni sul codice segreto impostato dall'avversario.
Una prima funzione di valutazione ritorna tanti pioli neri quante sono le posizioni in cui i ìl codice segreto e quello da tè sottomesso presentano lo stesso colore. Una seconda funzione (chiamare la quale non viene conteggiato come ulteriore tentativo se la chiami sullo stesso codice che hai appena passato alla funzione sopra) ti ritorna tanti pioli bianchi quanti sono gli ulteriori colori indovinati, ma collocati fuori posto.

Le regole ti verranno forse più chiare dopo qualche partita giocata online (usa 6 colori su 4 posizioni, possibilmente ripetuti):

http://www.webgamesonline.com/mastermind/index.php


MA SE INVECE LE FUNZIONI POTESSERO TORNARE VETTORI:

Durante la fase di gioco, per capire quanto il tuo codice si avvicina a quello del tuo avversario, potrai servirti della seguente funzione:

   \texttt{void checkCode(int attempt[ ], int result[ ])}
  
\medskip
  
\noindent
La funzione \texttt{checkCode} richiede in input:

   + l'array \texttt{attempt[ ]} di quattro cifre contenente il codice da te proposto;
   + un array \texttt{result[ ]} di due elementi in cui verr\`a salvato il risultato.


Il primo elemento di \texttt{result[ ]} indica il \textbf{numero di cifre giuste al posto giusto} che hai indovinato, mentre il secondo elemento di \texttt{result[ ]} indica \textbf{il numero di cifre giuste al posto sbagliato} che hai indovinato, ovvero quelle cifre che sono presenti nel codice del tuo avversario, ma non nella posizione da te proposta.

==Subtask==
Subtask 1: nessuna limitazione sul numero di tentativi
Subtask 2: cerca di abbassare i tentativi nel caso medio
Subtask 3: cerca di abbassare i tentativi nel caso peggiore
