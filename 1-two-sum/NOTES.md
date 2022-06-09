o(n^2) solution is that for each element in the array, you iterate through the array again to find its two sum counterpart. \
this requires a nested for loop.

o(n) solution is to maintain a hash table of array elements mapped to an index key whilst traversing the array. 
then, for each element in the array, check if its two sum counterpart is in the hash table. 
if yes, then return the index key. if no, then store this element in the hash table and continue traversing. 

