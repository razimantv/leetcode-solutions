# Range module

[Problem link](https://leetcode.com/problems/range-module)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/range-module

typedef tuple<int, int, int> pvs;

class RangeModule {
 public:
  vector<pvs> prefix;
  RangeModule() {
    prefix.push_back({0, 0, 0});
    prefix.push_back({1'000'000'000, 0, 0});
  }

  void add(int pos) {
    pvs temp{pos, 0, 0};
    auto vit = lower_bound(prefix.begin(), prefix.end(), temp);
    auto [p, v, s] = *vit;
    if (p != pos) {
      auto [pp, pv, ps] = *(vit - 1);
      prefix.insert(vit, {pos, pv, ps + (pos - pp) * pv});
    }
  }

  void change(int l, int r, int v) {
    pvs temp{l, 0, 0};
    auto vl = lower_bound(prefix.begin(), prefix.end(), temp);
    std::get<1>(*vl) = v;
    temp = {r, 0, 0};
    auto vr = lower_bound(prefix.begin(), prefix.end(), temp);
    vr = prefix.erase(++vl, vr);
    while (vr != prefix.end()) {
      auto [pp, pv, ps] = *(vr - 1);
      std::get<2>(*vr) = ps + pv * (std::get<0>(*vr) - pp);
      ++vr;
    }
  }

  int get(int p) {
    pvs temp{p, 0, 0};
    auto vit = lower_bound(prefix.begin(), prefix.end(), temp);
    auto [pp, pv, ps] = *(--vit);
    return ps + pv * (p - pp);
  }

  void addRange(int left, int right) {
    add(left);
    add(right);
    change(left, right, 1);
  }

  bool queryRange(int left, int right) {
    return get(right) - get(left) == right - left;
  }

  void removeRange(int left, int right) {
    add(left);
    add(right);
    change(left, right, 0);
  }
};
```