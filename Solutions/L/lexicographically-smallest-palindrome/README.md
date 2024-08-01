# Lexicographically smallest palindrome

[Problem link](https://leetcode.com/problems/lexicographically-smallest-palindrome/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/lexicographically-smallest-palindrome/

class Solution {
 public:
  string makeSmallestPalindrome(string s) {
    for (int i = 0, j = s.size() - 1; i < j; ++i, --j)
      s[i] = s[j] = min(s[i], s[j]);
    return s;
  }
};
```
## Tags

* [Palindrome](/Collections/palindrome.md#palindrome)
