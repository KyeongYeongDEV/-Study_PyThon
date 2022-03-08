#반복문 while
"""
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
    """

#탈출 break
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

#처음으로 돌아가기 continue
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)
