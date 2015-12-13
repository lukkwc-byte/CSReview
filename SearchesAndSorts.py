class Search():
    def BinarySearch(A, value):
        A.sort()
        return Search.BSHelper(A, value, 0, len(A)-1)

    def BSHelper(A, value, s, e):
        if s==e:
            if A[s]==value:
                return True
            else:
                return False
        
        m=int((e-s)/2) + s
        print(m)
        
        if A[m] == value:
            return True
        elif A[m] > value:
            return Search.BSHelper(A, value, 0, m)
        else:
            return Search.BSHelper(A, value, m, len(A)-1)

class Sort():
    def BubbleSort(A):
        for i in range(1, len(A)):
            for j in range(len(A)-i):
                if A[j]>A[j+1]:
                    temp=A[j]
                    A[j]=A[j+1]
                    A[j+1]=temp
        return A

    def SelectionSort(A):
        for i in range(len(A)):
            localMin=999999
            localMinI=0
            for j in range(i, len(A)):
                if A[j] < localMin:
                    localMin=A[j]
                    localMinI=j
            temp=A[i]
            A[i]=localMin
            A[localMinI]=temp
        return A

    def MergeSort(A):
        if len(A) < 2:
            return A
        
        mid=int(len(A)/2)
        left=Sort.MergeSort(A[0:mid])
        right=Sort.MergeSort(A[mid:len(A)])
        
        return Sort.Merge(left, right)

    def Merge(A, B):
        i=j=0
        C=[]
        
        while i < len(A) and j < len(B):
            if A[i]<=B[j]:
                C.append(A[i])
                i+=1
            else:
                C.append(B[j])
                j+=1

        while (i < len(A)):
            C.append(A[i])
            i+=1

        while (j < len(B)):
            C.append(B[j])
            j+=1

        return C

    def QuickSort(A):
        Sort.QS(A, 0, len(A)-1)

    def QS(A, s, e):
        if s < e:
            p=Sort.partition(A, s, e)
            Sort.QS(A, s, p-1)
            Sort.QS(A, p+1, e)

    def partition(A, s, e):
        pivot=A[s]
        i=s+1
        j=e
        done=False
        while not done:
            while i <= j and A[i] <= pivot:
                i+=1
            while j >= i and A[j] >=pivot:
                j-=1
            if j < i:
                done = True
            else:
                temp=A[i]
                A[i]=A[j]
                A[j]=temp
        temp=A[j]
        A[j]=pivot
        A[s]=temp

        return j

A=[5,34,2,4]
Sort.QuickSort(A)
print(A)

