
class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        // Use sets to store unique elements of nums1 and nums2
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        List<List<Integer>> arr = new ArrayList<>();
        List<Integer> first = new ArrayList<>();
        List<Integer> second = new ArrayList<>();
        
        // Add elements of nums1 and nums2 to their respective sets
        for (int ele : nums1) {
            set1.add(ele);
        }
        for (int ele : nums2) {
            set2.add(ele);
        }

        // Find elements in nums2 that are not in nums1
        for (int ele : set2) {
            if (!set1.contains(ele)) {
                first.add(ele);
            }
        }

        // Find elements in nums1 that are not in nums2
        for (int ele : set1) {
            if (!set2.contains(ele)) {
                second.add(ele);
            }
        }

        arr.add(second);
        arr.add(first);
        return arr;
    }
}
