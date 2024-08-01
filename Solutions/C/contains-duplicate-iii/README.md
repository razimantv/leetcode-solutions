# Contains duplicate iii

[Problem link](https://leetcode.com/problems/contains-duplicate-iii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/contains-duplicate-iii

class Solution {
 public:
  bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, long long t) {
    if (!k) return false;
    map<long long, int> s;
    for (int i = 0; i < nums.size(); ++i) {
      auto sit = s.lower_bound(nums[i] - t);
      if (sit != s.end() and sit->first <= nums[i] + t) return true;
      if (i >= k) {
        sit = s.find(nums[i - k]);
        if (--(sit->second) == 0) s.erase(sit);
      }
      s[nums[i]]++;
    }
    return false;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search) > [C++ set](/Collections/binary-search.md#c---set)
