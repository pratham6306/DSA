class Solution {
    public int countMajoritySubarrays(int[] nums, int target) {
        int count = 0;
        for(int i = 0; i < nums.length; i++){
            int c = 0;
            for(int j = i; j < nums.length; j++){
                if(nums[j] == target) c++;
                if(2 * c > j - i + 1) count++;

            }
        }
        return count;
    }
}