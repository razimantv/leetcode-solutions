# Find the sequence of strings appeared on the screen

[Problem link](https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ret = [""]
        for c in target:
            ret += [
                ret[-1] + chr(ord('a') + x)
                for x in range(ord(c) - ord('a') + 1)
            ]
        return ret[1:]
```
## Tags

* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Elementwise processing using a vector](/Collections/brute-force-enumeration.md#elementwise-processing-using-a-vector)
