

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
    /*
    
    long long start = 0, end = x, mid;
    if (x == 1 || x == 0){
        return x;
    }
    while (start < end){
        mid = (start + end) / 2;
        if ((mid * mid) > x){
            end = mid-1;
        }
        else if ((mid * mid) < x){
            start = mid+1;
        }
        else{
            return mid;
        }
    }*/
    return 0;
}