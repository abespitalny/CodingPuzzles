import math

# Time complexity: O(n) where n is the number of nodes.
# Space complexity: O(1) because I'm reusing the input array to store the subtree sums.
def drainagePartition(parent, inputs):
    totalInput = sum(inputs)
    # Calculate all the subtree sums by working from leaf to root.
    for i in reversed(range(1, len(parent))):
        node = i
        inputs[parent[node]] += inputs[node]

    # Compute all possible partitions and return the one with minimum difference.
    minDiff = math.inf
    for i in inputs:
        # Partition 1 = Total - Partition 2
        # Therefore, |Partition 1 - Partition 2| = |(Total - Partition 2) - Partition 1|
        partitionDiff = abs((totalInput - i) - i)
        if partitionDiff < minDiff:
            minDiff = partitionDiff

    return minDiff
