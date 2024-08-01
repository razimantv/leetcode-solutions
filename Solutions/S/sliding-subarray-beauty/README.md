# Sliding subarray beauty

[Problem link](https://leetcode.com/problems/sliding-subarray-beauty/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sliding-subarray-beauty/

class Solution {
 public:
  vector<int> getSubarrayBeauty(vector<int>& nums, int k, int x) {
    vector<int> cnt(51), ret;
    for (int i = 0, n = nums.size(); i < n; ++i) {
      if (nums[i] < 0) ++cnt[-nums[i]];
      if (i >= k and nums[i - k] < 0) --cnt[-nums[i - k]];
      if (i >= k - 1) {
        ret.push_back(0);
        for (int j = 50, tot = 0; j; --j) {
          tot += cnt[j];
          if (tot >= x) {
            ret.back() = -j;
            break;
          }
        }
      }
    }
    return ret;
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
* [Hashmap](/Collections/hashmap.md#hashmap)
