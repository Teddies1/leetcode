

int mySqrt(int x){
    long long square, prev, i;
    
    if (x < 4 && x != 0){
        return 1;
    }
    
    for (i = 1; i <= (x/2)+1; i++){
        square = i * i;
        if (square > x){
            return i-1;
        }
        if (square == x){
            return i;
        }
    }
    return 0;
}