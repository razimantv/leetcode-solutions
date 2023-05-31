# Unique email addresses

[Problem link](https://leetcode.com/problems/unique-email-addresses)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/unique-email-addresses

class Solution {
 public:
  int numUniqueEmails(vector<string>& emails) {
    unordered_set<string> ss;
    for (string& s : emails) {
      string cur;
      for (int i = 0, right = 0, plus = 0; s[i]; ++i) {
        if (s[i] == '@') right = 1;
        if (right)
          cur += s[i];
        else if (plus or s[i] == '.')
          continue;
        else if (s[i] == '+')
          plus = 1;
        else
          cur += s[i];
      }
      ss.insert(cur);
    }
    return ss.size();
  }
};
```