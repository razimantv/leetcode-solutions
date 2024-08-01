# Number of excellent pairs

[Problem link](https://leetcode.com/problems/number-of-excellent-pairs)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-excellent-pairs

class Solution {
 public:
  long long countExcellentPairs(vector<int>& nums, int pp) {
    unordered_map<int, long long> cnt;
    unordered_set<int> seen;
    for (int x : nums)
      if (!seen.count(x)) seen.insert(x), ++cnt[__builtin_popcount(x)];

    long long ret{};
    for (auto [k, v] : cnt)
      for (auto [k2, v2] : cnt)
        if (k + k2 >= pp) ret += v * v2;
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Hashmap](/Collections/hashmap.md#hashmap)
