# Maximum palindromes after operations

[Problem link](https://leetcode.com/problems/maximum-palindromes-after-operations/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-palindromes-after-operations/

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        cnts = sorted([len(word) // 2 for word in words])
        good = sum(val // 2 for val in Counter(''.join(words)).values())
        ret = 0
        for cnt in cnts:
            if cnt <= good:
                ret += 1
                good -= cnt
            else:
                break
        return ret
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Palindrome](/Collections/palindrome.md#palindrome)
