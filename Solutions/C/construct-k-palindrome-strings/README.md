# Construct k palindrome strings

[Problem link](https://leetcode.com/problems/construct-k-palindrome-strings/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/construct-k-palindrome-strings/

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return len(s) >= k and sum(x & 1 for x in Counter(s).values()) <= k
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Palindrome](/Collections/palindrome.md#palindrome)
