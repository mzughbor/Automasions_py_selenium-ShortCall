'''
def summusin(n1,n2 ):
    result = n1 + n2
    print(result)

def subtract(n1 ,n2):
    result = n1 - n2
    print(result)

def multiplcaition(n1, n2):
    result = n1 * n2
    print(result)

def division(n1, n2):
    result = n1 / n2
    print(result)

#####################################################

n1 = eval(input('Enter The First Number :'))  #you can use : eval or int ....
n2 = eval(input('Enter The Second Number :'))
The_Operator=input('Enter your operator :')
if The_Operator =='+':
    summusin(n1,n2)
elif The_Operator =='-':
    subtract(n1,n2)
elif The_Operator =='*':
    multiplcaition(n1,n2)
else:division(n1,n2)

####################################################

def MaxNum(x,y,z): # OR you can use simpleset way by usind " and " " or " ...
    if x > y:
        if x > z:
            print('the maximum number is :', x)
        elif z > x:
            print('the maximum number is :', z)
    elif x > z:
        print('the maximum number is :', y)
    else:
        if y > z:
            print('the maximum number is :', y)
        else:
            print('the maximum number is :', z)

MaxNum(1,7,2)

####################################################
sum = 0
list = [8,2,3,0,7]
for x in range(0,len(list)):
    num = list[x]
    sum += num
print(sum)
'''
####################################################

