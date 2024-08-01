# Count substrings starting and ending with given character

[Problem link](https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/

class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        x = Counter(s)[c]
        return x * (x + 1) // 2
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Closed form expressions](/Collections/mathematics.md#closed-form-expressions)
