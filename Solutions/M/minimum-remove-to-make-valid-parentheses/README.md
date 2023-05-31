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

* [Prefix](/README.md#Prefix) > [Sum](/README.md#Prefix-Sum) > [Valid brackets](/README.md#Prefix-Sum-Valid_brackets)
* [Array scanning](/README.md#Array_scanning) > [From both ends of array](/README.md#Array_scanning-From_both_ends_of_array)
