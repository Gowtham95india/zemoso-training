f = open('_sudoku.txt', 'r')
puzzle = {}
count = 0
answres = []
temp_digits = []
for _line in f.readlines():
    if 'Grid' in _line:
        puzzle[count] =  temp_digits
        temp_digits = []
        count += 1
    else:
        temp_digits.append([int(_letter) for _letter in _line.strip()])

print len(puzzle)

def getcolele(sud, cpos):
   return [int(sud[l][cpos]) for l in range(10)]

def getboxele(sud, row, cpos):
    intpos = (row/3)*3

for sudoku in puzzle.values():
    for row in sudoku:
        for blank in row:


"""
    for _n, _p in puzzle.iteritems():
        boxed = {0:[], 1:[], 2:[]}
        box = []
        for _row in _p:
            for _num in _row:
                if _num != 0 and _p.index(_row) == 0:
                    boxed[0].append(_num)
                if _num !=0 and _p.index(_row) > 2:
                   boxed[_row.index(_num)].append(_num)
                if _row.index(_num) < 3 and _p.index(_row) < 3 and _num != 0: box.append(_num)

        print boxed, box
        raw_input()
"""
