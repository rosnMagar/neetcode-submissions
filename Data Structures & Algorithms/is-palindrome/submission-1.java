class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        s = s.replaceAll("[^a-z0-9]", "");

        Integer eIndex = s.length() - 1;
        
        for(Integer bIndex = 0; bIndex < s.length() / 2; bIndex++){
            if(s.charAt(bIndex) != s.charAt(eIndex))
                return false;
            eIndex--;
        }

        return true;

    }
}
