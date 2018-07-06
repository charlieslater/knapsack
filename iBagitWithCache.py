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
#
# 'bag' is a dictionary of bag size dictionaries
#
bag = {}
for sz in range(bagsize+1):
    bag[sz] = {0:0}
n = numitems
bag0 = bag[0]
for j in range(0,n+1):
    bag0[j] = 0
bagsizes = range(bagsize+1)
#
#    Recall there are three cases:
#    1. Item won't fit in bag at all.  Skip it
#    2. Adding the item makes things worse.  Don't use it.
#    3. Adding the item to the solution for bag small enough 
#       to fit in the current bag along with the item makes
#       things better. Use the item along with the solution 
#       for the smaller bag. 
#       
#    Memory usage is significant for large problems.  Therefore,
#    we don't keep solutions for all bags, just solutions for bags
#    with one fewer items.
#
for j in range(1,n+1):
    for sz in bagsizes:
        if j-2 in bag[sz]:
            del bag[sz][j-2]  # don't keep solutions for all bags
        if sizes[j] > sz: 
            bag[sz][j] = bag[sz][j-1]  # cache previous optimum
            continue
        smaller = sz-sizes[j]
        smallerV = bag[smaller][j-1]
        bagsz = bag[sz]
        bag[sz][j] = max(bagsz[j-1], smallerV + values[j])

print(bag[bagsize][n])
