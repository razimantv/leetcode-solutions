# Isomorphic strings

[Problem link](https://leetcode.com/problems/isomorphic-strings)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/isomorphic-strings

class Solution {
 public:
  bool isIsomorphic(string s, string t) {
    unordered_map<char, char> fwmap, bwmap;
    for (int i = 0, n = s.size(); i < n; ++i) {
      char a = s[i], b = t[i];
      if ((fwmap.count(a) and fwmap[a] != b) or
          (bwmap.count(b) and bwmap[b] != a))
        return false;
      fwmap[bwmap[b] = a] = b;
    }
    return true;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Forward and backward](/Collections/hashmap.md#forward-and-backward)
