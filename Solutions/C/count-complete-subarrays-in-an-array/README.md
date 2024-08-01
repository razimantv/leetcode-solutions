# Count complete subarrays in an array

[Problem link](https://leetcode.com/problems/count-complete-subarrays-in-an-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution {
 public:
  int countCompleteSubarrays(vector<int>& nums) {
    unordered_set<int> all(nums.begin(), nums.end());
    int s = all.size(), ret{};
    for (int n = nums.size(), i = n - 1; i >= 0; --i) {
      unordered_set<int> seen;
      for (int j = i; j >= 0; --j) {
        seen.insert(nums[j]);
        if (seen.size() == s) {
          ret += j + 1;
          break;
        }
      }
    }
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
