# Rearranging fruits

[Problem link](https://leetcode.com/problems/rearranging-fruits/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/rearranging-fruits/

class Solution {
 public:
  long long minCost(vector<int>& basket1, vector<int>& basket2) {
    map<int, int> diff;
    for (int x : basket1) ++diff[x];
    for (int x : basket2) --diff[x];
    vector<int> toswap;
    int small = diff.begin()->first;
    for (auto [k, v] : diff) {
      if (v & 1) return -1;
      for (int i = 0; i < abs(v) / 2; ++i) toswap.push_back(k);
    }

    long long ret{};
    for (int i = 0, L = toswap.size() / 2; i < L; ++i)
      ret += min(toswap[i], 2 * small);
    return ret;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Hashmap](/Collections/hashmap.md#hashmap)
