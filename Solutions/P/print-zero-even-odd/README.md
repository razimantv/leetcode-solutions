# Print zero even odd

[Problem link](https://leetcode.com/problems/print-zero-even-odd)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/print-zero-even-odd

class ZeroEvenOdd {
 private:
  int n;
  mutex m;
  condition_variable cv;
  int status;

 public:
  ZeroEvenOdd(int n) {
    this->n = n;
    status = 0;
    cv.notify_all();
  }

  // printNumber(x) outputs "x", where x is an integer.
  void zero(function<void(int)> printNumber) {
    for (int i = 0; i < n; ++i) {
      {
        unique_lock<mutex> lk(m);
        cv.wait(lk, [&]() { return status == (i & 1) << 1; });
        printNumber(0);
        ++status;
      }
      cv.notify_all();
    }
  }

  void even(function<void(int)> printNumber) {
    for (int i = 2; i <= n; i += 2) {
      {
        unique_lock<mutex> lk(m);
        cv.wait(lk, [&]() { return status == 3; });
        printNumber(i);
        status = 0;
      }
      cv.notify_all();
    }
  }

  void odd(function<void(int)> printNumber) {
    for (int i = 1; i <= n; i += 2) {
      {
        unique_lock<mutex> lk(m);
        cv.wait(lk, [&]() { return status == 1; });
        printNumber(i);
        status = 2;
      }
      cv.notify_all();
    }
  }
};
```
## Tags

* [Concurrency](/Collections/concurrency.md#concurrency)
