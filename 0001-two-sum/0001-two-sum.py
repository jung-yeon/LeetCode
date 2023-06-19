class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer=[]
        for i in range(0, len(nums)):
            sum = 0
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    answer.append(i)
                    answer.append(j)
        return answer
