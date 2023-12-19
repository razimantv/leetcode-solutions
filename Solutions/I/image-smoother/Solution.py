# https://leetcode.com/problems/image-smoother/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ret = [[0] * n for _ in range(m)]
        for i in range(m):
            imin, imax = max(i-1, 0), min(i+1, m-1)
            for j in range(n):
                jmin, jmax = max(j-1, 0), min(j+1, n-1)
                ret[i][j] = sum([
                    img[x][y]
                    for x in range(imin, imax+1)
                    for y in range(jmin, jmax+1)
                ]) // ((imax - imin + 1) * (jmax - jmin + 1))
        return ret
