# Circular sentence

[Problem link](https://leetcode.com/problems/circular-sentence/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/circular-sentence/

class Solution {
 public:
  bool isCircularSentence(string sentence) {
    istringstream iss(sentence);
    vector<string> vec;
    string temp;
    while (iss >> temp) vec.push_back(temp);
    for (int i = 0, n = vec.size(); i < n; ++i)
      if (vec[i].back() != vec[(i + 1) % n][0]) return false;
    return true;
  }
};
```
## Tags

* [String](/README.md#String) > [Parsing](/README.md#String-Parsing)
