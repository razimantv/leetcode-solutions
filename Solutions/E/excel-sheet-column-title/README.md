# Excel sheet column title

[Problem link](https://leetcode.com/problems/excel-sheet-column-title/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/excel-sheet-column-title/

class Solution {
 public:
  string convertToTitle(int n) {
    string s;
    while (n) {
      s += ('A' + (--n) % 26);
      n /= 26;
    }
    reverse(s.begin(), s.end());
    return s;
  }
};
```
## Tags

* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Basic](/README.md#Mathematics-Number_theory-Basic)
