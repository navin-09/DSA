class Equilibrium:
    def findEquilibriumIndex(self,arr):
        total_sum = sum(arr)
        left_sum = 0
        for i,num in enumerate(arr):
            right_sum = total_sum-left_sum-num
            if(left_sum == right_sum):
                return i
            left_sum += num
        return -1

        

equilibrium = Equilibrium()
result = equilibrium.findEquilibriumIndex([-7, 1, 5, 2, -4, 3, 0])
print(result)
