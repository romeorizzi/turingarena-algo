Write a function that finds out the heaviest murble into a set of n murbles numbered from 0 to n - 1.

int individua(long int n, long int maxLies) {
...
}

Il parametro n che viene passato alla tua funzione è il numero di biglie che essa dovrà gestire. Il valore di ritorno dovrà essere un'intero tra 0 ed n-1, e dovrà corrispondere all'indice della biglia di peso massimo.
E' dato sapere che le n biglie differiscono tutte per peso. Per confrontarle, potrai servirti di una bilancia a braccia eguali invocando, dalla tua implementazione della procedura individua, la seguente funzione:

The parameter n which gets passed to your function is the number of murbles under exam. The return value must be an integer from 0 to n-1, namely, the index of the heaviest murble.
The n murbles all differ in weight. To compare them, you can use a scale by invoking, from within your implementation of procedure individua, the following function:

int pesa(long int bigliaA, long int bigliaB)

Function pesa returns
* -1, if bigliaA is leighter than bigliaB;
* 1, if bigliaA is heavier than bigliaB.
In the more advanced subtask, the scale can tell some lies, but only at most maxLies of them, the second input parameter of function individua.


Subtasks
* Subtask 0 [1 punti]: the heaviest murble is numbered 2.
* Subtask 1 [2 punti]: n = 2, the scale is always true (maxLies= 0).
* Subtask 2 [4 punti]: maxLies= 0, you are allowed at most n calls to int pesa.
* Subtask 3 [8 punti]: maxLies= 0, at most n - 1 calls to int pesa.
* Subtask 4 [16 punti]: at most one single lie (maxLies≤ 1).
* Subtask 5 [5 punti]: maxLies≤ 1), at most 3n - 3 calls to int pesa.
* Subtask 6 [32 punti]: maxLies≤ 1, at most 2n calls to int pesa.
* Subtask 7 [16 punti]: maxLies≤ 1, at most 2n - 1 calls to int pesa.
* Subtask 8 [16 punti]: maxLies≤ k, at most (k + 1)(n - 1) + k = n(k + 1) - 1 calls to int pesa.

Assumptions
* The program stops after the first call to function pensoCheMaxSia or when the time limit has been
exceeded.
* 1 ≤ n ≤ 1 000 000.