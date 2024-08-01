# Contains duplicate ii

[Problem link](https://leetcode.com/problems/contains-duplicate-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/contains-duplicate-ii

class Solution {
public:
  bool containsNearbyDuplicate(vector<int> &nums, int k) {
    unordered_map<int, int> cnt;
    for (int i = 0, n = nums.size(); i < n; ++i) {
      if (cnt[nums[i]]++)
        return true;
      if (i >= k)
        --cnt[nums[i - k]];
    }
    return false;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Sliding window](/Collections/sliding-window.md#sliding-window)
