# Remove all occurrences of a substring

[Problem link](https://leetcode.com/problems/remove-all-occurrences-of-a-substring)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/remove-all-occurrences-of-a-substring

class Solution {
 public:
  string removeOccurrences(string s, string part) {
    int p = part.size();
    while (1) {
      auto cur = s.find(part);
      if (cur == std::string::npos) return s;
      s = s.substr(0, cur) + s.substr(cur + p);
    };
    return s;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
