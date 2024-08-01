# Excel sheet column number

[Problem link](https://leetcode.com/problems/excel-sheet-column-number)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/excel-sheet-column-number

class Solution {
 public:
  int titleToNumber(string s) {
    int ret = 0;
    for (int i = s.size() - 1, p = 1; i >= 0; --i) {
      ret += p * (s[i] - 'A' + 1);
      if (i) p *= 26;
    }
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
