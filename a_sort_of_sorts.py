def insertionSort(mylist):
   for index in range(0,len(mylist)):

     currentvalue = mylist[index]
     position = index

     while position>0 and mylist[position-1]>currentvalue:
         mylist[position]=mylist[position-1]
         position = position-1

     mylist[position]=currentvalue

mylist = [67,45,2,13,1,998]
print ("let's put the following list items in ascending order with an insertion sort:")
print (mylist)
print ("\n")
insertionSort(mylist)
print(mylist)

mylist = [89,23,33,45,10,12,45,45,45]
print ("\nGreat, now let's put this next group of list items in ascending order via the same method:")
print (mylist)
print ("\n")
insertionSort(mylist)
print(mylist)
