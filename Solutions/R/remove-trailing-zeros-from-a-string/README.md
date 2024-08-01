# Remove trailing zeros from a string

[Problem link](https://leetcode.com/problems/remove-trailing-zeros-from-a-string/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

class Solution {
 public:
  string removeTrailingZeros(string num) {
    while (num.back() == '0') num.pop_back();
    return num;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
