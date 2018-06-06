It is a curious fact that if we pick up any three points $A$, $B$ and $C$ of the $xy$ plane, all three having only integer coordinates, then the double of the area of the triangle $ABC$ will be a natural number.
In producing a most simple and robust solution to the algorithmic problem here below you are likely to assess this truth (get your own proof as a byproduct) and generalize it to polygons. 

Goal 1: Given three points $A$, $B$, $C$ in the $xy$ plane, say:
           $A=(A_x,A_y)$, $B=(Bx,By)$, $C=(Cx,Cy)$,
	determine whether these three points are collinear.   

Goal 2: Given the three points, compute the area of the triangle having them as its vertices. It will help you to know that, if the vertices are labelled $A$, $B$, $C$ going round the triangle anti-clockwise, then the value of the area equals the precise half of the determinant of the following 3x3 matrix:

   1 x_A y_A
   1 x_B y_B
   1 x_C y_C

(If you are curious where this piece of magic might possibly come from, one best explanation comes form vector products. See e.g.:
https://www.youtube.com/watch?v=WeS4J4-Psqs
In any case, in this problem, we take the above formula (or any equivalent one) as our starting point, and use it for our best.)

Notice that if you swap two rows, that is, if you pick up the vertices clockwise, then the value of the determinant flips in sign.

Goal 3: More in general, given the (cyclically) ordered list of the vertices of a polygon, compute the area of that polygon. Also here, with an elegant solution you might possibly realize that if all coordinates of all vertices are even integer numbers then the area will be an even natural. Could you discover this more general truth as a self-refinement of the above one (that is, as a corollary of its special case)?  


==Goal Summary ==
Goal 1: given three points, return zero iff the three points are collinear
Goal 2: correctly compute the area of triangles
Goal 3: correctly compute the area of convex polytopes
Goal 4: correctly compute the area of the enclosed polygon when the closed broken line joining the points vertex[0], vertex[1], ..., vertex[n-1], vertex[0] is simple (that is, no two segments of the broken line share a point except for segments that are consecutive in the cyclic order which of course share the common endpoint).

==Assumption==

In all instances (that is, test cases) submitted to your code, all coordinates of all vertices are even integers. As such, there exist simple solutions to this challenge where computation will remain within the integers, these have no risk to produce rounding errors. Still, a solution is a solution: you are allowed to internally work with floats. In this case, be reassured that rounding to the closest integer will produce the precise answer. (However, simply rounding down might not). 