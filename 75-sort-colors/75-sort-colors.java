class Solution {
    public void sortColors(int[] nums) {
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
    }
    
}