#include <chrono>
#include <iostream>
#include <numeric>
#include <vector>

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

std::vector<int> getConcatenation1(std::vector<int> &nums)
{
  const size_t n = nums.size();
  std::vector<int> ans(2 * n);
  for (size_t i = 0; i < n; ++i)
    ans[i] = ans[i + n] = nums[i];
  return ans;
}

std::vector<int> getConcatenation1b(std::vector<int> &nums)
{
  const size_t n = nums.size();
  std::vector<int> ans(2 * n);
  for (size_t i = 0; i < n; ++i) {
    ans[i] = nums[i];
    ans[i + n] = nums[i];    
  }
  return ans;
}

std::vector<int> getConcatenation2(std::vector<int> &nums)
{
  const size_t n = nums.size();
  std::vector<int> ans(nums);
  ans.resize(2 * n);
  for (size_t i = 0; i < n; ++i)
    ans[i + n] = nums[i];
  return ans;
}

std::vector<int> getConcatenation2b(std::vector<int> &nums)
{
  const size_t n = nums.size();
  std::vector<int> ans;
  ans.resize(2 * n);
  for (size_t i = 0; i < n; ++i)
    ans[i] = ans[i + n] = nums[i];
  return ans;
}

std::vector<int> getConcatenation3(std::vector<int> &nums)
{
  const size_t n = nums.size();
  std::vector<int> ans(nums);
  ans.reserve(2 * n);
  for (int x : nums)
    ans.push_back(x);
  return ans;
}

std::vector<int> getConcatenation4(std::vector<int> &nums)
{
  const size_t n = nums.size();
  std::vector<int> ans(nums);
  ans.reserve(2 * n);
  for (int x : nums)
    ans.push_back(x);
  return ans;
}

std::vector<int> getConcatenation4b(std::vector<int> &nums)
{
  const size_t n = nums.size();
  std::vector<int> ans;
  ans.reserve(2 * n);
  for (int x : nums)
    ans.push_back(x);
  for (int x : nums)
    ans.push_back(x);
  return ans;
}

std::vector<int> getConcatenation5(std::vector<int> &nums)
{
  const size_t n = nums.size();
  std::vector<int> ans;
  ans.insert(ans.end(), nums.begin(), nums.end());
  ans.insert(ans.end(), nums.begin(), nums.end());
  return ans;
}

std::vector<int> getConcatenation5b(std::vector<int> &nums)
{
  const size_t n = nums.size();
  std::vector<int> ans;
  ans.reserve(2 * n);
  ans.insert(ans.end(), nums.begin(), nums.end());
  ans.insert(ans.end(), nums.begin(), nums.end());
  // is there a ranges::insert?
  return ans;
}

std::vector<int> getConcatenation5c(std::vector<int> &nums)
{
  const size_t n = nums.size();
  std::vector<int> ans(nums);
  ans.reserve(2 * n);
  ans.insert(ans.end(), nums.begin(), nums.end());
  return ans;
}

std::vector<int> getConcatenation6(std::vector<int> &nums)
{
  const size_t n = nums.size();
  std::vector<int> ans;
  ans.reserve(2 * n);
  std::copy(nums.begin(), nums.end(), std::back_inserter(ans));
  std::copy(nums.begin(), nums.end(), std::back_inserter(ans));
  return ans;
}

int main()
{
  std::vector<int> inp(10'000'000);
  // std::ranges::iota(inp, 0);
  std::iota(inp.begin(), inp.end(), 0);
  Timer t;
  getConcatenation1(inp);
  const float dur1 = t.timeSinceLastMs();
  getConcatenation1b(inp);
  const float dur1b = t.timeSinceLastMs();
  getConcatenation2(inp);
  const float dur2 = t.timeSinceLastMs();
  getConcatenation2b(inp);
  const float dur2b = t.timeSinceLastMs();
  getConcatenation3(inp);
  const float dur3 = t.timeSinceLastMs();
  getConcatenation4(inp);
  const float dur4 = t.timeSinceLastMs();
  getConcatenation4b(inp);
  const float dur4b = t.timeSinceLastMs();
  getConcatenation5(inp);
  const float dur5 = t.timeSinceLastMs();
  getConcatenation5b(inp);
  const float dur5b = t.timeSinceLastMs();
  getConcatenation5c(inp);
  const float dur5c = t.timeSinceLastMs();
  getConcatenation6(inp);
  const float dur6 = t.timeSinceLastMs();
  std::cout << dur1 << ' ' << dur1b << ' ' << dur2 << ' ' << dur2b <<  ' ' << dur3 << ' ' << dur4 << ' ' << dur4b << ' ' << dur5 << ' ' << dur5b << ' ' << dur5c << ' ' << dur6 << '\n';
  return 0;
}
