# Sentence similarity iii

[Problem link](https://leetcode.com/problems/sentence-similarity-iii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sentence-similarity-iii

class Solution {
 public:
  vector<string> convert(string &s) {
    istringstream iss(s);
    string cur;
    vector<string> v;
    while (iss >> cur) {
      v.push_back(cur);
    }
    return v;
  }
  bool areSentencesSimilar(string sentence1, string sentence2) {
    auto v1 = convert(sentence1), v2 = convert(sentence2);
    if (v1.size() > v2.size()) swap(v1, v2);

    while (!v1.empty() and v1.back() == v2.back()) v1.pop_back(), v2.pop_back();
    reverse(v1.begin(), v1.end());
    reverse(v2.begin(), v2.end());
    while (!v1.empty() and v1.back() == v2.back()) v1.pop_back(), v2.pop_back();

    return v1.empty();
  }
};
```