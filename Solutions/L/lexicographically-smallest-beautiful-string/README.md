# Lexicographically smallest beautiful string

[Problem link](https://leetcode.com/problems/lexicographically-smallest-beautiful-string/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/lexicographically-smallest-beautiful-string/

class Solution {
 public:
  string smallestBeautifulString(string s, int k) {
    char last = 'a' + k - 1;
    int pos = s.size() - 1;
    while (pos >= 0) {
      char& c = s[pos];
      while (++c <= last)
        if ((pos == 0 or c != s[pos - 1]) and (pos < 2 or c != s[pos - 2]))
          break;
      if (c <= last) break;
      --pos;
    }
    if (pos < 0) return "";
    while (s[++pos]) {
      char& c = s[pos];
      for (c = 'a';; ++c)
        if (c != s[pos - 1] and (pos == 1 or c != s[pos - 2])) break;
    }
    return s;
  }
};
```
## Tags

* [Palindrome](/Collections/palindrome.md#palindrome)
