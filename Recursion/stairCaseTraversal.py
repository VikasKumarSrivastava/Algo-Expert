# TC - O(N)
# SC - O(N)
# Sliding window concept is used.
# Can be done by recursion,memoization and dynamic programming but they will have greater Time and Space Complexity than Sliding window concept.
# Problem Statement https://www.algoexpert.io/questions/staircase-traversal
def staircaseTraversal(height, maxSteps):
    currentNumberOfWays = 0
    waysToTop =[1]

    for currentHeight in range(1,height+1):
        startOfWindow = currentHeight - maxSteps - 1
        endOfWindow = currentHeight - 1

        if startOfWindow >= 0:
            currentNumberOfWays -= waysToTop[startOfWindow]
        currentNumberOfWays += waysToTop[endOfWindow]
        waysToTop.append(currentNumberOfWays)
    return waysToTop[height]
