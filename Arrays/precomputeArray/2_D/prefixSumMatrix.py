class PrefixSumMatrix:
    def prefix_sum_2d(self, matrix):
        row = len(matrix)
        col = len(matrix)

        prefixArray = [[0]*col for i in range(row)]
        
        for i in range(row):
            for j in range(col):
                top = prefixArray[i-1][j] if i>0 else 0
                left = prefixArray[i][j-1] if j>0 else 0
                diag = prefixArray[i-1][j-1] if i>0 and j>0 else 0
                prefixArray[i][j] = matrix[i][j]+top+left-diag

        return prefixArray
    
    def prefix_sum_2d_with_padding(self, matrix):
        rows, cols = len(matrix), len(matrix[0])

        # Create prefix array with +1 padding (row+1 x col+1)
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                top = prefix[i - 1][j]
                left = prefix[i][j - 1]
                diag =  prefix[i - 1][j - 1]
                prefix[i][j] = matrix[i - 1][j - 1] + top +left - diag
                     
        return prefix

   
    def submatrix_sum(self,mat, r1, c1, r2, c2):
        prefix = self.prefix_sum_2d_with_padding(mat)
        r1+=1
        c1+=1
        r2+=1
        c2+=1
        
        top = prefix[r1-1][c2] if r1 > 0 else 0
        left = prefix[r2][c1-1] if c1 > 0 else 0
        diag = prefix[r1-1][c1-1] if r1 > 0 and c1 > 0 else 0
        return prefix[r2][c2] - top - left + diag

    def sum_of_all_subarray_matrix(self,mat):
        row = len(mat)
        col = len(mat[0])

        total_sum = 0

        for i in range(row):
           for j in range(col):
               total_sum += mat[i][j]*(i+1)*(j+1)*(row-i)*(col-j)
        return total_sum
               
# Example matrix
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

prefixSumMatrix = PrefixSumMatrix()

pref = prefixSumMatrix.prefix_sum_2d(mat)
pref1 = prefixSumMatrix.prefix_sum_2d_with_padding(mat)
for row in pref:
    print(row)
for row in pref1:
    print(row)

total_subarray_sum = prefixSumMatrix.sum_of_all_subarray_matrix(mat)
print('total_subarray_sum:',total_subarray_sum)



print('submatrix_sum==>',prefixSumMatrix.submatrix_sum(mat, 1, 1, 2, 2))  # sum of [[5,6],[8,9]] = 28

