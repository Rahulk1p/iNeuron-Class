def addTwoList(list1, list2):
    if len(list1) != len(list2):
        print("List must be of same size")
    else:
        counter = 0
        sum=[]
        print(range(len(list1)-1))
        for x in range(len(list1)):
            sum.append(list1[x] + list2[x])
        return sum

list1 = [1,3,2,4,3]
list2 = [1,3,2,4,3]
print(addTwoList(list1,list2))