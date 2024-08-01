# Count the digits that divide a number

[Problem link](https://leetcode.com/problems/count-the-digits-that-divide-a-number/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-the-digits-that-divide-a-number/

class Solution {
 public:
  int countDigits(int num) {
    auto s = to_string(num);
    int cnt{};
    for (char c : s)
      if (num % stoi(c + string("")) == 0) ++cnt;
    return cnt;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
