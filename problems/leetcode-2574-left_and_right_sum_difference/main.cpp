#include "utils.hpp"

#include <fmt/core.h>

#include <algorithm>
#include <cstdlib>
#include <vector>

void printVector(const std::vector<int>& v) {
  for (int n : v)
    fmt::print("{} ", n);
  fmt::print("\n");
}

std::vector<int> leftRigthDifference1(std::vector<int>& nums) {
  std::vector<int> leftSum(nums.size());
  std::vector<int> rightSum(nums.size());
  std::vector<int> answer(nums.size());
  leftSum[0] = 0;
  rightSum[nums.size() - 1] = 0;
  for (int i = 1; i < nums.size(); ++i)
    leftSum[i] = leftSum[i - 1] + nums[i - 1];
  for (int i = nums.size() - 2; i > -1; --i)
    rightSum[i] = rightSum[i + 1] + nums[i + 1];
  for (int i = 0; i < nums.size(); ++i)
    answer[i] = abs(leftSum[i] - rightSum[i]);
  return answer;
}

std::vector<int> leftRigthDifference2(std::vector<int>& nums) {
  std::vector<int> ans;
  int leftSum{};
  int rightSum{};

  for (auto x : nums)
    rightSum += x;

  for (auto x : nums) {
    rightSum -= x;
    ans.push_back(abs(leftSum - rightSum));
    leftSum += x;
  }

  return ans;
}

std::vector<int> leftRigthDifference2b(std::vector<int>& nums) {
  std::vector<int> ans(nums.size(), 0);
  int leftSum{};
  int rightSum{};

  for (auto x : nums)
    rightSum += x;

  for (size_t i = 0; i < nums.size(); ++i) {
    rightSum -= nums[i];
    ans[i] = abs(leftSum - rightSum);
    leftSum += nums[i];
  }

  return ans;
}

int main() {
  std::vector<int> inp(1000, 1);
  Timer t;
  const int nCalc = 10'000;
  for (int i = 0; i < nCalc; ++i)
    leftRigthDifference1(inp);
  float dur1 = t.timeSinceLastMs();
  for (int i = 0; i < nCalc; ++i)
    leftRigthDifference2(inp);
  float dur2 = t.timeSinceLastMs();
  fmt::print("dur1 {}, dur2 {}\n", dur1, dur2);
  for (int i = 0; i < nCalc; ++i)
    leftRigthDifference2b(inp);
  float dur2b = t.timeSinceLastMs();
  fmt::print("dur1 {}, dur2 {}, dur2b {}\n", dur1, dur2, dur2b);
}