How many comparisons do we need in order to find the maximum among $n$ elements?
You might have come up with an algorithm that settles for the maximum within $n-1$ comparisons. This exercise settles up a kind of proof/disproof game providing you a framework to formally prove that this was optimal in a rather strong sense.

To call for a comparison, your algorithm placed two elements on the two plates of a scale, and got the result of the comparison from the adversary. We will prove that even if you could choose the output of the comparision, besides the two elements involved, still $n-2$ comparisons, however choosen, will not allow to tell the maximum. With this strong statement, the dynamic nature of the process of detecting the maximum by pair comparisons fades away. You can lay down all your cards immidiately since the adversary has disappeared. 

More details:

We assume the $n$ elements of a totally ordered set are labelled with the naturals from $1$ to $n$, this label is just a name and does not have anything to do with the position of the element in the total order which is totally unknown except for what gets revealed by the comparisons. Comparisons come with an outcome: with an ordered pair of labels $(i,j)$ we represent a comparison which has established that the element labelled $j$ is bigger than the element labelled $i$ in the total order.

Goal:

Given any set of $n-2$ comparisons your algorithm must prove that:

* either the given comparisons are inconsistent. In this case your procedure should return a directed cycle, say $i_0, i_1, \ldots, i_{t-1}$ such that $(i_j, i_{(j+1})%t)$ occurs among the given comparisons for every $j$;
* or they do not allow to tell the maximum since two topological sorts exist which are compatible with the assigned comparisons but differ on which element they place last. In the second case, your procedure completes the proof by constructing the two topological sorts.

