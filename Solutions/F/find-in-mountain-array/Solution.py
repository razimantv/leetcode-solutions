# https://leetcode.com/problems/find-in-mountain-array/

class Solution:
    def findInMountainArray(self, target: int, ar: 'MountainArray') -> int:
        N = ar.length()

        cache = {}
        def get(i: int):
            if i in cache:
                return cache[i]
            else:
                cache[i] = ar.get(i)
                return cache[i]

        # Find first index i such that a[i] < a[i-1]
        start, end = 1, N-1
        while end-start > 1:
            mid = (end+start)//2
            if get(mid) < get(mid-1):
                end = mid
            else:
                start = mid

        ranges = [[0, start, 1], [start, N-1, -1]]
        for start, end, dir in ranges:
            if get(start)*dir > target*dir:
                continue
            elif get(start) == target:
                return start

            while end-start > 1:
                mid = (start+end) // 2
                x = get(mid)
                if x == target:
                    return mid
                elif x*dir < target*dir:
                    start = mid
                else:
                    end = mid
            if get(end) == target:
                return end

        return -1
