# https://leetcode.com/problems/k-th-smallest-prime-fraction/

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)

        def work(num, den):
            l = 0
            cnt, numb, denb = 0, 0, 1
            for r in range(n):
                while l < r and arr[l] * den <= arr[r] * num:
                    l += 1
                cnt += l
                if l and arr[l-1] * denb > arr[r] * numb:
                    numb, denb = arr[l-1], arr[r]
            return cnt, numb, denb

        start, den = 0, 1
        while True:
            start, den = start * 2, den * 2
            cnt, numb, denb = work(start + 1, den)
            if cnt == k:
                return [numb, denb]
            elif cnt < k:
                start += 1

        return [0, 0]
