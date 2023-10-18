#Q7:Reverse_Integer leetcode
#Medium
## Given a signed 32-bit integer x, return x with its digits reversed. 
## If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str( abs(x))[::-1]) 
        if x < 0:
            rev = -rev
        int_max = 2**31 - 1
        int_min = -2**31
        return rev if int_min <= rev <= int_max else 0  
