// https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

class Solution {
 public:
  int minIncrements(int n, vector<int>& cost) {
    int ret{};
    for (int rc = n - 1, lc = rc - 1, node = lc >> 1; node >= 0;
         --node, lc -= 2, rc -= 2) {
      ret += max(cost[lc], cost[rc]) - min(cost[lc], cost[rc]);
      cost[node] += max(cost[lc], cost[rc]);
    }
    return ret;
  }
};
