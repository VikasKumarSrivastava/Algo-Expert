#problem Statement:
 https://www.algoexpert.io/questions/product-sum
def productSumHelper(array,multiplier):
    productSum = 0
    for i in array:
        if type(i) is list:         
            productSum += productSumHelper(i,multiplier+1)
        else:
            productSum += i
    return productSum * multiplier
def productSum(array):
    # Write your code here.
    return productSumHelper(array,1)


# TC = O(N)
# where N is the total no. of elements including the sub-elements
# SC = O(depth)
# where depth is the level of sub-elements in the array leading to the exact no. of recursive call required.
