class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i=0,j=1;
        for(i=0;i<nums.length-1;i++){
            for(j=1;j<nums.length;j++){
                if (nums[i]==target-nums[j]){
                    return new int[]{i,j};
                }
            }
        }
        throw new IllegalArgumentException("no two sum solution");    //without this line error: no return
    }
}
