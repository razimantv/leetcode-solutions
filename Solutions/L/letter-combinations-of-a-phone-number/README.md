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

* [Brute force enumeration](/README.md#Brute_force_enumeration) > [Elementwise processing using a vector](/README.md#Brute_force_enumeration-Elementwise_processing_using_a_vector)
