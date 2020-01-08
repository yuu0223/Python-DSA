class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        
        repeat_num = 0
        missing_num = 0
        
        new=[x for x in range(1,len(nums)+1)]
        
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                repeat_num = nums[i]
                
        missing = list(set(new)-set(nums)) #set用差集合取得missing值
        
        for a in range(0,len(missing)):
            missing_num = missing[a]
            
        return repeat_num,missing_num
