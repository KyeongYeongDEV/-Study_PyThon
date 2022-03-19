#클래스

#더하기 기능을 구현한 파이썬 코드
result = 0

def add(num):
        global result
        result += num
        return result

print(add(3))
print(add(4))
#이전에 계산한 결괏값을 유지하기 위해서 result 전역번수(global)을 사용했다.

#2대의 계산기가 필요한 경우
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))
#딱히 상관은 없지만 계산기의 수가 엄청 많이 필요하다면 코드가 엄청 길어질 것이다.

# class Calculator:
#         def ___inin__