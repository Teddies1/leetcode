class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int left = 0;
        int right = n-1;
        int left_max = height[left];
        int right_max = height[right];
        int trapped_water = 0;
        while(left < right) {
            if(left_max < right_max) {
                left += 1;
                left_max = Math.max(left_max, height[left]);
                trapped_water += left_max - height[left];
            }
            else{
                right -= 1;
                right_max = Math.max(right_max, height[right]);
                trapped_water += right_max - height[right];
            }
        }
        return trapped_water;
    }
}