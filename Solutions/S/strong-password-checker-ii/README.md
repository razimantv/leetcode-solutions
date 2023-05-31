# Strong password checker ii

[Problem link](https://leetcode.com/problems/strong-password-checker-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/strong-password-checker-ii

class Solution {
 public:
  bool strongPasswordCheckerII(string password) {
    int n = password.size();
    if (n < 8) return false;

    string allowed = "!@#$%^&*()-+";
    unordered_set<char> ok;
    for (char c : allowed) ok.insert(c);

    bool upper = false, lower = false, digit = false, special = false;
    for (int i = 0; i < n; ++i) {
      if (i and password[i] == password[i - 1]) return false;
      if (isupper(password[i]))
        upper = true;
      else if (islower(password[i]))
        lower = true;
      else if (isdigit(password[i]))
        digit = true;
      else if (ok.count(password[i]))
        special = true;
      else
        return false;
    }
    return upper and lower and digit and special;
  }
};
```