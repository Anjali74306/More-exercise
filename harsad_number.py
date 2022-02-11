# x = 42
# x_digits = list(str(x))
# print(x_digits)

def harsad():
    i=1
    while (i<=1000):
        k=i
        sum=0
        while(k>0):
            b=k%10
            k=k//10
            sum+=b
        if i%sum==0:
            print(i,"is harsad number")
        i=i+1
harsad()