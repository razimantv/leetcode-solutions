# First missing positive

[Problem link](https://leetcode.com/problems/first-missing-positive)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/first-missing-positive

class Solution {
 public:
  int firstMissingPositive(vector<int>& nums) {
    int N = nums.size();
    for (int i = 0; i < N; ++i) {
      if (nums[i] > 0 and nums[i] <= N and nums[nums[i] - 1] != nums[i]) {
        swap(nums[i], nums[nums[i] - 1]);
        --i;
      }
    }

    for (int i = 0; i < N; ++i)
      if (nums[i] != i + 1) return i + 1;
    return N + 1;
  }
};
```
## Tags

* [Unique/duplicate element finding with bizarro algorithms](/Collections/unique-duplicate-element-finding-with-bizarro-algorithms.md#unique-duplicate-element-finding-with-bizarro-algorithms)
