# Repeated dna sequences

[Problem link](https://leetcode.com/problems/repeated-dna-sequences)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/repeated-dna-sequences

class Solution {
 public:
  vector<string> findRepeatedDnaSequences(string s) {
    unordered_map<string, int> rep;
    vector<string> ret;
    for (int i = 0, N = s.size(); i + 9 < N; ++i) {
      string cur = s.substr(i, 10);
      if (++rep[cur] == 2) ret.push_back(cur);
    }
    return ret;
  }
};
```