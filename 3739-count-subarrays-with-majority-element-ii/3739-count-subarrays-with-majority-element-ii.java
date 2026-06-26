import java.util.*;

class Solution {

    class FenwickTree {
        int[] bit;

        FenwickTree(int n) {
            bit = new int[n + 2];
        }

        void update(int idx, int val) {
            while (idx < bit.length) {
                bit[idx] += val;
                idx += idx & -idx;
            }
        }

        int query(int idx) {
            int sum = 0;
            while (idx > 0) {
                sum += bit[idx];
                idx -= idx & -idx;
            }
            return sum;
        }
    }

    public long countMajoritySubarrays(int[] nums, int target) {
        int n = nums.length;

        // Prefix sums after converting target -> +1, others -> -1
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + (nums[i] == target ? 1 : -1);
        }

        // Coordinate Compression
        int[] sorted = prefix.clone();
        Arrays.sort(sorted);

        HashMap<Integer, Integer> rank = new HashMap<>();
        int id = 1;
        for (int x : sorted) {
            if (!rank.containsKey(x)) {
                rank.put(x, id++);
            }
        }

        FenwickTree bit = new FenwickTree(id);

        long ans = 0;

        for (int p : prefix) {
            int r = rank.get(p);

            // Number of previous prefix sums < current prefix
            ans += bit.query(r - 1);

            // Insert current prefix
            bit.update(r, 1);
        }

        return ans;
    }
}