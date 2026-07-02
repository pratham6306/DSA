import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) return 0;

        Map<Character, Integer> lastIndex = new HashMap<>();
        int maxLen = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (lastIndex.containsKey(c)) {
                // Move left to one past previous index of c, but never move left backward
                left = Math.max(left, lastIndex.get(c) + 1);
            }
            lastIndex.put(c, right);
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
