class Solution:
    def maximumProduct(self, nums):
        
        n = len(nums)
        max1, max2, max3 = -float('inf'), -float('inf'), -float('inf')
        min1, min2 = float('inf'), float('inf')
        
        for num in nums:
            if num>max1:
                max3, max2, max1 = max2, max1, num
            elif num>max2:
                max2, max3 = num, max2
            elif num>max3:
                max3 = num
            
            if num<min1:
                min1, min2 = num, min1
            elif num<min2:
                min2 = num
        
        return max(min1*min2*max1, max1*max2*max3)
    