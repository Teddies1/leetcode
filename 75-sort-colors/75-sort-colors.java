class Solution {
    public void sortColors(int[] nums) {
        /*
        int[] colors = new int[3];
        int j = 0;
        
        for(int i = 0; i < nums.length; i++){
            colors[nums[i]]++;
        }
        for (int i = 0; i < 3; i++){
            while(colors[i] > 0){
                nums[j++] = i;
                colors[i]--;
            }
        }
        */
        int low = 0, high = nums.length-1, iter = 0;
        int temp;
        while (iter <= high){
            if(nums[iter] == 0){
                temp = nums[iter];
                nums[iter] = nums[low];
                nums[low] = temp;
                low++; 
                iter++;
            }
            else if(nums[iter] == 1){
                iter++;
            }
            else{
                temp = nums[iter];
                nums[iter] = nums[high];
                nums[high] = temp;
                high--;
            }
        }
    }
    
}