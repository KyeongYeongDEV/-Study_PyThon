#https://wikidocs.net/42526

#1.
a = 80
b=75
c=55
d = (a+b+c)/3
print(d)

#2번
if 13%2 == 1 :
    print("홀수")

#3번 문자열 슬라이싱
a = "881120-1068234"
b = a[0:6]
c = a[7:]
print(b,"  ",c)

#4번
pin = "881120-1068234"
print(pin[7])

#5번 replace
a = "a:b:c:d"
print(a.replace(":","#"))

#6번
a = [1,3,5,4,2]
a.sort(reverse=True)

#7번
print(" ".join(['Life', 'is', 'too', 'short']))

#8번
"""
a = (1,2,3)
b =(4)
c = a+b
print(c)"""

#9번


#10번
a = {'A':90, 'B':80, 'C':70}
print(a["B"])

#11번 이유:a=b라고 되어있는데 a를 바꿨기 때문
a = b = [1, 2, 3]
a[1] = 4
print(b)