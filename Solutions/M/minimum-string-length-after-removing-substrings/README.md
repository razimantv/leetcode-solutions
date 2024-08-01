# Minimum string length after removing substrings

[Problem link](https://leetcode.com/problems/minimum-string-length-after-removing-substrings/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

class Solution {
 public:
  int minLength(string s) {
    vector<char> stack;
    for (char c : s) {
      if (!stack.empty() and ((c == 'D' and stack.back() == 'C') or
                              (c == 'B' and stack.back() == 'A')))
        stack.pop_back();
      else
        stack.push_back(c);
    }
    return stack.size();
  }
};
```
## Tags

* [Stack](/Collections/stack.md#stack) > [From array elements](/Collections/stack.md#from-array-elements)
