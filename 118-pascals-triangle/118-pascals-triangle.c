

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** generate(int numRows, int* returnSize, int** returnColumnSizes){
    int i,j;
    
    *returnSize = numRows;
    int** array = (int**)malloc(sizeof(int*)* numRows);
     *returnColumnSizes = malloc(numRows*sizeof(int));
    
    
    for (i = 0; i < numRows; i++){
        
        array[i] = (int*)malloc((i+1) * sizeof(int));
        (*returnColumnSizes)[i] = i+1;
        
        for (j = 0; j <= i; j++){
            if (j == 0 || j == i){
                array[i][j] = 1;
            }
            else{
                array[i][j] = array[i-1][j-1] + array[i-1][j];
            }
            
        }
        
    }
    return array;
}