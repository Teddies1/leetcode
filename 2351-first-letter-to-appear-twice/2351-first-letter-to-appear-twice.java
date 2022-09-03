class Solution {
    public char repeatedCharacter(String s) {
        HashMap<Character, Integer> hash = new HashMap<Character, Integer>();
        char res = ' ';
        int count = 0;
        for (int i = 0; i < s.length(); i++){
            
            System.out.println(hash);
            if (hash.containsKey(s.charAt(i))){
                res = s.charAt(i);
                break;
            }
            hash.put(s.charAt(i), 1);
            
        }
        return res;
    }
}