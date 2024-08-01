# Add digits

[Problem link](https://leetcode.com/problems/add-digits)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/add-digits

class Solution {
 public:
  int addDigits(int num) { return (num - 1) % 9 + 1; }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
