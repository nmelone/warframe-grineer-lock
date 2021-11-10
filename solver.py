import itertools
import json

#Generate every permutation of the grineer puzzle
perms = list(itertools.permutations('12345678', 8))
# print(len(perm))
# print(perm)

#Precalculated distances from 1 -> X where is is the next number to hit
distances = {
    "cw": {
        1: 0,
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 7
    },
    "ccw": {
        1: 0,
        2: 7,
        3: 6,
        4: 5,
        5: 4,
        6: 3,
        7: 2,
        8: 1
    }
}

#Looks up the distance from x -> y with the given direction d
#Does this by rotating the numbers x,y such that x becomes equal to 1
def getDistance(x, y, d):
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    y = nums[y - nums.index(x) - 1]
    return distances[d][y]

#Goes through every number in the permutation given and adds all the distances up
def calcDistance(perm):
    direction = {True: "cw", False: "ccw"}
    total = getDistance(1, int(perm[0]), direction[True])
    for x in range(len(perm) - 1):
        total = total + \
            getDistance(int(perm[x]), int(perm[x+1]), direction[x % 2])
    return total


totalDistance = {}
#goes through every permutation and calculates distance of path stores in totalDistance
for perm in perms:
    total = calcDistance(perm)
    totalDistance[''.join(perm)] = total

smallestKey = min(totalDistance, key=totalDistance.get)
largestKey = max(totalDistance, key=totalDistance.get)

print("The shortest order is: " + smallestKey, "\nDistance: ", totalDistance[smallestKey])
print("The longest order is: " + largestKey, "\nDistance: ",totalDistance[largestKey])



