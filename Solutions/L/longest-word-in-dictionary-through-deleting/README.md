# Longest word in dictionary through deleting

[Problem link](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-word-in-dictionary-through-deleting

class Solution {
 public:
  string findLongestWord(string s, vector<string>& d) {
    string ret = "";

    for (const auto& s2 : d) {
      bool flag = true;
      for (int i = 0; char c : s2) {
        while (flag and (s[i] != c)) {
          if (s[i] == 0) {
            flag = false;
          }
          ++i;
        }
        if (!flag) break;
        ++i;
      }

      if (flag and
          (s2.size() > ret.size() or (s2.size() == ret.size() and s2 < ret)))
        ret = s2;
    }
    return ret;
  }
};
```
## Tags

* [String](/Collections/string.md#string) > [Subsequence](/Collections/string.md#subsequence)
