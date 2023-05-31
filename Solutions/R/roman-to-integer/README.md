# Roman to integer

[Problem link](https://leetcode.com/problems/roman-to-integer)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/roman-to-integer

class Solution {
 public:
  int romanToInt(string s) {
    vector<pair<string, int>> conv = {
        {"M", 1000}, {"CM", 900}, {"D", 500}, {"CD", 400}, {"C", 100},
        {"XC", 90},  {"L", 50},   {"XL", 40}, {"X", 10},   {"IX", 9},
        {"V", 5},    {"IV", 4},   {"I", 1}};

    int ret = 0;
    for (int i = 0, N = s.size(); i < N;) {
      for (auto [str, val] : conv) {
        int n = str.size();
        if (s.substr(i, n) == str) {
          ret += val;
          i += n;
          break;
        }
      }
    }
    return ret;
  }
};
```