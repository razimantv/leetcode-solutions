# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        fw, bw = {}, {}
        tot, ret = 0, []
        for x, c in queries:
            if x in fw:
                pc = fw[x]
                bw[pc].pop(x)
                if not bw[pc]:
                    tot -= 1
            fw[x] = c
            if c not in bw:
                bw[c] = {}
            if not bw[c]:
                tot += 1
            bw[c][x] = 1
            ret.append(tot)
        return ret
