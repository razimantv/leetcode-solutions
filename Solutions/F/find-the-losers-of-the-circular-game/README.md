# Find the losers of the circular game

[Problem link](https://leetcode.com/problems/find-the-losers-of-the-circular-game/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-losers-of-the-circular-game/

class Solution {
 public:
  vector<int> circularGameLosers(int n, int k) {
    vector<int> ret, got(n);
    for (int i = 0, j = 0; !got[i]; got[i] = 1, i = (i + k * ++j) % n)
      ;
    for (int i = 0; i < n; ++i)
      if (!got[i]) ret.push_back(i + 1);
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
