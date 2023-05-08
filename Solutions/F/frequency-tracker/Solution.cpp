// https://leetcode.com/problems/frequency-tracker/

class FrequencyTracker {
 public:
  unordered_map<int, int> cnt, fcnt;
  FrequencyTracker() {}

  void add(int number) {
    if (cnt[number]) --fcnt[cnt[number]];
    ++fcnt[++cnt[number]];
  }

  void deleteOne(int number) {
    if (cnt[number]) {
      --fcnt[cnt[number]];
      if (--cnt[number]) ++fcnt[cnt[number]];
    }
  }

  bool hasFrequency(int frequency) { return fcnt[frequency]; }
};
