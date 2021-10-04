#函數變數生命週期
def test():
    #global a
    a = 5000 #自創一個區域變數  離開函數立即死亡
    print(f'函數內的a:{a}')
a = 10 #main中的變數，為全域變數
def test2():
    global a
    print(a)
test()
test2()
print(f'main中的a:{a}')
#參數型態
def adult(age):
    if not isinstance(age,(int,float)): #isinstance 實例化
        raise TypeError('型態錯誤，請重新再輸入一遍') #丟出一個例外
    if 35 >= age >= 18:
        print('青年人')
    elif 65 >= age >=36:
        print('中年人')
    elif age >= 66:
        print('老年人')
    else:
        print('未成年人')
adult(21)
adult(15)
adult(54)
adult(83)
#adult('小朋友')
#多值返回
import math
def point(radius,angle): #半徑
    x = radius * math.cos(angle*math.pi/180)
    y = radius * math.sin(angle*math.pi/180)
    return x,y #實際上是傳回tuple => return(x,y)
point(100,30)
print(point(100,30))
h,v = point(100,30)
print(f'x:{h}')
print(f'y:{v}')
p = point(100,30)
print(f'x:{p[0]}')
print(f'y:{p[1]}')
#預設參數
#預設參數：不給值時使用；若有給值，則使用給定的值
#預設參數只能寫在非預設參數的右邊
"""for i in range(0,360):
    print(point(100,i))"""
def point(radius,angle=0): #半徑
    x = radius * math.cos(angle*math.pi/180)
    y = radius * math.sin(angle*math.pi/180)
    return x, y
x,y = point(100) #計算0度
print(x,y)
x,y = point(100,30) #計算30度
print(x,y)
#可變參數
def cal(a,b,c):
    sum = (a+b+c)
    return sum
print(cal(10,20,30))
def cal(*n): #*可將資料轉成tuple接收
    sum = 0
    for i in n:
        sum += i
    return sum
d = [1,2,3,4,5]
print(cal(10,20,30,40))
print(cal(1,2,3,4,5,6,7,8,9,10))
print(cal(d[0],d[1],d[2],d[3],d[4]))
print(cal(*d)) #*可將d拆成一個個可變參數
#Recursive 遞迴 自己呼叫自己，但卻不是自己
def f(n):
    if n == 1:
        return 1
    else:
        return n*f(n-1)
print(f(5))
print(f(1))
print(f(2))