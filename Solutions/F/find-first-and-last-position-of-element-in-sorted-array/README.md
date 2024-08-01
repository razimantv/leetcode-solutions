# Find first and last position of element in sorted array

[Problem link](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution {
 public:
  vector<int> searchRange(vector<int>& nums, int target) {
    int left = 0;
    int right = nums.size() - 1;

    int start = -1;
    while (left <= right) {
      int mid = (left + right) / 2;
      if (nums[mid] == target && (mid == 0 or nums[mid - 1] != target)) {
        start = mid;
        break;
      } else if (nums[mid] >= target) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }

    int last = -1;
    left = 0;
    right = nums.size() - 1;
    while (left <= right) {
      int mid = (left + right) / 2;
      if (nums[mid] == target &&
          (mid + 1 == nums.size() or nums[mid + 1] != target)) {
        last = mid;
        break;
      } else if (nums[mid] <= target) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return {start, last};
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
