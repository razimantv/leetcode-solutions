# Unique morse code words

[Problem link](https://leetcode.com/problems/unique-morse-code-words)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/unique-morse-code-words

class Solution {
 public:
  int uniqueMorseRepresentations(vector<string>& words) {
    vector<string> morse{".-",   "-...", "-.-.", "-..",  ".",    "..-.", "--.",
                         "....", "..",   ".---", "-.-",  ".-..", "--",   "-.",
                         "---",  ".--.", "--.-", ".-.",  "...",  "-",    "..-",
                         "...-", ".--",  "-..-", "-.--", "--.."};
    unordered_set<string> seen;
    for (const string& s : words) {
      string cur;
      for (char c : s) cur += morse[c - 'a'];
      seen.insert(cur);
    }
    return seen.size();
  }
};
```