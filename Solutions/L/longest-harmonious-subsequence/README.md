# Longest harmonious subsequence

[Problem link](https://leetcode.com/problems/longest-harmonious-subsequence)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-harmonious-subsequence

class Solution {
 public:
  int findLHS(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int best = 0;
    for (int i = 0, j = 0, n = nums.size(); j < n; ++j) {
      while (nums[j] - nums[i] > 1) ++i;
      if (nums[j] - nums[i] == 1) best = max(best, j - i + 1);
    }
    return best;
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
