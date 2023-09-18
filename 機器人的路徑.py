def getIndex():
    gridMap = []
    x = 0
    y = 0
    for i in range(int(input().split()[0])):
        gridMap.append([int(i) for i in input().split()])
        if min(gridMap[i]) < gridMap[x][y]:
            x = i
            y = gridMap[i].index(min(gridMap[i]))
    return gridMap, x, y

def 

if __name__ == "__main__":
    GridMap, x, y = getIndex()    
