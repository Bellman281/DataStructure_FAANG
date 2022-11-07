
'''
Q438
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]


'''
from unittest import result


def findAnagrams(s:str, p:str):
    result = []
    if len(p) > len(s): 
        return result
    
    pmap = {}
    stringmap = {}

    for i in range(len(p)):
        ##hashmap for P
        pmap[p[i]] = 1 + pmap.get(p[i],0)
        ## initial hashmap for string S
        stringmap[s[i]] = 1 + stringmap.get(s[i],0)

    result = [0] if pmap == stringmap else []

    left = 0
  
    for right in range(len(p),len(s)):
        stringmap[s[right]] = 1 + stringmap.get(s[right],0)
        stringmap[s[left]] -= 1
        
        if stringmap[s[left]] == 0:
            stringmap.pop(s[left])
        left += 1
        if stringmap == pmap :
            result.append(left)
    return result


print(findAnagrams(s = "cbaebabacd", p = "abc"))