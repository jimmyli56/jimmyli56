import statistics
GDP = [308,301,305,309,322,331,333,349,336,338,364,377,400,422,447,483,512,535,524,577]

def mean(data):
    sum = 0
    for i in data:
        sum += i
    return round(sum/len(data),2)

def median(data):
    data.sort()
    if len(data) % 2 == 0:
        return (data[len(data)//2 - 1] + data[len(data)//2]) / 2
    else:
        return data[len(data)//2]

def mode(data):
    frequency = {}
    for i in data:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    mode = max(frequency, key=frequency.get)
    if frequency[mode] == 1:
        return None
    else:
        return mode

def varience(data):
    sum = 0
    mean_value = mean(data)
    for i in data:
        sum += (i - mean_value)**2
    return round(sum/len(data),2)

def covarience(data1, data2):
    sum = 0
    mean1 = mean(data1)
    mean2 = mean(data2)
    for i in range(len(data1)):
        sum += (data1[i]-mean1)*(data2[i]-mean2)
    return round(sum/len(data1),2)

def standard_deviation(data):
    return round(varience(data)**0.5,2)
print("My calculations:")
print("mean: ",mean(GDP))
print("median: ",median(GDP))
print("mode: ",mode(GDP))
print("variance: ", varience(GDP))
print("standard deviation: ",standard_deviation(GDP))


print("")

print("Statistics module calculatiuons: ")
print("mean: ",statistics.mean(GDP))
print("median: ",statistics.median(GDP))
print("mode: ",statistics.mode(GDP))
print("varience: ",statistics.pvariance(GDP))
print("standard deviation: ",statistics.stdev(GDP))
