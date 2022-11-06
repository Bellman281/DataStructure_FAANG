'''
Given two binary strings a and b, return their sum as a binary string.

Input: a = "11", b = "1"
Output: "100"

'''

from tokenize import String


class Solution :
    def addBinary(self,a: str ,b: str) -> str:
        sum_ = { (0,0) : (0,0),
                 (1,0) : (1,0), 
                 (0,1) : (1,0),
                 (1,1) : (0,1)
        }
        if len(b) > len(a):
            temp = a
            a = b
            b = temp
        a = a [::-1]
        b = b [::-1]
        print(list(zip(list(a),list(b))))
        return a + b


t = Solution()
print(t.addBinary(a = "19200", b = "100"))

