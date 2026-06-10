class Solution {
    public boolean isAnagram(String s, String t) {
        // ['r','a','c','e','c','a','r']
        // get ascii
        // add
        // do the same for possible anagram
        // if sum is same then is anagram
        // some edge cases with this method ja == fe
        
        // soln 2
        // use a hashmap

        if(s.length() != t.length()) return false;

        Map<Character, Integer> h1 = generateHash(s);
        Map<Character, Integer> h2 = generateHash(t);

        for(Map.Entry<Character, Integer> e : h1.entrySet()){
            char key = e.getKey();
            if (h2.get(key) == e.getValue()){
                continue;
            }else{
                return false;
            }
        }
        return true;

    }
    private int sumHash(Map<Character, Integer> hash){
        int sum = 0;

        return sum;
    }
    private Map<Character, Integer> generateHash(String s){
        
        Map<Character, Integer> hashMapString = new HashMap<>();
        for(char c : s.toCharArray()){
            if(hashMapString.get(c) != null)
                hashMapString.put(c, hashMapString.get(c) + 1);
            else
                hashMapString.put(c, 1);
        }
        return hashMapString;
    }
}
