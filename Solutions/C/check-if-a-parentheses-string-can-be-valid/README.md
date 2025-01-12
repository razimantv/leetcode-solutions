# Check if a parentheses string can be valid

[Problem link](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) & 1:
            return False
        open, unlocked = [], []
        for i, (c, lock) in enumerate(zip(s, locked)):
            if lock == '0':
                unlocked.append(i)
            elif c == '(':
                open.append(i)
            elif open or unlocked:
                (open if open else unlocked).pop()
            else:
                return False
        return len(unlocked) >= len(open) and all(
            i > j for i, j in zip(unlocked[::-1], open[::-1])
        )
```
## Tags

* [Stack](/Collections/stack.md#stack) > [Valid brackets](/Collections/stack.md#valid-brackets)
* [Greedy](/Collections/greedy.md#greedy)
