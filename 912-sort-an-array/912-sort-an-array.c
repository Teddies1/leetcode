

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void merge(int* array, int left, int middle, int right){
    int i = left, j = middle+1, k = 0;
    int N = right - left + 1;
    int temp[N];
    while (i <= middle && j <= right){
        if (array[i] < array[j]){
            temp[k++] = array[i++];
        }
        else{
            temp[k++] = array[j++];
        }
    }
    while (i <= middle){
        temp[k++] = array[i++];
    }
    while (j <= right){
        temp[k++] = array[j++];
    }
    for (k = 0; k < N; k++){
        array[k+left] = temp[k];
    }
}
void mergesort(int low, int high, int* array){
    int mid;
     
    if (low < high){
        mid = (low + high)/2;
        mergesort(low, mid, array);
        mergesort(mid + 1, high, array);
        merge(array, low, mid, high);
    }
}
int* sortArray(int* nums, int numsSize, int* returnSize){
    *returnSize = numsSize;
    mergesort(0, numsSize-1, nums);

    return nums;
    
}