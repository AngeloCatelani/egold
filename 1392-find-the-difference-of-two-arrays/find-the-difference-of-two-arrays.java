class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        List<List<Integer>> arr = new ArrayList<>();
        List<Integer> first = new ArrayList<>();
        List<Integer> second = new ArrayList<>();

        for(int e : nums1){
            set1.add(e);
        }
        for(int e : nums2){
            set2.add(e);
        }
        for(int e : set1){
            if(!set2.contains(e)){
                first.add(e);
            }
        }
        for(int e : set2){
            if(!set1.contains(e)){
                second.add(e);
            }
        }
        arr.add(first);
        arr.add(second);
        return arr;
    }
}