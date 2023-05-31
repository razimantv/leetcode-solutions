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

* [Unique/duplicate element finding with bizarro algorithms](/README.md#Unique_duplicate_element_finding_with_bizarro_algorithms)
* [Array scanning](/README.md#Array_scanning) > [In-place modification](/README.md#Array_scanning-In_place_modification)
