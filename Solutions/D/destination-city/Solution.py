# https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        pair = {u: v for u, v in paths}
        u = paths[0][0]
        while u in pair:
            u = pair[u]
        return u
