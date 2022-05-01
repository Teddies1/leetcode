

void reverseString(char* s, int sSize){
    int end = sSize-1;
    int start = 0;
    int temp;
    if (sSize <= 1){
        return;
    }
    temp = s[start];
    s[start] = s[end];
    s[end] = temp;
    
    reverseString(s+1, sSize-2);
    
    
    
}