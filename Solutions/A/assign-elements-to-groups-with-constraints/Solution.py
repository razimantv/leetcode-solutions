# https://leetcode.com/problems/assign-elements-to-groups-with-constraints/

class Solution:
    def assignElements(
        self, groups: list[int], elements: list[int]
    ) -> list[int]:
        n, pos, gmax = len(groups), defaultdict(list), max(groups)
        for i, x in enumerate(groups):
            pos[x].append(i)

        epos, ret = set(), [-1] * n
        for i, x in enumerate(elements):
            if x in epos:
                continue
            for j in range(x, gmax + 1, x):
                for k in pos[j]:
                    ret[k] = i
                pos[j] = []
            epos.add(x)
        return ret
# https://leetcode.com/problems/assign-elements-to-groups-with-constraints/
