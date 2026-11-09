# https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/


class Solution:
    def busiestServers(
        self, k: int, arrival: list[int], load: list[int]
    ) -> list[int]:
        free = SortedList(range(k))
        events = SortedList((x, i) for i, x in enumerate(arrival))
        cnt = defaultdict(int)

        while events:
            t, i = events.pop(0)
            if i < 0:
                free.add(-1 - i)
                continue

            t += load[i]
            if not free:
                continue

            i %= k
            j = free[0] if free[-1] < i else free[free.bisect_left(i)]
            free.remove(j)
            cnt[j] += 1
            events.add((t, -1 - j))

        m = max(cnt.values())
        return [k for k, v in cnt.items() if v == m]
