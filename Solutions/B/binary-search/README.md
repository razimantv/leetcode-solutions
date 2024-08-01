# Binary search

[Problem link](https://leetcode.com/problems/binary-search)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/binary-search

class Solution {
 public:
  int search(vector<int>& nums, int target) {
    int start = 0, end = nums.size();
    while (end - start > 1) {
      int mid = (start + end) / 2;
      if (nums[mid] <= target)
        start = mid;
      else
        end = mid;
    }
    return (nums[start] == target) ? start : -1;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
