# Maximum 69 number

[Problem link](https://leetcode.com/problems/maximum-69-number)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-69-number

class Solution {
 public:
  int maximum69Number(int num) {
    auto s = to_string(num);
    for (char& c : s) {
      if (c == '6') {
        c = '9';
        break;
      }
    }
    return stoi(s);
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
