class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runSum=list()
        runningsum=[]
        for i in range(len(nums)):
            for j in range (i+1):   #when it's rang(i), the first value is always 0, because for 0 in range 0 , it's 0
                runSum.append(nums[j])
            runningsum.append(sum(runSum))
            runSum.clear()
        return runningsum
        
"""        result = []    #smarter way
        
        runningsum = 0
        
        for num in nums:
            runningsum +=num
            result.append(runningsum)
            
        return result"""
