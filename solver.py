import itertools
import json

perms = list(itertools.permutations('12345678', 8))
# print(len(perm))
# print(perm)

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


def getDistance(x, y, d):
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    y = nums[y - nums.index(x) - 1]
    return distances[d][y]


def calcDistance(perm):
    direction = {True: "cw", False: "ccw"}
    total = getDistance(1, int(perm[0]), direction[True])
    for x in range(len(perm) - 1):
        total = total + \
            getDistance(int(perm[x]), int(perm[x+1]), direction[x % 2])
    return total


totalDistance = {}
for perm in perms:
    total = calcDistance(perm)
    totalDistance[''.join(perm)] = total

smallestKey = min(totalDistance, key=totalDistance.get)
largestKey = max(totalDistance, key=totalDistance.get)

print("The shortest order is: " + smallestKey, "\nDistance: ", totalDistance[smallestKey])
print("The longest order is: " + largestKey, "\nDistance: ",totalDistance[largestKey])

sortTotalDistance = dict(sorted(totalDistance.items(), key=lambda item: item[1]))
with open("E:/Nico/Documents/GitHub/warframe-grineer-lock/sortedTotalDistance.json", 'w') as f:
    json.dump(sortTotalDistance,f)