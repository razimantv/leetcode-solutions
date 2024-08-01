# String compression ii

[Problem link](https://leetcode.com/problems/string-compression-ii/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/string-compression-ii/

class Solution {
 public:
  inline int mask(int c, int cnt, int k) {
    return ((c - 'a') << 14) | (cnt << 7) | k;
  }
  inline tuple<int, int, int> unmask(int m) {
    return {(m >> 14) + 'a', (m >> 7) & 127, m & 127};
  }
  void put(unordered_map<int, int>& m, int key, int val) {
    if (m.count(key))
      m[key] = min(m[key], val);
    else
      m[key] = val;
  }
  int getLengthOfOptimalCompression(string s, int K) {
    unordered_map<int, int> dp{{mask(26 + 'a', 1, 0), 0}};
    for (char c : s) {
      unordered_map<int, int> newdp;
      for (auto& [key, v] : dp) {
        auto [prevc, cnt, k] = unmask(key);
        if (k < K) put(newdp, mask(prevc, cnt, k + 1), v);
        if (c == prevc) {
          ++cnt;
          int add = (cnt == 2 or cnt == 10 or cnt == 100);
          put(newdp, mask(c, cnt, k), v + add);
        } else
          put(newdp, mask(c, 1, k), v + 1);
      }
      dp = newdp;
    }

    int best = 100;
    for (auto& [k, v] : dp) best = min(best, v);
    return best;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Partial bottom-up](/Collections/dynamic-programming.md#partial-bottom-up)
