# https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {x: i + 1 for i, x in enumerate(sorted(list(set(arr))))}
        return [rank[x] for x in arr]
