// https://leetcode.com/problems/maximum-frequency-stack

class FreqStack {
 public:
  unordered_map<int, int> freq;
  set<tuple<int, int, int>, greater<tuple<int, int, int>>> best;
  int i;

  FreqStack() {}

  void push(int x) { best.insert({++freq[x], ++i, x}); }

  int pop() {
    auto [f, p, v] = *best.begin();
    best.erase(best.begin());
    --freq[v];
    return v;
  }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 */
