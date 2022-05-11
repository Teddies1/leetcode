

int climbStairs(int n){
    int array[46];
    
    // if you count n = 5,
    // notice that n[5] is n[4] + n[3]. basically n-1 + n-2
    
    //base cases up to n = 3

    array[0] = 0;
    array[1] = 1;
    array[2] = 2;
    array[3] = 3;
    array[4] = 5;
    
    for (int i = 5; i <= n; i++){
        array[i] = array[i-1] + array[i-2];
    }
    
    return array[n];
    
}