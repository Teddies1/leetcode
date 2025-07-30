class Solution {
    public boolean canArrange(int[] arr, int k) {
        if (arr == null){
            return false;
        }
        int[] freqMap = new int[k];

        for (int number: arr){
            int remainder = (number % k);
            if (remainder < 0){
                remainder += k;
            }
            freqMap[remainder]++;

        }

        if (freqMap[0] % 2 == 1){
            return false;
        }
        
        for (int i = 1; i < (k / 2)+1; i++){
            if (freqMap[i] != freqMap[k-i]){
                return false;
            }
        }

        return true;
    }
}