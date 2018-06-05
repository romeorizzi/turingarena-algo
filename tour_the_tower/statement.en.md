A question: in the tower of Hanoi puzzle, does there exists a sequence of moves which allows to visit each valid configuration precisely once? (A configuration is a placement of the $n$ disks on the three pegs; it is valid when no disk is placed on top of a smaller one.)
In this problem you are asked to compute the number of valid configurations and to settle the above question with an algorithm yielding a solution for every possible $n$.
If the question is clear to you, produce the template file for your choosen language: you can directy start from there.
Keep on reading here otherwise, if the question remains rather obscure to you.
In case you don't know the tower of Hanoi classic puzzle, we suggest you to first approach that famous problem, you can find the classic version plus some variants among the problems of TuringArena. In any case, we provide the necessary background and some links here below.

In the figure you see a wooden set of the tower of Hanoi puzzle game.

![Hanoi tower with $8$ disks.](figures/220px-Tower_of_Hanoi.jpeg)

Three vertical rods rise up from a basement.
We are also given $n$ wooden disks of different sizes, and numbered from $1$ to $n$, from the smallest to the largest. The disks are actually donuts, that is, they have an hole which allows to slide them onto the vertical rods.
The puzzle starts with the disks orderly stacked on the first rod, the smallest disk $1$ at the top, thus making a conical shape resting on the largest disk $n$ placed over the wooden basement.

The objective of the puzzle is to move the entire stack to the third rod, obeying the following simple rules:

1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
3. No disk may be placed on top of a smaller disk.

Applet to play:
http://www.softschools.com/games/logic_games/tower_of_hanoi/

Animated gif with solution when $n=4$: 

![optimal solution for $n=4$](figures/Tower_of_Hanoi_4.gif)


Some references:

https://en.wikipedia.org/wiki/Tower_of_Hanoi
