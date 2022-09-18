class Solution {
    public int longestPalindrome(String s) {
        int count = 0;
        int flag = 0;
        int[] letter = new int[58];
        for (int i = 0; i < s.length(); i++){
            int word = s.charAt(i) - 65;
            letter[word]++;
        }
        for (int i = 0; i < letter.length; i++){
            if (letter[i] % 2 == 0){
                count += letter[i];
            }
            else{
                flag = 1;
                count += letter[i] - 1;
            }
        }
        if (flag == 1){
            count++;
        }
        return count;
    }
}