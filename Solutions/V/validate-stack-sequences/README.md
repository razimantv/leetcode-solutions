# Validate stack sequences

[Problem link](https://leetcode.com/problems/validate-stack-sequences)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/validate-stack-sequences

class Solution {
 public:
  bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
    stack<int> s;
    for (int i = 0, j = 0, n = pushed.size(); j < n; ++j) {
      while (i < n and (i <= j or s.top() != popped[j])) s.push(pushed[i++]);
      if (s.top() != popped[j]) return false;
      s.pop();
    }

    return true;
  }
};
```