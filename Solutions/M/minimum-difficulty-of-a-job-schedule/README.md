# Minimum difficulty of a job schedule

[Problem link](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

class Solution {
 public:
  int minDifficulty(vector<int>& jobDifficulty, int d) {
    int n = jobDifficulty.size();
    if (n < d) return -1;
    vector<vector<int>> dp(d + 1, vector<int>(n + 1, 1 << 30));
    dp[0][0] = 0;
    for (int i = 1; i <= d; ++i) {
      for (int j = 0; j < n; ++j) {
        for (int k = j, cur = 0; k >= 0; --k) {
          cur = max(cur, jobDifficulty[k]);
          dp[i][j + 1] = min(dp[i][j + 1], dp[i - 1][k] + cur);
        }
      }
    }
    return dp.back().back();
  }
};
```
### Solution.py
```py
# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        n = len(jobs)
        if n < d:
            return -1

        dp = [0] * n
        for i in range(n):
            dp[i] = max(jobs[i], dp[i-1] if i else 0)

        inf = 1 << 30
        for k in range(1, d):
            newdp = [inf] * n
            mon = []
            for j in range(n):
                x = jobs[j]
                y = dp[j-1] if j else inf
                while mon:
                    dpi, vi, best = mon[-1]
                    if vi <= x:
                        y = min(y, dpi)
                        mon.pop()
                    else:
                        break
                best = mon[-1][2] if mon else inf
                best = min(best, x+y)
                mon.append((y, x, best))
                newdp[j] = best
            dp = newdp
        return dp[-1]
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
* [Stack](/Collections/stack.md#stack) > [Monotonic stack](/Collections/stack.md#monotonic-stack)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Monotonic stack/deque](/Collections/dynamic-programming.md#monotonic-stack-deque)
