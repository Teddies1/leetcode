class Solution {
    public int maxIceCream(int[] costs, int coins) {
        int res = 0;
        Arrays.sort(costs);
        for (int i = 0; i < costs.length; i++){
            if(coins >= costs[i] && coins > 0){
                coins -= costs[i];
                res++;
            }
        }
        return res;
    }
}