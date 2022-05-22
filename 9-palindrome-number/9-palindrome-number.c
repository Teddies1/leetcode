#include <math.h>


bool isPalindrome(int x){
    if (x != 0 && x % 10 == 0){
        return false;
    }
    if (x < 0){
        return false;
    }
    if (x == 0){
        return true;
    }
    int count = 0;
    int temp = x;
    long long res = 0;
    int num = 0;
    
    /*while(temp){
        num = temp % 10;
        count++;
        temp /= 10;
    }
    temp = x;*/
    
    while(temp){
        num = temp % 10;
        res += num;
        res *= 10;
        temp /= 10;
    }
    res /= 10;
    
    
    return (res == x);
}