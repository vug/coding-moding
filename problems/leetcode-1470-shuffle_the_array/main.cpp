#include "utils.hpp"

#include <fmt/core.h>
#include <range/v3/range.hpp>
#include <range/v3/view.hpp>

#include <numeric>
// #include <ranges>
#include <vector>

std::vector<int> shuffle1(std::vector<int>& nums, int n) {
  std::vector<int> ans(nums.size());
  size_t ix = 0;   // running index for ans
  size_t ix1 = 0;  // running index for first section
  size_t ix2 = n;  // running index for second section
  for (size_t i = 0; i < n; ++i) {
    ans[ix++] = nums[ix1++];
    ans[ix++] = nums[ix2++];
  }
  return ans;
}

// Faster than 1 probably because less variable tracking?
std::vector<int> shuffle1b(std::vector<int>& nums, int n) {
  std::vector<int> ans(nums.size());
  for (size_t i = 0; i < n; ++i) {
    ans[2 * i]     = nums[i];
    ans[2 * i + 1] = nums[i + n];
  }
  return ans;
}

std::vector<int> shuffle1c(std::vector<int>& nums, int n) {
  std::vector<int> ans;
  ans.reserve(nums.size());
  for (size_t i = 0; i < n; ++i) {
    ans.push_back(nums[i]);
    ans.push_back(nums[i + n]);
  }
  return ans;
}

// not so fast
namespace vw = ranges::views;
std::vector<int> shuffle2(std::vector<int>& nums, int n) {
  std::vector<int> ans;
  ans.reserve(2 * n);
  for (auto [x, y] : vw::zip(vw::take(nums, n), vw::drop(nums, n))) {
    ans.push_back(x);
    ans.push_back(y);
  }
  return ans;
}

int main() {
  std::vector<int> inp(10'000);
  std::iota(inp.begin(), inp.end(), 0);
  Timer t;
  for (int i = 0; i < 10'000; ++i)
    shuffle1(inp, inp.size() / 2);
  float dur1 = t.timeSinceLastMs();
  for (int i = 0; i < 10'000; ++i)
    shuffle1b(inp, inp.size() / 2);
  float dur1b = t.timeSinceLastMs();
  for (int i = 0; i < 10'000; ++i)
    shuffle1c(inp, inp.size() / 2);
  float dur1c = t.timeSinceLastMs();
  for (int i = 0; i < 10'000; ++i)
    shuffle2(inp, inp.size() / 2);
  float dur2 = t.timeSinceLastMs();
  fmt::print("dur1 {} dur1b {} dur1c {} dur2 {}\n", dur1, dur1b, dur1c, dur2);
}