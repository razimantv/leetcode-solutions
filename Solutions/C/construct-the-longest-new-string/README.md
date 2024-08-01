# Construct the longest new string

[Problem link](https://leetcode.com/problems/construct-the-longest-new-string/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/construct-the-longest-new-string/

class Solution {
 public:
  int longestString(int x, int y, int z) {
    if (x > y) swap(x, y);
    y = min(y, x + 1);
    return 2 * (x + y + z);
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Basic](/Collections/mathematics.md#basic)
