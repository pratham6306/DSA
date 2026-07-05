class Solution(object):
    def maxDigitRange(self, nums):
        ans = 0
        l = [int(max(str(x))) - int(min(str(x))) for x in nums]
        range = max(l)
        for i in nums:
            if int(max(str(i))) - int(min(str(i))) == range:
                ans += i
        return ans
        