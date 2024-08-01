# Longest increasing subsequence

[Problem link](https://leetcode.com/problems/longest-increasing-subsequence)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-increasing-subsequence

class Solution {
 public:
  int lengthOfLIS(vector<int>& nums) {
    int N = nums.size();
    vector<int> DP(N);

    int ret = 0;
    for (int i = 0; i < N; ++i) {
      DP[i] = 1;
      for (int j = 0; j < i; ++j)
        if (nums[j] < nums[i]) DP[i] = max(DP[i], DP[j] + 1);
      ret = max(ret, DP[i]);
    }
    return ret;
  }
};
```
## Tags

* [Suboptimal solution](/Collections/suboptimal-solution.md#suboptimal-solution)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Longest increasing subsequence](/Collections/dynamic-programming.md#longest-increasing-subsequence)
