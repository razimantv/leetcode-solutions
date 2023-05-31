# Single element in a sorted array

[Problem link](https://leetcode.com/problems/single-element-in-a-sorted-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/single-element-in-a-sorted-array

class Solution {
 public:
  int singleNonDuplicate(vector<int>& nums) {
    int N = nums.size() / 2;
    int start = -1, end = N;
    while (end - start > 1) {
      int mid = (end + start) >> 1;
      if (nums[mid * 2] == nums[mid * 2 + 1])
        start = mid;
      else
        end = mid;
    }
    return nums[2 * end];
  }
};
```