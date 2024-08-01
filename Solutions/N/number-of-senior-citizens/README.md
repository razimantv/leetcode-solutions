# Number of senior citizens

[Problem link](https://leetcode.com/problems/number-of-senior-citizens/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-senior-citizens/

class Solution {
 public:
  int countSeniors(vector<string>& details) {
    int ret{};
    for (string s : details)
      if (s.substr(11, 2) > "60") ++ret;
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
