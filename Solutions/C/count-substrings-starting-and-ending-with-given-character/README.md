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

* [Hashmap](/README.md#Hashmap) > [Counter](/README.md#Hashmap-Counter)
* [Mathematics](/README.md#Mathematics) > [Combinatorics](/README.md#Mathematics-Combinatorics)
* [Mathematics](/README.md#Mathematics) > [Closed form expressions](/README.md#Mathematics-Closed_form_expressions)
