# Find the punishment number of an integer

[Problem link](https://leetcode.com/problems/find-the-punishment-number-of-an-integer/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

class Solution {
 public:
  bool poss(string& s, int i, int target) {
    if (!s[i]) return !target;
    for (int pref{}; s[i]; ++i) {
      pref = pref * 10 + s[i] - '0';
      if (pref > target) break;
      if (poss(s, i + 1, target - pref)) return true;
    }
    return false;
  }
  int punishmentNumber(int n) {
    int ret{};
    for (int i = 1; i <= n; ++i) {
      auto s = to_string(i * i);
      if (poss(s, 0, i)) ret += i * i;
    }
    return ret;
  }
};
```
## Tags

* [Backtracking](/Collections/backtracking.md#backtracking)
