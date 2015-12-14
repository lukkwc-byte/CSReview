def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
#print(sum_of_first_n)

Gen=(n*n for n in range(4))
for i in Gen:
    print(i)

#print(next(Gen))

queue=[]
p={}

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

it=iter(queue)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

queue.append(5)

print(next(it))


""""
def update(process):
    global queue
    if process in p:
        p[process][1]=time.time()
        check(process)
    else:
        p[process]=[time.time(), None]
        queue.append(process)

def check(process):
    global queue
    if queue[0]==process:
        while p[queue[0]][1]!=None:
            print(p[process][0], p[process][1])
            queue.pop(0)

"""
