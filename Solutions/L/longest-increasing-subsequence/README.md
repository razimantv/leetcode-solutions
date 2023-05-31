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

* [Suboptimal solution](/README.md#Suboptimal_solution)
* [Dynamic programming](/README.md#Dynamic_programming) > [Longest increasing subsequence](/README.md#Dynamic_programming-Longest_increasing_subsequence)
