# Time needed to rearrange a binary string

[Problem link](https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string

class Solution {
 public:
  int secondsToRemoveOccurrences(string s) {
    int n = s.size(), ret = 0;
    while (1) {
      int cur = 0;
      for (int i = 0; i < n - 1; ++i) {
        if (s[i] == '0' and s[i + 1] == '1') {
          swap(s[i], s[i + 1]);
          cur = 1;
          ++i;
        }
      }
      if (cur)
        ++ret;
      else
        break;
    }
    return ret;
  }
};
```