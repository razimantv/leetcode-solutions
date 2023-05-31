# Destroy sequential targets

[Problem link](https://leetcode.com/problems/destroy-sequential-targets/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/destroy-sequential-targets/

class Solution {
 public:
  int destroyTargets(vector<int>& nums, int space) {
    unordered_map<int, int> m;
    int best = -1, ret = -1;
    for (int x : nums) ++m[x % space];
    for (int x : nums) {
      if (best < m[x % space] or (best == m[x % space] and ret > x))
        best = m[x % space], ret = x;
    }
    return ret;
  }
};
```
## Tags

* [Hashmap](/README.md#Hashmap)
* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Basic](/README.md#Mathematics-Number_theory-Basic)
