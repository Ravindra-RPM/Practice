num = int(input("Enter a number for dispaling fibonachi series: "))-1

a=0
b=1
print(a,b, end=' ')
for i in range(1,num):
    c=a+b
    a=b
    b=c
    print(c, end=' ')
