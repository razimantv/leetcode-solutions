# Score of parentheses

[Problem link](https://leetcode.com/problems/score-of-parentheses)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/score-of-parentheses

class Solution {
 public:
  int scoreOfParentheses(string S) {
    vector<vector<int>> pref{{}};
    for (char c : S) {
      if (c == '(') {
        pref.back().push_back(0);
        pref.push_back({});
      } else if (pref.back().empty()) {
        pref.pop_back();
        ++pref.back().back();
      } else {
        int cur = accumulate(pref.back().begin(), pref.back().end(), 0);
        pref.pop_back();
        pref.back().back() += 2 * cur;
      }
    }
    return accumulate(pref.back().begin(), pref.back().end(), 0);
  }
};
```