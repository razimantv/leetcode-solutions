# Max consecutive ones iii

[Problem link](https://leetcode.com/problems/max-consecutive-ones-iii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/max-consecutive-ones-iii

class Solution {
 public:
  int longestOnes(vector<int>& nums, int k) {
    int ret = 0;
    for (int i = 0, j = -1, n = nums.size(), use = 0; i < n and j < n; ++i) {
      while (use <= k and j < n) use += (++j == n or nums[j] == 0);
      ret = max(ret, j - i);
      use -= (nums[i] == 0);
    }
    return ret;
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
