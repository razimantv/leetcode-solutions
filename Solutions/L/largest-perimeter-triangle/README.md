# Largest perimeter triangle

[Problem link](https://leetcode.com/problems/largest-perimeter-triangle/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/largest-perimeter-triangle/

class Solution {
 public:
  int largestPerimeter(vector<int>& nums) {
    sort(nums.begin(), nums.end(), greater<int>());
    int n = nums.size();
    for (int i = 0; i + 2 < n; ++i)
      if (nums[i] < nums[i + 1] + nums[i + 2])
        return nums[i] + nums[i + 1] + nums[i + 2];
    return 0;
  }
};
```
## Tags

* [Sorting](/README.md#Sorting)
* [Mathematics](/README.md#Mathematics) > [Basic](/README.md#Mathematics-Basic)
