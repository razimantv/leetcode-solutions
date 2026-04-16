# https://leetcode.com/problems/closest-equal-element-queries/

class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        n, pos = len(nums), defaultdict(list)
        for i, x in enumerate(nums):
            pos[x]. append(i)

        for i, q in enumerate(queries):
            v = pos[nums[q]]
            if len(v) == 1:
                queries[i] = -1
                continue
            idx = bisect_left(v, q)
            queries[i] = min(
                q - (v[idx - 1] if idx else (v[-1] - n)),
                (v[idx + 1] if idx != len(v) - 1 else (v[0] + n)) - q
            )

        return queries
