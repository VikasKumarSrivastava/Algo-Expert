# problem statement :https://www.algoexpert.io/questions/powerset
#TC: O(N*2^N)
#SC: O(N*2^N)
# where N is the length of the input array
def powersetHelper(array,idx,curr_powerset,ans):
    if idx == len(array):
        ans.append(curr_powerset)
        return
    #include
    powersetHelper(array,idx+1,curr_powerset+[array[idx]],ans)
    #exclude
    powersetHelper(array,idx+1,curr_powerset,ans)
  
def powerset(array):
    # Write your code here.
    ans =[]
    curr_powerset =[]
    idx =0
    powersetHelper(array,idx,curr_powerset,ans)
    return ans
