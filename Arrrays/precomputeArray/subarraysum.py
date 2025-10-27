class Subarray:
    def total_subarray_sum_contribution_method(self, arr):
        total_sum = 0
        n = len(arr)
        for i in range(n):
            total_sum += arr[i]*(i+1)*(n-i)
        return total_sum
    
    def max_subarray_sum_kadens(self,arr):
        current_sum = arr[0]
        max_sum = arr[0]
        for i in arr:
            curr_sum = max(current_sum+i, i)
            max_sum = max(max_sum,curr_sum)

        return max_sum
    
    def max_subarray_sum_with_len_k_sliding_window(self,arr,k):
        sumk = sum(arr[:k])
        max_sum = 0
        j=0
        for i in range(k,len(arr)):
            sumk = sumk - arr[j] + arr[i] 
            max_sum = max(max_sum,sumk)
            j+=1
        return max_sum


subarray = Subarray()
total_subarray_sum = subarray.total_subarray_sum_contribution_method([1,2,3])
max_subarray_sum = subarray.max_subarray_sum_kadens([-1,2,-3,4,-5,6])
max_subarray_sum_len_k = subarray.max_subarray_sum_with_len_k_sliding_window([-1,2,-3,4,-5,6],3)
print({'total_subarray_sum':total_subarray_sum,'max_subarray_sum':max_subarray_sum,'max_subarray_sum_len_k':max_subarray_sum_len_k})