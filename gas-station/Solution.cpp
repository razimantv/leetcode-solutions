// https://leetcode.com/problems/gas-station

class Solution {
 public:
  int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
    int N = gas.size(), worst = 0, id = -1, cum = 0;
    for (int i = 0; i < N; ++i) {
      if ((cum += gas[i] - cost[i]) < worst) worst = cum, id = i;
    }
    return (cum < 0) ? -1 : (id + 1);
  }
};
