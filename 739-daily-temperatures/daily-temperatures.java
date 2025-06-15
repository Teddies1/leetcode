class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] ans = new int[n];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++){
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]){
                int index = stack.pop();
                ans[index] = i - index;
            }
            stack.push(i);
        }

        return ans;
        /*
            stack contains 0
            check 74, 74 > 73 so ans[0] = 1 - 0 = 1, add 74 to stack
            check 75, 75 > 74 so ans[1] = 2 - 1 = 1, add 75 to stack
            check 71, 71 < 75 so add 71 to stack
            check 69, 69 < 71 so add 69 to stack

            check 72, 72 > 69 so ans[4] = 5 - 4 = 1
            check 71, 72 > 71 so ans[3] = 5 - 3 = 2
        
         */
    }   
}