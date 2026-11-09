class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start= count =0
        k%=n

        while count<n:
            current = start
            res= nums[start]
            while True:
                idx = (current +k)%n
                nums[idx], res=  res, nums[idx]
                current  =  idx
                count+=1
                if current==start:
                    break
            start+=1