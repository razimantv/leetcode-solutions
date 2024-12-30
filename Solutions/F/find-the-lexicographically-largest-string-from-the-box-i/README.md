# Find the lexicographically largest string from the box i

[Problem link](https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n, best = len(word), 0
        L = n - numFriends + 1
        for i in range(1, n):
            for j in range(min(L, n - i)):
                if word[i + j] > word[best + j]:
                    best = i
                    break
                elif word[i + j] < word[best + j]:
                    break
        return word[best:best + L]
```
## Tags

* [String](/Collections/string.md#string)
* [Greedy](/Collections/greedy.md#greedy)
