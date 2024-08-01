# Maximal square

[Problem link](https://leetcode.com/problems/maximal-square)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximal-square

class Solution {
 public:
  int maximalSquare(vector<vector<char>>& matrix) {
    if (matrix.empty()) return 0;
    int M = matrix.size(), N = matrix[0].size();
    vector<vector<int>> ps(M + 1, vector<int>(N + 1, 0));

    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
        ps[i + 1][j + 1] =
            ps[i + 1][j] + ps[i][j + 1] - ps[i][j] + (matrix[i][j] == '1');
      }
    }

    int best = 0;
    for (int i = 1; i <= M; i++)
      for (int j = 1; j <= N; j++)
        for (int k = best; k <= min(i, j); k++) {
          if (ps[i][j] - ps[i - k][j] - ps[i][j - k] + ps[i - k][j - k] ==
              k * k)
            best = k;
          else
            break;
        }
    return best * best;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [2D](/Collections/prefix.md#2d)
