# Determine if two strings are close

[Problem link](https://leetcode.com/problems/determine-if-two-strings-are-close)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/determine-if-two-strings-are-close

class Solution {
 public:
  pair<string, vector<int>> freq(const string& s) {
    unordered_map<char, int> cnt;
    for (char c : s) ++cnt[c];

    vector<int> f;
    string ss;
    for (auto [v, c] : cnt) ss += v, f.push_back(c);
    sort(f.begin(), f.end());
    sort(ss.begin(), ss.end());
    return {ss, f};
  }
  bool closeStrings(string word1, string word2) {
    return freq(word1) == freq(word2);
  }
};
```
### Solution.py
```py
# https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        return sorted(c1.keys()) == sorted(c2.keys()) and sorted(c1.values()) == sorted(c2.values())
```
## Tags

* [Counting elements in array](/Collections/counting-elements-in-array.md#counting-elements-in-array)
* [Hashmap](/Collections/hashmap.md#hashmap)
