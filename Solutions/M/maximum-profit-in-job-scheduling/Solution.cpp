// https://leetcode.com/problems/maximum-profit-in-job-scheduling

class Solution {
 public:
  int jobScheduling(vector<int>& startTime, vector<int>& endTime,
                    vector<int>& profit) {
    startTime.push_back(0);
    endTime.push_back(0);
    profit.push_back(0);
    int N = startTime.size();

    vector<int> order(N);
    iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(),
         [&endTime](int i, int j) { return endTime[i] < endTime[j]; });

    endTime.push_back(0);
    for (int i = 1; i < N; ++i) {
      endTime.back() = startTime[order[i]];
      auto it = upper_bound(
          order.begin(), order.end() - 1, N,
          [&endTime](int i, int j) { return endTime[i] < endTime[j]; });
      profit[order[i]] =
          max(profit[order[i - 1]], profit[order[i]] + profit[*--it]);
    }
    return profit[order[N - 1]];
  }
};
