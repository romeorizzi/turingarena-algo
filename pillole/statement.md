Pillole (pillole)

# Descrizione del problema

La zia Lucilla deve assumere ogni giorno mezza pillola di una certa medicina. Lei inizia il trattamento
con una bottiglia che contiene esattamente N pillole.
Durante il primo giorno lei prende una pillola dalla bottiglia, la spezza in due, ne ingerisce una
metà e rimette l'altra metà nella bottiglia.
Nei giorni seguenti lei prende un pezzo a caso della bottiglia (potrebbe essere una pillola intera
o una mezza pillola). Se ha pescato una mezza pillola la ingerisce. Se ha pescato una pillola intera la
spezza a metà, rimette una delle due mezze pillole nella bottiglia e ingerisce l'altra mezza pillola.
La zia può così svuotare la bottiglia in tanti modi diversi. Rappresentiamo il trattamento come una
stringa di 2N caratteri, in cui il carattere i è I se la zia ha pescato una pillola intera nel giorno i e M
se la zia ha invece pescato una mezza pillola. Nel caso in cui la bottiglia originaria contiene 3 pillole
intere, le possibili sequenze sono le seguenti:

IIIMMM IIMIMM IIMMIM IMIIMM IMIMIM

Quindi vi sono 5 modi sostanzialmente diversi di consumare un vasetto di 3 pillole.

# Goals

Goal 1: offri un'implementazione corretta della funzione num_modi(N) che, dato in input l'intero N,
ritorna il numero dei possibili modi di consumare un vasetto di N pillole.
L'implementazione è considerata corretta se risponde correttamente per ogni numero naturale N <= 10.

Goal 2: offri un'implementazione corretta della procedura elenca_modi() che, dato N, elenca uno
ad uno tutti gli num_modi(N) modi possibili. Per comunicare un dato modo al programma valutatore,
la funzione utilizza N chiamate alla primitiva pescatoMezza() ed N chiamate alla primitiva pescatoIntera(), nel giusto ordine, ed infine una chiamata alla callback done().

Ad esempio, per comunicare il modo IIMMIM, la procedura elenca_modi(3) dovrebbe effettuare la seguente sequenza di chiamate:

pescatoIntera()
pescatoIntera()
pescatoMezza()
pescatoIntera()
pescatoMezza()
pescatoMezza()
done()

Goal 3: offri un'implementazione corretta ed efficiente della funzione num_modi(N). In pratica,
il tuo codice dovrà rispondere entro una frazione di secondo per ogni N <= 30.
Si noti che la risposta è un numero grande fino a 3814986502092304.
(E'per questa ragione che utilizziamo tipi numerici di sufficiente capienza.)

