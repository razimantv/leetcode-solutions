# Random pick with weight

[Problem link](https://leetcode.com/problems/random-pick-with-weight)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/random-pick-with-weight

class Solution {
 public:
  map<int, int> wmap;
  int tot;

  Solution(vector<int>& w) {
    tot = 0;
    for (int i = 0; i < w.size(); i++) {
      if (w[i] == 0) continue;
      wmap[tot += w[i]] = i;
    }
  }

  int pickIndex() { return wmap.lower_bound(rand() % tot + 1)->second; }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
```
## Tags

* [Design data structure](/README.md#Design_data_structure)
* [Mathematics](/README.md#Mathematics) > [Probability](/README.md#Mathematics-Probability)
* [Binary search](/README.md#Binary_search) > [Prefix sum](/README.md#Binary_search-Prefix_sum)
* [Binary search](/README.md#Binary_search) > [C++ set](/README.md#Binary_search-C___set)
* [Prefix](/README.md#Prefix) > [Sum](/README.md#Prefix-Sum)
