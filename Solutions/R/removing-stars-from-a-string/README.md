# Removing stars from a string

[Problem link](https://leetcode.com/problems/removing-stars-from-a-string/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/removing-stars-from-a-string/

class Solution {
 public:
  string removeStars(string s) {
    string ret;
    for (char c : s) {
      if (c == '*') {
        if (!ret.empty()) ret.pop_back();
      } else
        ret += c;
    }
    return ret;
  }
};
```
## Tags

* [Stack](/Collections/stack.md#stack)
