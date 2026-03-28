# data structures
# 5. set

set_ds= {1,1,2,3,4,5,5,6,7}
print(set_ds)
set_ds.add(55)
print(set_ds)

set_ds.remove(55)
print(set_ds)

#operations
set_ds1 = {10,20,30,40,50,60}
set_ds2 = {10,20,100,200,300,400}

print(set_ds1.union(set_ds2))
print(set_ds1.intersection(set_ds2))
print(set_ds1.difference(set_ds2))

set_ds1.clear()
print(set_ds1)