public class Solution {
    public int[] sortArray(int[] nums) {
        mergeSort(nums, 0, nums.length - 1);
        return nums;
    }

    private void merge(int[] arr, int L, int M, int R) {
        int leftLen = M - L + 1;
        int rightLen = R - M;

        int[] left = new int[leftLen];
        int[] right = new int[rightLen];

        for (int i = 0; i < leftLen; i++) {
            left[i] = arr[L + i];
        }
        for (int i = 0; i < rightLen; i++) {
            right[i] = arr[M + 1 + i];
        }

        int i = 0, j = 0, k = L;

        while (i < leftLen && j < rightLen) {
            if (left[i] <= right[j]) {
                arr[k] = left[i];
                i++;
            } else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        while (i < leftLen) {
            arr[k] = left[i];
            i++;
            k++;
        }
        while (j < rightLen) {
            arr[k] = right[j];
            j++;
            k++;
        }
    }

    private void mergeSort(int[] arr, int l, int r) {
        if (l < r) {
            int m = l + (r - l) / 2;

            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);

            merge(arr, l, m, r);
        }
    }

   
}
