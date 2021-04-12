# -*- coding:utf-8 -*-

class Solution:
    def getLongestPalindrome(self, A, n):
        # write code here
        def func(A, left, right):
            while left >=0 and right < n and A[left]==A[right]:
                left -= 1
                right += 1
            return right-left-1
        res = 0
        for i in range(n-1):
            res = max(res, func(A, i, i), func(A, i, i+1))  #odd and even are different
        return res
       #there is another method to solve this problem, but the above one is easier to understand I think:
"""
# -*- coding:utf-8 -*-
#从头到尾扫描字符串，每增加一个新的字符，判断以这个字符结尾，且长度为maxLen+1或者maxLen+2的子串是否为回文，如果是，更新。
class Solution:
    def getLongestPalindrome(self, A, n):
        # write code here
        max_len = 0
        for i in range(n):
            oddNum = A[i-max_len-1:i+1]
            evenNum = A[i-max_len:i+1]
            if i-max_len-1>=0 and oddNum == oddNum[::-1]:
                max_len+=2
            elif i-max_len>=0 and evenNum == evenNum[::-1]:
                max_len+=1
        return max_len
        """
