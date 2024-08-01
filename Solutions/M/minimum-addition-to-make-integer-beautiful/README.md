# Minimum addition to make integer beautiful

[Problem link](https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

class Solution {
 public:
  long long makeIntegerBeautiful(long long n, int target) {
    string s = to_string(n);

    int cnt{};
    for (char c : s) cnt += c - '0';
    if (cnt <= target) return 0;

    int L = s.size(), i{};
    long long pref{};
    for (int cur = 0; i < L; ++i) {
      cur += s[i] - '0';
      if (cur >= target) break;
      pref = pref * 10 + s[i] - '0';
    }

    ++pref;
    while (i++ < L) pref *= 10;
    return pref - n;
  }
};
```
## Tags

* [Number transformations based on mathematical rules](/Collections/number-transformations-based-on-mathematical-rules.md#number-transformations-based-on-mathematical-rules)
