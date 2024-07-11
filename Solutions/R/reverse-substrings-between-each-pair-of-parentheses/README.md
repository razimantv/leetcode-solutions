# Reverse substrings between each pair of parentheses

[Problem link](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        def work(s):
            if not s:
                return ""
            if s[0] not in '()':
                return s[0] + work(s[1:])
            pref = 0
            for i, c in enumerate(s):
                pref += 1 if c == '(' else -1 if c == ')' else 0
                if not pref:
                    return work(s[i-1:0:-1]) + work(s[i+1:])
        return work(s)
```
## Tags

* [Prefix](/README.md#Prefix) > [Sum](/README.md#Prefix-Sum) > [Valid brackets](/README.md#Prefix-Sum-Valid_brackets)
* [String](/README.md#String) > [Parsing](/README.md#String-Parsing) > [Recursive](/README.md#String-Parsing-Recursive)
