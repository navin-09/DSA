class Solution:
    def left_shift(self,num):
        return num << 3
    def right_shift(self,num):
        return num >> 1

solution = Solution()
ls1 = solution.left_shift(5)
ls2 = solution.left_shift(ls1)
print(ls1,ls2)

rs1 = solution.right_shift(4)
rs2 = solution.right_shift(rs1)
print(rs1,rs2)

#  5 << 4 ==> 5* 2**4 
#  5 >> 4 ===> 5 // 2**4

