# Text justification

[Problem link](https://leetcode.com/problems/text-justification)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/text-justification

class Solution {
 public:
  vector<string> fullJustify(vector<string>& words, int maxWidth) {
    vector<string> ret;
    for (int i = 0, j = 0, w = words.size(); i < w; i = j) {
      int minlen = -1;
      for (j = i; j < w; ++j)
        if (minlen + 1 + words[j].size() > maxWidth)
          break;
        else
          minlen += 1 + words[j].size();

      ret.push_back({});
      for (int rem = (j == w) ? 0 : maxWidth - minlen; i < j; ++i) {
        ret.back() += words[i];
        if (i != j - 1) {
          int add = (rem + j - i - 2) / (j - 1 - i);
          ret.back() += string(add + 1, ' ');
          rem -= add;
        }
      }
      ret.back() += string(maxWidth - ret.back().size(), ' ');
    }
    return ret;
  }
};
```