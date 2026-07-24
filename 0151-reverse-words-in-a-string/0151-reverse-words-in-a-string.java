class Solution {
    public String reverseWords(String s) {
      ArrayList<String> list = new ArrayList<>(Arrays.asList(s.trim().split("\\s+")));
      Collections.reverse(list);
      return String.join(" ", list);  
    }
}