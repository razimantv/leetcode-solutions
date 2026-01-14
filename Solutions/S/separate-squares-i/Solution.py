# https://leetcode.com/problems/separate-squares-i/

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        start, end, A = inf, -inf, 0
        for x, y, l in squares:
            start, end, A = min(start, y), max(end, y + l), A + l * l
        for i in range(50):
            mid, cur = (start + end) / 2, 0
            for x, y, l in squares:
                if mid > y + l:
                    cur += l * l
                elif mid > y:
                    cur += l * (mid - y)
            if cur >= A / 2:
                end = mid
            else:
                start = mid
        return end
