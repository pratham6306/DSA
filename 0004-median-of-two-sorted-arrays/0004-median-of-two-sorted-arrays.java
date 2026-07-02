class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] arr = new int[nums1.length + nums2.length];
        int a = 0, b = 0;

        for (int i = 0; i < arr.length; i++) {
            if (a < nums1.length && (b >= nums2.length || nums1[a] < nums2[b])) {
                arr[i] = nums1[a];
                a++;
            } else {
                arr[i] = nums2[b];
                b++;
            }
        }

        int n = arr.length;
        if (n % 2 == 1) {
            return arr[n / 2];
        } else {
            return (arr[n / 2 - 1] + arr[n / 2]) / 2.0;
        }
    }
}
