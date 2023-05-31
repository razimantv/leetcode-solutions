# Sort array by parity ii

[Problem link](https://leetcode.com/problems/sort-array-by-parity-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sort-array-by-parity-ii

class Solution {
 public:
  vector<int> sortArrayByParityII(vector<int>& nums) {
    for (int i = 0, j = 1, n = nums.size(); i < n and j < n;) {
      if (!(nums[i] & 1))
        i += 2;
      else if (nums[j] & 1)
        j += 2;
      else {
        swap(nums[i], nums[j]);
        j += 2;
        i += 2;
      }
    }
    return nums;
  }
};
```