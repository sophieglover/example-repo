

def minesweeper(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])

    for current_row in range(num_rows):

        for current_col in range(num_cols):

            if grid[current_row][current_col] == "#":

                continue

            if grid[current_row][current_col] == "-":

                mine_counter = 0

                if (current_row - 1 >= 0) and (current_col - 1 >= 0):
                    if grid[current_row - 1][current_col - 1] == "#":
                        mine_counter += 1
                        
                if (current_row - 1 >= 0):
                    if grid[current_row - 1][current_col] == "#":
                        mine_counter += 1
                        
                if (current_row - 1 >= 0) and (current_col + 1 < num_cols):
                    if grid[current_row - 1][current_col + 1] == "#":
                        mine_counter += 1
                        
                if (current_col - 1 >= 0):
                    if grid[current_row][current_col - 1] == "#":
                        mine_counter += 1
                        
                if (current_col + 1 < num_cols):
                    if grid[current_row][current_col + 1] == "#":
                        mine_counter += 1
                        
                if (current_row + 1 < num_rows) and (current_col - 1 >= 0):
                    if grid[current_row + 1][current_col - 1] == "#":
                        mine_counter += 1
                        
                if (current_row + 1 < num_rows):
                    if grid[current_row + 1][current_col] == "#":
                        mine_counter += 1
                        
                if (current_row + 1 < num_rows) and (current_col + 1 < num_cols):
                    if grid[current_row + 1][current_col + 1] == "#":
                        mine_counter += 1

                grid[current_row][current_col] = str(mine_counter)

    return grid

test_grid = [["#", "-", "-", "-", "-"],
             ["-", "#", "-", "-", "-"],
             ["-", "-", "#", "-", "-"],
             ["-", "-", "-", "#", "-"],
             ["-", "-", "-", "-", "#"]]

result = minesweeper(test_grid)

for row in result:
    print(" ".join(row))











                