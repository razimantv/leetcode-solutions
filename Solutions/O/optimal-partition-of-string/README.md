# Optimal partition of string

[Problem link](https://leetcode.com/problems/optimal-partition-of-string/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/optimal-partition-of-string/

class Solution {
 public:
  int partitionString(string s) {
    int ret = 1;
    unordered_set<char> seen;
    for (char c : s) {
      if (seen.count(c)) {
        ++ret;
        seen.clear();
      }
      seen.insert(c);
    }
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Unique elements in subarray](/Collections/unique-elements-in-subarray.md#unique-elements-in-subarray)
