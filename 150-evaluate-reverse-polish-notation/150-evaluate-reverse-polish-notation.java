class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> s = new Stack<Integer>();
        Integer one, two;
        for (String token: tokens){
            
                
                switch(token){
                    case "+": 
                        s.push(s.pop() + s.pop());
                        break;
                    case "/":      
                         one = Integer.valueOf(s.pop());
                         two = Integer.valueOf(s.pop());
                        s.push(two / one);
                        break;
                    case "*": 
                        s.push(s.pop() * s.pop());
                        break;
                    case "-": 
                         one = Integer.valueOf(s.pop());
                         two = Integer.valueOf(s.pop());
                        s.push(two - one);
                        break;
                    default:
                        s.push(Integer.valueOf(token));
                }
                
        
        }
        return s.pop();
    }
}