'''
49. Group Anagrams

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


'''
from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List [List[str]]:
    result = defaultdict(list)

    for i in range(len(strs)):
        charCount = {k:0 for k in range(97,123)  } #a...z
        for c in strs[i]:
            if ord(c) in charCount.keys():
                charCount[ord(c)] += 1
        t = tuple([(chr(k),v) for (k,v) in charCount.items() if charCount[k] > 0])
        result[t].append(strs[i]) 
        
        
    return result.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
