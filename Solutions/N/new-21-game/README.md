# New 21 game

[Problem link](https://leetcode.com/problems/new-21-game/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/new-21-game/

class Solution {
 public:
  double new21Game(int n, int k, int maxPts) {
    if (!k) return 1;
    // f(i) = sum_{j = i-k .. i-1} f(j) / maxPts
    vector<double> prob(n + 1), psum(n + 1);
    prob[0] = psum[0] = 1;
    for (int i = 1; i <= n; ++i) {
      int l = max(i - maxPts, 0), r = min(i - 1, k - 1);
      if (r >= l) prob[i] = (psum[r] - (l ? psum[l - 1] : 0)) / maxPts;
      psum[i] = psum[i - 1] + prob[i];
    }
    return psum[n] - psum[k - 1];
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Probability](/Collections/mathematics.md#probability)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
