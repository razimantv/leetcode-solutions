# https://leetcode.com/problems/palindromic-path-queries-in-a-tree/


class Solution:
    def palindromePath(
        self, n: int, edges: list[list[int]], s: str, queries: list[str]
    ) -> list[bool]:
        ls = list(s)

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dfs_order, start, end, depth = [], [-1] * n, [-1] * n, [0] * n
        anc = [[-1] * n]

        def dfs(u, par):
            start[u] = len(dfs_order)
            anc[0][u] = par
            dfs_order.append(u)
            for v in adj[u]:
                if v == par:
                    continue
                depth[v] = depth[u] + 1
                dfs(v, u)
            end[u] = len(dfs_order)

        dfs(0, -1)

        while max(anc[-1]) > -1:
            anc.append(
                [
                    anc[-1][anc[-1][i]] if anc[-1][i] > -1 else -1
                    for i in range(n)
                ]
            )

        def lca(u, v):
            if depth[u] > depth[v]:
                u, v = v, u

            if depth[v] > depth[u]:
                d = depth[v] - depth[u]
                for i, par in enumerate(anc):
                    if d & (1 << i):
                        v = par[v]

            if u == v:
                return u

            for par in anc[::-1]:
                if par[u] != par[v]:
                    u, v = par[u], par[v]
            return anc[0][u]

        base = 1
        while n >= base:
            base <<= 1
        seg = [0] * (base << 1)

        for i, c in enumerate(s):
            mask = 1 << (ord(c) - ord("a"))
            seg[base + start[i]] ^= mask
            seg[base + end[i]] ^= mask
        for i in range(base - 1, 0, -1):
            seg[i] = seg[i << 1] ^ seg[(i << 1) | 1]

        def seg_update(u, x):
            u += base
            while u:
                seg[u] ^= x
                u >>= 1

        def seg_query(u):
            u += base
            ret = seg[u]
            while u:
                if u & 1:
                    ret ^= seg[u ^ 1]
                u >>= 1
            return ret

        def update(u, c):
            mask = (1 << (ord(c) - ord("a"))) ^ (1 << (ord(ls[u]) - ord("a")))
            ls[u] = c
            seg_update(start[u], mask)
            seg_update(end[u], mask)

        def query(u, v):
            w = lca(u, v)
            ret = (
                seg_query(start[u])
                ^ seg_query(start[v])
                ^ (1 << (ord(ls[w]) - ord("a")))
            )
            return ret.bit_count() <= 1

        ret = []
        for q in queries:
            t, a, b = q.split()
            if t == "query":
                ret.append(query(int(a), int(b)))
            else:
                update(int(a), b)
        return ret
