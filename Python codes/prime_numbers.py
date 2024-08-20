# write a python code for finding first 5 prime numbers form 1-100
count = 0
for i in range(1,100):
    flag=False
    num = i
    if num==2:
        print(f" {num} is Prime Number")
    elif num > 2:
        for i in range(2,num):
            if num%i == 0:
                flag = False
                break
            else:
                flag=True
    if flag==True:
        print(f" {num} is Prime Number")
        count += 1
    # print(count)
    if count == 4:
        break
        