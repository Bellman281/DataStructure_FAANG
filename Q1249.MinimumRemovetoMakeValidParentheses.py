'''
1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
 so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"

'''

def minRemoveToMakeValid(s: str) ->str:
        result = list(s)
        stack = []
        for i,char in enumerate(result):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    result[i]= ''
        for j in stack:
            result[j] = ""
        return ''.join(result)


print(minRemoveToMakeValid( s = "lee(t(c)o)de)" ))