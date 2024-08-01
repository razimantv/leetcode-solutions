# Minimum number of operations to reinitialize a permutation

[Problem link](https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation

class Solution {
 public:
  int reinitializePermutation(int n) {
    vector<int> perm(n);
    for (int i = 0; i < n; ++i) {
      if (i % 2)
        perm[i] = n / 2 + (i - 1) / 2;
      else
        perm[i] = i / 2;
    }

    vector<char> seen(n);
    int ret = 1;
    for (int i = 0; i < n; ++i) {
      if (seen[i]) continue;
      int cur = 0;
      for (int j = i; !seen[j]; j = perm[j]) seen[j] = 1, ++cur;
      ret = (ret / __gcd(ret, cur) * cur);
    }
    return ret;
  }
};
```
## Tags

* [Permutation](/Collections/permutation.md#permutation) > [Cycle](/Collections/permutation.md#cycle)
