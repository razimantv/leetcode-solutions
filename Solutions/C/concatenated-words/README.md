# Concatenated words

[Problem link](https://leetcode.com/problems/concatenated-words)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/concatenated-words

class Solution {
 public:
  vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
    sort(words.begin(), words.end(), [&](const string& s1, const string& s2) {
      return s1.size() < s2.size();
    });

    int lmax = words.back().size();
    vector<unordered_set<int>> seen(lmax + 1);

    vector<string> ret;
    int p1 = 37, m1 = 2'108'523'447 / p1;
    for (const string& s : words) {
      int l = s.size();
      vector<int> dp(l + 1);
      dp[l] = 1;
      int hash{};
      for (int i = l - 1; i >= 0; --i) {
        hash = 0;
        for (int j = i; j < l; ++j) {
          hash = (hash * p1 + s[j] - 'a') % m1;
          if (dp[j + 1] and seen[j - i + 1].count(hash)) {
            dp[i] = 1;
            if (i) break;
          }
        }
      }
      if (dp[0]) ret.push_back(s);
      seen[l].insert(hash);
    }
    return ret;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search) > [Hashing](/Collections/string.md#hashing)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
