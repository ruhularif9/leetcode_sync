# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0  
        for num in nums:
            if i < 2 or num != nums[i-2]:
                nums[i] = num
                i += 1
        return i



        