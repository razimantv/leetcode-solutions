# https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

class Solution:
    def pathExistenceQueries(
        self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]
    ) -> list[bool]:
        nums_ordered = sorted([(x, i) for i, x in enumerate(nums)])
        order = {u: i for i, (x, u) in enumerate(nums_ordered)}
        
        skip, r = [[]], 0
        for l in range(n):
            while r < n and nums_ordered[r][0] - nums_ordered[l][0] <= maxDiff:
                r += 1
            skip[0].append(r - 1)

        while True:
            changed, cur = False, []
            for l in range(n):
                cur.append(skip[-1][skip[-1][l]])
                if cur[l] != skip[-1][l]:
                    changed = True
            
            if changed:
                skip.append(cur)
            else:
                break
        
        def work(u, v):
            u, v = sorted([order[u], order[v]])
            return skip[-1][u] >= v
        
        return [work(u, v) for u, v in queries]
