#함수의 결괏값은 언제나 하나이다
def add_and_mul(a,b): 
    return a+b, a*b
#위의 함수를 
result = add_and_mul(3,4) 
#이렇게 나타내면 오류가 발생할까?
result = (7, 12) #오류는 발생하지 않고 튜플로 나타내게 된다
#만약 2개 따로 받고 싶다면
result1, result2 = add_and_mul(3, 4) #이렇게 하면 된다


#매개변수 초기값 미리 설정하기
def say_myself(name, old, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")
#man이 Ture이기 때무에 남자입니다가 출력이된다
say_myself("박응선", 27, False)
#False로 바뀌면서 여자입니다가 출력이 된다.
'''
def say_myself(name, man=True, old): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man: 
        print("남자입니다.") 
    else: 
        print("여자입니다.")
#이것을 실행시키면 오류가 발생한다
#초기값을 설정을 해주려면 중간이 아닌 젤 마지막에 해야 한다.
'''

#함수 안에서 선언ㅇ한 변수의 호력 범위
# vartest.py
a = 1
def vartest(a):
    a = a +1

vartest(a)
print(a)
#2가 출력이 될 것 같지만 
#1이 출력이 된다.
#그 이유는 함수 안에서 이름이 같이만 새로 만은 매개변수는 
#함수 안에서만 사용하면 "함수만의 변수"이기 때문이다.
#즉, 위의 함수에 들어간 a는 먼저 선언된 a가 아니다


#함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기
a = 1 
def vartest(a): 
    a = a +1 
    return a

a = vartest(a)  #대입을 통해 함수 안에 있는 a의 값을 밖에 있는 a의 값에 대입을 해줬다
print(a)

# 2. global 명령어 사용하기
a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() 
print(a)
#global을 사용하면 함수 밖의 a변수를 직접 사용하겠다는 뜻이다
#하지만 사용하지 않는 것이 좋다
#왜냐하면 함수는 독립적으로 존재하는 것이 좋기 때문이다. 

#lambda
#lambda는 함수를 생성할 때 사용하는 에약어로 def와 동일하다
#보통 함수를 한 줄로 간결하게 만들 떄 사용
add = lambda a, b: a+b #add는 두 개의 인수를 받아 서로 더해주는 lambda함수이다
result = add(3, 4)
print(result)
7

def add(a, b):
    return a+b

result = add(3, 4)
print(result)
7
#함수가 하는 일은 위의 것과 완전히 동일하다

