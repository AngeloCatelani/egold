class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i = 0; i< arr.length; i++){
            if(map.containsKey(arr[i])){
                map.put(arr[i],map.getOrDefault(arr[i], 0) + 1);
            }
            else{
                map.put(arr[i],1);
            }
        }
        //check values same means return true; else false
    //    Set<Integer> set = new HashSet<>(map.values());
    Set<Integer> set = new HashSet<>();
      for (int value : map.values()) {
            if(!set.contains(value)){   
                set.add(value);

            }
            else{
                return false;
            }
        }
        return true;

    }
}