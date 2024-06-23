# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        def get(il, ir, jl, jr):
            ni, nj = ir - il, jr - jl
            ileft, iright = [[] for _ in range(ni)], [[] for _ in range(ni)]
            jleft, jright = [[] for _ in range(nj)], [[] for _ in range(nj)]

            for i in range(il, ir):
                iar = i - il
                i1, i2, j1, j2, x = [
                    301, -1, 301, -1, 1 << 20
                ] if not iar else ileft[iar - 1]
                for j in range(jl, jr):
                    if grid[i][j]:
                        i1, j1 = min(i1, i), min(j1, j)
                        i2, j2 = max(i2, i), max(j2, j)
                ileft[iar] = [i1, i2, j1, j2, (i2 - i1 + 1) * (j2 - j1 + 1)]

            for i in range(ir - 1, il - 1, -1):
                iar = i - il
                i1, i2, j1, j2, x = [
                    301, -1, 301, -1, 1 << 20
                ] if i == ir - 1 else iright[iar + 1]
                for j in range(jl, jr):
                    if grid[i][j]:
                        i1, j1 = min(i1, i), min(j1, j)
                        i2, j2 = max(i2, i), max(j2, j)
                iright[iar] = [i1, i2, j1, j2, (i2 - i1 + 1) * (j2 - j1 + 1)]

            for j in range(jl, jr):
                jar = j - jl
                i1, i2, j1, j2, x = [
                    301, -1, 301, -1, 1 << 20
                ] if not jar else jleft[jar - 1]
                for i in range(il, ir):
                    if grid[i][j]:
                        i1, j1 = min(i1, i), min(j1, j)
                        i2, j2 = max(i2, i), max(j2, j)
                jleft[jar] = [i1, i2, j1, j2, (i2 - i1 + 1) * (j2 - j1 + 1)]

            for j in range(jr - 1, jl - 1, -1):
                jar = j - jl
                i1, i2, j1, j2, x = [
                    301, -1, 301, -1, 1 << 20
                ] if j == jr - 1 else jright[jar + 1]
                for i in range(il, ir):
                    if grid[i][j]:
                        i1, j1 = min(i1, i), min(j1, j)
                        i2, j2 = max(i2, i), max(j2, j)
                jright[jar] = [i1, i2, j1, j2, (i2 - i1 + 1) * (j2 - j1 + 1)]

            return iright[0][-1], min(
                min((l[-1] + r[-1]
                    for l, r in zip(ileft[:-1], iright[1:])), default=1 << 20),
                min((l[-1] + r[-1]
                    for l, r in zip(jleft[:-1], jright[1:])), default=1 << 20)
            )

        m, n = len(grid), len(grid[0])
        ret = m * n
        for i in range(1, m):
            l1, l2 = get(0, i, 0, n)
            r1, r2 = get(i, m, 0, n)
            ret = min(ret, l1 + r2, l2 + r1)
        for i in range(1, n):
            l1, l2 = get(0, m, 0, i)
            r1, r2 = get(0, m, i, n)
            ret = min(ret, l1 + r2, l2 + r1)
        return ret
