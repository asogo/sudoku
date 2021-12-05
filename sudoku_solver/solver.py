def find_next_empty(puzzle):
    # find next row, col on the puzzle that's ont filled yet --> rep with 1
    # return row, col tuple (or (None,None) if there is none)
    # indices 0-8
    for r in range(9):  # r row , c column
        for c in range(9):  # range(9) = 0-8
            if puzzle[r][c] == -1:
                return r, c
    return None, None  # if no spaces remain


def is_valid(puzzle, guess, row, col):
   # is the gugess at row/col valid? true if valid or false

   #  row:
   row_vals = puzzle[row]
   if guess in row_vals:
       return False

     # column; col_vals = [1]
    # for i in range(9): #go thru all rows
     #   col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    # the square
    # tricky. find starting index of 3x3 row matrix, then same with cols
    # iterate over the 3 values in the row/col
    row_start = (row//3) #1st set of 3 rows, 2nd set of 3 rows or the 3rd
    col_start = (col//3)*3

    for r in range(row_start, row_start + 3):
        for c in range(col_start,col_start + 3):
            if puzzle[r][c] == guess:
                return False
                # if we get here, its valid
    return True

def solve_sudoku(puzzle):
    # solve using backtracking
    # the puzzle is a list of lists, where each inner list is a row in the puzzle
    # lists are mutable so the puzzle will be changed to the solution if the solution exists
    row, col = find_next_empty(puzzle)
    # step 1.1: if none left, we"re done bc no no valid inputs
    if row is None:
        return True

    # step 2: if there's a spot. Come up with a guess 1-9, 
    for guess in range (1,10):
        # step 3: check if guess is valid
        if is_valid(puzzle,guess,row,col):
            # step 3. 1: valid, so place that guess on the puzzle
            puzzle[row][col] = guess
            # recurse
            # step 4. recursively call the fctn
            if solve_sudoku(puzzle):
                return True

        # if not valid: OR our guess doesn't solve the puzzle
        # back track, try again 
        puzzle[row][col] = -1 #reset guess
        # step 6: if none work, we cannot find a solution and it is unsolveble
    return False
