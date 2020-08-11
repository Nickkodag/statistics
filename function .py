import math
def mean(value):
    return sum(value)*1.0/len(value)
def staDev(value):
    length=len(value)
    m=mean(value)
    total_sum=0
    for i in range (length):
        total_sum+=(value[i]-m)**2
    underroot=total_sum*0.1/length  

    return math.sqrt(underroot)

x=[2,3,455,67,78,898,87,5,4,45,56]
standev=staDev(x)
print(standev) 