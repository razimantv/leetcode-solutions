// https://leetcode.com/problems/number-of-recent-calls

class RecentCounter {
  queue<int> q;

 public:
  RecentCounter() {}

  int ping(int t) {
    q.push(t);
    while (!q.empty()) {
      int f = q.front();
      if (t - f > 3000)
        q.pop();
      else
        break;
    }
    return q.size();
  }
};

