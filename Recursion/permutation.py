problem statement: https://www.algoexpert.io/questions/permutations

#solution 1
def getPermutationsHelper(array,curr_perm,permArray):
    if not len(array) and len(curr_perm):
        permArray.append(curr_perm)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i+1:]
            newPerm = curr_perm + [array[i]]
            getPermutationsHelper(newArray,newPerm,permArray)
def getPermutations(array):
    # Write your code here.
    permArray = []
    curr_perm =[]
    getPermutationsHelper(array,curr_perm,permArray)
    return permArray

TC: O(N!*N*N)
SC : O(N!*N)

#solution 2
def swap(array,i,j):
    array[i],array[j]= array[j],array[i]
    
def getPermutationsHelper(i,array,permArray):
    if  i == len(array) - 1:
        permArray.append(array[:]) # saving the snapshot of current array
    else:
        for j in range(i,len(array)):
            swap(array,i,j)
            getPermutationsHelper(i+1,array,permArray)
            swap(array,i,j)


def getPermutations(array):
    # Write your code here.
    permArray = []
    currentIndex = 0
    getPermutationsHelper(currentIndex,array,permArray)
    return permArray
TC: O(N!*N*N)
SC : O(N!*N)
