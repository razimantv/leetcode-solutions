# Minimum amount of time to collect garbage

[Problem link](https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

class Solution {
 public:
  int garbageCollection(vector<string>& garbage, vector<int>& travel) {
    unordered_map<char, int> cnt, last;
    int g = garbage.size();
    for (int i = 0; i < g; ++i) {
      for (char c : garbage[i]) ++cnt[c], last[c] = i;
    }
    for (int i = 1; i < g - 1; ++i) travel[i] += travel[i - 1];
    int ret = 0;
    for (auto [k, v] : cnt) ret += v + (last[k] ? travel[last[k] - 1] : 0);
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
