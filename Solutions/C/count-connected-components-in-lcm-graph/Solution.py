# https://leetcode.com/problems/count-connected-components-in-lcm-graph

class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        ret = len([x for x in nums if x > threshold])
        nums = sorted([x for x in nums if x <= threshold])
        if not nums:
            return ret
        lim = nums[-1] + 1
        par = [0] * lim
        for x in nums:
            par[x] = x

        def parent(u):
            if par[u] == u:
                return u
            par[u] = parent(par[u])
            return par[u]

        for g in range(1, lim):
            small = -1
            for x in range(g, lim, g):
                if not par[x]:
                    continue
                if small == -1:
                    small = x
                    ps = parent(x)
                if small * x > threshold * g:
                    break
                par[parent(x)] = ps
        return ret + len(set(parent(x) for x in nums))
