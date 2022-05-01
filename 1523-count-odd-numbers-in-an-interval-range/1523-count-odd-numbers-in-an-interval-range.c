

int countOdds(int low, int high){
    int count = 0;
    int range = high - low + 1;
    if(range % 2 == 0){
        return range/2;
    }
    else{
        if (low % 2 && high % 2){
            return range/2 + 1;
        }
        else if( !(low%2) && !(high%2)){
            return range/2;
        }
    }
    return 0;
    
}