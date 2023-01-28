# part1 q4
# init 2 lists
lst1 = [1,3,5]
lst2 = [2,4,6]

# do concat
catlist1 = lst1+lst2
# print result
print catlist1

# modify lst1
lst1.append(7)

# if python makes a copy then output should be [1, 3, 5, 2, 4, 6]
# else it should be [1, 3, 5, 7, 2, 4, 6]
print catlist1

# output should be [1, 3, 5, 2, 4, 6], 
# that means it makes a copy