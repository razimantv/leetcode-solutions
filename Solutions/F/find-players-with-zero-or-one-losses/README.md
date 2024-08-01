# Find players with zero or one losses

[Problem link](https://leetcode.com/problems/find-players-with-zero-or-one-losses/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution {
 public:
  vector<vector<int>> findWinners(vector<vector<int>>& matches) {
    unordered_map<int, int> cnt;
    for (auto& m : matches) {
      cnt[m[0]];
      cnt[m[1]]++;
    }
    vector<vector<int>> ret(2);
    for (auto& [k, v] : cnt) {
      if (v < 2) ret[v].push_back(k);
    }
    for (auto& r : ret) sort(r.begin(), r.end());
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
