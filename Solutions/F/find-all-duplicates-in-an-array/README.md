# Find all duplicates in an array

[Problem link](https://leetcode.com/problems/find-all-duplicates-in-an-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-all-duplicates-in-an-array

class Solution {
 public:
  vector<int> findDuplicates(vector<int>& nums) {
    vector<int> ret;
    for (int i = 0; i < nums.size(); ++i) {
      if (nums[i] == i + 1 or nums[i] == 0) continue;
      if (nums[nums[i] - 1] == nums[i]) {
        ret.push_back(nums[i]);
        nums[i] = 0;
      } else {
        swap(nums[i], nums[nums[i] - 1]);
        --i;
      }
    }
    return ret;
  }
};
```
## Tags

* [Unique/duplicate element finding with bizarro algorithms](/Collections/unique-duplicate-element-finding-with-bizarro-algorithms.md#unique-duplicate-element-finding-with-bizarro-algorithms)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [In-place modification](/Collections/array-scanning.md#in-place-modification)
