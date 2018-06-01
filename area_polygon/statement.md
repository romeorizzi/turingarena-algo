It is a curious fact that if we pick up any three points $A$, $B$ and $C$ of the $xy$ plane, all three having only integer coordinates, then the double of the area of the triangle $ABC$ will be a natural number.
In producing a most simple and robust solution to the algorithmic problem here below you are likely to assess this truth and actually get some elegant proof of it as a byproduct or corollary of your sound work. 

   Given three points in the plane, compute the area of the triangle having them as its vertices.

More in general, given the (cyclically) ordered list of the vertices of a polygon, compute the area of that polygon. Also here, with an elegant solution you might possibly realize that if all coordinates of all vertices are even integer numbers then the area will be an even natural. Could you discover this more general truth as a self-refinement of the above one (that is, as a corollary of its special case)?  


==Subtask==
Subtask 1: given three points, return zero iff the three points are collinear
Subtask 2: correctly compute the area of triangles
Subtask 3: correctly compute the area of convex polytopes
Subtask 4: correctly compute the area of the enclosed polygon when the closed broken line joining the points vertex[0], vertex[1], ..., vertex[n-1], vertex[0] is simple (that is, no two segments of the broken line share a point except for segments that are consecutive in the cyclic order which of course share the common endpoint).

==Assumption==

In all instances (that is, test cases) submitted to your code, all coordinates of all vertices are even integers. As such, there exist simple solutions to this challenge where computation will remain within the integers, these have no risk to produce rounding errors. Still, a solution is a solution: you are allowed to internally work with floats. In this case, be reassured that rounding to the closest integer will produce the precise answer. (However, simply rounding down might not). 