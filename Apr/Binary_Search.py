#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 如果目标值存在返回下标，否则返回 -1
# @param nums int整型一维数组 
# @param target int整型 
# @return int整型
#
class Solution:
    def search(self , nums , target ):
        # write code here
        j=-1
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if target>nums[mid]: left=left+1
            elif target<nums[mid]: right= right-1
            elif target==nums[mid]: 
                while mid!=0 and nums[mid-1]==nums[mid]: #make sure it's the first time that target appears.
                    mid=mid-1
                    j=mid
                j=mid
                break
        return j
                
            
