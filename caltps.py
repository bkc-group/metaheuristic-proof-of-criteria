f = open('./results-50/dpos-200-3', 'r')
sum = 0
av=0
points=[]
for line in f:
    av+=1
    sum += int(line.split(" ")[3])
    points.append(int(line.split(" ")[3]))

print("{} point {} avg".format(av,sum/av))
