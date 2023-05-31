# Reverse words in a string

[Problem link](https://leetcode.com/problems/reverse-words-in-a-string)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/reverse-words-in-a-string

class Solution {
 public:
  string reverseWords(string s) {
    istringstream iss(s);
    vector<string> v;
    string temp;
    while (iss >> temp) v.push_back(temp);
    if (v.empty()) return "";
    temp = v.back();
    for (int i = v.size() - 1; i--;) temp += " " + v[i];
    return temp;
  }
};
```