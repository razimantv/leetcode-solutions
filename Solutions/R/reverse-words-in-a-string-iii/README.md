# Reverse words in a string iii

[Problem link](https://leetcode.com/problems/reverse-words-in-a-string-iii/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution {
 public:
  string reverseWords(string s) {
    istringstream iss(s);
    string ret, cur;
    while (iss >> cur) {
      if (ret.size()) ret += " ";
      reverse(cur.begin(), cur.end());
      ret += cur;
    }
    return ret;
  }
};
```
## Tags

* [String](/Collections/string.md#string) > [Parsing](/Collections/string.md#parsing)
