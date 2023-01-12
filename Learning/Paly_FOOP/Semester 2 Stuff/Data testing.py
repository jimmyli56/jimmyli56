import statistics
sum = 0
data = [1,1,2,5,7,8]
for i in data:
    sum += i
data.sort()
mean1 = round(sum/len(data),2)
mid = len(data)//2
if (len(data)%2 == 1):
    mid = data[mid]
print(mid)
print(statistics.median(data))

d=dict()
print(max(d, key=d.get))