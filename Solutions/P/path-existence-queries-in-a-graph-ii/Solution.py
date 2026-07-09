# https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

class Solution:
    def pathExistenceQueries(
        self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]
    ) -> list[int]:
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
        jmax = 1 << (len(skip) - 1)
        
        def work(u, v):
            if u == v:
                return 0
            u, v = sorted([order[u], order[v]])
            if skip[-1][u] < v:
                return -1
            
            j, ret = jmax, 1
            for i in range(len(skip) - 1, -1, -1):
                if skip[i][u] < v:
                    u, ret = skip[i][u], ret + j
                j >>= 1
            return ret
        
        return [work(u, v) for u, v in queries]
