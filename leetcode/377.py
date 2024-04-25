from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
                    print(dp, i , num)

        return dp[target]


if __name__ == '__main__':
    # print(Solution().combinationSum4(nums = [1,2,3], target = 4))
    print(Solution().combinationSum4(nums = [4,2,1], target = 32))
