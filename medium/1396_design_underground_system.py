"""
An underground railway system is keeping track of customer travel times between different stations.
They are using this data to calculate the average time it takes to travel from one station to another.

Implement the UndergroundSystem class:

-    void checkIn(int id, string stationName, int t)
        A customer with a card ID equal to id, checks in at the station stationName at time t.
        A customer can only be checked into one place at a time.
-    void checkOut(int id, string stationName, int t)
        A customer with a card ID equal to id, checks out from the station stationName at time t.
-    double getAverageTime(string startStation, string endStation)
        Returns the average time it takes to travel from startStation to endStation.
        The average time is computed from all the previous traveling times from startStation to endStation that happened
          directly, meaning a check in at startStation followed by a check out from endStation.
-    The time it takes to travel from startStation to endStation may be different from the time it takes to travel from
      endStation to startStation.
    There will be at least 1 customer that has traveled from startStation to endStation before getAverageTime is called.

You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then
checks out at time t2, then t1 < t2. All events happen in chronological order.
"""

import collections


class UndergroundSystem:
    """
    Runtime: 244 ms, faster than 51.66% of Python3
    Memory Usage: 23.9 MB, less than 87.54% of Python3

    Time complexity: O(1)
    Space complexity: O(P+S^2), where S is the number of stations on the network, and P is the number of passengers
    making a journey concurrently during peak time.
    """

    def __init__(self):
        self.user_itineraries = {}  # <UserId, [StationId, CheckInTime]>
        self.travel_times = collections.defaultdict(list)  # <StartStationId-EndStationId, [TravelDuration]>

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user_itineraries[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.user_itineraries:
            from_station, start_time = self.user_itineraries.pop(id)
            direction = self.get_direction_key(from_station, stationName)
            self.travel_times[direction].append(t - start_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        direction = self.get_direction_key(startStation, endStation)
        times = self.travel_times[direction]
        return sum(times) / len(times)

    def get_direction_key(self, from_station: str, to_station: str) -> str:
        return f"{from_station}-{to_station}"


if __name__ == '__main__':
    u_sys_1 = UndergroundSystem()
    u_sys_1.checkIn(45, "Leyton", 3)
    u_sys_1.checkIn(32, "Paradise", 8)
    u_sys_1.checkIn(27, "Leyton", 10)
    u_sys_1.checkOut(45, "Waterloo", 15)  # Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
    u_sys_1.checkOut(27, "Waterloo", 20)  # Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
    u_sys_1.checkOut(32, "Cambridge", 22)  # Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
    assert u_sys_1.getAverageTime("Paradise", "Cambridge") == 14  # One trip "Paradise" -> "Cambridge", (14) / 1 = 14
    assert u_sys_1.getAverageTime("Leyton", "Waterloo") == 11  # Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
    u_sys_1.checkIn(10, "Leyton", 24)
    assert u_sys_1.getAverageTime("Leyton", "Waterloo") == 11  # return 11.0
    u_sys_1.checkOut(10, "Waterloo", 38)  # Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
    assert u_sys_1.getAverageTime("Leyton", "Waterloo") == 12  # Three trips "Leyton"->"Waterloo", (10+12+14) / 3 = 12
