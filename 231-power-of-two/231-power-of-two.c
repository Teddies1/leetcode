

bool isPowerOfTwo(int n){
    /*
    1
    10
    100
    1000
    10000
    */
    
    long count = 0;
    if (n < 0){
        return false;
    }
    while(n){
        if ((n & 1) == 1){
            count++;
        }
        n >>= 1;
    }
    if (count == 1){
        return true;
    }
    else{
        return false;
    }
    
}