You first receive a list of natural numbers list_of_vals.

Next, you receive a natural number val.
In as short time as possible,
you must find out whether val occurs among the numbers in list__of_vals.

You should submit a file containing the implementations of two functions.

1. the database set up function:
      function store_list(int n, int[] list_of_vals)
   which is allowed to take O(n) time;

2. the query function:
      function find_val(int val) -> int;
      // find_val returns the first position of val within list_of_vals
      // returns -1 if val does not occur within list_of_vals

In a full solution, function find_val should cost only polylogarithmic time.