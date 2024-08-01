# Backspace string compare

[Problem link](https://leetcode.com/problems/backspace-string-compare)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/backspace-string-compare

class Solution {
 public:
  char next(string &S, int &i) {
    int c = 0;
    while (1) {
      if (i < 0) return '#';
      if (S[i] == '#')
        c++;
      else if (c-- == 0)
        return S[i--];
      i--;
    }
  }
  bool backspaceCompare(string S, string T) {
    int i = S.size() - 1, j = T.size() - 1;
    while (i >= 0 or j >= 0) {
      if (next(S, i) != next(T, j)) return false;
    }
    return true;
  }
};
```
## Tags

* [Time reversed simulation](/Collections/time-reversed-simulation.md#time-reversed-simulation)
