# Array of doubled pairs

[Problem link](https://leetcode.com/problems/array-of-doubled-pairs)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/array-of-doubled-pairs

class Solution {
 public:
  bool canReorderDoubled(vector<int>& arr) {
    auto comp = [](int a, int b) {
      return (abs(a) == abs(b)) ? (a < b) : (abs(a) < abs(b));
    };
    map<int, int, decltype(comp)> cnt(comp);

    for (auto x : arr) ++cnt[x];
    for (auto& [x, c] : cnt) {
      while (c) {
        --c;
        if (--cnt[x * 2] < 0) return false;
      }
    }
    return true;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
* [Hashmap](/Collections/hashmap.md#hashmap)
