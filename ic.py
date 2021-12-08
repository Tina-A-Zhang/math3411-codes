freq=[5,2,2,2,1,5,4,5,3,1,5,1,1,1,1,2,3,3,2,2]
n=0
sum = 0
for i in freq:
    n = n+ i
    sum = sum + i*i

ic=(sum-n)/(n*n-n)
print("The index of coincidence is: "+str(ic))
r=(0.0273*n)/((n-1)*ic-0.0385*n+0.0658)
print("Estimated keyword length is: "+str(r))

