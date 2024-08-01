# Check if array is good

[Problem link](https://leetcode.com/problems/check-if-array-is-good/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/check-if-array-is-good/

class Solution {
 public:
  bool isGood(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    for (int i = 0, n = nums.size(); i < n; ++i)
      if (nums[i] != i + 1 - (i == n - 1)) return false;
    return true;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
