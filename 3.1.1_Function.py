#함수

#구조
"""
def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
   """
#def은 한수를 만들 때 사용되는 예액어

#예
def add(a, b): 
    return a + b
#이 함수의 이름은 add이고 2개의 값을 받으며 결괏값은 2개의 입력을 더한 값이다.
a = 3
b = 4
c = add(a, b)
print(c)
7

#입력값이 없는 함수
def say(): 
    return 'Hi' 

#결과값이 없는 함수
def add(a, b): 
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

a = add(3, 4)
print(a)
None
#a의 결과값은 None이다 None은 거짓을 나타내는 자료형

#함수 이름 지정하여 호출하기
def add(a, b):
    return a+b

#매개변수 지정하여 호출하기
result = add(a=3, b=7)  # a에 3, b에 7을 전달
print(result)
10
result = add(b=5, a=3)  # b에 5, a에 3을 전달
print(result)
8

#입력값이 몇 개가 될지 모를 떄는 어떻게 해야 할까
"""
def 함수이름(*매개변수): 
    <수행할 문장>
"""
#예
def add_many(*args): 
    result = 0 
    for i in args: 
        result = result + i 
    return result 
#매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아서 튜플로 만들어 준다.
esult = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)
55

#또 다른 예
def add_mul(choice, *args): 
    if choice == "add": 
        result = 0 
        for i in args: 
            result = result + i 
    elif choice == "mul": 
        result = 1 
        for i in args: 
            result = result * i 
    return result 
#위의 것은 다음과 같이 사용된다
result = add_mul('add', 1,2,3,4,5)
print(result)
15
result = add_mul('mul', 1,2,3,4,5)
print(result)
120

#키워드 파라미터 kwargs
def print_kwargs(**kwargs):
    print(kwargs)
#위의 함수는 매개변수 kwargs를 출력하는 함수이다
print_kwargs(a=1)
{'a': 1}
print_kwargs(name='foo', age=3)
{'age': 3, 'name': 'foo'}
#매개변수 이름 앞에 **를 붙이면
#매개변수 kwargs는 딕셔너리가 되고 
#모든 key = value 형태의 결괏값이 그 딕셔너리에 저장된다.

