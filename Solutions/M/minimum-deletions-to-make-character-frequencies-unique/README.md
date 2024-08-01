# Minimum deletions to make character frequencies unique

[Problem link](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique

class Solution {
 public:
  int minDeletions(string s) {
    unordered_map<char, int> cnt;
    for (char c : s) ++cnt[c];
    unordered_set<int> seen;

    int ret{};
    for (auto [k, v] : cnt) {
      while (v and seen.count(v)) --v, ++ret;
      seen.insert(v);
    }
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
