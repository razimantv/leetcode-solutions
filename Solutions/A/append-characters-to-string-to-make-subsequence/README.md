# Append characters to string to make subsequence

[Problem link](https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution {
 public:
  int appendCharacters(string s, string t) {
    int i = 0, j = 0;
    while (s[i] and t[j])
      if (s[i++] == t[j]) ++j;
    return t.size() - j;
  }
};
```
## Tags

* [Greedy](/README.md#Greedy)
* [String](/README.md#String) > [Subsequence](/README.md#String-Subsequence)
