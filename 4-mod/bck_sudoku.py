from itertools import permutations as per

shouldhave = '123456789'

sudos = [''.join(l for l in _gen) for _gen in per(shouldhave)]
kudos = {
        0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[],
        15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[], 25:[], 26:[], 27:[], 28:[],
        29:[], 30:[], 31:[], 32:[], 33:[], 34:[], 35:[], 36:[], 37:[], 38:[], 39:[], 40:[], 41:[], 42:[],
        43:[], 44:[], 45:[], 46:[], 47:[], 48:[], 49:[], 50:[]
}

su_sum = 0

f = open('_sudoku.txt', 'r')
count = 50
while count > 0:
    _line = f.readline()
    if 'Grid' in _line:
        _firstrow = f.readline().strip()
        boxes = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[] }
        _shdntcnt =  {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[] }
        '''for _inbox in _firstrow:
            if _inbox != '0': 
                boxes[_firstrow.index(_inbox)//3].append(_inbox)
        '''
        for _next8rows in range(2,10):
            _thisline = f.readline().strip()
            for _cur in range(8):
                if _thisline[_cur] != '0':
                    box_count = (_next8rows//3) + _cur // 3
#                    print box_count
                    boxes[box_count].append(_thisline[_cur])
                    _shdntcnt[_cur].append(_thisline[_cur])
#        print "Working with Grid-%s contains firstrow as %s"%(50-count,_firstrow)
#        print boxes, _shdntcnt
        for _fixed in sudos:
            if all(_fixed[x]==y and _fixed[0] not in _shdntcnt[0] and _fixed[1] not in _shdntcnt[1] and _fixed[2] not in _shdntcnt[2] and _fixed[3] not in _shdntcnt[3] and _fixed[4] not in _shdntcnt[4] and _fixed[5] not in _shdntcnt[5] and _fixed[6] not in _shdntcnt[6] and _fixed[7] not in _shdntcnt[7] and _fixed[8] not in _shdntcnt[8] and _fixed[0] not in boxes[0] and  _fixed[1] not in boxes[1] and _fixed[2] not in boxes[2] and _fixed[3] not in boxes[3] and _fixed[4] not in boxes[4] and _fixed[5] not in boxes[5] and _fixed[6] not in boxes[6] and _fixed[7] not in boxes[7] and _fixed[8] not in boxes[8] for x,y in enumerate(_firstrow) if y != '0'):
                su_sum += int(_fixed[:3])
#                print "Found Grid-%s contains firstrow as %s"%(50-count,_fixed)
                if _fixed[:3] not in kudos[50-count]:
                    kudos[50-count].append(_fixed[:3])
#        print _fixed
#        raw_input()
        count -= 1

for item,value in kudos.iteritems():
    print item, value
    raw_input()
print su_sum
