# Splitting a string into descending consecutive values

[Problem link](https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values

class Solution {
 public:
  bool splitString(string s) {
    int n = s.size();
    long long lim = 1000000000000ll;
    for (int i = 1; i < n; ++i) {
      long long cur = 0;
      bool flag = true;
      for (int j = 0; j < i; ++j) {
        cur = cur * 10 + (s[j] - '0');
        if (cur >= lim) {
          flag = false;
          break;
        }
      }
      if (!flag) continue;

      long long curcur = 0;
      int last = i;
      for (int j = i; j < n; ++j) {
        curcur = curcur * 10 + (s[j] - '0');
        if (curcur == cur - 1 and
            (curcur > 0 or j == n - 1 or s[j + 1] > '0')) {
          cur = curcur;
          curcur = 0;
          last = j + 1;
        } else if (curcur >= cur) {
          flag = false;
          break;
        }
      }
      if (flag and last == n) return true;
    }
    return false;
  }
};
```