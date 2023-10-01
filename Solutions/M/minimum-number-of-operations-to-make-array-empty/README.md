# Minimum number of operations to make array empty

[Problem link](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

class Solution {
 public:
  int minOperations(vector<int>& nums) {
    unordered_map<int, int> cnt;
    for (int x : nums) ++cnt[x];
    int ret{};
    for (auto [k, v] : cnt) {
      if (v == 1) return -1;
      ret += (v + 2) / 3;
    }
    return ret;
  }
};
```
## Tags

* [Hashmap](/README.md#Hashmap)
* [Mathematics](/README.md#Mathematics) > [Basic](/README.md#Mathematics-Basic)
