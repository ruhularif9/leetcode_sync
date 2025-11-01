class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0 

        for right in nums:
            if right != val:
                nums[left] = right
                left += 1

        return left 

        