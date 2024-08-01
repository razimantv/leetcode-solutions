# Minimum operations to collect elements

[Problem link](https://leetcode.com/problems/minimum-operations-to-collect-elements/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-operations-to-collect-elements/

class Solution {
 public:
  int minOperations(vector<int>& nums, int k) {
    unordered_set<int> seen;
    for (int n = nums.size(), i = n - 1; i >= 0; --i) {
      if (nums[i] <= k) seen.insert(nums[i]);
      if (seen.size() == k) return n - i;
    }
    return -1;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Right to left](/Collections/array-scanning.md#right-to-left)
