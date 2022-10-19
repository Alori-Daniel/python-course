var1 = list(("monday", "tuesday"))   #used to declare a list
#print(type(var1))

#print(len(var1))                 #used to know to length

#indexing list
#print(var1[0]

#editing lists
#var1[0]="friday"
#print(var1)

#inserting into list
#var1.insert(0,"saturday")
#print(var1)

#adding a list to another list
weekends = ["saturday", "sunday"]

#print(var1)
#print(weekends)

var1.extend(weekends)

print(var1)


#inserting into the end of the list
#var1.append("sunday")
#print(var1)

#removing elements from a list
#var1.clear()
#var1.remove("sunday")
#print(var1)

#removing elements from a list using index

#var1.pop() #pop function used from removing elements
#print(var1)

#deleting a variable
#del var1[2]
#print(var1)

#sorting elements in a list
#print(f'Unsorted: {var1}\n')
#var1.sort()
#print(f'sorted: {var1}')

#printf('{} is {} years old' .format(name,new))
#print(f'{name} is {new} years old)

#Using integers
#Age=[10,11,23,45,9,3,56,78]
#print(f'unsorted: {Age}')
#Age.sort()
#print(f'Ascending: {Age}')
#Age.sort(reverse=True) #sport in descending order
#print(f'Descending: {Age}')
