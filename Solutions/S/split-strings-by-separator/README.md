# Split strings by separator

[Problem link](https://leetcode.com/problems/split-strings-by-separator/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/split-strings-by-separator/

class Solution {
 public:
  vector<string> splitWordsBySeparator(vector<string>& words, char separator) {
    vector<string> ret;
    for (const auto& w : words) {
      if (ret.empty() or !ret.back().empty()) ret.push_back("");
      for (char c : w) {
        if (c == separator) {
          if (!ret.back().empty()) ret.push_back("");
        } else
          ret.back().push_back(c);
      }
    }
    if (ret.back().empty()) ret.pop_back();
    return ret;
  }
};
```
## Tags

* [String](/Collections/string.md#string) > [Parsing](/Collections/string.md#parsing)
