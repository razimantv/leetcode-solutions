# How many numbers are smaller than the current number

[Problem link](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number

class Solution {
 public:
  vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
    auto ret = nums;
    for (auto& x : ret) {
      int cur = 0;
      for (int y : nums)
        if (y < x) ++cur;
      x = cur;
    }
    return ret;
  }
};
```
## Tags

* [Suboptimal solution](/README.md#Suboptimal_solution)
* [Simple implementation](/README.md#Simple_implementation)
