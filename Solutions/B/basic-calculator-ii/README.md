# Basic calculator ii

[Problem link](https://leetcode.com/problems/basic-calculator-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/basic-calculator-ii

class Solution {
 public:
  int getn(const string &s, int &i) {
    int ret = 0;
    while (s[i] == ' ') ++i;
    while (isdigit(s[i])) ret = ret * 10 + (s[i++] - '0');
    return ret;
  }
  int calculate(string s) {
    vector<int> s1;
    vector<char> s2;
    for (int i = 0; s[i];) {
      s1.push_back(getn(s, i));
      if (!s2.empty()) {
        if (s2.back() == '*') {
          int cur = s1.back();
          s1.pop_back();
          s1.back() *= cur;
          s2.pop_back();
        } else if (s2.back() == '/') {
          int cur = s1.back();
          s1.pop_back();
          s1.back() /= cur;
          s2.pop_back();
        }
      }
      while (s[i] and (s[i] == ' ')) ++i;
      if (s[i])
        s2.push_back(s[i++]);
      else
        break;
    }
    int ret = s1[0];
    for (int i = 0; i < s2.size(); ++i) {
      if (s2[i] == '+')
        ret += s1[i + 1];
      else
        ret -= s1[i + 1];
    }
    return ret;
  }
};
```
## Tags

* [Stack](/Collections/stack.md#stack) > [Numerical operations](/Collections/stack.md#numerical-operations)
* [String](/Collections/string.md#string) > [Parsing](/Collections/string.md#parsing)
