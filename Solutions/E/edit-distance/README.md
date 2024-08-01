# Edit distance

[Problem link](https://leetcode.com/problems/edit-distance)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/edit-distance

class Solution {
 public:
  int minDistance(string A, string B) {
    int M = A.size(), N = B.size();
    if (M * N == 0) return M + N;
    vector<vector<int>> DP(M + 1, vector<int>(N + 1, 0));
    for (int i = 0; i <= M; i++) {
      for (int j = 0; j <= N; j++) {
        DP[i][j] = max(i, j);
        if (i * j == 0) continue;
        if (A[i - 1] == B[j - 1])
          DP[i][j] = DP[i - 1][j - 1];
        else
          DP[i][j] =
              min(DP[i][j],
                  min(min(DP[i - 1][j], DP[i][j - 1]), DP[i - 1][j - 1]) + 1);
      }
    }
    return DP[M][N];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
