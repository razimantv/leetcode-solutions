# Number of valid words for each puzzle

[Problem link](https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

class Solution:
    def findNumOfValidWords(
        self, words: list[str], puzzles: list[str]
    ) -> list[int]:
        def bit(c):
            return 1 << (ord(c) - ord('a'))

        def mask(word):
            return reduce(ior, (bit(c) for c in word))

        def allmasks(word):
            masks = [bit(word[0])]
            for c in map(bit, word[1:]):
                for i in range(len(masks)):
                    masks.append(masks[i] | c)
            return sum(cnt.get(m, 0) for m in masks)

        cnt = Counter(map(mask, words))
        return list(map(allmasks, puzzles))
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
