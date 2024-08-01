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

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
