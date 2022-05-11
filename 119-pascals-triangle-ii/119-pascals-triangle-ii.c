

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* getRow(int rowIndex, int* returnSize){
    int i,j;
    *returnSize = (rowIndex + 1);
    int** array = (int**)malloc(sizeof(int*)* (rowIndex + 1));
    
    for (i = 0; i < (rowIndex + 1); i++){
        array[i] = (int*)malloc((i+1) * sizeof(int));
        for (j = 0; j <= i; j++){
            if (j == 0 || j == i){
                array[i][j] = 1;
            }
            else{
                array[i][j] = array[i-1][j-1] + array[i-1][j];
            }
            
        }
        
    }
    return array[rowIndex];
    
}