from turingarena import *

import random, math

algorithm = submitted_algorithm()

done_moves = 0
wrong_move = False
rod = [1 for _ in range(10)] # stores a config: rod[disk] tells the peg on which disk is currently sitting

goals = {
    "collinearity_check": True,
    "triangles": True,
    "convex_polytopes": True,
    "polygons": True,
}

def correct_signed_area_of_triangle(A, B, C):
    """
    returns the "signed" area of the triangle whose vertices are:
    1.    A=(A[0],A[1])=(x_A,y_A),
    2.    B=(B[0],B[1])=(x_B,y_B),
    3.    C=(C[0],C[1])=(x_C,y_C),
    The area is "signed" in that it can be either:
    - zero when the three points are collinear;
    - positive, when A,B,C is the cyclic order in which the vertices are encountered proceeding clockwise; 
    - positive, when A,B,C is the cyclic order in which the vertices are encountered proceeding clockwise.
    An important fact to know: 
    The signed area value equals the determinant value of the following 3x3 matrix:
       1 x_A y_A
       1 x_B y_B
       1 x_C y_C
    """
    return  A[0] * B[1] + B[0] * C[1] + C[0] * A[1] \
           -B[0] * A[1] - C[0] * B[1] - A[0] * C[1]



def correct_area_of_polytope(n, vertex):
   area = 0;
   for i in range(2,n):
       area += correct_signed_area_of_triangle(vertex[0], vertex[i-1], vertex[i])
   return math.fabs(area)


for N in range(5):
    if goals["collinearity_check"] == True:
        A = [2*random.randint(-49, 50), 2*random.randint(-49, 50)]
        B = [2*random.randint(-49, 50), 2*random.randint(-49, 50)]
        multiplier = random.randint(0,10)
        C = [a + multiplier*(b-a) for a, b in zip(A, B)]
        # A,B,C should be three collinear points in the xy-plane
        assert correct_area_of_polytope(3, [A,B,C]) == 0
        with algorithm.run() as process:
            print("considering the three collinear points ", [A,B,C])
            risp = process.call.area_of_polytope(3, [A,B,C])
            if risp == 0:
                print(f'Your area_of_polytope function returned  0. This is CORRECT.')
            else:
                print(f'Your area_of_polytope function returned  {risp}. This is WRONG.')
                goals["collinearity_check"] = False
                goals["triangles"] = False
                goals["convex_polytopes"] = False
                goals["polygons"] = False

        C[1] += 2
        # A,B,C should now be three NON collinear points in the xy-plane
        assert correct_area_of_polytope(3, [A,B,C]) != 0
        with algorithm.run() as process:
            print("considering the three NON-collinear points ", [A,B,C])
            risp = process.call.area_of_polytope(3, [A,B,C])
            if risp != 0:
                print(f'Your area_of_polytope function returned a NON-zerp value. This is CORRECT.')
            else:
                print(f'Your area_of_polytope function returned  {risp}. This is WRONG.')
                goals["collinearity_check"] = False
                goals["triangles"] = False
                goals["convex_polytopes"] = False
                goals["polygons"] = False
            if goals["triangles"] == True and risp != correct_area_of_polytope(3, [A,B,C]):
                print("considering triangle ", [A,B,C])
                print(f'The true value of its area is {correct_area_of_polytope(3, [A,B,C])}. However, your area_of_polytope function returned {risp}. This is WRONG.')
                goals["triangles"] = False
                goals["convex_polytopes"] = False
                goals["polygons"] = False

for N in range(5):
    if goals["triangles"] == True:
        A = [2*random.randint(-4, 5), 2*random.randint(-4, 5)]
        B = [2*random.randint(-4, 5), 2*random.randint(-4, 5)]
        C = [2*random.randint(-4, 5), 2*random.randint(-4, 5)]            
        print("considering triangle ", [A,B,C])
        with algorithm.run() as process:
            print("considering triangle ", [A,B,C])
            risp = process.call.area_of_polytope(3, [A,B,C])
            if risp == correct_area_of_polytope(3, [A,B,C]):
                print(f'area_of_polytope -> {risp:d}. This is CORRECT.')
            else:
                print(f'The true value of its area is {correct_area_of_polytope(3, [A,B,C])}. However, your area_of_polytope function returned {risp}. This is WRONG.')
                goals["triangles"] = False
                goals["convex_polytopes"] = False
                goals["polygons"] = False

for N in range(3,10):
    if goals["convex_polytopes"] == True:
        P=[[0,0]] + [[20*(N-i) +2*max(i,N-i), 20*i +2*max(i,N-i)] for i in range(N-1)]
        print("considering polytope ", P)
        with algorithm.run() as process:
            risp = process.call.area_of_polytope(N, P)
            if risp == correct_area_of_polytope(N, P):
                print(f'area_of_polytope -> {risp:d}. This is CORRECT.')
            else:
                print(f'area_of_polytope -> {risp:d}. This is WRONG.')
                goals["convex_polytopes"] = False
                goals["polygons"] = False
        P = list(reversed(P))        
        print("considering polytope ", P)
        with algorithm.run() as process:
            risp = process.call.area_of_polytope(N, P)
            if risp == correct_area_of_polytope(N, P):
                print(f'area_of_polytope -> {risp:d}. This is CORRECT.')
            else:
                print(f'area_of_polytope -> {risp:d}. This is WRONG.')
                goals["convex_polytopes"] = False
                goals["polygons"] = False
            

            
evaluation_result(goals=goals)
