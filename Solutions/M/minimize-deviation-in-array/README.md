# Minimize deviation in array

[Problem link](https://leetcode.com/problems/minimize-deviation-in-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimize-deviation-in-array

class Solution {
 public:
  int minimumDeviation(vector<int>& nums) {
    set<pair<int, int>> cur;

    int R = 0;
    for (int n : nums) {
      int l, r;
      if (n & 1)
        l = n, r = n << 1;
      else {
        r = l = n;
        while ((l & 1) == 0) l >>= 1;
      }
      R = max(R, l);
      cur.insert({l, r});
    }

    int best = R - cur.begin()->first;
    while (!cur.empty()) {
      auto [l, r] = *cur.begin();
      cur.erase(cur.begin());
      best = min(best, R - l);
      if (l == r) break;
      R = max(R, l <<= 1);
      cur.insert({l, r});
    }
    return best;
  }
};
```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue)
