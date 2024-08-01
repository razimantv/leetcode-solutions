# Print foobar alternately

[Problem link](https://leetcode.com/problems/print-foobar-alternately)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/print-foobar-alternately

class FooBar {
 private:
  int n;

 public:
  static condition_variable cv1, cv2;
  static mutex m1, m2;
  static bool stat1, stat2;
  FooBar(int n) { this->n = n; }

  void foo(function<void()> printFoo) {
    for (int i = 0; i < n; i++) {
      // printFoo() outputs "foo". Do not change or remove this line.
      if (i) {
        unique_lock<mutex> lk(m1);
        cv1.wait(lk, [] { return stat1; });
        stat1 = false;
      }
      printFoo();
      {
        lock_guard<mutex> lk(m2);
        stat2 = true;
      }
      cv2.notify_one();
    }
  }

  void bar(function<void()> printBar) {
    for (int i = 0; i < n; i++) {
      // printBar() outputs "bar". Do not change or remove this line.
      {
        unique_lock<mutex> lk(m2);
        cv2.wait(lk, [] { return stat2; });
        stat2 = false;
      }
      printBar();
      if (i < n - 1) {
        {
          lock_guard<mutex> lk(m1);
          stat1 = true;
        }
        cv1.notify_one();
      }
    }
  }
};

condition_variable FooBar::cv1;
condition_variable FooBar::cv2;
mutex FooBar::m1;
mutex FooBar::m2;
bool FooBar::stat1 = false;
bool FooBar::stat2 = false;
```
## Tags

* [Concurrency](/Collections/concurrency.md#concurrency)
