# Image overlap

[Problem link](https://leetcode.com/problems/image-overlap)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/image-overlap

class Solution {
 public:
  int largestOverlap(vector<vector<int>>& A, vector<vector<int>>& B) {
    int best = 0, N = A.size();
    for (int sx = 1 - N; sx < N; ++sx) {
      for (int sy = 1 - N; sy < N; ++sy) {
        int cur = 0;
        for (int i = max(0, sx); i <= min(0, sx) + N - 1; ++i) {
          for (int j = max(0, sy); j <= min(0, sy) + N - 1; ++j) {
            cur += A[i][j] * B[i - sx][j - sy];
          }
        }
        best = max(best, cur);
      }
    }
    return best;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
* [Matrix](/Collections/matrix.md#matrix) > [Geometric transformation](/Collections/matrix.md#geometric-transformation)
