# Remove letter to equalize frequency

[Problem link](https://leetcode.com/problems/remove-letter-to-equalize-frequency/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution {
 public:
  bool equalFrequency(string word) {
    map<char, int> cnt;
    for (char c : word) ++cnt[c];
    map<int, int> cntmap;
    for (auto [k, v] : cnt) ++cntmap[v];

    if (cntmap.size() > 2) return false;
    if (cntmap.size() == 1)
      return cntmap.begin()->first == 1 or cntmap.begin()->second == 1;

    auto [k1, v1] = *cntmap.begin();
    auto [k2, v2] = *cntmap.rbegin();
    return ((k1 == 1 and v1 == 1) or (v2 == 1 and k2 == k1 + 1));
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Group items](/Collections/hashmap.md#group-items)
