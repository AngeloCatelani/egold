// public class Solution {
//     public int[] sortArray(int[] nums) {
//         mergeSort(nums, 0, nums.length - 1);
//         return nums;
//     }

//     private void merge(int[] arr, int L, int M, int R) {
//         int leftLen = M - L + 1;
//         int rightLen = R - M;

//         int[] left = new int[leftLen];
//         int[] right = new int[rightLen];

//         for (int i = 0; i < leftLen; i++) {
//             left[i] = arr[L + i];
//         }
//         for (int i = 0; i < rightLen; i++) {
//             right[i] = arr[M + 1 + i];
//         }

//         int i = 0, j = 0, k = L;

//         while (i < leftLen && j < rightLen) {
//             if (left[i] <= right[j]) {
//                 arr[k] = left[i];
//                 i++;
//             } else {
//                 arr[k] = right[j];
//                 j++;
//             }
//             k++;
//         }

//         while (i < leftLen) {
//             arr[k] = left[i];
//             i++;
//             k++;
//         }
//         while (j < rightLen) {
//             arr[k] = right[j];
//             j++;
//             k++;
//         }
//     }

//     private void mergeSort(int[] arr, int l, int r) {
//         if (l < r) {
//             int m = l + (r - l) / 2;

//             mergeSort(arr, l, m);
//             mergeSort(arr, m + 1, r);

//             merge(arr, l, m, r);
//         }
//     }

   
// }
class Solution {
    //Using Merge Sort
    public int[] sortArray(int[] nums) {
        mergeSort(nums, 0, nums.length-1);
        return nums;
    }
    public void mergeSort(int []arr, int low, int high){
        if(low >= high) return;

        int mid = (low+high)/2;
        mergeSort(arr, low, mid);
        mergeSort(arr, mid+1, high);
        merge(arr, low, high, mid);
    }
    public void merge(int []arr, int low, int high, int mid){
        ArrayList<Integer> temp = new ArrayList<>();
        int left = low;
        int right = mid+1;

        while(left <= mid && right <= high){
            if(arr[left] <= arr[right]){
                temp.add(arr[left]);
                left++;
            }else{
                temp.add(arr[right]);
                right++;
            }
        }
        while(left <= mid){
            temp.add(arr[left]);
            left++;
        }
        while(right <= high){
            temp.add(arr[right]);
            right++;
        }
        for(int i=low; i<= high; i++){
            arr[i] = temp.get(i-low);
        }
    }
}
