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

* [Palindrome](/Collections/palindrome.md#palindrome)
* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Self-inverse property of xor](/Collections/bitwise-operation.md#self-inverse-property-of-xor)
* [Hashmap](/Collections/hashmap.md#hashmap)
* [Prefix](/Collections/prefix.md#prefix) > [Bitwise operation](/Collections/prefix.md#bitwise-operation)
