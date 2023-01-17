sum = 0
data = [308,301,305,309,322,331,333,349,336,338,364,377,400,422,447,483,512,535,524,577]
for i in data:
    sum += i
data.sort()
mean = round(sum/len(data),2)
median = data[len(data)//2]
mode = max(set(data), key=data.count)

def varience(data):
    sum = 0
    for i in data:
        sum += (i-mean)**2
    return round(sum/len(data),2)

standard_deviation = round(varience(data)**0.5,2)

print("mean: ",mean)
print("median: ",median)
print("mode: ",mode)
print("varience: ", varience(data))
print("standard deviation: ", standard_deviation)
