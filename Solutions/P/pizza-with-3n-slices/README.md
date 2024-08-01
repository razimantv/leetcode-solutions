# Pizza with 3n slices

[Problem link](https://leetcode.com/problems/pizza-with-3n-slices)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/pizza-with-3n-slices

class Solution {
 public:
  int maxSizeSlices(vector<int>& slices) {
    int N3 = slices.size(), N = N3 / 3;

    int ret;
    {
      int shift = -1;
      vector<vector<int>> DP(N3, vector<int>(N + 1, 0));
      DP[1][1] = slices[1 + shift];
      for (int i = 2; i < N3; ++i) {
        for (int j = 1; j <= N; ++j) {
          DP[i][j] = max(DP[i - 1][j], DP[i - 2][j - 1] + slices[i + shift]);
        }
      }
      ret = DP[N3 - 1][N];
    }
    {
      int shift = 0;
      vector<vector<int>> DP(N3, vector<int>(N + 1, 0));
      DP[1][1] = slices[1 + shift];
      for (int i = 2; i < N3; ++i) {
        for (int j = 1; j <= N; ++j) {
          DP[i][j] = max(DP[i - 1][j], DP[i - 2][j - 1] + slices[i + shift]);
        }
      }
      ret = max(ret, DP[N3 - 1][N]);
    }
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Cyclic array](/Collections/dynamic-programming.md#cyclic-array)
