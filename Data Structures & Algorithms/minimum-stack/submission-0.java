class MinStack {

    private List<Integer> stack_values = new ArrayList<Integer>(); 

    public MinStack() {
        
    }
    
    public void push(int val) {
        this.stack_values.add(val);
    }
    
    public void pop() {
        this.stack_values.remove(this.stack_values.size() - 1);
    }
    
    public int top() {
        return this.stack_values.get(this.stack_values.size() - 1);
    }
    
    public int getMin() {
        return Collections.min(this.stack_values);
    }
}
