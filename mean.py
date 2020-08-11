# how to create mean calculator 
def mean(value):
    length=len(value)
    total_sum=0
    for i in range (length):
        total_sum+=value[i]
#second methon  #  total_sum+=sum(value)    
    average=total_sum*0.1/length
    return(average)

x=[2,3,455,67,78,898,87,5,4,45,56]
n=mean(x)
print(n)    
