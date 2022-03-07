#bool true(참)과 false(거짓)을 나타내는 자료형

#파이썬에서 불은 첫 글자를 대문자로 써줘야 한다
a = True
b = False

#type() 함수를 사용하면 변수의 자료형이 뭔지 알 수 있다
type(a)
#<class 'bool'>
type(b)
#<class 'bool'>


#문자열, 리스트, 튜플, 딕셔너리 등의 값이
# 비어 있으면(" ", [ ], ( ), { }) 거짓이 된다
#비어 있지 않으면 참이다.


#불 연산
bool('python')
True
bool('')
False
bool(0)
False