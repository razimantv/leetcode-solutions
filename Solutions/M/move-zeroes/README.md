# Move zeroes

[Problem link](https://leetcode.com/problems/move-zeroes)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/move-zeroes

class Solution {
 public:
  void moveZeroes(vector<int>& nums) {
    int next = 0;
    for (int i = 0; i < nums.size(); ++i) {
      if (nums[i] != 0) nums[next++] = nums[i];
    }
    while (next < nums.size()) nums[next++] = 0;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [In-place modification](/Collections/array-scanning.md#in-place-modification)
