# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

class Solution:
    def minJumps(self, nums: list[int]) -> int:
        n, nmax = len(nums), max(nums) + 1
        primes, factors, invprime = [], [[] for _ in range(nmax)], {}
        for i in range(2, nmax):
            if not factors[i]:
                invprime[i] = len(primes)
                primes.append(i)
                for j in range(i, nmax, i):
                    factors[j].append(i)

        adj = [
            [x for x in (i - 1, i + 1) if 0 <= x < n] for i in range(n)
        ] + [[] for _ in primes]
        for i, x in enumerate(nums):
            if x in invprime:
                adj[i].append(n + invprime[x])
            for p in factors[x]:
                adj[n + invprime[p]].append(i)

        dist, cur, next = [0] + [inf] * (len(adj) - 1), [0], []
        while cur:
            while cur:
                u = cur.pop()
                for v in adj[u]:
                    dv = v < n
                    if dist[u] + dv < dist[v]:
                        dist[v] = dist[u] + dv
                        [cur, next][dv].append(v)
            cur, next = next, []

        return dist[n - 1]
