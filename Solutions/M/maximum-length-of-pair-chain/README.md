# Maximum length of pair chain

[Problem link](https://leetcode.com/problems/maximum-length-of-pair-chain/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-length-of-pair-chain/

class Solution {
 public:
  // ChatGPT solution
  int findLongestChain(vector<vector<int>>& pairs) {
    sort(pairs.begin(), pairs.end(),
         [](const vector<int>& p1, const vector<int>& p2) {
           return p1[1] < p2[1];
         });

    int longestChain = 1;
    int end = pairs[0][1];

    for (int i = 1; i < pairs.size(); ++i) {
      if (pairs[i][0] > end) {
        longestChain++;
        end = pairs[i][1];
      }
    }

    return longestChain;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
