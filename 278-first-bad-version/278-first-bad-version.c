// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n) {
    if (n == 1){
        return isBadVersion(1);
    }
    /*
    for (int i = n; i >= 0; i--){
        if (isBadVersion(i-1) == false){
            return i;
            
        }
    }
    */
    long upper = n;
    long lower = 1;
    long mid;
    while(upper >= lower){
        
        mid = (upper + lower)/2;
    
        //if middle call is false, it means the 1st bad version is to the right
        //if middle call is true, it means the 1st bad version is to the left
        if(isBadVersion(mid) == false){
            if (isBadVersion(mid+1) == true && isBadVersion(mid-1) == false){
                return mid+1;
            }
            lower = mid+1;
        }
        else{
            if (isBadVersion(mid+1) == true && isBadVersion(mid-1) == false){
                return mid;
            }
            upper = mid-1;
        }
    }
    return mid;
}