# https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

class Solution:
    def maxTaskAssign(
        self, tasks: list[int], workers: list[int], pills: int, strength: int
    ) -> int:
        tasks, workers = sorted(tasks), sorted(workers)

        def work(k):
            left, sl = pills, SortedList(workers[-k:])
            for task in tasks[k - 1::-1]:
                if sl[-1] >= task:
                    next = sl.bisect_left(task)
                elif left and sl[-1] + strength >= task:
                    next = sl.bisect_left(task - strength)
                    left -= 1
                else:
                    return False
                sl.pop(next)
            return True

        start, end = 0, min(len(tasks), len(workers)) + 1
        while end - start > 1:
            mid = (start + end) // 2
            if work(mid):
                start = mid
            else:
                end = mid
        return start
