# Search insert position

[Problem link](https://leetcode.com/problems/search-insert-position)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/search-insert-position

class Solution {
 public:
  int searchInsert(vector<int>& nums, int target) {
    return lower_bound(nums.begin(), nums.end(), target) - nums.begin();
  }
};
```