class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        if (s.length() == 1){
            return false;
        }
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            
            if (c == '(' || c == '[' || c == '{'){
                stack.push(c);
            }
            else{
                switch(c){
                    case ')': 
                        if (stack.empty() || stack.pop() != '('){
                            return false;
                        }
                        else{
                            continue;
                        }
                    case ']': 
                        if (stack.empty() || stack.pop() != '['){
                            return false;
                        }
                        else{
                            continue;
                        }
                    case '}': 
                        if ( stack.empty() || stack.pop() != '{'){
                            return false;
                        }
                        else{
                            continue;
                        }
                }
            }
            
        }
        if (!(stack.empty())){
            return false;
        }        
        return true;
        
        
    }
}