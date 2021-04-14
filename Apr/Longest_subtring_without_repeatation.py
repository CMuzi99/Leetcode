#brute force always time out
"""class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start,end):
            chars =[0]*128
            for i in range(start, end+1):
                 c = s[i]
                 chars[ord(c)]+=1   #the numer of the character that string has.
                 if chars[ord(c)]>1: 
                        return False
            return True
        
        n=len(s)
        res=0
        for i in range(n):
            for j in range(i,n):
                if check(i,j):
                    res=max(res,j-i+1)
        return res
    """
#sliding windowclass Solution:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars=[0]*128
        left=right=0
        length=len(s)
        res=0
        while right<length:
            r=s[right]  #刚开始移动右窗？然后把char里面对应的variable值+1；
            chars[ord(r)]+=1
            while chars[ord(r)]>1:  #如果大于1，说明这个字母已经出现过，开始出现重复
                l=s[left]   #左边的窗户右移1
                chars[ord(l)]-=1  #-1因为左窗右移1
                left+=1
            res=max(res,right-left+1)
            right+=1
        return res
     
    
    
                
        
    
                
        
