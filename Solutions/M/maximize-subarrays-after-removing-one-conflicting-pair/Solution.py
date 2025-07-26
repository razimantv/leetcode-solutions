# https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

class Solution:
    def maxSubarrays(self, n: int, conflict: list[list[int]]) -> int:
        left = defaultdict(list)
        for i, pair in enumerate(conflict):
            left[max(pair)].append((min(pair), i))

        last2, tot, delta = [(0, -1)] * 2, 0, defaultdict(int)
        for i in range(1, n + 1):
            for x in left[i]:
                last2 = sorted(last2 + [x])[1:]
            (pos1, id1), (pos2, id2) = last2
            tot += i - pos2
            delta[id2] += pos2 - pos1
            # print(i, tot, delta)

        return tot + max(delta.values())
