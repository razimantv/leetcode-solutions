# Find subarrays with equal sum

[Problem link](https://leetcode.com/problems/find-subarrays-with-equal-sum/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-subarrays-with-equal-sum/

class Solution {
 public:
  bool findSubarrays(vector<int>& nums) {
    int n = nums.size();
    unordered_set<int> seen;
    for (int i = 1; i < n; ++i) {
      int cur = nums[i] + nums[i - 1];
      if (seen.count(cur)) return true;
      seen.insert(cur);
    }
    return false;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
