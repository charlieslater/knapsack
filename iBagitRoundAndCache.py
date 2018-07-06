W = 0

fname ='bag1.txt'
print('data from',fname)
f = open(fname,'r')
bagsize,numitems = map(int,f.readline().split())
print('bagsize =',bagsize,', numitems =', numitems)
W = bagsize
sizes = {}
values = {}
i = 1
rfactor = 5
for line in f:
    v,sz = map(int,line.split())
    values[i] = v
    sizes[i] = rfactor * int(sz/rfactor)
    i += 1

bag = {}
for sz in range(0,bagsize+rfactor,rfactor):
    bag[sz] = {0:0}
n = numitems
bag0 = bag[0]
for j in range(0,n+1):
    bag0[j] = 0
bagsizes = range(rfactor,bagsize+rfactor,rfactor)
for j in range(1,n+1):
    for sz in bagsizes:
        if sizes[j] > sz: 
            bagsz = bag[sz]
            bagsz[j] = bagsz[j-1]
            if j-2 in bagsz:
                del bagsz[j-2]
            continue
        less_sz = sz-sizes[j]
        baglsz = bag[less_sz]
        smallerV = baglszSmallerV = baglsz[j-1]
        bagsz = bag[sz]
        best = max(bagsz[j-1], smallerV + values[j])
        bagsz = bag[sz]
        bagsz[j] = best
        if j-2 in bagsz:
            del bagsz[j-2]
        if smallerV != baglszSmallerV:
            print("j=",j)
            print("(w,j-1)=",(w,j-1))
            print("sizes[j]=",sizes[j])
            print("lessweight =",lessweight)

print(bag[bagsize][n])
