# Using a robot to print the lexicographically smallest string

[Problem link](https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

class Solution {
 public:
  string robotWithString(string s) {
    string right = s;
    int n = s.size();
    for (int i = n - 2; i >= 0; --i) right[i] = min(right[i], right[i + 1]);

    string t, ret;
    for (int i = 0; i < n; ++i) {
      while (!t.empty() and t.back() <= right[i]) {
        ret.push_back(t.back());
        t.pop_back();
      }
      t.push_back(s[i]);
    }
    while (!t.empty()) {
      ret.push_back(t.back());
      t.pop_back();
    }
    return ret;
  }
};
```
## Tags

* [Stack](/README.md#Stack) > [From array elements](/README.md#Stack-From_array_elements)
* [Array scanning](/README.md#Array_scanning) > [Right to left](/README.md#Array_scanning-Right_to_left)
* [Prefix](/README.md#Prefix) > [Extremum](/README.md#Prefix-Extremum)
