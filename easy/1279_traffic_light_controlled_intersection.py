"""
There is an intersection of two roads. First road is road A where cars travel from North to South in direction 1 and
from South to North in direction 2. Second road is road B where cars travel from West to East in direction 3 and
from East to West in direction 4.

There is a traffic light located on each road before the intersection. A traffic light can either be green or red.

    Green means cars can cross the intersection in both directions of the road.
    Red means cars in both directions cannot cross the intersection and must wait until the light turns green.

The traffic lights cannot be green on both roads at the same time. That means when the light is green on road A,
it is red on road B and when the light is green on road B, it is red on road A.

Initially, the traffic light is green on road A and red on road B. When the light is green on one road, all cars can
cross the intersection in both directions until the light becomes green on the other road. No two cars traveling on
different roads should cross at the same time.

Design a deadlock-free traffic light controlled system at this intersection.

Implement the function void carArrived(carId, roadId, direction, turnGreen, crossCar) where:
    carId is the id of the car that arrived.
    roadId is the id of the road that the car travels on.
    direction is the direction of the car.
    turnGreen is a function you can call to turn the traffic light to green on the current road.
    crossCar is a function you can call to let the current car cross the intersection.
Your answer is considered correct if it avoids cars deadlock in the intersection. Turning the light green on a road
when it was already green is considered a wrong answer.

Example 1:
Input: cars = [1,3,5,2,4], directions = [2,1,2,4,3], arrivalTimes = [10,20,30,40,50]
Output: [
"Car 1 Has Passed Road A In Direction 2",    // Traffic light on road A is green, car 1 can cross the intersection.
"Car 3 Has Passed Road A In Direction 1",    // Car 3 crosses the intersection as the light is still green.
"Car 5 Has Passed Road A In Direction 2",    // Car 5 crosses the intersection as the light is still green.
"Traffic Light On Road B Is Green",          // Car 2 requests green light for road B.
"Car 2 Has Passed Road B In Direction 4",    // Car 2 crosses as the light is green on road B now.
"Car 4 Has Passed Road B In Direction 3"     // Car 4 crosses the intersection as the light is still green.
]
"""

from threading import Lock


class TrafficLight:
    """
    1. Track state of the light (which lane is green)
    2. Use threading Lock with context manager to acquire/release thread so that only 1 car is ever processed at a time.

    Runtime: 48 ms, faster than 59.35% of Python3
    Memory Usage: 15.6 MB, less than 22.76% of Python3
    """

    def __init__(self):
        self.curr_green = 1
        self.light_lock = Lock()

    def carArrived(
            self,
            carId: int,  # ID of the car
            roadId: int,  # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
            direction: int,  # Direction of the car
            turnGreen: 'Callable[[], None]',  # Use turnGreen() to turn light to green on current road
            crossCar: 'Callable[[], None]'  # Use crossCar() to make car cross the intersection
    ) -> None:
        def change_light(road_id):
            if self.curr_green != road_id:
                turnGreen()
                self.curr_green = road_id

        # acquire lock if available, change_light/crossCar, then release lock
        with self.light_lock:  # restricts threads to process 1 car at a time
            change_light(roadId)
            crossCar()
