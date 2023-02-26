#pragma once

#include <chrono>

namespace ch = std::chrono;
class Timer
{
 private:
  ch::time_point<ch::steady_clock> initTime;
  ch::time_point<ch::steady_clock> lastTime;
 public:
  Timer() : 
    initTime(ch::steady_clock::now()), 
    lastTime(initTime) {}
  
  float timeSinceInitMs() const {
    const auto now = ch::steady_clock::now();
    return ch::duration_cast<ch::milliseconds>(now - initTime).count();
  }

  float timeSinceLastMs() {
    const auto now = ch::steady_clock::now();
    const auto result = ch::duration_cast<ch::milliseconds>(now - lastTime);
    lastTime = now;
    return result.count();
  }  
};