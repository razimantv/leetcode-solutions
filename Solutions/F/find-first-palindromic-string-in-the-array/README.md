# Find first palindromic string in the array

[Problem link](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return next((word for word in words if word == word[::-1]), "")
```
## Tags

* [Palindrome](/Collections/palindrome.md#palindrome)
* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
