
# Recursively count the length of array


class Solution(object):
    def count(self, nums):
        """
        :type x: int
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        else:
            return 1 + self.count(nums[1:])


def main():
    nums = [2, 3, 5, 6, 7, 8, 9]
    print(Solution().count(nums))


if __name__ == "__main__":
    main()