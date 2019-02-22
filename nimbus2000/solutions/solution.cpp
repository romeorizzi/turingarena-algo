
/*
1 x_A y_A
1 x_B y_B
1 x_C y_C

Area of triangle ABC = determinant of the above matrix.
  In other words,
*/

int area(int x_A, int y_A, int x_B, int y_B, int x_C, int y_C) {
     return  x_A * y_B + x_B * y_C + x_C * y_A
            -x_B * y_A - x_C * y_B - x_A * y_C;
}

int can_go(int x1, int y1, int x2, int y2, int x3, int y3,
	   int x1_t, int y1_t, int x2_t, int y2_t, int x3_t, int y3_t) {
  return area(x1, y1, x2, y2, x3, y3) == area(x1_t, y1_t, x2_t, y2_t, x3_t, y3_t);
}
  
