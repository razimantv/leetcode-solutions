# Minimum distance to the target element

[Problem link](https://leetcode.com/problems/minimum-distance-to-the-target-element)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-distance-to-the-target-element

class Solution {
 public:
  int getMinDistance(vector<int>& nums, int target, int start) {
    int n = nums.size(), best = n;
    for (int i = 0; i < n; ++i)
      if (nums[i] == target) best = min(best, abs(start - i));
    return best;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
