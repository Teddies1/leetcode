#include <math.h>
#include <stdio.h>

int kthGrammar(int n, int k){
    /*
    1)        0                   1    2    3    4 
    2)        01                 1 2  3 4  5 6  7 8          parent index is current index divided by 2
    3)       0110                                            and rounded up
    4)     01101001           
    5) 0110100110010110  
    */
    if (n == 1){
        return 0;
    }
    if (k == 1){
        return 0;
    }
    int parent = kthGrammar(n-1, k/2 + k%2);
    
    if (parent == 1){
        if (k % 2 == 0){
            return 0;
        }
        else{
            return 1;
        }
    }
    else{
       if (k % 2 == 0){
            return 1;
        }
        else{
            return 0;
        } 
    }
     
}