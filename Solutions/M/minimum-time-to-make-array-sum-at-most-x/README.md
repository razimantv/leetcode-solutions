# Minimum time to make array sum at most x

[Problem link](https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

class Solution {
 public:
  int minimumTime(vector<int>& nums1, vector<int>& nums2, int target) {
    // at time T:
    // unchanged: a + bT
    // changed at t: b(T-t)
    // sum: sum(a + Tb) - sum_j (a_j + b_j t_j)
    // among selected: optimal to pick with increasing b
    int n = nums1.size();
    vector<int> idx(n);
    iota(idx.begin(), idx.end(), 0);
    sort(idx.begin(), idx.end(),
         [&](int i, int j) { return nums2[i] < nums2[j]; });

    vector<int> dp(n + 1);
    for (int x : idx)
      for (int i = n; i; --i)
        dp[i] = max(dp[i], dp[i - 1] + nums1[x] + i * nums2[x]);

    int atot = accumulate(nums1.begin(), nums1.end(), 0),
        btot = accumulate(nums2.begin(), nums2.end(), 0);
    for (int i = 0; i <= n; ++i)
      if (atot + i * btot - dp[i] <= target) return i;
    return -1;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Index array](/Collections/sorting.md#index-array)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Greedy](/Collections/greedy.md#greedy)
