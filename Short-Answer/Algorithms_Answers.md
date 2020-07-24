#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

The runtime will depend on the input n with larger n values taking longer to run.

b) O(n^2)

The first for loop is O(n) and the nested while loop is also O(n), so the runtime complexity is O(n^2).

c) O(n)

The recursive function will run n times before reaching the base case. 



## Exercise II
We can use a binary search to find the optimal distance for dropping the egg. We would start by dropping the egg at the middle floor of the building. If the egg breaks, then we are too high. We can move to the middle of the lower half and repeat the process. If the egg didn't break at the middle, we would go to the middle of the upper half. This would have a runtime complexity of O(log n). 


