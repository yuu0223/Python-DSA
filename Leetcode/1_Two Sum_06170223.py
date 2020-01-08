class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(0,len(nums)):
            for a in range(i+1,len(nums)):
             
                    if nums[i] + nums[a] == target:
                
                        return i,a
