# Remove invalid parentheses

[Problem link](https://leetcode.com/problems/remove-invalid-parentheses)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/remove-invalid-parentheses

class Solution {
  string valid(const string& s, const vector<int>& par, int mask) {
    string ret;
    int pref = 0;
    for (int i = 0, j = 0; s[i]; ++i) {
      if (par[j] == i) {
        if (mask & (1 << (j++))) continue;
      }

      ret += s[i];
      if (s[i] == '(')
        ++pref;
      else if (s[i] == ')')
        if (--pref < 0) return "";
    }
    if (pref) return "";
    return ret;
  }

 public:
  vector<string> removeInvalidParentheses(string s) {
    vector<int> par;
    int L = s.size();
    for (int i = 0; i < L; ++i)
      if (!isalpha(s[i])) par.push_back(i);

    int M = par.size();
    par.push_back(L);

    vector<string> ret{""};
    int bestbits = L + 1;
    for (int i = 0; i < (1 << M); ++i) {
      int b = __builtin_popcount(i);
      if (b > bestbits) continue;

      auto str = valid(s, par, i);
      if (str.empty()) continue;
      if (b < bestbits) {
        bestbits = b;
        ret.clear();
      }
      ret.push_back(str);
    }

    sort(ret.begin(), ret.end());
    int l = 0;
    for (int i = 0; i < ret.size(); ++i) {
      if (!i or ret[i] != ret[i - 1]) ret[l++] = ret[i];
    }
    ret.erase(ret.begin() + l, ret.end());
    return ret;
  }
};
```
## Tags

* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Combinatorial](/Collections/brute-force-enumeration.md#combinatorial)
* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [Valid brackets](/Collections/prefix.md#valid-brackets)
