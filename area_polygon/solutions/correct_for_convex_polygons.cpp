// evaluation_assert data["goals"]["collinearity_check"]
// evaluation_assert data["goals"]["triangles"]
// evaluation_assert data["goals"]["convex_polygons"]
// evaluation_assert not data["goals"]["all_polygons"]


int signed_area_of_triangle(int* A, int* B, int* C) {
/*
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

*/
  
  return  ( A[0] * B[1] + B[0] * C[1] + C[0] * A[1]
	   -B[0] * A[1] - C[0] * B[1] - A[0] * C[1] ) /2;
}

int my_abs(int a) { return (a>=0) ? a : -a; }

int area_of_polygon(int n, int** vertex) {
  int area = 0;
  for(int i = 2; i<n; i++)
    area += signed_area_of_triangle(vertex[0], vertex[i-1], vertex[i]);
  return my_abs(area);
}
