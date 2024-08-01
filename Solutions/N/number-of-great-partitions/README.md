# Number of great partitions

[Problem link](https://leetcode.com/problems/number-of-great-partitions/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-great-partitions/

class Solution {
 public:
  const int MOD = 1'000'000'007;
  void add(int& x, int y) {
    x += y;
    if (x >= MOD) x -= MOD;
  }
  int countPartitions(vector<int>& nums, int k) {
    long long tot = accumulate(nums.begin(), nums.end(), 0ll);
    if (tot < 2 * k) return 0;

    vector<int> dp(k);
    dp[0] = 1;
    int ret = 1;
    for (int x : nums) {
      for (int i = k - 1; i >= x; --i) add(dp[i], dp[i - x]);
      ret <<= 1;
      if (ret >= MOD) ret -= MOD;
    }

    for (int x : dp)
      for (int i = 0; i < 2; ++i) add(ret, MOD - x);
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Knapsack](/Collections/dynamic-programming.md#knapsack)
