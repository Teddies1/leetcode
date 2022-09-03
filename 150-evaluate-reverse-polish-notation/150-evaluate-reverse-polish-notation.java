class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> s = new Stack<Integer>();
        
        for (String token: tokens){
            
            if (token.equals("+") || token.equals("/") || token.equals("-") || token.equals("*")){
                Integer one = Integer.valueOf(s.pop());
                Integer two = Integer.valueOf(s.pop());
                System.out.printf("%d %d\n", one, two);
                switch(token){
                    case "+": 
                        s.push(one + two);
                        break;
                    case "/": 
                        
                     
                            s.push(two / one);
                        
                        break;
                    case "*": 
                        s.push(one * two);
                        break;
                    case "-": 
                        s.push(two - one);
                        break;
                }
            }
            else{
                s.push(Integer.valueOf(token));
            }
        }
        return s.pop();
    }
}