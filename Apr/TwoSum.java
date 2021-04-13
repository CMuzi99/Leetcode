class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i=0,j=1;
        for(i=0;i<nums.length-1;i++){
            for(j=i+1;j<nums.length;j++){   //If i use j=1, the nafter the first round of i, j begins from 1 again, so here is j=i+1
                if (nums[i]==target-nums[j]){
                    return new int[]{i,j};
                }
            }
        }
        throw new IllegalArgumentException("no two sum solution");    //without this line error: no return
    }
}
