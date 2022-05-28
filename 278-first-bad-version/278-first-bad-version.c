// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n) {
    if (n == 1){
        return isBadVersion(1);
    }
    for (int i = n; i >= 0; i--){
        if (isBadVersion(i-1) == false){
            return i;
            
        }
    }
    return 0;
}