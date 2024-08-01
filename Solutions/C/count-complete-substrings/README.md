# Count complete substrings

[Problem link](https://leetcode.com/problems/count-complete-substrings/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-complete-substrings/

class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        cur = [0] * 26
        pref = [cur.copy()]
        n, lastbad, ret = len(word), -1, 0
        for i in range(n):
            if i > 0 and abs(ord(word[i]) - ord(word[i-1])) > 2:
                lastbad = i - 1
            cur[ord(word[i]) - ord('a')] += 1
            pref.append(cur.copy())
            for x in range(1, 27):
                ip = i - x * k
                if ip < lastbad:
                    break

                baddelta = 0
                for c1, c2 in zip(cur, pref[ip+1]):
                    if c1 - c2 != 0 and c1 - c2 != k:
                        baddelta = c1 - c2
                        break
                else:
                    ret += 1

                if baddelta > k:
                    break
        return ret
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
