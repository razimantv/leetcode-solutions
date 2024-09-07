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

```
## Tags

* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Probability](/Collections/mathematics.md#probability)
* [Binary search](/Collections/binary-search.md#binary-search) > [Prefix sum](/Collections/binary-search.md#prefix-sum)
* [Binary search](/Collections/binary-search.md#binary-search) > [C++ set](/Collections/binary-search.md#c---set)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
