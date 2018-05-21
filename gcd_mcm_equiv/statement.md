Let $a$ and $b$ be two positive integers.
The *minimum common multiple* $\mcm(a,b)$ of $a$ and $b$ is the minimum integer which is divisible both by $a$ and by $b$.
We need to compute $\mcm(\cdot,\cdot)$ when summing fractions.

The *greatest common divisor* $\gcd(a,b)$ of $a$ and $b$ is the maximum integer which divides both $a$ and $b$.
We need to compute $\gcd(\cdot,\cdot)$ when solving modular equations and in many other situations.

In this exercise we are not asking you to solve any problem like computing $\mcm(\cdot,\cdot)$ or $\gcd(\cdot,\cdot)$, but rather to explore the mutual relation among these two problems.
First show that the problem of computing $\mcm(\cdot,\cdot)$ is no way more difficult than the problem of computing $\gcd(\cdot,\cdot)$ by reducing the former to the latter. Assume to have access to an oracle that answers any $\gcd(\cdot,\cdot)$ query you may pose her and write a function that correctly computes $\mcm(\cdot,\cdot)$ by resorting on this oracle.

Next, prove the equivalence of the two problems by providing a reduction in the opposite direction. Assume to have access to an oracle that answers any $\mcm(\cdot,\cdot)$ query you may pose her and write a function that correctly computes $\gcd(\cdot,\cdot)$ by resorting on this oracle.
