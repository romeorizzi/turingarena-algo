# evaluation_assert data["goals"]["collinearity_check"]
# evaluation_assert data["goals"]["triangles"]
# evaluation_assert data["goals"]["convex_polygons"]
# evaluation_assert data["goals"]["all_polygons"]

import random

def signed_area_of_triangle(A, B, C):
    """
    returns the "signed" area of the triangle whose vertices are:
    1.    A=(A[0],A[1])=(x_A,y_A),
    2.    B=(B[0],B[1])=(x_B,y_B),
    3.    C=(C[0],C[1])=(x_C,y_C),
    The area is "signed" in that it can be either:
    - zero when the three points are collinear;
    - negative, when A,B,C is the cyclic order in which the vertices are encountered proceeding clockwise; 
    - positive, when A,B,C is the cyclic order in which the vertices are encountered proceeding counter-clockwise.
    An important fact to know: 
    The signed area value equals the precise half of the determinant value of the following 3x3 matrix:

       1 x_A y_A
       1 x_B y_B
       1 x_C y_C
    """

    return  (   A[0] * B[1] + B[0] * C[1] + C[0] * A[1]     \
               -B[0] * A[1] - C[0] * B[1] - A[0] * C[1] ) /2

assert signed_area_of_triangle([0,0], [2,0], [1,1]) == 1
assert signed_area_of_triangle([0,0], [1,1], [2,0]) == -1

def determinant3(M):
    return M[0][0]*M[1][1]*M[2][2]+M[0][1]*M[1][2]*M[2][0]+M[0][2]*M[1][0]*M[2][1]    \
          -M[0][2]*M[1][1]*M[2][0]-M[0][1]*M[1][0]*M[2][2]-M[0][0]*M[1][2]*M[2][1]

def determinant2(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]

def signed_area_of_triangle_as_determinant3(A, B, C):
    M = [ (1, 1, 1), (A[0], B[0], C[0]), (A[1], B[1], C[1])]
    return determinant3(M) / 2

def signed_area_of_triangle_as_determinant2(A, B, C):
    M = [ tuple(map(lambda x, y: x - y, B, A)), tuple(map(lambda x, y: x - y, C, A))]
    return determinant2(M) / 2

Points = [(random.randint(-100,100), random.randint(-100,100)) for _ in range(5)]
for A in Points:
    for B in Points:
        for C in Points:
            assert signed_area_of_triangle(A, B, C) == signed_area_of_triangle_as_determinant3(A, B, C)
            assert signed_area_of_triangle(A, B, C) == signed_area_of_triangle_as_determinant2(A, B, C)


def my_abs(a):
    if a >= 0:
        return a
    else:
        return -a

def area_of_polygon(n, vertex):
  area = 0
  for i in range(2,n):
    area += my_abs( signed_area_of_triangle(vertex[0],vertex[i-1],vertex[i]) )
  return area

