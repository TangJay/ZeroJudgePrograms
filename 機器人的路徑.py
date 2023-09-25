import sys


def getIndex():
    gridMap = []
    x = 0
    y = 0
    for i in range(int(input().split()[0])):
        gridMap.append([int(i) for i in input().split()])
        if min(gridMap[i]) < gridMap[y][x]:
            x = gridMap[i].index(min(gridMap[i]))
            y = i
    return gridMap, x, y


def calculate(gridmap, x, y):
    points = 0
    while True:
        y, x, points = moving(gridmap, x, y, points)


def moving(gridmap, x, y, points):
    points += gridmap[y][x]
    gridmap[y][x] = 1000000
    directions = [1000000, 1000000, 1000000, 1000000]
    if x != 0:
        directions[0] = gridmap[y][x - 1]
    if x != len(gridmap[y]) - 1:
        directions[1] = gridmap[y][x + 1]
    if y != 0:
        directions[2] = gridmap[y - 1][x]
    if y != len(gridmap) - 1:
        directions[3] = gridmap[y + 1][x]
    next = directions.index(min(directions))
    if min(directions) == 1000000:
        print(points)
        sys.exit()
    elif next == 0:
        return y, x - 1, points
    elif next == 1:
        return y, x + 1, points
    elif next == 2:
        return y - 1, x, points
    elif next == 3:
        return y + 1, x, points


if __name__ == "__main__":
    gridMap, x, y = getIndex()
    calculate(gridMap, x, y)
