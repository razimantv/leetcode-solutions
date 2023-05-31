# Replace all digits with characters

[Problem link](https://leetcode.com/problems/replace-all-digits-with-characters)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/replace-all-digits-with-characters

class Solution {
 public:
  string replaceDigits(string s) {
    int N = s.size();
    for (int i = 1; i < N; i += 2) {
      s[i] += s[i - 1] - '0';
    }
    return s;
  }
};
```