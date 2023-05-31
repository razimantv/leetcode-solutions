# Wildcard matching

[Problem link](https://leetcode.com/problems/wildcard-matching)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/wildcard-matching

class Solution {
 public:
  bool isMatch(string s, string p) {
    int L = s.size();
    vector<char> poss(L + 1), pref(L + 1, 1);

    poss[0] = 1;
    for (char c : p) {
      for (int i = L; i >= 0; --i)
        poss[i] = (c == '*') ? pref[i]
                             : ((i > 0) and (c == '?' or c == s[i - 1]) and
                                poss[i - 1]);

      pref[0] = poss[0];
      for (int i = 1; i <= L; ++i) pref[i] = pref[i - 1] or poss[i];
    }
    return poss[L];
  }
};
```