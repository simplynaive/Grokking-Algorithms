
# Recursively add up an array


class Solution(object):
    def sum(self, nums):
        """
        :type x: int
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        else:
            return nums[0] + self.sum(nums[1:])


def main():
    nums = [2, 3, 5, 6]
    print(Solution().sum(nums))


if __name__ == "__main__":
    main()