"""
Recursive solution to knapsack problem.  Extremely slow, but works
for problems with a very small number of possible sizes.
"""
fname ='bag0.txt'
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
    """
    There are three cases:
    1. Item won't fit in bag at all.  Skip it
    2. Adding the item makes things worse.  Don't use it.
    3. Adding the item to the solution for bag small enough 
       to fit in the current bag along with the item makes
       things better. Use the item along with the solution 
       for the smaller bag. 
    """
    if sz == 0 or j == 0: return 0
    if sizes[j] > sz: 
        return bag(sz,j-1) 
    return max(bag(sz,j-1),bag(sz-sizes[j],j-1)+values[j])
def bag(sz,j):
    return cases(sz,j)
    
print(bag(bagsize,numitems))
