# Maximum beauty of an array after applying operation

[Problem link](https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

class Solution {
 public:
  int maximumBeauty(vector<int>& nums, int k) {
    sort(nums.begin(), nums.end());
    int best{1};
    for (int n = nums.size(), l = 0, r = 0; r < n; ++r) {
      while (nums[r] - nums[l] > 2 * k) ++l;
      best = max(best, r - l + 1);
    }
    return best;
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
