import random

# Defining Variable
START_NODE = "S |"
GOAL_NODE = "G |"
BLOCK = "X |"
NAVIGATOR = "o |"
# The amount of Blocks
block_Count = 4
# total time taken
TotalPathTime = 0
# Best time taken
BestPathTime = 0
# Array to record previous positions
previous_Positions = []
# Array to record previous rows
previous_Rows = []

# Creating a maze with 2D array
MAZE = [
    [" ", " 0", "  1", "  2", "  3", "  4", "  5","",""],
    ["0|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["1|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["2|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["3|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["4|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["5|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["", "", "", "", "", "", "","",""]
]

# Since the starting point of the maze has to be in between 0-11 we have to select either the first row or second row
# Random Start Position

# Random row selection
select_StartRow = random.randrange(1, 6)
# Randomly get start position
select_StartingPosition = random.randrange(1, 3)

# Since the goal point of the maze has to be in between 24-35 we have to select either the fifth row or sixth row
# Randomly get goal position

# Random row selection
select_GoalRow = random.randrange(1, 6)
# Randomly get goal position
select_GoalPosition = random.randrange(5, 7)

# Creating the START and GOAL on the maze
MAZE[select_StartRow][select_StartingPosition] = START_NODE
MAZE[select_GoalRow][select_GoalPosition] = GOAL_NODE

# Since there need to be 4 blocks
while block_Count > 0:
    # Random row selection
    randomRowBlock = random.randrange(1, 6)
    # Randomly get block position
    randomPositionBlock = random.randrange(1, 7)
    block_Count = block_Count - 1

    if MAZE[randomRowBlock][randomPositionBlock] == "  |":
        MAZE[randomRowBlock][randomPositionBlock] = BLOCK
    else:
        block_Count = block_Count + 1

# DFS maze Navigation
current_Row = select_StartRow
current_Position = select_StartingPosition


# Print maze
def output():
    # output
    for r in MAZE:
        for c in r:
            print(c, end=" ")
        print()

# Adding to previous row
previous_Rows.append(current_Row)
# Adding the previous positions
previous_Positions.append(current_Position)
while True:
    Check = 0
    TotalPathTime = TotalPathTime + 1
    BestPathTime = BestPathTime + 1

    # Checking West for available slots
    if MAZE[current_Row][current_Position - 1] == "  |":
        current_Position = current_Position - 1
        MAZE[current_Row][current_Position] = NAVIGATOR
        print("Moving West")
    # Checking West for goal
    elif MAZE[current_Row][current_Position - 1] == GOAL_NODE:
        print("GOAL Reached")
        break

    # Checking North West for available slots
    elif MAZE[current_Row-1][current_Position-1] == "  |":
        current_Row = current_Row - 1
        current_Position = current_Position - 1
        MAZE[current_Row][current_Position] = NAVIGATOR
        print("Moving North West")
    elif MAZE[current_Row-1][current_Position-1] == GOAL_NODE:
        print("GOAL Reached")
        break

    # Checking North for available slots
    elif MAZE[current_Row - 1][current_Position] == "  |":
        current_Row = current_Row - 1
        MAZE[current_Row][current_Position] = NAVIGATOR
        print("Moving North")
    # Checking North for goal
    elif MAZE[current_Row - 1][current_Position] == GOAL_NODE:
        print("GOAL Reached")
        break

    # Checking North East for available slots
    elif MAZE[current_Row-1][current_Position+1] == "  |":
        current_Row = current_Row - 1
        current_Position = current_Position + 1
        MAZE[current_Row][current_Position] = NAVIGATOR
        print("Moving North East")
    elif MAZE[current_Row-1][current_Position+1] == GOAL_NODE:
        print("GOAL Reached")
        break

    # checking East for available slots
    elif MAZE[current_Row][current_Position + 1] == "  |":
        current_Position = current_Position + 1
        MAZE[current_Row][current_Position] = NAVIGATOR
        print("Moving East")
        # checking East for goal
    elif MAZE[current_Row][current_Position + 1] == GOAL_NODE:
        print("GOAL Reached")
        break

    # Checking South East for available slots
    elif MAZE[current_Row+1][current_Position+1] == "  |":
        current_Row = current_Row + 1
        current_Position = current_Position + 1
        MAZE[current_Row][current_Position] = NAVIGATOR
        print("Moving South East")
    elif MAZE[current_Row+1][current_Position+1] == GOAL_NODE:
        print("GOAL Reached")
        break

    # Checking South for available slots
    elif MAZE[current_Row + 1][current_Position] == "  |":
        current_Row = current_Row + 1
        MAZE[current_Row][current_Position] = NAVIGATOR
        print("Moving South")
    # checking South for goal
    elif MAZE[current_Row + 1][current_Position] == GOAL_NODE:
        print("GOAL Reached")
        break

    # Checking South West for available slots
    elif MAZE[current_Row-1][current_Position-1] == "  |":
        current_Row = current_Row - 1
        current_Position = current_Position - 1
        MAZE[current_Row][current_Position] = NAVIGATOR
        print("Moving South West")
    elif MAZE[current_Row-1][current_Position-1] == GOAL_NODE:
        print("GOAL Reached")
        break

    # When going in the wrong way
    elif MAZE[current_Row][current_Position] == BLOCK or START_NODE:
        print("Went on the Wrong Path")
        print("Retrace Step")
        BestPathTime = BestPathTime - 2
        # checking if the previous position is on the West
        if previous_Positions[-2] - previous_Positions[-1] == 1:
            current_Position = previous_Positions[-2]
        # checking if the previous position is on the North West
        elif previous_Positions[-2] - previous_Positions[-1] == 1 and previous_Rows[-2] - previous_Rows[-1] == 1:
            current_Row = previous_Rows[-2]
            current_Position = previous_Positions[-2]

        # checking if the previous position is on the North
        elif previous_Rows[-2] - previous_Rows[-1] == 1:
            current_Row = previous_Rows[-2]

        # Checking if the previous position is on the North East
        elif previous_Rows[-2] - previous_Rows[-1] == 1 and previous_Positions[-2] - previous_Positions[-1] == 1:
            current_Row = previous_Rows[-2]
            current_Position = previous_Positions[-2]

        # checking if the previous position is on the East
        elif previous_Positions[-2] - previous_Positions[-1] == 1:
            current_Position = previous_Positions[-2]

        # Checking if the previous position is on the South East
        elif previous_Positions[-2] - previous_Positions[-1] == 1 and previous_Rows[-2] - previous_Rows[-1] == 1:
            current_Row = previous_Rows[-2]
            current_Position = previous_Positions[-2]

        # checking if the previous position is on the South
        elif previous_Rows[-2] - previous_Rows[-1] == 1:
            current_Row = previous_Rows[-2]

        # checking if the previous position is on the South West
        elif previous_Rows[-2] - previous_Rows[-1] == 1 and previous_Positions[-2] - previous_Positions[-1] == 1:
            current_Row = previous_Rows[-2]
            current_Position = previous_Positions[-2]

        # removal of the previous path
        del previous_Rows[-1]
        del previous_Positions[-1]
        Check = Check + 1
    # add to list if it's in the correct path
    if Check == 0:
        previous_Rows.append(current_Row)
        previous_Positions.append(current_Position)

    output()

print ("Total time taken to reach the goal : ", +TotalPathTime)
print ("Best Time Taken to reach the goal : ", +BestPathTime)
