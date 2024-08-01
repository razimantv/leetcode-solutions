# Global and local inversions

[Problem link](https://leetcode.com/problems/global-and-local-inversions)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/global-and-local-inversions

class Solution {
 public:
  bool isIdealPermutation(vector<int>& A) {
    int lim = 0;
    for (int i = 0, N = A.size(); i < N; ++i) {
      if (A[i] < lim) return false;
      if (i) lim = max(lim, A[i - 1]);
    }
    return true;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Extremum](/Collections/prefix.md#extremum)
* [Permutation](/Collections/permutation.md#permutation) > [Inversions](/Collections/permutation.md#inversions)
