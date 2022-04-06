from leetcode import *

# Time: O(m*n + log(m*n)). We need to calculate distances between all pairs of workers and bikes and then we need to sort the distances.
# This time complexity calculation is a little off because there are not m*n possible distances rather there are 1998 possible distances
# because the coordinates range from (0,0) to (999,999). So, it should be O(m*n + K) where K is the number of possible Manhattan distances.
# Space: O(m*n + m + n + K) = O(m*n + K).
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distToWorkerBikePairs = {}
        for i in range(len(workers)):
            for j in range(len(bikes)):
                dist = self.dist(workers[i], bikes[j])
                workerBikePairs = distToWorkerBikePairs.get(dist, [])
                if len(workerBikePairs) == 0:
                    distToWorkerBikePairs[dist] = workerBikePairs
                workerBikePairs.append((i, j))

        sortedDist = sorted(distToWorkerBikePairs.keys())
        assignments = [-1]*len(workers)
        assignedBikes = set()
        for i in range(len(sortedDist)):
            workerBikePairs = distToWorkerBikePairs[sortedDist[i]]
            for worker, bike in workerBikePairs:
                if assignments[worker] == -1 and bike not in assignedBikes:
                    assignments[worker] = bike
                    assignedBikes.add(bike)

            if len(assignedBikes) == len(workers):
                break

        return assignments

    # Manhattan distance.
    def dist(self, posA: List[int], posB: List[int]) -> int:
        return abs(posA[0] - posB[0]) + abs(posA[1] - posB[1])

solution = Solution()

# Expected: [1,0]
print(solution.assignBikes(workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]))

# Expected: [0,2,1]
print(solution.assignBikes(workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]))
