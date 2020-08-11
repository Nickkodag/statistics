import random
import math
###Confidence Interval
#x=[1,2,3,4,5,6,7,8]
#bootstrap=[1,2,3,4,5,6,7]\
def makerandomlist(value):
    length=len(value)
    newlist=[]
    for i in range (length):
        random_num=random.randint(0,length-1)
        newlist.append(value[random_num]*1.0)
    return newlist

def mean(value):
    return sum(value)*0.1/len(value)
def staDev(value):
    length=len(value)
    m=mean(value)
    total_sum=0
    for i in range (length):
        total_sum+=(value[i]-m)**2
    underroot=total_sum*0.1/length  

    return math.sqrt(underroot)

def makeAveragelist(value,numsimulation):
    Averagelist=[]
    simulation=1
    while simulation<=numsimulation:
        templist=makerandomlist(value)
        tempmean=mean(templist)
        Averagelist.append(tempmean)
        simulation+=1
        return Averagelist
def getcondidenceInterval(Averagelist,confidence):
    side_inerval= (100.0-confidence)/200.0
    length=len(Averagelist)
    cut_off=length*side_inerval
    new_list=[]
    for i in range (length):
        if  i >= cut_off and length -i > cut_off:
            newlist.append(Averagelist(i))
        return new_list    

def makeconfidenceInterval(value,numsimulation,confidence):
    Averagelist=makeAveragelist(value,numsimulation)
    Averagelist.sort()
    print(mean(Averagelist))
    print(staDev(Averagelist))


    interval_list=getcondidenceInterval(Averagelist,confidence)
    interval_list.sort()
    
    avearge=(interval_list[0]+interval_list[-1])/2
    difference=average-interval_list[0]
    return (average,difference)

x=[1,2,3,4,5,6,77,45,98,78,87]
info=makeconfidenceInterval(x,1000,95)
print(info[0])
print (info[1])