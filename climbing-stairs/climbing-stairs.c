

int climbStairs(int n){
    int array[45];
    
    // if you count n = 5,
    // notice that n[5] is n[4] + n[3]. basically n-1 + n-2
    
    //base cases up to n = 3

    array[0] = 1;
    array[1] = 2;
    
    
    
    for (int i = 2; i < n; i++){
        array[i] = array[i-1] + array[i-2];
    }
    
    return array[n-1];
    
}