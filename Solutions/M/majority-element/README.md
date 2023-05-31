# Majority element

[Problem link](https://leetcode.com/problems/majority-element)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/majority-element

class Solution {
 public:
  int majorityElement(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    return nums[nums.size() / 2];
  }
};
```
## Tags

* [Suboptimal solution](/README.md#Suboptimal_solution)
* [Sorting](/README.md#Sorting)
