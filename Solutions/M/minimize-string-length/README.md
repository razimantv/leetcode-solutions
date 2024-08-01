# Minimize string length

[Problem link](https://leetcode.com/problems/minimize-string-length/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimize-string-length/

class Solution {
 public:
  int minimizedStringLength(string s) {
    unordered_set<char> ch(s.begin(), s.end());
    return ch.size();
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
