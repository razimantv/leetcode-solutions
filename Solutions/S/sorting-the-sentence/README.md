# Sorting the sentence

[Problem link](https://leetcode.com/problems/sorting-the-sentence)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sorting-the-sentence

class Solution {
 public:
  string sortSentence(string s) {
    vector<string> v(10);
    istringstream iss(s);

    string t;
    while (iss >> t) {
      int l = t.size();
      v[t[l - 1] - '0'] = t.substr(0, l - 1);
    }

    string ret;
    for (string x : v) {
      if (x.empty()) continue;
      if (!ret.empty()) ret += " ";
      ret += x;
    }
    return ret;
  }
};
```