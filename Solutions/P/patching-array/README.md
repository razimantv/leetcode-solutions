# Patching array

[Problem link](https://leetcode.com/problems/patching-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/patching-array

class Solution {
 public:
  int minPatches(vector<int>& nums, int n) {
    int ret = 0;
    for (long long lim = 0, i = 0, m = nums.size(); lim < n;) {
      if (i < m and nums[i] <= lim + 1)
        lim += nums[i++];
      else
        ++ret, lim = 2 * lim + 1;
    }
    return ret;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
