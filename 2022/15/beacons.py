from collections import namedtuple

TEST_CASE = """Sensor at x=8, y=7: closest beacon is at x=2, y=10"""

#TEST_CASE = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
#Sensor at x=9, y=16: closest beacon is at x=10, y=16
#Sensor at x=13, y=2: closest beacon is at x=15, y=3
#Sensor at x=12, y=14: closest beacon is at x=10, y=16
#Sensor at x=10, y=20: closest beacon is at x=10, y=16
#Sensor at x=14, y=17: closest beacon is at x=10, y=16
#Sensor at x=8, y=7: closest beacon is at x=2, y=10
#Sensor at x=2, y=0: closest beacon is at x=2, y=10
#Sensor at x=0, y=11: closest beacon is at x=2, y=10
#Sensor at x=20, y=14: closest beacon is at x=25, y=17
#Sensor at x=17, y=20: closest beacon is at x=21, y=22
#Sensor at x=16, y=7: closest beacon is at x=15, y=3
#Sensor at x=14, y=3: closest beacon is at x=15, y=3
#Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

Point = namedtuple("Point", "x y")


def compute(s: str) -> int:
    sensors = []
    beacons = []
    coords_covered = []
    for line in s.splitlines():
        sensor_str, beacon_str = line.split(":")
        sx_str, sy_str = sensor_str.split(",")
        bx_str, by_str = beacon_str.split(",")
        sx = int(sx_str.split("=")[1])
        sy = int(sy_str.split("=")[1])
        bx = int(bx_str.split("=")[1])
        by = int(by_str.split("=")[1])
        sensors.append(Point(sx, sy))
        beacons.append(Point(bx, by))

    # Take the Manhattan distance between each
    # sensor and its beacon. Then, tag all the points
    # within that distance of the sensor as covered by
    # adding them to `coords_covered`. At the end, sort
    # by y, and see how many there are in `coords_covered`
    # with y=2m.
    distances = [abs(s.x - b.x) + abs(s.y - b.y) for s, b in zip(sensors, beacons)]

    for sensor, distance in zip(sensors, distances):
        for x in range(sensor.x, sensor.x + distance):
            for y in range(sensor.y, sensor.y + distance):
                if abs(sensor.x - x) + abs(sensor.y - y) <= distance:
                    coords_covered.append(Point(x, y))
        for x in range(sensor.x - distance, sensor.x):
            for y in range(sensor.y - distance, sensor.y):
                if abs(sensor.x - x) + abs(sensor.y - y) <= distance:
                    coords_covered.append(Point(x, y))

    of_interest = [c for c in coords_covered if c.y == 10]
    breakpoint()


def run_test():
    output = compute(TEST_CASE)
    assert output == 26, output


if __name__ == "__main__":
    run_test()
    # with open("./input.txt", "r", encoding="utf-8") as f:
    #    s = "".join(line for line in f)
    # print(compute(s))
