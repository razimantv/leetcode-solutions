# Valid parentheses

[Problem link](https://leetcode.com/problems/valid-parentheses)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/valid-parentheses

class Solution {
 public:
  bool isValid(string s) {
    map<char, char> match{{')', '('}, {']', '['}, {'}', '{'}};
    stack<char> cur;
    for (char c : s) {
      if (!match.count(c))
        cur.push(c);
      else if (cur.empty() or cur.top() != match[c])
        return false;
      else
        cur.pop();
    }
    return cur.empty();
  }
};
```