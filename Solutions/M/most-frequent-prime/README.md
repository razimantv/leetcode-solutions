# Most frequent prime

[Problem link](https://leetcode.com/problems/most-frequent-prime/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/most-frequent-prime/

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        def isprime(n):
            p = 2
            while p * p <= n:
                if n % p == 0:
                    return False
                p += 1
            return True

        ctr = defaultdict(int)
        m, n = len(mat), len(mat[0])
        dirs = [
            (dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]
            if dx ** 2 + dy ** 2
        ]
        for i in range(m):
            for j in range(n):
                for di, dj in dirs:
                    cur = mat[i][j]
                    ii, jj = i + di, j + dj
                    while 0 <= ii < m and 0 <= jj < n:
                        cur = cur * 10 + mat[ii][jj]
                        ii, jj = ii + di, jj + dj
                        ctr[cur] += 1

        best = (0, -1)
        for k, v in ctr. items():
            if isprime(k):
                best = max(best, (v, k))
        return best[1]
```
## Tags

* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
