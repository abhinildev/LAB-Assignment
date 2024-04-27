#implementing a queue
queue=[]
#inserting elements
x=int(input("Enter the no of elements"))
for i in  range(0,x):
    y=int(input("Enter the elements you want to insert"))
    queue.append(y)
    if i==x:
        print("Queue is full")

print(queue)
#deleting elements from the queue\
k=int(input("Enter no of elements you want to delete"))
for i in range(0,k):
    z=queue.pop(0)
    print(z)
#queue after deletinh elements
print(queue)