my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)
my_list2 = [50, 60, 70]
my_list.extend(my_list2)
del my_list[-1]
my_list.sort()

#Final list
print(my_list)

#Find and print the index of the value 30 in my_list
index_30 = my_list.index(30)
print("Index of 30:", index_30)
