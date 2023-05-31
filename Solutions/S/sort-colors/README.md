# Sort colors

[Problem link](https://leetcode.com/problems/sort-colors)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sort-colors

class Solution {
 public:
  void sortColors(vector<int>& nums) {
    for (int i = 0, j = 0, k = nums.size(); j < k;) {
      if (nums[j] == 0) {
        swap(nums[i++], nums[j++]);
      } else if (nums[j] == 2) {
        swap(nums[j], nums[--k]);
      } else {
        j++;
      }
    }
  }
};
```