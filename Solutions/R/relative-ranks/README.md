# Relative ranks

[Problem link](https://leetcode.com/problems/relative-ranks/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/relative-ranks/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rankscores = sorted([(-x, i) for i, x in enumerate(score)])
        for r, (x, i) in enumerate(rankscores):
            score[i] = str(r + 1) if r > 2 else [
                "Gold", "Silver", "Bronze"
            ][r] + " Medal"
        return score
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Remembering index](/Collections/sorting.md#remembering-index)
* [Permutation](/Collections/permutation.md#permutation) > [Inverse](/Collections/permutation.md#inverse)
