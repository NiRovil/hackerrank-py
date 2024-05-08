
class MedianSortedArray {

    public static void main(String[] args) {
        
        int n1[] = {1,2};
        int n2[] = {3,4};

        System.out.println(findMedianSortedArrays(n1, n2));
    }

    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n1 = nums1.length;
        int n2 = nums2.length;
        int arr[] = new int[n1 + n2];

        int i = 0, j = 0, k = 0;

        while(i < n1 && j < n2){
            if (nums1[i] < nums2[j]){
                arr[k++] = nums1[i++];
            } else {
                arr[k++] = nums2[j++];
            }
        }
        
        while (i < n1) arr[k++] = nums1[i++];
        while (j < n2) arr[k++] = nums2[j++];

        int n3 = arr.length;
        double even = n3 % 2;

        if (even == 0){
            int middle = arr.length / 2;
            return (double) (arr[middle - 1] + arr[middle]) / 2;
        } else {
            int oMiddle = arr.length / 2;
            return arr[oMiddle];
        }

    }
}
