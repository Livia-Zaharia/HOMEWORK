matrix=[[2,5,6,7],[2,4,8,9],[6,7,5,9],[3,2,1,4]]
# sum of all even no
# sum of all odd numbers
# sum of all no under the main diagonal
# sum of all numbers over the second diagonal
# mean of numbers on the main and second diagonal

sum_even=0
sum_odd=0

for i in range (len(matrix)):
    for j in range (len(matrix[i])):
        if matrix[i][j]%2 ==0:
            sum_even+= matrix[i][j]
        else:
            sum_odd+=matrix[i][j]

print("sum of even no is ", sum_even)
print("sum of odd no is ", sum_odd)

len_index=len(matrix)
mean_1_diag=0
mean_2_diag=0

for i in range (len_index):
    mean_1_diag+=matrix[i][i]
    mean_2_diag+=matrix[i][len_index-1-i]

mean_1_diag=mean_1_diag/len_index
mean_2_diag=mean_2_diag/len_index


print("mean of numbers on first diagonal is ", mean_1_diag)
print("mean of numbers on second diagonal is ", mean_2_diag)

sum_under_1_diag=0
sum_above_2_diag=0

for i in range (len(matrix)):
    for j in range (i+1):
        sum_under_1_diag+=matrix[i][j]

for i in range (len(matrix)):
    for j in range (len(matrix[i])-i):
        sum_above_2_diag+=matrix[i][j]

print("sum of numbers below first diagonal is ", sum_under_1_diag)
print("sum of numbers above second diagonal is ",sum_above_2_diag)