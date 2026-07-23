class Solution {
    public int uniqueXorTriplets(int[] nums) {
        int n = nums.length;
        if (n <= 2) return n;
        
        // 32 - leading zeros gives the exact bit length of the integer
        int bits = 32 - Integer.numberOfLeadingZeros(n);
        return 1 << bits;
    }
}