class Solution {
    private int[][] array;
    
    public int longestCommonSubsequence(String text1, String text2) {
        array = new int[text1.length()+1][text2.length()+1];
        return helper(text1, text2, 0, 0);
    }
    public int helper(String text1, String text2, int i, int j){
        if (i == text1.length() || j == text2.length()){
            return array[i][j] = 0;
        }
        if (array[i][j] != 0){
            return array[i][j];
        }
        if (text1.charAt(i) == text2.charAt(j)){
            return array[i][j] = 1 + helper(text1, text2, i+1, j+1);
        }
        else{
            return array[i][j] = Math.max(helper(text1, text2, i+1, j), helper(text1, text2, i, j+1));
        }
        
    }
}