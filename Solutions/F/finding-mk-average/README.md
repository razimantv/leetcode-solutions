# Finding mk average

[Problem link](https://leetcode.com/problems/finding-mk-average)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/finding-mk-average

class MKAverage {
  deque<pair<int, int>> cur;
  set<pair<int, int>> small, large, rest;
  int s, m, k;
  long long tot;

 public:
  MKAverage(int m, int k) : s(0), m(m), k(k), tot(0ll) {}

  void addElement(int num) {
    cur.push_back({num, s++});
    if (s < m) return;
    if (s == m) {
      for (auto vp : cur) {
        small.insert(vp);
        if (small.size() <= k) continue;
        auto vp2 = *small.rbegin();
        small.erase(vp2);
        large.insert(vp2);
        if (large.size() <= k) continue;
        auto vp3 = *large.begin();
        large.erase(large.begin());
        rest.insert(vp3);
        tot += vp3.first;
      }
    } else {
      {
        auto vp = cur.back();
        small.insert(vp);
        auto vp2 = *small.rbegin();
        small.erase(vp2);
        large.insert(vp2);
        auto vp3 = *large.begin();
        large.erase(large.begin());
        rest.insert(vp3);
        tot += vp3.first;
      }
      {
        auto vp = cur.front();
        cur.pop_front();
        if (rest.count(vp)) {
          rest.erase(vp);
          tot -= vp.first;
        } else if (small.count(vp)) {
          small.erase(vp);
          auto vp2 = *rest.begin();
          rest.erase(rest.begin());
          tot -= vp2.first;
          small.insert(vp2);
        } else if (large.count(vp)) {
          large.erase(vp);
          auto vp2 = *rest.rbegin();
          rest.erase(vp2);
          tot -= vp2.first;
          large.insert(vp2);
        }
      }
    }
    // std::cout << "small:";
    // for (auto [v, p] : small) cout << " " << v;
    // std::cout << "large:";
    // for (auto [v, p] : large) cout << " " << v;
    // std::cout << "rest:";
    // for (auto [v, p] : rest) cout << " " << v;
    // std::cout << "\n";
  }

  int calculateMKAverage() {
    if (s < m) return -1;
    return tot / (m - 2 * k);
  }
};

```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue) > [K smallest/largest elements](/Collections/priority-queue.md#k-smallest-largest-elements) > [Transfer between the two](/Collections/priority-queue.md#transfer-between-the-two)
* [Averaging from total and count](/Collections/averaging-from-total-and-count.md#averaging-from-total-and-count)
