class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[0:n]
        y = nums[n:]
        for i in range(int(len(nums)/2)):
            nums[2*i] = x[i]
            nums[2*i+1] = y[i]
        return nums
