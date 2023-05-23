class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length-1;
        int currmax = 0, ans = 0;
        while(right > left){
            int width = right - left;
            int hgt = Math.min(height[left], height[right]);
            currmax = width * hgt;
            ans = Math.max(currmax, ans);
            if (height[left] > height[right]){
                right--;
            }
            else{
                left++;
            }
        }
        return ans;
    }
}