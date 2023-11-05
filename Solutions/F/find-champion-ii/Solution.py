# https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        deg = defaultdict(int)
        for u, v in edges:
            deg[v] += 1
        good = [u for u in range(n) if not deg[u]]
        return -1 if len(good) != 1 else good[0]
