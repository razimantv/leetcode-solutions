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

* [Sorting](/Collections/sorting.md#sorting)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Basic](/Collections/mathematics.md#basic)
