# Maximum profit in job scheduling

[Problem link](https://leetcode.com/problems/maximum-profit-in-job-scheduling)

## Solutions


### Solution.cpp
```cpp
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
```
## Tags

* [Sorting](/README.md#Sorting) > [Custom](/README.md#Sorting-Custom)
* [Intervals](/README.md#Intervals) > [DP with binary search](/README.md#Intervals-DP_with_binary_search)
* [Dynamic programming](/README.md#Dynamic_programming) > [Intervals](/README.md#Dynamic_programming-Intervals)
