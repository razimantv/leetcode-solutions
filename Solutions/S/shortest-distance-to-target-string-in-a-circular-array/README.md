# Shortest distance to target string in a circular array

[Problem link](https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

class Solution {
 public:
  int closetTarget(vector<string>& words, string target, int start) {
    int n = words.size(), ret = n;
    for (int i = 0; i < n; ++i) {
      if (words[i] != target) continue;
      int cur = abs(i - start);
      ret = min(ret, min(cur, n - cur));
    }
    return ret == n ? -1 : ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
