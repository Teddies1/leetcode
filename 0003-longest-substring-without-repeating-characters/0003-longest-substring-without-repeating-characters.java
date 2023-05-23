class Solution {
    public int lengthOfLongestSubstring(String s) {
        /*
        HashMap<Character, Integer> maps = new HashMap<>();
        int lp = 0, rp = 0, ans = 0, max = 0;
        for (rp = 0; rp < s.length(); rp++){
            if (maps.containsKey(s.charAt(rp))){
                while(rp >= lp && s.charAt(lp) == s.charAt(rp)){
                    maps.remove(s.charAt(lp));
                    lp++;
                }
            }
            maps.put(s.charAt(rp), rp);
            max= Math.max(max, rp - lp + 1);
        }
        return max;
        */
        int[] nextOccurence = new int[128];
        int ans = 0;
        int left = 0;
        for (int i = 0; i < s.length(); i++){
            left = Math.max(left, nextOccurence[s.charAt(i)]);
            ans = Math.max(ans, i - left + 1);
            nextOccurence[s.charAt(i)] = i + 1;
        }
        return ans;
    }
}