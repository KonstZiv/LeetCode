'''
Given an array nums of integers, return how many of them contain an even number of digits.
'''


def findNumbers(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return len([x for x in nums if len(str(x)) % 2 == 0])


if __name__ == '__main__':
    nums = [555, 901, 482, 1771]
    print(findNumbers(nums))
