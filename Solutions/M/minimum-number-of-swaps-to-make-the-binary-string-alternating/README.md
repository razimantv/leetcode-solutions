# Minimum number of swaps to make the binary string alternating

[Problem link](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating

class Solution {
 public:
  int minSwaps(string s) {
    int cnt[2] = {0};
    for (char c : s) ++cnt[c - '0'];

    if (max(cnt[0], cnt[1]) - min(cnt[0], cnt[1]) > 1) return -1;

    int best = 1'000'000;
    for (char c = '0'; c <= '1'; ++c) {
      int cur = 0;
      if (cnt[c - '0'] < cnt['1' - c]) continue;
      for (int i = 0, n = s.size(); i < n; ++i) {
        char cc = c ^ (i & 1);
        if (cc != s[i]) ++cur;
      }
      best = min(best, cur);
    }
    return best / 2;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
