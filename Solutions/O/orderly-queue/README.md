# Orderly queue

[Problem link](https://leetcode.com/problems/orderly-queue)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/orderly-queue

class Solution {
 public:
  string orderlyQueue(string s, int k) {
    if (k > 1) {
      sort(s.begin(), s.end());
      return s;
    }

    int N = s.size();
    string best = s;
    s += s;

    for (int i = 1; i < N; ++i) best = min(best, s.substr(i, N));
    return best;
  }
};
```
## Tags

* [Permutation](/Collections/permutation.md#permutation) > [Swaps](/Collections/permutation.md#swaps)
