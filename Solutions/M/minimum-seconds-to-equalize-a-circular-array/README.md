# Minimum seconds to equalize a circular array

[Problem link](https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

class Solution {
 public:
  int minimumSeconds(vector<int>& nums) {
    unordered_map<int, vector<int>> pos;
    int n = nums.size(), ret = n / 2;
    for (int i = 0; i < n; ++i) pos[nums[i]].push_back(i);
    for (auto& [k, vec] : pos) {
      int gap{n + vec[0] - vec.back() - 1};
      for (int i = 1, l = vec.size(); i < l; ++i)
        gap = max(gap, vec[i] - vec[i - 1] - 1);
      ret = min(ret, (gap + 1) / 2);
    }
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Group items](/Collections/hashmap.md#group-items)
