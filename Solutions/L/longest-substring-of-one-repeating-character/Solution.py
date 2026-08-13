# https://leetcode.com/problems/longest-substring-of-one-repeating-character/

from sortedcontainers import SortedList


class Solution:
    def longestRepeating(
            self, s: str, queryCharacters: str, queryIndices: list[int]
    ) -> list[int]:
        def merge(sl, group):
            if sl[-1][1] == group[1]:
                sl[-1][2] += group[2]
            else:
                sl.add(group)

        groups = SortedList([[-1, '$', 1]])
        for i, c in enumerate(s):
            merge(groups, [i, c, 1])
        groups.add([len(s), 'zz', 1])
        group_sizes = SortedList([g[-1] for g in groups])

        ret = []
        for c, idx in zip(queryCharacters, queryIndices):
            g_idx = groups.bisect_right([idx + 1, 'a', 0])

            cur_groups = SortedList([pop := groups.pop(g_idx - 2)])
            group_sizes.pop(group_sizes.bisect_left(pop[-1]))

            pop = groups.pop(g_idx - 2)
            if pop[0] < idx:
                merge(cur_groups, [*pop[:2], idx - pop[0]])
            group_sizes.pop(group_sizes.bisect_left(pop[-1]))
            merge(cur_groups, [idx, c, 1])
            if pop[0] + pop[2] > idx + 1:
                merge(cur_groups, [idx + 1, pop[1], pop[0] + pop[2] - 1 - idx])

            merge(cur_groups, pop := groups.pop(g_idx - 2))
            group_sizes.pop(group_sizes.bisect_left(pop[-1]))

            groups.update(cur_groups)
            group_sizes.update([g[-1] for g in cur_groups])
            ret.append(group_sizes[-1])
        return ret
