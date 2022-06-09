## 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/
## 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0 or ( x % 10 == 0 and x != 0 )):
            return False
        i = 0
        while (x>i):
            i= i*10 + x % 10
            x = int(x/10)
        return x==i or x==int(i/10)
        
