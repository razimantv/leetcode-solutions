# Happy students

[Problem link](https://leetcode.com/problems/happy-students/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/happy-students/

class Solution {
 public:
  int countWays(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int n = nums.size(), ret = (nums[0] > 0) + (nums[n - 1] < n);
    for (int i = 0, n = nums.size(); i < n - 1; ++i)
      if (nums[i] <= i and nums[i + 1] > i + 1) ++ret;
    return ret;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
