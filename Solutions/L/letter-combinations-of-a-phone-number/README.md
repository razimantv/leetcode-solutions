# Letter combinations of a phone number

[Problem link](https://leetcode.com/problems/letter-combinations-of-a-phone-number)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution {
 public:
  vector<string> letterCombinations(string digits) {
    if (digits.empty()) return {};
    vector<string> ret{""};
    vector<string> keys{"abc", "def",  "ghi", "jkl",
                        "mno", "pqrs", "tuv", "wxyz"};
    for (char c : digits) {
      vector<string> cur;
      for (const string& s : ret)
        for (char add : keys[c - '2']) cur.push_back(s + add);
      ret = cur;
    }
    return ret;
  }
};
```
## Tags

* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Elementwise processing using a vector](/Collections/brute-force-enumeration.md#elementwise-processing-using-a-vector)
