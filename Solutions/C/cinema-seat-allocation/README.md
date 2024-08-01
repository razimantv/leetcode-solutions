# Cinema seat allocation

[Problem link](https://leetcode.com/problems/cinema-seat-allocation)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/cinema-seat-allocation

class Solution {
 public:
  int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {
    unordered_map<int, int> mask;
    for (const auto& v : reservedSeats) {
      int r = v[0], p = v[1];
      mask[r] |= (1 << (p - 1));
    }

    int ret = 2 * (n - mask.size());
    for (auto [k, v] : mask) {
      int m1 = 30, m2 = 120, m3 = 480;
      if (!(v & m1) and !(v & m3))
        ret += 2;
      else if (!(v & m1) or !(v & m2) or !(v & m3))
        ++ret;
    }
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Hashmap](/Collections/hashmap.md#hashmap)
