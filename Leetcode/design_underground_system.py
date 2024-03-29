'''
An underground railway system is keeping track of customer travel times between different stations.
They are using this data to calculate the average time it takes to travel from one station to another.

Implement the UndergroundSystem class:
- void checkIn(int id, string stationName, int t)
    - A customer with a card ID equal to id, checks in at the station stationName at time t.
    - A customer can only be checked into one place at a time.
- void checkOut(int id, string stationName, int t)
    - A customer with a card ID equal to id, checks out from the station stationName at time t.
- double getAverageTime(string startStation, string endStation)
    - Returns the average time it takes to travel from startStation to endStation.
    - The average time is computed from all the previous traveling times from startStation to endStation that happened directly,
      meaning a check in at startStation followed by a check out from endStation.
    - The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
    - There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.

You may assume all calls to the checkIn and checkOut methods are consistent.
If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.
'''

# Time: O(1)
# Space: O(n + m^2) where n is the number of people who checked in and m is the number of stations.
class UndergroundSystem:
    def __init__(self):
        self.checkIns = {}
        self.averageTimes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkIns[id]
        timeTaken = t - startTime
        avg, count = self.averageTimes.get((startStation, stationName), (0, 0))
        avg = ((avg * count) + timeTaken) / (count + 1)
        self.averageTimes[(startStation, stationName)] = (avg, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.averageTimes[(startStation, endStation)][0]

undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)  # Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
undergroundSystem.checkOut(27, "Waterloo", 20)  # Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
undergroundSystem.checkOut(32, "Cambridge", 22) # Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
print(undergroundSystem.getAverageTime("Paradise", "Cambridge")) # return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))    # return 11.00000. Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
undergroundSystem.checkIn(10, "Leyton", 24)
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))    # return 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38)  # Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))    # return 12.00000. Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12

undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(10, "Leyton", 3)
undergroundSystem.checkOut(10, "Paradise", 8) # Customer 10 "Leyton" -> "Paradise" in 8-3 = 5
print(undergroundSystem.getAverageTime("Leyton", "Paradise")) # return 5.00000, (5) / 1 = 5
undergroundSystem.checkIn(5, "Leyton", 10)
undergroundSystem.checkOut(5, "Paradise", 16) # Customer 5 "Leyton" -> "Paradise" in 16-10 = 6
print(undergroundSystem.getAverageTime("Leyton", "Paradise")) # return 5.50000, (5 + 6) / 2 = 5.5
undergroundSystem.checkIn(2, "Leyton", 21)
undergroundSystem.checkOut(2, "Paradise", 30) # Customer 2 "Leyton" -> "Paradise" in 30-21 = 9
print(undergroundSystem.getAverageTime("Leyton", "Paradise")) # return 6.66667, (5 + 6 + 9) / 3 = 6.66667
