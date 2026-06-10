class Solution {
    public boolean hasDuplicate(int[] nums) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int num : nums){
            if(list.contains(num)){
                return true;
            }
            list.add(num);
        } 
        return false;
    }
}
