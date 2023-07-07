list = [ ]
poslist = [ ]
n=int(input("Enter number of elements: "))
print("Enter the elements:")
for i in range(0,n):
    element = int(input( ))
    list.append(element)
for i in range(0,n):
    if(list[i]>0):
        poslist.append(list[i])
print("Original List: ",list)
print("Positive List: ",poslist)