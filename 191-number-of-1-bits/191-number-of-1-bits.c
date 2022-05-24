int hammingWeight(uint32_t n) {
    int i = 1;
    int res = 0;
    
    while(n){
        if ((1 & n) == 1){
            res++;
        }
        n >>= 1;
    }
    return res;
    
}