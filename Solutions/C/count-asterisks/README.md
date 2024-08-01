# Count asterisks

[Problem link](https://leetcode.com/problems/count-asterisks)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-asterisks

class Solution {
 public:
  int countAsterisks(string s) {
    int ret = 0;
    for (int i = 0, j = 0; s[i]; ++i) {
      if (s[i] == '|') j ^= 1;
      if (!j and s[i] == '*') ++ret;
    }
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
