set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}


print("set 1 elements")
for element in set1:
    print(element,end=" ")
print("\nset 2 elements:")
for element in set2:
    print(element,end=" ")
    print()
    
    
    union_set=set1.union(set2)
print("union of set1 and set2:,union_set")