// https://leetcode.com/problems/maximum-number-of-robots-within-budget/

class Solution {
 public:
  int maximumRobots(vector<int>& chargingTimes, vector<int>& runningCosts,
                    long long budget) {
    int n = chargingTimes.size(), best = 0;
    long long tot = 0;
    deque<pair<int, int>> dq;
    for (int i = 0, l = 0; i < n; ++i) {
      tot += runningCosts[i];
      while (!dq.empty() and dq.back().first <= chargingTimes[i]) dq.pop_back();
      dq.push_back({chargingTimes[i], i});
      if (!dq.empty() and (i - l + 1) * tot + dq.front().first > budget) {
        tot -= runningCosts[l];
        if (dq.front().second == l++) dq.pop_front();
      }
      best = max(best, i - l + 1);
    }
    return best;
  }
};
