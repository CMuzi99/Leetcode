class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i=0,j=1;
        for(i=0;i<nums.length-1;i++){
            for(j=i+1;j<nums.length;j++){   //I don't know why here j=i+1; I use j=1 then it's wrong
                if (nums[i]==target-nums[j]){
                    return new int[]{i,j};
                }
            }
        }
        throw new IllegalArgumentException("no two sum solution");    //without this line error: no return
    }
}
