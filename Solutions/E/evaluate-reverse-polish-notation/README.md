# Evaluate reverse polish notation

[Problem link](https://leetcode.com/problems/evaluate-reverse-polish-notation)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution {
 public:
  int evalRPN(vector<string>& tokens) {
    vector<int> v;
    for (const string& t : tokens) {
      if (t.size() > 1 or isdigit(t[0]))
        v.push_back(stoi(t));
      else {
        int op2 = v.back();
        v.pop_back();
        int op1 = v.back();
        v.pop_back();
        if (t == "+")
          v.push_back(op1 + op2);
        else if (t == "-")
          v.push_back(op1 - op2);
        else if (t == "*")
          v.push_back(op1 * op2);
        else if (t == "/")
          v.push_back(op1 / op2);
      }
    }
    return v[0];
  }
};
```
## Tags

* [Stack](/Collections/stack.md#stack) > [Numerical operations](/Collections/stack.md#numerical-operations)
