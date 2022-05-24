

/**
 * Note: The returned array must be malloced, assume caller calls free().
}
 */


int* countBits(int n, int* returnSize){
    *returnSize = n+1;
    int *array = (int*)malloc(sizeof(int)* *returnSize);
    int count = 0;

    for (int i = 0; i <= n; i++){
        unsigned int temp = i;
        while(temp){
            if ((1 & temp) == 1){
                count++;
            }
            temp >>= 1;
        }
        array[i] = count;
        count = 0;
        temp = i;
    }
    
    return array;
}