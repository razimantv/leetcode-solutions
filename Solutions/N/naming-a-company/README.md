# Naming a company

[Problem link](https://leetcode.com/problems/naming-a-company)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/naming-a-company

class Solution {
 public:
  long long distinctNames(vector<string>& ideas) {
    unordered_set<string> seen;
    for (const string& s : ideas) seen.insert(s);
    vector<vector<int>> cnt(26, vector<int>(26));
    for (string s : ideas) {
      char c = s[0];
      for (char cp = 'a'; cp <= 'z'; ++cp) {
        if (cp == c) continue;
        s[0] = cp;
        if (!seen.count(s)) ++cnt[c - 'a'][cp - 'a'];
      }
    }

    long long ret = 0;
    for (int i = 0; i < 26; ++i)
      for (int j = 0; j < i; ++j) ret += 2 * cnt[i][j] * (long long)cnt[j][i];
    return ret;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
