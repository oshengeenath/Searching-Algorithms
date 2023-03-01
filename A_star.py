import random

# define Variable
START_NODE = "S |"
GOAL_NODE = "G |"
BLOCK = "X |"
NAVIGATOR = "o |"
Empty_Value = "  |"
count = 4  # the amount of Blocks
TotalTimeTaken = 0  # total time taken
# Creating Maze in a 2D array
Maze = [
    [" ", " 0", "  1", "  2", "  3", "  4", "  5", "", ""],
    ["0|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["1|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["2|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["3|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["4|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["5|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["", "", "", "", "", "", "", "", ""]
]

# since the starting poit of the maze has to be in between 0-11 we have to select either the first row or second row
# random Start Position

# random row selection
select_StartRow = random.randrange(1, 6)
# randomly get start position
select_StartingPosition = random.randrange(1, 3)

# randomly get goal position
select_GoalRow = random.randrange(1, 6)  # random row selection
# randomly get goal position
select_GoalPosition = random.randrange(5, 7)

# Creating the START and GOAL on the maze
Maze[select_StartRow][select_StartingPosition] = START_NODE
Maze[select_GoalRow][select_GoalPosition] = GOAL_NODE

# since there need to be 4 blocks
while count > 0:
    randomRowBlock = random.randrange(1, 6)
    randomPositionBlock = random.randrange(1, 7)
    count = count - 1

    if Maze[randomRowBlock][randomPositionBlock] == "  |":
        Maze[randomRowBlock][randomPositionBlock] = BLOCK
    else:
        count = count + 1


# Print maze
def output():
    # output
    for r in Maze:
        for c in r:
            print(c, end=" ")
        print()


# Chebyshev Distance
GoalRow = select_GoalRow
GoalPosition = select_GoalPosition

currentNodeRow = select_StartRow
currentNodePosition = select_StartingPosition
# ChebyshevDistance = max((currentNodePosition - GoalPosition) * (-1), (currentNodeRow - GoalRow) * (-1))
output()
while True:
    checkWest = max(((currentNodePosition - 1) - GoalPosition) * (-1), (currentNodeRow - GoalRow) * (-1))
    checkNorthWest = max(((currentNodePosition - 1) - GoalPosition) * (-1), ((currentNodeRow - 1) - GoalRow) * (-1))
    checkNorth = max((currentNodePosition - GoalPosition) * (-1), ((currentNodeRow - 1) - GoalRow) * (-1))
    checkNorthEast = max(((currentNodePosition + 1) - GoalPosition) * (-1), ((currentNodeRow - 1) - GoalRow) * (-1))
    checkEast = max(((currentNodePosition + 1) - GoalPosition) * (-1), (currentNodeRow - GoalRow) * (-1))
    checkSouthEast = max(((currentNodePosition + 1) - GoalPosition) * (-1), ((currentNodeRow + 1) - GoalRow) * (-1))
    checkSouth = max((currentNodePosition - GoalPosition) * (-1), ((currentNodeRow + 1) - GoalRow) * (-1))
    checkSouthWest = max(((currentNodePosition - 1) - GoalPosition) * (-1), ((currentNodeRow + 1) - GoalRow) * (-1))
    arr = [checkWest,checkNorthWest,checkNorth,checkNorthEast,checkEast,checkSouthEast,checkSouth,checkSouthWest]
    loopCount = 0

    is_west_run = False
    is_north_west_run = False
    is_north_run = False
    is_north_east_run = False
    is_east_run = False
    is_south_east_run = False
    is_south_run = False
    is_south_west_run = False
    while True:

        minValue = min(arr)
        # check west
        if minValue == checkWest and not is_west_run:
            is_west_run = True
            if Maze[currentNodeRow][currentNodePosition - 1 ] == Empty_Value or Maze[currentNodeRow][currentNodePosition - 1 ] == GOAL_NODE:
                currentNodePosition = currentNodePosition - 1
                currentNodeRow = currentNodeRow
                print("Going West")
                break
            elif Maze[currentNodeRow][currentNodePosition - 1] != Empty_Value or Maze[currentNodeRow][currentNodePosition - 1] != GOAL_NODE:
                for i in range(len(arr)):
                    if arr[i] == minValue:
                        del arr[i]
                        break
        # check North West
        elif minValue == checkNorthWest and not is_north_west_run:
            is_north_west_run = True
            if Maze[currentNodeRow - 1][currentNodePosition - 1 ] == Empty_Value or Maze[currentNodeRow - 1][currentNodePosition - 1 ] ==  GOAL_NODE:
                currentNodePosition = currentNodePosition - 1
                currentNodeRow = currentNodeRow - 1
                print("Going North West")
                break
            elif Maze[currentNodeRow - 1][currentNodePosition - 1] != Empty_Value or Maze[currentNodeRow - 1][currentNodePosition - 1] != GOAL_NODE:
                for i in range(len(arr)):
                    if arr[i] == minValue:
                        del arr[i]
                        break
        # check North
        elif minValue == checkNorth and not is_north_run:
            is_north_run = True
            if Maze[currentNodeRow - 1][currentNodePosition ] == Empty_Value or Maze[currentNodeRow - 1][currentNodePosition ] == GOAL_NODE:
                currentNodePosition = currentNodePosition
                currentNodeRow = currentNodeRow - 1
                print("Going North")
                break
            elif Maze[currentNodeRow - 1][currentNodePosition] != Empty_Value or Maze[currentNodeRow - 1][currentNodePosition] !=GOAL_NODE:
                for i in range(len(arr)):
                    if arr[i] == minValue:
                        del arr[i]
                        break
        # check North East
        elif minValue == checkNorthEast and not is_north_east_run:
            is_north_east_run = True
            if Maze[currentNodeRow - 1][currentNodePosition + 1 ] == Empty_Value or Maze[currentNodeRow - 1][currentNodePosition + 1 ] == GOAL_NODE:
                currentNodePosition = currentNodePosition + 1
                currentNodeRow = currentNodeRow - 1
                print("Going North East")
                break
            elif Maze[currentNodeRow - 1][currentNodePosition + 1] != Empty_Value or Maze[currentNodeRow - 1][currentNodePosition + 1] !=  GOAL_NODE:
                loopCount = loopCount + 1
                for i in range(len(arr)):
                    if arr[i] == minValue:
                        del arr[i]
                        break
        # check East
        elif minValue == checkEast and not is_east_run:
            is_east_run = True
            if Maze[currentNodeRow][currentNodePosition + 1 ] == Empty_Value or Maze[currentNodeRow][currentNodePosition + 1 ] == GOAL_NODE:
                currentNodePosition = currentNodePosition + 1
                currentNodeRow = currentNodeRow
                print("Going East")
                break
            elif Maze[currentNodeRow][currentNodePosition + 1] != Empty_Value or Maze[currentNodeRow][currentNodePosition + 1] != GOAL_NODE:
                loopCount = loopCount + 1
                for i in range(len(arr)):
                    if arr[i] == minValue:
                        del arr[i]
                        break
        # check south East
        elif minValue == checkSouthEast and not is_south_east_run:
            is_south_east_run = True
            if Maze[currentNodeRow + 1][currentNodePosition + 1] == Empty_Value or Maze[currentNodeRow + 1][currentNodePosition + 1] == GOAL_NODE:
                currentNodePosition = currentNodePosition + 1
                currentNodeRow = currentNodeRow + 1
                print("Going South East")
                break
            elif Maze[currentNodeRow + 1][currentNodePosition + 1] != Empty_Value or Maze[currentNodeRow + 1][currentNodePosition + 1] != GOAL_NODE:
                loopCount = loopCount + 1
                for i in range(len(arr)):
                    if arr[i] == minValue:
                        del arr[i]
                        break
        # check south
        elif minValue == checkSouth and not is_south_run:
            is_south_run = True
            if Maze[currentNodeRow + 1][currentNodePosition] == Empty_Value or Maze[currentNodeRow + 1][currentNodePosition] == GOAL_NODE:
                currentNodePosition = currentNodePosition
                currentNodeRow = currentNodeRow + 1
                print("Going south")
                break
            elif Maze[currentNodeRow + 1][currentNodePosition] != Empty_Value or Maze[currentNodeRow + 1][currentNodePosition] != GOAL_NODE:
                for i in range(len(arr)):
                    if arr[i] == minValue:
                        del arr[i]
                        break
        # check south West
        elif minValue == checkSouthWest and not is_south_west_run:
            is_south_west_run = True
            if Maze[currentNodeRow + 1][currentNodePosition - 1 ] == Empty_Value or Maze[currentNodeRow + 1][currentNodePosition - 1 ] == GOAL_NODE:
                currentNodePosition = currentNodePosition - 1
                currentNodeRow = currentNodeRow + 1
                print("Going south west")
                break
            elif Maze[currentNodeRow + 1][currentNodePosition - 1 ] != Empty_Value or Maze[currentNodeRow + 1][currentNodePosition - 1 ] != GOAL_NODE:
                for i in range(len(arr)):
                    if arr[i] == minValue:
                        del arr[i]
                        break

    if Maze[currentNodeRow][currentNodePosition] == Empty_Value:
        Maze[currentNodeRow][currentNodePosition] = NAVIGATOR
        TotalTimeTaken = TotalTimeTaken + 1

    elif Maze[currentNodeRow][currentNodePosition] == GOAL_NODE:
        print("GOAL")
        print("Total Time taken to reach the goal : ",TotalTimeTaken + 1)
        break
    output()
