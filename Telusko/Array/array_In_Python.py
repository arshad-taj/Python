import array
val = array.array('i',[1,1,1])

rr = "ss dd dd fff gg gg".split()
print(rr)

#copying array

val_copy = array.array(val.typecode,val)
print(f'copy of array val : {val_copy}')