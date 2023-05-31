# Delete operation for two strings

[Problem link](https://leetcode.com/problems/delete-operation-for-two-strings)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/delete-operation-for-two-strings

class Solution {
 public:
  int minDistance(string word1, string word2) {
    int m = word1.size(), n = word2.size();
    vector<int> LCS(m + 1);
    for (int i = 0, temp, prev; i < n; ++i) {
      prev = 0;
      for (int j = 0; j < m; ++j) {
        if (word2[i] == word1[j])
          temp = prev + 1;
        else
          temp = max(LCS[j + 1], LCS[j]);
        prev = LCS[j + 1];
        LCS[j + 1] = temp;
      }
    }
    return m + n - 2 * LCS[m];
  }
};
```
## Tags

* [Dynamic programming](/README.md#Dynamic_programming) > [Longest common subsequence](/README.md#Dynamic_programming-Longest_common_subsequence)
* [Dynamic programming](/README.md#Dynamic_programming) > [Array reuse](/README.md#Dynamic_programming-Array_reuse)
