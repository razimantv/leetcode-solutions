// https://leetcode.com/problems/incremental-memory-leak

class Solution {
 public:
  vector<int> memLeak(int memory1, int memory2) {
    for (int i = 1;; ++i) {
      int& x = (memory1 < memory2) ? memory2 : memory1;
      if (x < i) return {i, memory1, memory2};
      x -= i;
    }
  }
};
