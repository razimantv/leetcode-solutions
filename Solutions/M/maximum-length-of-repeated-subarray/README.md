# Maximum length of repeated subarray

[Problem link](https://leetcode.com/problems/maximum-length-of-repeated-subarray)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-length-of-repeated-subarray

class Solution {
 public:
  int findLength(vector<int>& nums1, vector<int>& nums2) {
    int m = nums1.size(), n = nums2.size();
    vector<int> dp(n + 1);
    int best = 0;
    for (int i = m - 1; i >= 0; --i)
      for (int j = 0; j < n; ++j) {
        if (nums1[i] == nums2[j])
          dp[j] = 1 + dp[j + 1];
        else
          dp[j] = 0;
        best = max(best, dp[j]);
      }
    return best;
  }
};
```
## Tags

* [Dynamic programming](/README.md#Dynamic_programming) > [Array reuse](/README.md#Dynamic_programming-Array_reuse)
* [Dynamic programming](/README.md#Dynamic_programming) > [Longest common subsequence](/README.md#Dynamic_programming-Longest_common_subsequence)
