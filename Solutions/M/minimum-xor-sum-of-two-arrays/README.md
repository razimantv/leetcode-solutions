# Minimum xor sum of two arrays

[Problem link](https://leetcode.com/problems/minimum-xor-sum-of-two-arrays)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-xor-sum-of-two-arrays

class Solution {
 public:
  int minimumXORSum(vector<int>& nums1, vector<int>& nums2) {
    int n = nums1.size(), M = 1 << n;
    vector<vector<int>> DP(n + 1, vector<int>(M, 1000000000));
    DP[0][0] = 0;

    for (int i = 1; i <= n; ++i) {
      int cur = nums2[i - 1];
      for (int mask = 0; mask < M; ++mask) {
        for (int j = 0; j < n; ++j) {
          if (!(mask & (1 << j))) continue;
          DP[i][mask] =
              min(DP[i][mask], DP[i - 1][mask ^ (1 << j)] + (nums1[j] ^ cur));
        }
      }
    }
    return DP.back().back();
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Subsets](/Collections/dynamic-programming.md#subsets)
