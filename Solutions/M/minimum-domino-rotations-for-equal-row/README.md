# Minimum domino rotations for equal row

[Problem link](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-domino-rotations-for-equal-row

class Solution {
 public:
  int minDominoRotations(vector<int>& A, vector<int>& B) {
    int N = A.size();
    if (N < 2) return 0;

    int uu = 0, ud = 0, du = 0, dd = 0;
    for (int i = 0; i < N; ++i) {
      if (uu >= 0) {
        if (A[i] == A[0]) {
        } else if (B[i] == A[0])
          ++uu;
        else
          uu = -1;
      }
      if (ud >= 0) {
        if (B[i] == A[0]) {
        } else if (A[i] == A[0])
          ++ud;
        else
          ud = -1;
      }
      if (du >= 0) {
        if (A[i] == B[0]) {
        } else if (B[i] == B[0])
          ++du;
        else
          du = -1;
      }
      if (dd >= 0) {
        if (B[i] == B[0]) {
        } else if (A[i] == B[0])
          ++dd;
        else
          dd = -1;
      }
    }

    int best = N;
    if (uu != -1) best = min(best, uu);
    if (ud != -1) best = min(best, ud);
    if (du != -1) best = min(best, du);
    if (dd != -1) best = min(best, dd);
    return best == N ? -1 : best;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
