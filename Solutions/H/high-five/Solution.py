# https://leetcode.com/problems/high-five/

class Solution:
    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        best = defaultdict(list)
        for id, x in items:
            best[id].append(x)
        return sorted(
            [[id, sum(sorted(v)[-5:]) // 5] for id, v in best.items()]
        )
