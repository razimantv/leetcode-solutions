# Rabbits in forest

[Problem link](https://leetcode.com/problems/rabbits-in-forest)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/rabbits-in-forest

class Solution {
 public:
  int numRabbits(vector<int>& answers) {
    unordered_map<int, int> cnt;
    for (int x : answers) ++cnt[x];
    int ret = 0;
    for (auto [c, n] : cnt) {
      ret += (c + 1) * (n / (c + 1) + (n % (c + 1) > 0));
    }
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
