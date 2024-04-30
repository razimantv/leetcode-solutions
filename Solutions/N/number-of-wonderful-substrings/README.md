# Number of wonderful substrings

[Problem link](https://leetcode.com/problems/number-of-wonderful-substrings/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt, pref, ret = defaultdict(int), 0, 0
        for c in word:
            cnt[pref] += 1
            pref ^= (1 << (ord(c) - ord('a')))
            ret += cnt[pref] + sum(cnt[pref ^ (1 << i)] for i in range(10))
        return ret
```
## Tags

* [Palindrome](/README.md#Palindrome)
* [Bitwise operation](/README.md#Bitwise_operation) > [Self-inverse property of xor](/README.md#Bitwise_operation-Self_inverse_property_of_xor)
* [Hashmap](/README.md#Hashmap)
* [Prefix](/README.md#Prefix) > [Bitwise operation](/README.md#Prefix-Bitwise_operation)
