# Is subsequence

[Problem link](https://leetcode.com/problems/is-subsequence)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/is-subsequence

class Solution {
 public:
  bool isSubsequence(string s, string t) {
    if (s.empty()) return true;
    for (int i = 0, j = 0; j < t.size(); j++)
      if (s[i] == t[j] and ++i == s.size()) return true;
    return false;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [String](/Collections/string.md#string) > [Subsequence](/Collections/string.md#subsequence)
