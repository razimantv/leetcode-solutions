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

* [Prefix](/README.md#Prefix) > [Extremum](/README.md#Prefix-Extremum)
* [Permutation](/README.md#Permutation) > [Inversions](/README.md#Permutation-Inversions)
