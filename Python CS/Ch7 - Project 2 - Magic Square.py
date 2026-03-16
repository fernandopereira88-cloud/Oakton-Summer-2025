def is_magic_square(magic_list):
#    magic_list = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    nrows = 0
    ncols = 0
    sum_list =[]
    sum_loop=0
    count_not_magic = 0

    for row in magic_list:
        nrows +=1
    for column in magic_list:
        ncols +=1


    #Calculate sum for each row
    for row in range(nrows):
        for column in range(ncols):
            sum_loop = sum_loop + magic_list[row][column]
        sum_list.append(sum_loop)
        sum_loop = 0
        print(sum_list)
        
    #Calculate sum for each column
    for column in range(ncols):
        for row in range(nrows):

         sum_loop = sum_loop + magic_list[row][column]
        sum_list.append(sum_loop)
        sum_loop = 0
        print(sum_list)
        
    #Calculate sum for each primary diagonal
    for column in range(ncols):
        for row in range(nrows):
         if row == column:
          sum_loop = sum_loop + magic_list[row][column]
    sum_list.append(sum_loop)
    sum_loop = 0
    print(sum_list)

    #Calculate sum for each secondary diagonal
    for row in range(nrows):
        for column in range(ncols):
            print(row,column,nrows,sum_loop)        
            if row+column+2 == nrows+1:
                sum_loop = sum_loop + magic_list[row][column]
    sum_list.append(sum_loop)
    sum_loop = 0
    #print(sum_list)

    #Analyze values in the list
    for item1 in range(len(sum_list)):
        for item2 in range(len(sum_list)):
            if sum_list[item1] != sum_list[item2]:
                count_not_magic += 1
                
    if count_not_magic > 0:
        return False
    else:
        return True
