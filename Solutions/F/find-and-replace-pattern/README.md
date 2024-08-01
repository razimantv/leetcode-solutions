# Find and replace pattern

[Problem link](https://leetcode.com/problems/find-and-replace-pattern)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-and-replace-pattern

class Solution {
 public:
  vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
    vector<string> ret;
    for (int i = 0; pattern[i]; ++i) pattern[i] -= 'a';
    for (string& s : words) {
      vector<char> m1(26, -1), m2(26, -1);
      auto ss = s;
      bool flag = true;
      for (int i = 0; s[i]; ++i) {
        if (m1[s[i] -= 'a'] == pattern[i])
          continue;
        else if (m1[s[i]] != -1 or m2[pattern[i]] != -1) {
          flag = false;
          break;
        } else
          m1[s[i]] = pattern[i], m2[pattern[i]] = s[i];
      }
      if (flag) ret.push_back(ss);
    }
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Forward and backward](/Collections/hashmap.md#forward-and-backward)
