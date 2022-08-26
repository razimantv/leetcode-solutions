// https://leetcode.com/problems/maximize-distance-to-closest-person

class Solution {
 public:
  int maxDistToClosest(vector<int>& seats) {
    int N = seats.size();
    for (int i = 0, last = -1; i < N; ++i) {
      if (seats[i])
        last = i;
      else if (last == -1)
        seats[i] = -50000;
      else
        seats[i] = last - i;
    }

    int best = 0;
    for (int i = N - 1, last = N; i >= 0; --i) {
      if (seats[i] > 0)
        last = i;
      else if (last == N)
        best = max(best, -seats[i]);
      else
        best = max(best, min(-seats[i], last - i));
    }
    return best;
  }
};
