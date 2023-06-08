K, M = map(int, raw_input().strip().split(' '))
ls = []
for i in range(K):
    l = map(int, raw_input().strip().split(' ')[1:])
    ls.append(l)
    
level = len(ls) - 1
res = 0
def loopf(ls, level, s, m):
    global res
    if level < 0:
        if s > res:
            res = s
        return
    for i in ls[level]:
        loopf(ls, level-1, (s + i ** 2 % m) % m, m)
loopf(ls, level, 0, M)
print res