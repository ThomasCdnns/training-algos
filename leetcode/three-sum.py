class Solution:
    def threeSum(self, nums):
        hashmapMain = {}
        hashmapCopy = {}
        nums.sort()
        N, answers = len(nums), []
        for k in range(N):
            if nums[k] in hashmapMain:
                hashmapMain[nums[k]] += 1
            else:
                hashmapMain[nums[k]] = 1
        for i in range(N-2):
            for j in range(i+1, len(nums)-1):
                hashmapCopy = hashmapMain.copy()
                hashmapCopy[nums[i]] -= 1
                hashmapCopy[nums[j]] -= 1
                subTarget = 0 - (nums[i] + nums[j])
                if (subTarget in hashmapCopy) and (hashmapCopy[subTarget] > 0):
                    result = [nums[i], nums[j], subTarget]
                    result.sort()
                    if result not in answers:
                        answers.append(result)
        return answers


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            j, k = i+1, N-1
            while j < k:
                if nums[j]+nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j = j+1
                    while j < k and nums[j] == nums[j-1]:
                        j = j+1
                elif nums[j] + nums[k] < target:
                    j = j+1
                else:
                    k = k-1
        return result
