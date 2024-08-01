# Check distances between same letters

[Problem link](https://leetcode.com/problems/check-distances-between-same-letters/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/check-distances-between-same-letters/

class Solution {
 public:
  bool checkDistances(string s, vector<int>& distance) {
    map<char, int> pos;
    int n = s.size();
    for (int i = 0; i < n; ++i) {
      char c = s[i];
      if (pos.count(c) and i - pos[c] - 1 != distance[c - 'a']) return false;
      pos[c] = i;
    }
    return true;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
