class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int fir=0;
        int sec=0;
        int i;
        int capacity = nums.length;
        for (i=0;i<capacity;i++){
             if (nums[i]==1) {
                 fir=Math.max(fir,++sec);
                 }
                 else{
                     sec=0;
                 }
        }     
        return fir;
    }
}
