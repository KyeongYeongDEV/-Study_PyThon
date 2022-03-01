#문자열 관련 함수들

#문자 개수 세기(count)
a = "hobby"
a.count('b')
2
#문자열 중 'b'의 개수를 알려준다

#위치 알려주기 1 (find)
a = "Python is the best choice"
a.find('b')
14  #0부터 세기 때문에 b의 위치는 15가 아니라 14이다
a.find('k')
-1 #만약 찾는 문자가 존재하지 않는다면 -1을 출력한다.

#위치 알려주기 2 (index)
a = "Life is too short"
a.index('t')
8  #문자열 중 t가 처음 발견되는 위치를 반환한다.
a.index('k')
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#ValueError: substring not found     
#먄약 찾는 문자가 존재하지 않는다면 오류가 발생한다.

#문자열 삽입(join)
",".join('abcd')
'a,b,c,d'
#abcd 문자열 각각의 문자 사이에 ,를 삽입한다.
#join 함수는 문자열뿐만 아니라 앞으로 배울 리스트나 튜플도 입력으로 사용할 수 있다\

#소문자를 대문자로 바꾸기
a = "hi"
a.upper()
'HI'

#대문자를 소문자로 바꾸기
a = 'HI'
a.lower()
"hi"

#왼쪽 공백 지우기(lstrip)
a = ' hi '
a.lstrip()
"hi "
#문자열 중 가장 왼쪽에 있는 한 칸 이사으이 연속된 공백들을 모두 지운다

#오른쪽 공백 지우기 (rstrip)
a = " hi "
a.rstrip()
' hi'
#문자열 중 가장 왼쪽에 있는 한 칸 이사으이 연속된 공백들을 모두 지운다

#양쪽 공백 모두 지우기(strip)
a = " hi "
a.strip()
"hi"
#문자열 양쪽에 있는 한 칸 이상의 연속된 공백을 모두 지운다.

#문자열 바꾸기 (replace)
a = "Life is too short"
a.replace("Life", "Your leg")
'Your leg is too short'
#replace("바뀌게 될 문자열" , "바꿀 문자열")

#문자열 나누기(split)
a = "Life is too short"
a.split()
['Life', 'is', 'too', 'short']
#괄호에 아무것도 넣지 않으면 공백을 기준으로 나눈다

b = "a:b:c:d"
b.split(':')
['a', 'b', 'c', 'd']
#괄호에 특정값이 있는 경우 그 특정값을 구분자로 해서 나눈다