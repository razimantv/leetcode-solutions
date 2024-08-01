# Jewels and stones

[Problem link](https://leetcode.com/problems/jewels-and-stones)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/jewels-and-stones

class Solution {
 public:
  int numJewelsInStones(string J, string S) {
    char seen[256] = {0};
    for (auto c : J) seen[c] = 1;

    int tot = 0;
    for (auto c : S)
      if (seen[c]) tot++;
    return tot;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
