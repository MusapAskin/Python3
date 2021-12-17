array_2d=[[1,4,3],[3,1,9],[0,5,2]]

def find_sum_2d(array_2d):
    total=0
    for row in array_2d:
        for i in row:
            total +=i
    return total

print(find_sum_2d(array_2d))