sudoku = ''
total_sum = 0

def same_row(i,j): return (i/9 == j/9)
def same_col(i,j): return (i-j) % 9 == 0
def same_block(i,j): return (i/27 == j/27 and i%9/3 == j%9/3)

def r(a):
  global total_sum
  i = a.find('0')
  if i == -1:
    total_sum += int(a[:3])

  excluded_numbers = set()
  for j in range(81):
    if same_row(i,j) or same_col(i,j) or same_block(i,j):
      excluded_numbers.add(a[j])

  for m in '123456789':
    if m not in excluded_numbers:
      # At this point, m is not excluded by any row, column, or block, so let's place it and recurse
      r(a[:i]+m+a[i+1:])


file = open("_sudoku.txt", 'r')

for line  in file.readlines(): 
    line = line.strip()
    if 'Grid' not in line:
        sudoku += line.strip()
    elif 'Grid' in line:
        if len(sudoku) == 81:
            r(sudoku)
            sudoku = ''
        else: pass
print total_sum
