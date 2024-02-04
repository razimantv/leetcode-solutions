# https://leetcode.com/problems/find-the-grid-of-region-average/

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        tot = [[0] * n for _ in range(m)]
        cnt = [[0] * n for _ in range(m)]

        def good(i, j):
            for ii in range(i, i+3):
                for jj in range(j, j+3):
                    if ii != i and abs(image[ii][jj] - image[ii-1][jj]) > threshold:
                        return False
                    if jj != j and abs(image[ii][jj] - image[ii][jj-1]) > threshold:
                        return False
            return True

        for i in range(m - 2):
            for j in range(n - 2):
                if not good(i, j):
                    continue
                cur = 0
                for ii in range(i, i + 3):
                    for jj in range(j, j + 3):
                        cur += image[ii][jj]

                mean = cur // 9
                for ii in range(i, i + 3):
                    for jj in range(j, j + 3):
                        tot[ii][jj] += mean
                        cnt[ii][jj] += 1

        for i in range(m):
            for j in range(n):
                if cnt[i][j]:
                    image[i][j] = tot[i][j] // cnt[i][j]

        return image
