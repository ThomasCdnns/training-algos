class Solution:
    def threeSum(self, nums):
        answers = []
        hashmapMain = {}
        hashmapCopy = {}
        nums.sort()
        if len(nums)>=3:
            for k in range(len(nums)):
                if nums[k] in hashmapMain:
                    hashmapMain[nums[k]] += 1
                else:
                    hashmapMain[nums[k]] = 1
            for i in range(len(nums)-2):
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