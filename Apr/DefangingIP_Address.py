class Solution:
    def defangIPaddr(self, address: str) -> str:
      return address.replace(".","[.]")
#my original method is so complicated:
#     #  result=[]
#        for i in address:
#            if i==".":
#                result.append("[.]")
#            else:
#                result.append(i)
#        res=''.join(result)
    
#       return res   """
                
