# Minimum remove to make valid parentheses

[Problem link](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses

class Solution {
 public:
  string minRemoveToMakeValid(string s) {
    for (int i = 0, dir = 1; i < 2; ++i, dir = -dir) {
      string cur;
      for (int p = 0; char c : s) {
        int add = 0;
        if (c == '(')
          add = dir;
        else if (c == ')')
          add = -dir;
        if (p + add >= 0) cur += c, p += add;
      }
      s = cur;
      reverse(s.begin(), s.end());
    }
    return s;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [Valid brackets](/Collections/prefix.md#valid-brackets)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [From both ends of array](/Collections/array-scanning.md#from-both-ends-of-array)
