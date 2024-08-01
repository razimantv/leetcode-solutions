# Maximize greatness of an array

[Problem link](https://leetcode.com/problems/maximize-greatness-of-an-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximize-greatness-of-an-array/

class Solution {
 public:
  int maximizeGreatness(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int ret{};
    for (int i = 0, j = 0, n = nums.size(); j < n; ++j) {
      if (nums[j] > nums[i]) ++i, ++ret;
    }
    return ret;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Two pointers](/Collections/two-pointers.md#two-pointers)
