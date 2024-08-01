# Ambiguous coordinates

[Problem link](https://leetcode.com/problems/ambiguous-coordinates)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/ambiguous-coordinates

class Solution {
 public:
  bool goodint(const string& s) { return s[1] == 0 or s[0] > '0'; }

  bool goodfrac(const string& s) { return s.back() > '0'; }

  vector<string> getvalid(const string& s) {
    int L = s.size();
    vector<string> ret;
    if (goodint(s)) ret.push_back(s);
    for (int i = 1; i < L; ++i) {
      auto left = s.substr(0, i), right = s.substr(i);
      if (goodint(left) and goodfrac(right)) ret.push_back(left + "." + right);
    }
    return ret;
  }

  vector<string> ambiguousCoordinates(string s) {
    int L = s.size() - 2;
    vector<string> ret;
    for (int i = 1; i < L; ++i) {
      auto xvec = getvalid(s.substr(1, i));
      auto yvec = getvalid(s.substr(1 + i, L - i));
      for (auto x : xvec)
        for (auto y : yvec) ret.push_back("(" + x + ", " + y + ")");
    }
    return ret;
  }
};
```
## Tags

* [String](/Collections/string.md#string) > [Validation](/Collections/string.md#validation)
