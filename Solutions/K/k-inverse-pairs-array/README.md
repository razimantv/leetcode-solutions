# K inverse pairs array

[Problem link](https://leetcode.com/problems/k-inverse-pairs-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/k-inverse-pairs-array

class Solution {
 public:
  map<pair<int, int>, int> cache;
  const int MOD = 1'000'000'007;
  int kInversePairs(int n, int k) {
    if (k == 0)
      return 1;
    else if (n < 2)
      return 0;

    vector<int> dpsum(k + 2, 1);
    dpsum[0] = 0;

    for (int i = 2; i <= n; ++i) {
      for (int j = k + 1; j > 1; --j) {
        dpsum[j] += MOD - dpsum[j - min(j, i)];
        if (dpsum[j] >= MOD) dpsum[j] -= MOD;
      }
      for (int j = 2; j < k + 2; ++j) {
        dpsum[j] += dpsum[j - 1];
        if (dpsum[j] >= MOD) dpsum[j] -= MOD;
      }
    }

    return (dpsum[k + 1] + MOD - dpsum[k]) % MOD;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
