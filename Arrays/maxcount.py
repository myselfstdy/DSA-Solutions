arr = [1,0,0]
c=0
max_count = 0
for i in range(1,len(arr)):
    if arr[i]==arr[i-1]:
        c+=1
    else:
        max_count = max(max_count,c)
        c=1
max_count = max(max_count,c)
print(max_count)