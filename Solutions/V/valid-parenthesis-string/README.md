# Valid parenthesis string

[Problem link](https://leetcode.com/problems/valid-parenthesis-string)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/valid-parenthesis-string

class Solution {
 public:
  map<pair<int, int>, bool> memo;
  bool check(const string &s, int l, int r) {
    if (l > r) return true;
    if (s[l] == ')' or s[r] == '(') return false;
    if (l == r) return true;

    if (memo.count({l, r})) return memo[{l, r}];
    for (int m = l; m < r; m++)
      if (check(s, l, m) and check(s, m + 1, r)) return memo[{l, r}] = true;
    return memo[{l, r}] = check(s, l + 1, r - 1);
  }
  bool checkValidString(string s) { return check(s, 0, s.size() - 1); }
};
```