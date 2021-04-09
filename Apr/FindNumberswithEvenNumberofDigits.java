class Solution {
    public int findNumbers(int[] nums) {
        int number = 0;
        for(int i=0; i<nums.length;i++){
           String s = Integer.toString(nums[i]);  //Integer.toString(i) transfer the int i to string.
            if(s.length()%2==0){number++;}
        }
        return number;
    }
}
