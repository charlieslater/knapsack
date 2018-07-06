"""
Recursive solution to knapsack problem with naive memoization.  Ten

times faster than simple recursion, but still extremely slow!

"""
fname ='bag1.txt'
print('data from',fname)
f = open(fname,'r')
bagsize,numitems = map(int,f.readline().split())
print('bagsize =',bagsize,', numitems =', numitems)
sizes = {}
values = {}
i = 1
for line in f:
    v,sz = map(int,line.split())
    values[i] = v
    sizes[i] = sz
    i += 1

def cases(sz,j):
    if sz == 0 or j == 0: return 0
    if sizes[j] > sz: 
        return bag(sz,j-1)
    return max(bag(sz,j-1),bag(sz-sizes[j],j-1)+values[j])

cache = {}
def bag(sz,j):
    if (sz,j) in cache:
        return cache[(sz,j)]
    cache[(sz,j)] = cases(sz,j)
    return cases(sz,j)
    
print(bag(bagsize,numitems))
