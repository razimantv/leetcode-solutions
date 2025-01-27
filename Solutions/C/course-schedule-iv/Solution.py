# https://leetcode.com/problems/course-schedule-iv/

class Solution:
    def checkIfPrerequisite(
        self, n: int, prerequisites: list[list[int]], queries: list[list[int]]
    ) -> list[bool]:
        adj = [set() for _ in range(n)]
        for u, v in prerequisites:
            adj[u].add(v)

        @cache
        def query(u, v):
            return (v in adj[u]) or any(query(w, v) for w in adj[u])

        return [query(u, v) for u, v in queries]
