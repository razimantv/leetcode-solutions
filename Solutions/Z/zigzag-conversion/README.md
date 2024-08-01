# Zigzag conversion

[Problem link](https://leetcode.com/problems/zigzag-conversion/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/zigzag-conversion/

class Solution {
 public:
  string convert(string s, int r) {
    if (r == 1) return s;
    vector<string> rows(r);
    for (int i = 0, j = 0, dj = -1; s[i]; ++i, j += dj) {
      rows[j] += s[i];
      if (j == 0 or j == r - 1) dj = -dj;
    }
    return accumulate(rows.begin(), rows.end(), string());
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
