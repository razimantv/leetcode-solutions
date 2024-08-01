# Largest odd number in string

[Problem link](https://leetcode.com/problems/largest-odd-number-in-string)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/largest-odd-number-in-string

class Solution {
 public:
  string largestOddNumber(string num) {
    for (int i = num.size() - 1; i >= 0; --i)
      if (num[i] & 1) return num.substr(0, i + 1);
    return "";
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Right to left](/Collections/array-scanning.md#right-to-left)
