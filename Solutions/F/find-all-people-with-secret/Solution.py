# https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        knows, par = [0] * n, list(range(n))
        knows[0], knows[firstPerson] = 1, 1

        def parent(u):
            if par[u] != u:
                par[u] = parent(par[u])
            return par[u]

        l, m, meetings = 0, len(meetings), sorted(meetings, key=lambda x: x[2])
        while l < m:
            r, curknows, time = l, 0, meetings[l][2]
            while r < m:
                u, v, t = meetings[r]
                if t > time:
                    break
                pu, pv = parent(u), parent(v)
                if knows[pv]:
                    pu, pv = pv, pu
                par[pv] = pu
                r += 1

            for i in range(l, r):
                for u in meetings[i][:2]:
                    if knows[parent(u)]:
                        knows[u] = 1
                    else:
                        par[u] = u
            l = r

        return [i for i, x in enumerate(knows) if x]
