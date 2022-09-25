class Solution {
    public int coinChange(int[] coins, int amount) {
        /*
        dp[0] = 0
        dp[1] = 1
        dp[2] = min(2, 1) = 1
        dp[3] = min(2, 2) = 2
        dp[4] = min(3, 2) = 2
        dp[5] = min(3, 3, 1) = 1
        dp[6] = min(2, 3, 2) = 2
        dp[7] = min(3, 2, 2) = 2
        dp[8] = min(3, 3, 3) = 3
        dp[9] = min(4, 3, 3) = 3
        dp[10] = min(4, 4, 2) = 2
        dp[11] = min(3, 4, 3) = 3
        */
        int[] dp = new int[amount+1];
        for (int i = 0; i < amount+1; i++){
            dp[i] = amount+1;
        }
        dp[0] = 0;
        for (int i = 1; i < amount+1; i++){
            for (int coin: coins){
                if ((i-coin) >= 0){
                    dp[i] = Math.min(dp[i], dp[i-coin] + 1);
                }
            }
        }
        for (int i = 0; i < amount+1; i++){
           System.out.println(dp[i]);
        }
        return (dp[amount] > amount) ? -1 : dp[amount];
    }
}