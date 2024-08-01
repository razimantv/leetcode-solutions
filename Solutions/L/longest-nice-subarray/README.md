# Longest nice subarray

[Problem link](https://leetcode.com/problems/longest-nice-subarray/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-nice-subarray/

class Solution {
 public:
  int longestNiceSubarray(vector<int>& nums) {
    int best = 1, good = 0, n = nums.size();
    unordered_map<int, int> prev;
    for (int i = 0; i < n; ++i) {
      for (int j = 0, x = nums[i]; x; ++j, x >>= 1) {
        if (x & 1) {
          if (prev.count(j)) good = max(good, prev[j] + 1);
          prev[j] = i;
        }
      }
      best = max(best, i - good + 1);
    }
    return best;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Unique elements in subarray](/Collections/unique-elements-in-subarray.md#unique-elements-in-subarray)
