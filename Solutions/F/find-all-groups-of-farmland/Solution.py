# https://leetcode.com/problems/find-all-groups-of-farmland/

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        ret = []
        for i in range(m):
            for j in range(n):
                if not land[i][j]:
                    continue
                for ii in range(i, m):
                    if not land[ii][j]:
                        break
                    for jj in range(j, n):
                        if land[ii][jj]:
                            land[ii][jj] = 0
                            cur = [i, j, ii, jj]
                        else:
                            break
                ret.append(cur)
        return ret
