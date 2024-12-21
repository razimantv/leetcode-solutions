# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        sgn = [1, 1, -1, -1]

        def work(ar):
            psum, zeros = 0, 0
            for p, s in ar:
                if (psum := psum + s) == 0:
                    if (zeros := zeros + 1) == 3:
                        return True
            return False

        x, y = [
            sorted([
                (rectangle[j], sgn[j])
                for rectangle in rectangles for j in js
            ])
            for js in [[0, 2], [1, 3]]
        ]
        return work(x) or work(y)
