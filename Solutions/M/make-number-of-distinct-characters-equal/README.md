# Make number of distinct characters equal

[Problem link](https://leetcode.com/problems/make-number-of-distinct-characters-equal/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/make-number-of-distinct-characters-equal/

class Solution {
 public:
  unordered_map<char, int> cnt(const string& s) {
    unordered_map<char, int> ret;
    for (char c : s) ++ret[c];
    return ret;
  }
  bool isItPossible(string word1, string word2) {
    auto cnt1 = cnt(word1), cnt2 = cnt(word2);

    for (char c1 = 'a'; c1 <= 'z'; ++c1) {
      if (!cnt1[c1]) continue;
      for (char c2 = 'a'; c2 <= 'z'; ++c2) {
        if (!cnt2[c2]) continue;

        --cnt1[c1];
        ++cnt2[c1];
        --cnt2[c2];
        ++cnt1[c2];

        int diff{};
        for (auto [k, v] : cnt1) diff += !!v;
        for (auto [k, v] : cnt2) diff -= !!v;
        if (!diff) return true;

        ++cnt1[c1];
        --cnt2[c1];
        ++cnt2[c2];
        --cnt1[c2];
      }
    }
    return false;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Case-by-case analysis](/Collections/case-by-case-analysis.md#case-by-case-analysis)
