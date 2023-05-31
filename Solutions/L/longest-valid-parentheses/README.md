# Longest valid parentheses

[Problem link](https://leetcode.com/problems/longest-valid-parentheses)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-valid-parentheses

class Solution {
 public:
  int longestValidParentheses(string s) {
    int best = 0;
    std::vector<std::pair<int, int>> pref{{0, -1}};
    for (int i = 0, n = s.size(), cur = 0; i < n; ++i) {
      if (s[i] == '(') {
        ++cur;
        pref.push_back({cur, i});
      } else {
        --cur;
        while (!pref.empty() and pref.back().first > cur) pref.pop_back();
        if (!pref.empty() and pref.back().first == cur)
          best = max(best, i - pref.back().second);
        else
          pref.push_back({cur, i});
      }
    }
    return best;
  }
};
```
## Tags

* [Prefix](/README.md#Prefix) > [Sum](/README.md#Prefix-Sum)
* [Stack](/README.md#Stack) > [From array elements](/README.md#Stack-From_array_elements)
