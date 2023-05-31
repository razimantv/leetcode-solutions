# Steps to make array non decreasing

[Problem link](https://leetcode.com/problems/steps-to-make-array-non-decreasing)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/steps-to-make-array-non-decreasing

class Solution {
 public:
  int totalSteps(vector<int>& nums) {
    int n = nums.size();
    vector<pair<int, int>> stk;
    int ret = 0;
    for (int i = n - 1; i >= 0; --i) {
      int cur = 0;
      while (!stk.empty() and nums[i] > stk.back().first) {
        cur = max(cur + 1, stk.back().second);
        stk.pop_back();
      }
      ret = max(ret, cur);
      stk.push_back({nums[i], cur});
    }
    return ret;
  }
};
```