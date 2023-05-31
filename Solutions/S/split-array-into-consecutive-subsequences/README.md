# Split array into consecutive subsequences

[Problem link](https://leetcode.com/problems/split-array-into-consecutive-subsequences)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/split-array-into-consecutive-subsequences

class Solution {
 public:
  bool isPossible(vector<int>& nums) {
    map<int, int> cnt;
    for (int x : nums) ++cnt[x];

    map<int, int> seqs;
    for (int x : nums) {
      if (!cnt[x]) continue;
      if (seqs[x - 1])
        --seqs[x - 1], ++seqs[x], --cnt[x];
      else {
        if (!cnt[x + 1]-- or !cnt[x + 2]--) return false;
        ++seqs[x + 2], --cnt[x];
      }
    }
    return true;
  }
};
```