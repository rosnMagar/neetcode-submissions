class Solution {
    public boolean isValid(String s) {
        // this is an easy implementation of stack
        // push when we get a left side bracket, pop if we
        // get right side bracket and the top element in the stack
        // matches(opposite bracket) top element of the stack
        if(s.length() == 0 || s.length() == 1) return false;

        Stack<Character> stack = new Stack<>();

        for(int i = 0; i < s.length(); i++){
            Character c = s.charAt(i);
            if(stack.size() != 0){
                Character top = stack.peek();
                if(top == '{' && c == '}') { stack.pop(); continue; };
                if(top == '[' && c == ']') { stack.pop(); continue; };
                if(top == '(' && c == ')') { stack.pop(); continue; };
            }
            stack.push(c);
        }

        return stack.size() == 0;

    }
}
