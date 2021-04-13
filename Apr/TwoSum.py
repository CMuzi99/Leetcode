#I found it interesting and easier to solve problems in python. 
#The solution of same problem solved in java has been uploaded. It;s easier to understand in Java.
#in python I think the key is to understand the dictionary.
#In this problem the key is remaining, value is the order number.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i  #tough to understand what this means.
        return []
