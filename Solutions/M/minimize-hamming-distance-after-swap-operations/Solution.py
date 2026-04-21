# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

class Solution:
    def minimumHammingDistance(
        self, source: list[int], target: list[int], swaps: list[list[int]]
    ) -> int:
        n = len(source)
        par, inv, ret = list(range(n)), defaultdict(list), 0

        def parent(u):
            if u == par[u]:
                return u
            par[u] = parent(par[u])
            return par[u]

        for u, v in swaps:
            par[parent(u)] = parent(v)
        for u in range(n):
            inv[parent(u)].append(u)
        for group in inv.values():
            ctr = Counter(source[u] for u in group)
            for u in group:
                if ctr[x := target[u]]:
                    ctr[x] -= 1
                else:
                    ret += 1
        return ret
