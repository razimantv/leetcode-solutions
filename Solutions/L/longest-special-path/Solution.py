# https://leetcode.com/problems/longest-special-path

class Solution:
    def longestSpecialPath(
        self, edges: list[list[int]], nums: list[int]
    ) -> list[int]:
        adj: list[list[tuple[int, int]]] = [[] for _ in nums]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        ret, stack, last = [0, -1], [], defaultdict(list)

        def dfs(u, par, dist, good):
            nonlocal ret
            x = nums[u]
            if last[x]:
                good = max(good, last[x][-1] + 1)

            last[x].append(len(stack))
            stack.append(dist)
            ret = max(ret, [dist - stack[good], good - len(stack)])

            for v, w in adj[u]:
                if v != par:
                    dfs(v, u, dist + w, good)

            stack.pop()
            last[x].pop()

        dfs(0, -1, 0, 0)
        return [ret[0], -ret[1]]
