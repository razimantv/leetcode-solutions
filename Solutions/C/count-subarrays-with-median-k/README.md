# Count subarrays with median k

[Problem link](https://leetcode.com/problems/count-subarrays-with-median-k/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-subarrays-with-median-k/

class Solution {
 public:
  int countSubarrays(vector<int>& nums, int k) {
    unordered_map<int, int> cnt;
    cnt[0] = 1;

    int i = 0, n = nums.size(), pref = 0;
    for (; i < n and nums[i] != k; ++i) {
      if (nums[i] < k)
        --pref;
      else
        ++pref;
      ++cnt[pref];
    }

    int ret{};
    for (; i < n; ++i) {
      if (nums[i] < k)
        --pref;
      else if (nums[i] > k)
        ++pref;
      ret += cnt[pref] + cnt[pref - 1];
    }
    return ret;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Hashmap](/Collections/hashmap.md#hashmap)
