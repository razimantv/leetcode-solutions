# Valid number

[Problem link](https://leetcode.com/problems/valid-number)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/valid-number

class Solution {
 public:
  pair<bool, int> getdecimal(const string& s, int pos) {
    if (s[pos] == '+' or s[pos] == '-') ++pos;
    bool seen = false, good = false;

    for (;;) {
      if (s[pos] == 0 or s[pos] == 'E' or s[pos] == 'e')
        return {good, pos};
      else if (s[pos] == '.') {
        if (seen)
          return {false, pos};
        else
          seen = ++pos;
      } else if (isdigit(s[pos]))
        good = ++pos;
      else
        return {false, pos};
    }
  }

  pair<bool, int> getint(const string& s, int pos) {
    if (!s[pos]) return {false, pos};
    if (s[pos] == '+' or s[pos] == '-') ++pos;

    bool flag = false;
    for (;;) {
      if (s[pos] == 0)
        return {flag, pos};
      else if (isdigit(s[pos]))
        flag = ++pos;
      else
        return {false, pos};
    }
  }
  bool isNumber(string s) {
    pair<bool, int> ret = getdecimal(s, 0);
    if (!ret.first) return false;
    if (!s[ret.second]) return true;

    if (s[ret.second] == 'e' or s[ret.second] == 'E') {
      ret = getint(s, ret.second + 1);
      if (!ret.first) return false;
      if (!s[ret.second]) return true;
    }

    return !s[ret.second];
  }
};
```