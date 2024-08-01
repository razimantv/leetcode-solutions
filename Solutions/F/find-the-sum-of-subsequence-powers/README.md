# Find the sum of subsequence powers

[Problem link](https://leetcode.com/problems/find-the-sum-of-subsequence-powers/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

const int mod = 1'000'000'007;

void inc(int& x, int y) {
  x += y;
  if (x >= mod) x -= mod;
}

class Solution {
 public:
  int sumOfPowers(vector<int>& nums, int K) {
    int n = nums.size();
    sort(nums.begin(), nums.end());
    unordered_set<int> diffs;
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < i; ++j) diffs.insert(nums[i] - nums[j]);
    int ret = 0;
    for (auto d : diffs) {
      vector<vector<vector<int>>> dp(
          n, vector<vector<int>>(K + 1, vector<int>(2, 0))
      );
      for (int i = 0; i < n; ++i) {
        int x = nums[i];
        dp[i][1][0] = 1;
        for (int ii = 0; ii < i; ++ii) {
          int dd = x - nums[ii];
          if (dd < d) break;
          if (dd == d) {
            for (int k = 2; k <= K; ++k) {
              inc(dp[i][k][1], dp[ii][k - 1][0]);
              inc(dp[i][k][1], dp[ii][k - 1][1]);
            }
          } else {
            for (int k = 2; k <= K; ++k) {
              inc(dp[i][k][0], dp[ii][k - 1][0]);
              inc(dp[i][k][1], dp[ii][k - 1][1]);
            }
          }
        }
        ret = (ret + dp[i][K][1] * 1ll * d) % mod;
      }
    }
    return ret;
  }
};
```
### Solution.py
```py
# https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

class Solution:
    def sumOfPowers(self, nums: List[int], K: int) -> int:
        nums, n = sorted(nums), len(nums)
        diffs = sorted(list(set(
            nums[i] - nums[j] for i in range(n) for j in range(i)
        )))
        mod, prev, ret = 10 ** 9 + 7, 0, 0
        for d in diffs[::-1]:
            dpsum = [i for i in range(n + 1)]
            ii = [min(i, bisect_right(nums, nums[i]-d)) for i in range(n)]
            for k in range(2, K+1):
                old = dpsum.copy()
                for i in range(n):
                    dpsum[i + 1] = (dpsum[i] + old[ii[i]]) % mod
            ret = (ret + (dpsum[-1] + mod - prev) * d) % mod
            prev = dpsum[-1]
        return ret
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics) > [Inclusion-exclusion](/Collections/mathematics.md#inclusion-exclusion)
* [Binary search](/Collections/binary-search.md#binary-search)
