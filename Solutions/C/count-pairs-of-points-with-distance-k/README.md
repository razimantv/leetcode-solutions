# Count pairs of points with distance k

[Problem link](https://leetcode.com/problems/count-pairs-of-points-with-distance-k/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

class Solution {
 public:
  int countPairs(vector<vector<int>>& coordinates, int k) {
    unordered_map<long long, int> cnt;
    int ret{};
    for (auto xy : coordinates) {
      long long x = xy[0], y = xy[1];
      for (int i = 0; i <= k; ++i) {
        long long xyp = ((x ^ i) << 20) | (y ^ (k - i));
        ret += cnt[xyp];
      }
      ++cnt[(x << 20) | y];
    }
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Self-inverse property of xor](/Collections/bitwise-operation.md#self-inverse-property-of-xor)
