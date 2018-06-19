
# Recursively find the maximum in an array


class Solution(object):
    def findMax(self, nums):
        """
        :type x: int
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]
        temp = self.findMax(nums[1:])
        return nums[0] if nums[0] > temp else temp


def main():
    nums = [2, 3, 5, 6, 7, 8, 9]
    print(Solution().findMax(nums))


if __name__ == "__main__":
    main()