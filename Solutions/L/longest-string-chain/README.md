# Longest string chain

[Problem link](https://leetcode.com/problems/longest-string-chain)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-string-chain

class Solution {
 public:
  int longestStrChain(vector<string>& words) {
    unordered_map<string, int> m;
    sort(words.begin(), words.end(), [](const string& s1, const string& s2) {
      return s1.size() < s2.size();
    });
    int best = 0;
    for (const string& s : words) {
      int L = s.size(), cur = 0;
      string sub = s.substr(1);
      for (int i = 0;; ++i) {
        auto mit = m.find(sub);
        if (mit != m.end()) cur = max(cur, mit->second);
        if (i == L) break;
        sub[i] = s[i];
      }
      best = max(best, m[s] = ++cur);
    }
    return best;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
